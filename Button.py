import pygame

class Button():
    def __init__(self,x,y,status=None,color=(0,0,0)):
        self.x = x
        self.y = y
        self.color = color
        self.status = status
        self.font = pygame.font.SysFont('broadway', 40)

    def params(self):
        return (self.x, self.y, self.x+140,self.y+70)

    def inButton(self, pos):
        params = self.params()
        if pos[0] > params[0] and pos[1] > params[1] and pos[0] < params[0] + params[2] \
                and pos[1] < params[1] + params[3]:
            return True
        else:
            return False

    def is_triggered(self,pos,menu):
        if self.inButton(pos) is True:
            if self.status == "Play":
                menu.set_status('on')
                return "play"
            if self.status == "Quit":
                return "endgame"

    def draw(self,screen):
        pygame.draw.rect(screen,(154,205,50),(self.params()[0]-10,self.params()[1]-5,self.params()[0]+15,self.params()[2]/3-20),5)
        screen.blit(self.font.render(self.status, True, (0, 71, 49)),(self.x, self.y))