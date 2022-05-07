from typing import List, Tuple

import pygame
import pygame.gfxdraw

from display_element import DisplayElement
from map import Map, Point


class Field(DisplayElement):
    __AFTER_CELL_CLICK_DELAY = 200
    __AFTER_CHANGE_FIELD_DELAY = 500

    def __init__(self, size: tuple, land_cell_color: tuple, water_cell_color: tuple):
        super().__init__(size)
        self.__map = Map()
        self.__cell_width = 0
        self.__cell_height = 0
        self.__land_cell_color = land_cell_color
        self.__water_cell_color = water_cell_color

    def set_map_matrix(self, map_matrix: List[list]):
        self.__map = Map(map_matrix)
        self.__cell_width = self.width / self.__map.n if self.__map.n else 0
        self.__cell_height = self.height / self.__map.m if self.__map.m else 0

    def clean(self):
        print("Очищение")
        self.__map.reset_route()
        self.enable()

    def __catch_onclick_action(self, x, y):
        click = pygame.mouse.get_pressed()
        if click[0] == 1:
            mouse_pos = pygame.mouse.get_pos()
            if x < mouse_pos[0] < x + self.width and y < mouse_pos[1] < y + self.height:
                i, j = self.__get_indexes_by_coords(*mouse_pos, x, y)

                if self.__map[i][j] == 1:
                    if self.__map.route_start is None:
                        self.__map.set_route_start(Point(i, j))
                        print("Начало пути:", self.__map.route_start)
                    else:
                        self.__map.set_route_end(Point(i, j))
                        print("Конец пути:", self.__map.route_end)
                        self.disable()

                pygame.time.delay(Field.__AFTER_CELL_CLICK_DELAY)

    def __draw_cell_by_indexes(self, i, j, x, y, display, color):
        draw_x = x + j * self.__cell_width
        draw_y = y + i * self.__cell_height
        pygame.gfxdraw.box(display, pygame.Rect(draw_x, draw_y, self.__cell_width, self.__cell_height),
                           color)

    def draw_route(self, x, y, display, route: List[Tuple[int, int]]):
        print("Путь отрисовывается")
        for i, j in route:
            self.__draw_cell_by_indexes(i, j, x, y, display, (255, 0, 0))
            # pygame.time.delay(200)

    def draw(self, x, y, display):
        pygame.draw.rect(display, self.background_color, (x, y, *self.get_size()))  # убрать после отладки

        self.__draw_cells(x, y, display)

        if self.__map.route_start is not None:
            self.__draw_cell_by_indexes(*self.__map.route_start.to_tuple(), x, y, display, (255, 0, 0))

        if self.__map.route_end is not None:
            self.__draw_cell_by_indexes(*self.__map.route_end.to_tuple(), x, y, display, (255, 0, 0))

        if self.is_enabled():
            self.__catch_onclick_action(x, y)
        else:
            route = [point.to_tuple() for point in self.__map.get_route()]

            self.draw_route(x, y, display, route)
            pygame.time.delay(Field.__AFTER_CHANGE_FIELD_DELAY)

    def __draw_cells(self, x, y, display):
        draw_y = int(y)
        for i in range(self.__map.m):
            draw_x = int(x)
            for j in range(self.__map.n):
                draw_color = self.__land_cell_color if self.__map[i][j] else self.__water_cell_color
                pygame.gfxdraw.box(display, pygame.Rect(draw_x, draw_y, self.__cell_width, self.__cell_height),
                                   draw_color)
                draw_x += int(self.__cell_width)

            draw_y += int(self.__cell_height)

    def __get_indexes_by_coords(self, x, y, draw_x, draw_y) -> Tuple[int, int]:
        i = int(y - draw_y) // int(self.__cell_height)
        j = int(x - draw_x) // int(self.__cell_width)
        return i, j
