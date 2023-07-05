from nivel import *
from class_personaje import *
from class_enemigo import *
from class_plataforma import *
from animaciones import *
from Interfaz.GUI_form_contenedor_nivel import *

import pygame, sys

class NivelDos(Nivel):
    def __init__(self, pantalla):
        
        # Funciones

        W, H = 1400, 900
        TAMAÑO_PANTALLA = (W, H)
        FPS = 18
        velocidad_personaje = 20
        velocidad_enemigo = 4

        pygame.init()

        RELOJ = pygame.time.Clock()
        PANTALLA = pygame.display.set_mode(TAMAÑO_PANTALLA)

        # FONDO
        fondo = pygame.image.load("Recursos\Menu\Fondo_dos.jpg")
        fondo = pygame.transform.scale(fondo, TAMAÑO_PANTALLA)

        # Personaje
        posicion_inicial = (H / 2 - 300, 350)
        tamaño = (110, 120)

        #Enemigos
        posicion_inicial_enemigo_1 = (H / 2 + 150, 180)
        posicion_inicial_enemigo_2 = (H / 2 - 450, 200)
        posicion_inicial_enemigo_3 = (H / 2 + 650, 180)
        tamaño_enemigo = (100, 110)

        # Crear personaje
        mi_personaje = Personaje(tamaño, diccionario_animaciones_personaje, posicion_inicial, velocidad_personaje)
        rectangulo_personaje = mi_personaje.lados
    


        # Crear enemigo
        enemigo1 = Enemigos(tamaño_enemigo, animaciones_enemigo, posicion_inicial_enemigo_1, velocidad_enemigo)
        enemigo2 = Enemigos(tamaño_enemigo, animaciones_enemigo, posicion_inicial_enemigo_2, velocidad_enemigo)
        enemigo3 = Enemigos(tamaño_enemigo, animaciones_enemigo, posicion_inicial_enemigo_3, velocidad_enemigo)
        
        lista_enemigos = []
        lista_enemigos.append(enemigo1)
        lista_enemigos.append(enemigo2)
        lista_enemigos.append(enemigo3)

        

        # Piso
        piso = pygame.Rect(0, 60, W, 20)
        piso.top = H - 200

        Plataforma
        lista_plataformas = []


        def crear_plataforma(x, y, width, height):
            plataforma = Plataforma(x, y, width, height)
            lista_plataformas.append(plataforma)


        plataformas = [
            crear_plataforma(x=890, y=H - 500, width=500, height=80),
            crear_plataforma(x=500, y=H - 360, width=300, height=80),
            crear_plataforma(x=-30, y=H - 440, width=400, height=80)
        ]
        

        #Rectangulos-bordes
        lista_rectangulos = []
        lista_lados_rectangulos = []


        def crear_rectangulo(x, y, width, height):
            rectangulo = Rectangulo(x,y,width,height)
            lista_rectangulos.append(rectangulo)

            lados_rectangulo = rectangulo.lados_rectangulo
            lista_lados_rectangulos.append(lados_rectangulo)
            
        rectangulos = [
            crear_rectangulo(x=320, y=H - 500, width=50, height=50),
            crear_rectangulo(x=900, y=H - 580, width=50, height=50)
        ]
        


        #Corazones
        corazones = Corazones(w=200, h=60)

        #Colision Piso
        lados_piso = obtener_rectangulos(piso)


        # RECTANGULO-PERSONAJE
        x_inicial = H / 2 - 400
        y_inicial = 750

        super().__init__(pantalla, mi_personaje, lista_plataformas, lista_enemigos, lista_rectangulos, lista_lados_rectangulos,lados_piso, fondo, corazones, rectangulo_personaje)