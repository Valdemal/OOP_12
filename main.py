import game
import menu
import pygame
from button import Button
from field import Field
import tkinter
import tkinter.filedialog as fd
import os

GAME_NAME = "Карта"
WINDOW_SIZE = (700, 700)
MENU_SIZE = (WINDOW_SIZE[0], 100)
FIELD_SIZE = (WINDOW_SIZE[0], WINDOW_SIZE[1] - MENU_SIZE[1])
MENU_COLOR = (255, 255, 255)
LAND_CELL_COLOR = (225, 150, 57)
WATER_CELL_COLOR = (0, 0, 255)
MENU_BUTTON_COLOR = (154, 171, 187)
MENU_BUTTON_SIZE = (300, 75)


def create_load_button_for_field_menu(field: Field) -> Button:
    def load_map():
        root = tkinter.Tk()
        filetypes = (("Файл карты", "*.map"),)

        filename = fd.askopenfilename(title="Загрузить карту", initialdir=os.getcwd(), filetypes=filetypes)
        root.destroy()

        with open(filename, "r") as file:
            lines = file.readlines()
            matrix = [[int(symbol) for symbol in line.split()] for line in lines]

        field.set_map_matrix(matrix)

    return Button(size=MENU_BUTTON_SIZE, background_color=MENU_BUTTON_COLOR, text="Загрузить карту", action=load_map)


if __name__ == "__main__":
    game = game.Game(WINDOW_SIZE, GAME_NAME)
    menu = menu.Menu(MENU_SIZE, background_color=MENU_COLOR)
    field = Field(FIELD_SIZE, water_cell_color=WATER_CELL_COLOR, land_cell_color=LAND_CELL_COLOR)

    menu.add_button(create_load_button_for_field_menu(field))
    menu.add_button(
        Button(size=MENU_BUTTON_SIZE, background_color=MENU_BUTTON_COLOR, text="Очистить", action=field.clean))
    game.attach_display_elements([field, menu])

    while game.running():
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()

        game.graw()
