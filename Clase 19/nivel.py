import pygame, sys
from pygame.locals import *
from modo import *
from animaciones import *
from class_personaje import *

from Interfaz.GUI_form_contenedor_nivel import *


class Nivel:
    def __init__(self, pantalla, personaje_principal, lista_plataformas, lista_enemigos, lista_rectangulos, lados_rectangulos, piso, imagen_fondo, corazones, rectangulo_personaje): 
        self._slave = pantalla
        self.jugador = personaje_principal
        self.velocidad_jugador = 10
        self.imagen_fondo = imagen_fondo
        self.corazones = corazones
        self.lista_plataformas = lista_plataformas
        self.lista_enemigos = lista_enemigos
        self.lista_rectangulos = lista_rectangulos
        self.lados_rectangulos = lados_rectangulos
        self.rectangulo_personaje = rectangulo_personaje
        self.piso = piso
        self.lista_balas = []
        

    def update(self, lista_eventos):

        for evento in lista_eventos:
            if evento.type == pygame.KEYDOWN and evento.key == pygame.K_TAB:
                cambiar_modo()
        
        if len(self.lista_enemigos) > 0:
            self.leer_inputs()
            self.actualizar_pantalla()
            self.dibujar_rectangulos()
        else:
            self._slave.fill("red")


    def actualizar_pantalla(self):
        # Fondo
        self._slave.blit(self.imagen_fondo, (0, 0))
        # Plataformas
        for plataforma in self.lista_plataformas:
            self._slave.blit(plataforma.image, plataforma.rect)

        enemigos = None
        #enemigo
        for enemigo in self.lista_enemigos:
                enemigos = enemigo
                enemigo.updateEnemigo(self._slave, self.piso, self.lista_plataformas, self.jugador, self.lados_rectangulos, self.rectangulo_personaje)


        # Personaje
        self.jugador.update(self._slave, self.piso, self.lista_plataformas, enemigos, self.lista_enemigos, self.lista_balas)

        #Corazones
        self._slave.blit(self.corazones.image, (1300-200,0))
        if self.jugador.vida_del_personaje == 3:
            self.corazones.cargar_imagen(corazones_3)
        elif self.jugador.vida_del_personaje == 2:
            self.corazones.cargar_imagen(corazones_2)
        elif self.jugador.vida_del_personaje == 1:
            self.corazones.cargar_imagen(corazones_1)
        else:
            self.corazones.cargar_imagen(corazones_0)
        
    #Bala
    def crear_bala(self, w, h):
        self.bala = balas_aire(w, h, self.jugador)
        self._slave.blit(self.bala.image, self.bala.rectangulo_bala)
        self.lista_balas.append(self.bala)

    def leer_inputs(self):
        self.jugador.colision_detectada = False

        for lado in self.jugador.lados:
            rectangulo = self.jugador.lados[lado]
        keys = pygame.key.get_pressed()

        if (keys[pygame.K_RIGHT] and  rectangulo.right < 1300 - self.velocidad_jugador):
            self.jugador.que_hace = "derecha"
        elif (keys[pygame.K_LEFT] and rectangulo.left > self.velocidad_jugador):
            self.jugador.que_hace = "izquierda"
            if(keys[pygame.K_SPACE]):
                self.jugador.que_hace = "golpea"
        elif keys[pygame.K_UP]:
            if not self.jugador.esta_saltando:
                self.jugador.que_hace = "salta"
        elif keys[pygame.K_SPACE]:
            self.jugador.que_hace = "golpea"
            for enemigo in self.lista_enemigos:
                self.jugador.golpear_enemigo(enemigo, self.lista_enemigos)
        else:
            self.jugador.que_hace = "quieto"

        if pygame.mouse.get_pressed()[0]:
            self.jugador.que_hace = "dispara"
            self.crear_bala(50, 50)
            
            

    def dibujar_rectangulos(self):
        if get_modo():
            
            for bala in self.lista_balas:
                for lado in bala.lados_bala:
                    pygame.draw.rect(self._slave, ("yellow"), self.bala.lados_bala[lado], width=3)

            for rectangulo in self.lista_rectangulos:
                pygame.draw.rect(self._slave, (255, 0, 0), rectangulo.rect, width=3)

            for enemigo in self.lista_enemigos:
                for lado in enemigo.lados:
                    pygame.draw.rect(self._slave, "Blue", enemigo.lados[lado], 2)

            for plataforma in self.lista_plataformas:
                pygame.draw.rect(self._slave, (255, 0, 0), plataforma.rect, width=3)

            for lado in self.piso:
                pygame.draw.rect(self._slave, "Blue", self.piso[lado], 2)

            for lado in self.jugador.lados:
                pygame.draw.rect(self._slave, "yellow", self.jugador.lados[lado], 3)