import pygame
from pygame.locals import *
from Interfaz.GUI_form_menu_score import *
from Interfaz.GUI_form import *
from Interfaz.GUI_button_image import *
from Interfaz.GUI_form_final import *
from Interfaz.GUI_VICTORIA import *

class FormContenedorNivel(Form):
    def __init__(self, pantalla: pygame.Surface, nivel):
        super().__init__(pantalla, 0, 0, pantalla.get_width(), pantalla.get_height(), "black" )
        nivel._slave = self._slave
        self.nivel = nivel
        self.fondo = pygame.image.load("Recursos\Menu\Botones/niveles.png")
        self.fondo = pygame.transform.scale(self.fondo, (1400, 900))


        self._btn_home = Button_Image(screen = self._slave,
                master_x = self._x,
                master_y = self._y,
                x = self._w - 100,
                y = self._h - 100,
                w = 50,
                h = 50,
                onclick = self.btn_home_click,
                onclick_param = "",
                path_image = "Recursos\Menu\Botones\settings.png")    
        self.lista_widgets.append(self._btn_home)

    
    def update(self, lista_eventos):
        self.nivel.update(lista_eventos)
        for widget in self.lista_widgets:
            widget.update(lista_eventos)
        self.partida_ganada()
        self.draw()
        


    def btn_home_click(self, param):
        print("entre")
        self.end_dialog()


    def partida_ganada(self):   
        if len(self.nivel.lista_enemigos) == 0:
            self._master.fill("red")
            self.end_dialog()
            
            # interfaz = InterfazNombre()
            # self.show_dialog(interfaz)
            # interfaz.run()




    
