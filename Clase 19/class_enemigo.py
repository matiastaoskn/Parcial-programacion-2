import pygame
from settings import *
from class_personaje import *
from nivel import *
import random
import time

class Enemigos(Personaje):
    def __init__(self, tamaño, animaciones, posicion_inicial, velocidad_enemigo):
        self.ancho = tamaño[0]
        self.alto = tamaño[1]
    
        self.contador_pasos = 0
        self.accion = "camina_derecha"
        self.animaciones = animaciones
        self.rescalar_animaciones()
        self.esta_saltando = False
 
        rectangulo = self.animaciones["camina_derecha"][0].get_rect()
        rectangulo.x = posicion_inicial[0]
        rectangulo.y = posicion_inicial[1]
        self.lados = obtener_rectangulos(rectangulo)

        #Salto
        self.desplazamiento_y = 0
        self.velocidad_enemigo = velocidad_enemigo
        self.que_hace = "quieto"
        self.puede_saltar = True
        self.direccion = 1

        self.gravedad = 1
        self.potencia_salto = -15
        self.limite_velocidad_caida = 15

        #Atacar
        self.vida_enemigo = 3
        self.golpe_realizado = False
        self.golpe_realizado = False
        self.duracion_temporizador = 8
        self.tiempo_inicial = pygame.time.get_ticks()
        
    def rescalar_animaciones(self):
        for clave in self.animaciones:
            rescalarar_img(self.animaciones[clave], (self.ancho, self.alto))

    def animar(self, pantalla, que_animacion):
        animacion = self.animaciones[que_animacion]
        largo = len(animacion)
        if self.contador_pasos >= largo:
            self.contador_pasos = 0
        
        pantalla.blit(animacion[self.contador_pasos], self.lados["main"])
        self.contador_pasos += 1

    def mover(self, velocidad):
        if(self.que_hace != "golpear"):
            for lado in self.lados:
                self.lados[lado].x += velocidad

    def aplicar_gravedad(self, piso, lista_plataformas):
        if self.esta_saltando:
            for lado in self.lados:
                self.lados[lado].y += self.desplazamiento_y

            if self.desplazamiento_y + self.gravedad < self.limite_velocidad_caida:
                self.desplazamiento_y += self.gravedad

        if self.lados["bottom"].colliderect(piso["main"]):
            self.desplazamiento_y = 0
            self.esta_saltando = False
            self.lados["main"].bottom = piso["main"].top + 5
            self.puede_saltar = True
        else:
            self.esta_saltando = True
        
        for plataforma in lista_plataformas:
            if self.lados["bottom"].colliderect(plataforma.rect) and self.desplazamiento_y >= 0:
                self.desplazamiento_y = 0
                self.esta_saltando = False
                self.lados["main"].bottom = plataforma.rect.top + 5
                self.puede_saltar = True
                break

    def golpear_personaje_derecha(self, personaje, pantalla, rectangulo_personaje):
        if self.lados["right"].colliderect(personaje.lados["main"]) and self.golpe_realizado == False:
            self.golpe_realizado = True
            self.animar(pantalla, "ataca_derecha")
            self.personaje_golpeada(rectangulo_personaje, personaje)

    def golpear_personaje_izquierda(self, personaje, pantalla, rectangulo_personaje):
        if self.lados["left"].colliderect(personaje.lados["main"]) and self.golpe_realizado == False:
            self.golpe_realizado = True
            self.animar(pantalla, "ataca_derecha")
            self.personaje_golpeada(rectangulo_personaje, personaje)
            
    def personaje_golpeada(self, rectangulo_personaje, personaje):
        personaje.vida_del_personaje -= 1
        for lado in rectangulo_personaje:
            if self.que_hace == "camina_derecha":
                rectangulo_personaje["main"].x += 50
                rectangulo_personaje["bottom"].x += 50
                rectangulo_personaje["left"].x += 50
                rectangulo_personaje["top"].x += 50
                rectangulo_personaje["right"].x += 50
            else:
                rectangulo_personaje["main"].x -= 50
                rectangulo_personaje["bottom"].x -= 50
                rectangulo_personaje["left"].x -= 50
                rectangulo_personaje["top"].x -= 50
                rectangulo_personaje["right"].x -= 50
            
    def updateEnemigo(self, pantalla, piso, lista_plataformas, personaje, lados_rectangulos, rectangulo_personaje):


        self.tiempo_actual = pygame.time.get_ticks()
        self.tiempo_transcurrido_segundos = (self.tiempo_actual - self.tiempo_inicial) / 1000 
        
        if(self.golpe_realizado == True):
            if self.tiempo_transcurrido_segundos >= self.duracion_temporizador:
                print("pasaron 5 seugnos")
                self.golpe_realizado = False
                self.tiempo_inicial = self.tiempo_actual

        if self.que_hace == "dañado":
            self.animar(pantalla, "enemigo_dañado")

        elif self.que_hace == "quieto":
            self.animar(pantalla, "quieto")

        elif self.que_hace == "camina_derecha":
            self.animar(pantalla, "camina_derecha")

        elif self.que_hace == "camina_izquierda":
            self.animar(pantalla, "camina_izquierda")

        elif self.que_hace == "golpeando":
            self.animar(pantalla, "ataca_derecha")
        


        for lado in self.lados:
            rectangulo = self.lados[lado]



        if self.lados["main"].colliderect(lados_rectangulos[0]["right"]) and self.direccion == 1 :
            self.direccion = -1
            self.mover(self.velocidad_enemigo * -1)
            self.que_hace = "camina_izquierda"
        
        
        if self.lados["main"].colliderect(lados_rectangulos[1]["main"]) and self.direccion == -1 :
            self.direccion = 1
            self.mover(self.velocidad_enemigo * 1)
            self.que_hace = "camina_derecha"


        if(rectangulo.right < 1280 - self.velocidad_enemigo and self.direccion == 1):
            self.mover(self.velocidad_enemigo)
            self.que_hace = "camina_derecha"
            if(self.golpe_realizado == False):
                self.golpear_personaje_derecha(personaje, pantalla, rectangulo_personaje)
            
        if rectangulo.right >= 1280 - self.velocidad_enemigo and self.direccion == 1:
            self.direccion = -1
            self.mover(self.velocidad_enemigo * -1)
            self.que_hace = "camina_izquierda"
            if(self.golpe_realizado == False):
                self.golpear_personaje_izquierda(personaje, pantalla, rectangulo_personaje)

        elif rectangulo.left > self.velocidad_enemigo and self.direccion == -1:
            self.mover(self.velocidad_enemigo * -1)
            self.que_hace = "camina_izquierda"
            if(self.golpe_realizado == False):
                self.golpear_personaje_izquierda(personaje, pantalla, rectangulo_personaje)

        elif rectangulo.left <= self.velocidad_enemigo and self.direccion == -1:
            self.direccion = 1
            self.mover(self.velocidad_enemigo)
            self.que_hace = "camina_derecha"
            if(self.golpe_realizado == False):
                self.golpear_personaje_derecha(personaje, pantalla, rectangulo_personaje)



        self.aplicar_gravedad(piso, lista_plataformas)

