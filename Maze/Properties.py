class Properties:
    __scale = 50

    def getScale(self):
        return self.__scale

    def getSize(self, map):
        x = len(map)
        y = len(map[0])

        return x, y


