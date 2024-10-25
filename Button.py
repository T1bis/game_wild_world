import pygame

class Button():
    def __init__(self,x,y,size,status=None,color=(0,0,0)):
        self.x = x
        self.y = y
        self.size = size
        self.color = color
        self.status = status

    def params(self):
        return (self.x, self.y, self.size * 70 + 5,
                70)

    def inButton(self, pos):
        params = self.params()
        if pos[0] > params[0] and pos[1] > params[1] and pos[0] < params[0] + params[2] \
                and pos[1] < params[1] + params[3]:
            return True
        else:
            return False