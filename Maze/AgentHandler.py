from Maze.Properties import *


class setStart:
    __coordinate = None
    def __init__(self, startpoint, map):

        len = Properties().getSize(map)
        scale  = Properties().getSize(map)

        if startpoint is 1:
            self.__coordinate = [0,0]
        elif startpoint is 2:
            self.__coordinate = [0, (len[1]*scale)-scale]
        elif startpoint is 3:
            self.__coordinate = [(len[0]*scale)-scale, 0]
        elif startpoint is 4:
            self.__coordinate = [(len[0]*scale)-scale, (len[1]*scale)-scale]

    def getCoordinate(self):
        return self.__coordinate