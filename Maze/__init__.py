import pygame
from Maze import *
from Maze.Properties import *
from Maze.MazeGenerator import *
from Maze.Map import *


class Maze:

    def __init__(self, map):
        game_map = Map(map).getMazeMap()
        pygame.init()
        properties = Properties()
        screen = CreateWindow(properties, pygame,game_map).getScreen()
        done = False
        MakeMap(screen, pygame, properties,game_map)
        while not done:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    done = True

