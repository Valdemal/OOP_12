from typing import List, Tuple
import copy


class Point:
    def __init__(self, x: int, y: int):
        self.x = x
        self.y = y

    def __eq__(self, other) -> bool:
        return self.x == other.x and self.y == other.y

    def __ne__(self, other) -> bool:
        return not self == other

    def __str__(self) -> str:
        return f'({self.x}, {self.y})'

    def to_tuple(self) -> Tuple[int, int]:
        return self.x, self.y

    def distance(self, other) -> int:
        return abs(self.x - other.x) + abs(self.y - other.y) + 1


class Map:
    def __init__(self, matrix: List[List[int]] = None):
        self.__map_matrix = copy.deepcopy(matrix)
        self.__route_start = None
        self.__route_end = None
        self.__route = None
        self.__m = len(matrix) if matrix else 0
        self.__n = len(matrix[0]) if self.__m > 0 else 0

    def __getitem__(self, index: int) -> List[int]:
        return self.__map_matrix[index]

    @property
    def n(self):
        return self.__n

    @property
    def m(self):
        return self.__m

    @property
    def route_start(self) -> Point or None:
        return self.__route_start

    @property
    def route_end(self) -> Point or None:
        return self.__route_end

    def set_route_start(self, start: Point):
        self.__route_start = start

    def set_route_end(self, end: Point):
        self.__route_end = end

    def reset_route(self):
        self.__route = self.__route_start = self.__route_end = None

    def get_route(self) -> List[Point]:
        if self.__route is None:
            matrix_copy = copy.deepcopy(self.__map_matrix)

            self.__route = self.__get_shortest_path_between_points(
                matrix_copy,
                self.route_start,
                self.route_end,
                [self.route_start])

        return self.__route

    def __get_directions(self, map_matrix: List[list], start: Point, end: Point) -> List[Point]:
        possible_directions = [Point(start.x + 1, start.y),
                               Point(start.x - 1, start.y),
                               Point(start.x, start.y + 1),
                               Point(start.x, start.y - 1)]
        res = []

        for point in possible_directions:
            if 0 <= point.x < self.m and 0 <= point.y < self.n:
                if map_matrix[point.x][point.y] == 1:
                    if point == end:
                        return [point]
                else:
                    res.append(point)

        return sorted(res, key=lambda p: end.distance(p))

    def __get_shortest_path_between_points(self, map_matrix: List[list],
                                           start: Point, end: Point,
                                           route: List[Point]) -> List[Point] or None:

        if start == end:
            return route

        # ?????????????????? ?????????????????? ????????, ?????????? ?????????? ???????? ???? ?????? ?? ?????? ??????????????????????
        map_matrix[start.x][start.y] = 1

        shortest_route = None
        directions = self.__get_directions(map_matrix, start, end)

        for point in directions:
            last_route = self.__get_shortest_path_between_points(map_matrix, point, end, route + [point])

            if not shortest_route or (last_route and len(last_route) < len(shortest_route)):
                shortest_route = last_route

        return shortest_route
