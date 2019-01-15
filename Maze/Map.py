class Map:
    __maze_map = None

    def __init__(self, inputMap):
        map_file = None
        if type(inputMap) is str:
            map_file = open(inputMap, "r")
        elif type(inputMap) is list:
            self.__maze_map = inputMap
        map_matrix = []
        for line in map_file.readlines():
            x = []
            for a in line:
                if a is not "\n":
                    x.append(int(a))
            map_matrix.append(x)
        self.__maze_map = map_matrix

    def getMazeMap(self):
        return self.__maze_map









