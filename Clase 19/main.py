import pygame, sys
from settings import *
from pygame.locals import *
from class_personaje import *

from nivel import *
from modo import *
from animaciones import *

from nivel_uno import *
from nivel_dos import *
from Interfaz.GUI_form_prueba import * 

import sqlite3

with sqlite3.connect("Mi_base_datos.db") as conexion:
    try:
        # # Crear tabla
        # sentencia = '''
        #     create table Empleados
        #     (
        #         id integer primary key autoincrement,
        #         nombre text,
        #         apellido text,
        #         sueldo real
        #     )
        # '''
        # conexion.execute(sentencia)

        # Insertar datos
        # sentencia = '''
        #     insert into Empleados(nombre, apellido, sueld) values(?,?,?), ("Maria","Paz",3000)
        # '''
        # conexion.execute(sentencia)

        conexion.execute("insert into Empleados(nombre, apellido, sueld) values(?,?,?)", ("Maria","Paz",3000))

        conexion.commit()  # Aplicar los cambios
        print("Tabla creada y datos insertados correctamente")
    except Exception as e:
        print("Error:", str(e))

# Funciones

W, H = 1400, 900
TAMAÑO_PANTALLA = (W, H)
pantalla = pygame.display.set_mode((W, H))
FPS = 18
velocidad_personaje = 10
velocidad_enemigo = 8

form_prueba = FormPrueba(pantalla, 0, 0, W, H, "gold", "BLACK", 5, True)

pygame.init()
    
RELOJ = pygame.time.Clock()
PANTALLA = pygame.display.set_mode(TAMAÑO_PANTALLA)

# Cronometro
tiempo_inicial = 80
tiempo_restante = tiempo_inicial
fuente = pygame.font.SysFont(None, 138)
color_texto = ("black")
pos_texto = (W // 2, H - 550)



def abrir_menu(lista_eventos):
    form_prueba.update(lista_eventos)

while tiempo_restante > 0:
    
    RELOJ.tick(FPS)
    texto = fuente.render(str(int(tiempo_restante)), True, color_texto) 
    texto_rect = texto.get_rect(center=pos_texto)
    PANTALLA.blit(texto, texto_rect)
    
    lista_eventos = pygame.event.get()
    for evento in lista_eventos:
        if evento.type == pygame.QUIT:
            pygame.quit()
            sys.exit(0)

    abrir_menu(lista_eventos)
    pygame.display.update()

    #Cronometro
    tiempo_restante -= RELOJ.get_time() / 1000  # Restar el tiempo transcurrido en cada iteración
    

print("¡Tiempo agotado!")