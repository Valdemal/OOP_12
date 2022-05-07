from array import array
from re import L, match
import string

from map import Map, Point

# class Map:
#     UP = 0
#     BOTTOM = 1
#     LEFT = 2
#     RIGHT = 3
#
#     def __init__(self, srcPoint, destPoint) -> None:
#         self.__mapMatrix = []
#         self.__srcPoint = srcPoint
#         self.__destPoint = destPoint
#         self.__n = None
#         self.__m = None
#
#     def readMapFromFile(self, fileName: string) -> None:
#         f = open(fileName)
#
#         for line in f:
#             self.__mapMatrix.append([int(x) for x in line.split()])
#
#         self.__n = len(self.__mapMatrix)
#         self.__m = len(self.__mapMatrix[0])
#
#         f.close()
#
#     def getShortestPathBetweenPoint(self, mapMatrix=None, x=None, y=None, path=None) -> list:
#
#         if mapMatrix == None:
#             mapMatrix = self.__mapMatrix.copy()
#
#         if x == None and y == None:
#             x = self.__srcPoint[0]
#             y = self.__srcPoint[1]
#
#         def try_next(x, y):
#             ' Next position we can try '
#             return [(a, b) for a, b in [(x - 1, y), (x, y - 1), (x + 1, y), (x, y + 1)] if
#                     0 <= a < self.__n and 0 <= b < self.__m]
#
#         if path is None:
#             path = [self.__srcPoint]
#
#         if x == self.__destPoint[0] and y == self.__destPoint[1]:
#             return path
#
#         self.__mapMatrix[self.__destPoint[0]][self.__destPoint[1]] = 0
#
#         mapMatrix[x][y] = 1
#
#         shortestPath = None
#         for a, b in try_next(x, y):
#             if not mapMatrix[a][b]:
#                 last_path = self.getShortestPathBetweenPoint(mapMatrix, a, b, path + [(a, b)])
#
#                 if not shortestPath:
#                     shortestPath = last_path
#                 elif last_path and len(last_path) < len(shortestPath):
#                     shortestPath = last_path
#
#         mapMatrix[x][y] = 0
#
#         return shortestPath
#
#     def __getDirection(self, lastPoint, nextPoint) -> int:
#         if lastPoint[0] == nextPoint[0]:
#             if lastPoint[1] - nextPoint[1] < 0:
#                 return self.RIGHT
#             else:
#                 return self.LEFT
#
#         if lastPoint[1] == nextPoint[1]:
#             if lastPoint[0] - nextPoint[0] > 0:
#                 return self.UP
#             else:
#                 return self.BOTTOM
#
#     def printMapWithShortPath(self, shortestPath: list) -> None:
#         tempMap = self.__mapMatrix.copy()
#
#         start = shortestPath.pop(0)
#         tempMap[start[0]][start[1]] = "S"
#
#         end = shortestPath.pop()
#         tempMap[end[0]][end[1]] = "E"
#
#         lastPoint = start
#
#         for point in shortestPath:
#             direction = self.__getDirection(lastPoint, point)
#
#             if direction == self.UP:
#                 tempMap[point[0]][point[1]] = "|"
#             elif direction == self.BOTTOM:
#                 tempMap[point[0]][point[1]] = "|"
#             elif direction == self.RIGHT:
#                 tempMap[point[0]][point[1]] = ">"
#             elif direction == self.LEFT:
#                 tempMap[point[0]][point[1]] = "<"
#
#             lastPoint = point
#
#         for row in tempMap:
#             for el in row:
#                 print(el, end="  ")
#             print()
#

filename = 'examples/test.map'

with open(filename, "r") as file:
    lines = file.readlines()
    matrix = [[int(symbol) for symbol in line.split()] for line in lines]

m = Map(matrix)

m.set_route_start(Point(1, 2))
m.set_route_end(Point(3, 4))

route = m.get_route()

for point in route:
    print(point)