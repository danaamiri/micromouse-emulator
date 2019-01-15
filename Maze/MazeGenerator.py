class CreateWindow:
    screen = None
    windowX = 0
    windowY = 0

    def __init__(self, properties, pygame, map):
        xno = len(map)
        yno = len(map[0])
        print(xno)
        print(yno)
        blockSize = properties.getScale()
        self.windowX = blockSize * xno
        self.windowY = blockSize * yno
        self.screen = pygame.display.set_mode((self.windowY, self.windowX,))

    def getScreen(self):
        return self.screen

    def getDimension(self):
        return self.windowX, self.windowY


class MakeMap:
    map = None

    def __init__(self, screen, pg, properties, map):
        self.map = map
        scale = properties.getScale()
        x = 0
        screen.fill((0, 0, 0))
        for i in self.map:
            y = 0
            for j in i:
                if j == 1:
                    color = (255, 100, 0)
                    pg.draw.rect(screen, color, pg.Rect(y*scale, x*scale, scale, scale))
                    pg.display.flip()
                elif j == 's':
                    color = (10, 10, 100)
                    pg.draw.rect(screen, color, pg.Rect(y*scale, x*scale, scale, scale))
                    pg.display.flip()
                elif j == 'g':
                    color = (255, 10, 200)
                    pg.draw.rect(screen, color, pg.Rect(y*scale, x*scale, scale, scale))
                    pg.display.flip()

                y = y + 1
            x = x + 1



