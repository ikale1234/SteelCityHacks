import pygame
import random


class Circle:
    def __init__(self, width, height):
        self.radius = 50
        self.color = (23, 230, 216)
        self.visible = True
        self.width = width
        self.height = height
        self.x = random.randrange(50, width-50)
        self.y = random.randrange(150, height-50)
        self.circlelist = []
        self.tooclose = False
        self.tox = 0
        self.toy = 0
        self.xdiff = 0
        self.ydiff = 0

    def draw(self, win):
        if self.visible:
            pygame.draw.circle(
                win, self.color, (int(self.x), int(self.y)), self.radius)

    def changecolor(self, color):
        self.color = color

    def checkcircledistance(self):

        for i in range(len(self.circlelist)):
            if self.tooclose:
                break
            for j in range(len(self.circlelist)):
                self.xbetween = abs(
                    self.circlelist[i].tox - self.circlelist[j].tox)
                self.ybetween = abs(
                    self.circlelist[i].toy - self.circlelist[j].toy)
                if i != j:
                    if (self.xbetween**2+self.ybetween**2)**0.5 < 200:
                        for k in range(len(self.circlelist)):
                            self.circlelist[k].tox = random.randrange(
                                50, self.width-50)
                            self.circlelist[k].tox = random.randrange(
                                50, self.width-50)
                        self.tooclose = True
                        break
        while self.tooclose:
            self.tooclose = False
            for i in range(len(self.circlelist)):
                if self.tooclose:
                    break
                for j in range(len(self.circlelist)):
                    self.xbetween = abs(
                        self.circlelist[i].tox - self.circlelist[j].tox)
                    self.ybetween = abs(
                        self.circlelist[i].toy - self.circlelist[j].toy)
                    if i != j:
                        if (self.xbetween**2+self.ybetween**2)**0.5 < 200:
                            for k in range(len(self.circlelist)):
                                self.circlelist[k].tox = random.randrange(
                                    50, self.width-50)
                                self.circlelist[k].tox = random.randrange(
                                    50, self.width-50)
                            self.tooclose = True
                            break

    def changepos(self, circlelist):
        self.circlelist = circlelist
        for circle in self.circlelist:
            circle.tox = random.randrange(50, self.width-50)
            circle.toy = random.randrange(150, self.height-50)
        self.checkcircledistance()
        for circle in self.circlelist:
            circle.xdiff = circle.tox - circle.x
            circle.ydiff = circle.toy - circle.y

    def tp(self):
        for circle in self.circlelist:
            circle.x = circle.tox
            circle.y = circle.toy

    def slide(self, step):
        for circle in self.circlelist:
            circle.x += circle.xdiff/step
            circle.y += circle.ydiff/step
