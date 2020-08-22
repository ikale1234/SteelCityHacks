import pygame
import random
width = 1000
height = 900
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Trash Heroes")
pygame.init()


class Label:
    def __init__(self, text, size, color, bg_color, x, y):
        self.text = text
        self.size = size
        self.font = pygame.font.SysFont('arial', size)
        self.color = color
        self.width, self.height = self.font.size(self.text)
        self.bg_color = bg_color
        self.label = self.font.render(self.text, True, color, self.bg_color)
        self.rect = self.label.get_rect()
        self.x = x
        self.y = y
        self.rect.center = (self.x, self.y)
        self.in_rect = False

    def draw(self, win):
        win.blit(self.label, self.rect)

    def checkcursor(self, x, y, color):
        if x > self.x - self.width/2 and x < self.x + self.width/2:
            if y > self.y - self.height/2 and y < self.y + self.height/2:
                self.label = self.font.render(
                    self.text, True, self.color, color)
                self.in_rect = True
            else:
                self.label = self.font.render(
                    self.text, True, self.color, self.bg_color)
                self.in_rect = False
        else:
            self.label = self.font.render(
                self.text, True, self.color, self.bg_color)
            self.in_rect = False

    def changetext(self, text):
        self.label = self.font.render(text, True, self.color, self.bg_color)
        self.rect = self.label.get_rect()
        self.rect.center = (self.x, self.y)

    def changecolor(self, color):
        self.color = color
        self.label = self.font.render(
            self.text, True, self.color, self.bg_color)


class Math():
    def __init__(self):
        self.num1 = random.randrange(11)
        self.num2 = random.randrange(11)
        self.question = ""
        self.answer = ""
        self.answerList = []

    def addition(self):
        self.num1 = random.randrange(11)
        self.num2 = random.randrange(11)
        self.answerList = []
        self.question = "what is " + str(self.num1) + " + "+str(self.num2)+"?"
        self.answer = self.num1+self.num2
        self.answerList.append(self.answer)
        for i in range(5):
            fakeAnswer = random.randrange(21)
            while fakeAnswer in self.answerList:
                fakeAnswer = random.randrange(21)
            self.answerList.append(fakeAnswer)
        return self.question, self.answer, self.answerList


class Circle:
    def __init__(self):
        self.radius = 50
        self.color = (255, 0, 0)
        self.visible = True
        self.x = random.randrange(50, width-50)
        self.y = random.randrange(150, height-50)

    def draw(self):
        if self.visible:
            pygame.draw.circle(win, self.color, (self.x, self.y), self.radius)

    def changecolor(self, color):
        self.color = color

    def changepos(self):
        self.x = random.randrange(50, width-50)
        self.y = random.randrange(150, height-50)


class Game:
    def __init__(self):
        self.run = True
        self.circlelist = []
        self.bg_color = (255, 255, 255)
        self.tooclose = False
        self.math = Math()
        self.question, self.answer, self.answerList = self.math.addition()
        self.qlabel = Label(self.question, 25, (0, 0, 0),
                            (255, 255, 255), width/2, 25)
        self.points = 0
        self.pointsLabel = Label("Points: "+str(self.points), 25, (0, 0, 0),
                                 (255, 255, 255), width/2, 50)

        for i in range(5):
            self.circlelist.append(Circle())
        self.answerLabels = []

    def checkcircledistance(self):
        for i in range(len(self.circlelist)):
            if self.tooclose:
                break
            for j in range(len(self.circlelist)):
                self.xbetween = abs(
                    self.circlelist[i].x - self.circlelist[j].x)
                self.ybetween = abs(
                    self.circlelist[i].y - self.circlelist[j].y)
                if i != j:
                    if (self.xbetween**2+self.ybetween**2)**0.5 < 150:
                        for k in range(len(self.circlelist)):
                            self.circlelist[k].changepos()
                        self.tooclose = True
                        break
        while self.tooclose:
            self.tooclose = False
            for i in range(len(self.circlelist)):
                if self.tooclose:
                    break
                for j in range(len(self.circlelist)):
                    self.xbetween = abs(
                        self.circlelist[i].x - self.circlelist[j].x)
                    self.ybetween = abs(
                        self.circlelist[i].y - self.circlelist[j].y)
                    if i != j:
                        if (self.xbetween**2+self.ybetween**2)**0.5 < 150:
                            for k in range(len(self.circlelist)):
                                self.circlelist[k].changepos()
                            self.tooclose = True
                            break

        self.mousenotpressed = True

    def drawgame(self):
        for circle in self.circlelist:
            circle.draw()
        self.qlabel.draw(win)
        for label in self.answerLabels:
            label.draw(win)
        self.pointsLabel.draw(win)

    def rungame(self):
        self.checkcircledistance()
        for i in range(len(self.circlelist)):
            self.answerLabels.append(Label(str(self.answerList[i]), 25, (0, 0, 0), (
                255, 0, 0), self.circlelist[i].x, self.circlelist[i].y))
        while self.run:
            win.fill(self.bg_color)
            pygame.time.delay(10)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
            self.x, self.y = pygame.mouse.get_pos()
            pygame.event.get()
            if pygame.mouse.get_pressed() == (0, 0, 0):
                self.mousenotpressed = True
            if pygame.mouse.get_pressed() == (1, 0, 0) and self.mousenotpressed:
                for circle in self.circlelist:
                    self.xdiff = abs(self.x-circle.x)
                    self.ydiff = abs(self.y-circle.y)
                    if (self.xdiff**2+self.ydiff**2)**0.5 < 50:
                        if circle == self.circlelist[0]:
                            self.points += 1
                        else:
                            self.points -= 1
                        for circle in self.circlelist:
                            circle.changepos()
                            self.checkcircledistance()
                        self.math = Math()
                        self.question, self.answer, self.answerList = self.math.addition()
                        self.pointsLabel = Label("Points: "+str(self.points), 25, (0, 0, 0),
                                                 (255, 255, 255), width/2, 50)
                        self.qlabel = Label(self.question, 25, (0, 0, 0),
                                            (255, 255, 255), width/2, 25)
                        self.answerLabels = []
                        for i in range(len(self.circlelist)):
                            self.answerLabels.append(Label(str(self.answerList[i]), 25, (0, 0, 0), (
                                255, 0, 0), self.circlelist[i].x, self.circlelist[i].y))

                    self.mousenotpressed = False
            elif pygame.mouse.get_pressed() == (1, 0, 0):
                self.mousenotpressed = False
            self.drawgame()

            pygame.display.update()
        pygame.quit()


game = Game()
game.rungame()
