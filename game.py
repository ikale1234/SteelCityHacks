import pygame
import random
import time
import threading
width = 1000
height = 900
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Cool Math Game")
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

    def multiplication(self):
        self.num1 = random.randrange(11)
        self.num2 = random.randrange(11)
        self.answerList = []
        self.question = "what is " + str(self.num1) + " * "+str(self.num2)+"?"
        self.answer = self.num1*self.num2
        self.answerList.append(self.answer)
        for i in range(5):
            fakeAnswer = random.randrange(100)
            while fakeAnswer in self.answerList:
                fakeAnswer = random.randrange(100)
            self.answerList.append(fakeAnswer)
        return self.question, self.answer, self.answerList

    def subtraction(self):
        self.num1 = random.randrange(11)
        self.num2 = random.randrange(11)
        self.answerList = []
        if self.num1 > self.num2:
            self.answer = self.num1 - self.num2
            self.question = "what is " + \
                str(self.num1) + " - "+str(self.num2)+"?"
        else:
            self.answer = self.num2 - self.num1
            self.question = "what is " + \
                str(self.num2) + " - "+str(self.num1)+"?"
        self.answerList.append(self.answer)
        for i in range(5):
            fakeAnswer = random.randrange(11)
            while fakeAnswer in self.answerList:
                fakeAnswer = random.randrange(11)
            self.answerList.append(fakeAnswer)
        return self.question, self.answer, self.answerList

    def division(self):
        self.num1 = random.randrange(10, 100)
        self.num2 = random.randrange(1, 11)
        self.answerList = []
        while self.num1 % self.num2 != 0:
            self.num1 = random.randrange(10, 100)
            self.num2 = random.randrange(1, 11)
        self.answer = int(self.num1/self.num2)
        self.question = "what is " + str(self.num1) + " / "+str(self.num2)+"?"
        self.answerList.append(self.answer)
        for i in range(5):
            fakeAnswer = random.randrange(100)
            while fakeAnswer in self.answerList:
                fakeAnswer = random.randrange(100)
            self.answerList.append(fakeAnswer)
        return self.question, self.answer, self.answerList

    def get_question(self, mode):
        if mode == 'addition':
            question = self.addition()
        if mode == 'subtraction':
            question = self.subtraction()
        if mode == 'multiplication':
            question = self.multiplication()
        if mode == 'division':
            question = self.division()
        return question

    def anyMathQuestion(self):
        questionType = [self.addition(), self.multiplication(),
                        self.subtraction()]
        return questionType[random.randrange(3)]


class Circle:
    def __init__(self):
        self.radius = 50
        self.color = (23, 230, 216)
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
        self.points = 0
        self.points_label = Label("Points: "+str(self.points), 25, (0, 0, 0),
                                  (255, 255, 255), width*0.9, 25)
        self.play_label = Label("Play Game", 25, (0, 0, 0),
                                (255, 255, 255), width/2, 650)
        self.game_title_label = Label("Cool Math Game", 40, (0, 0, 0),
                                      (255, 255, 255), width/2, 150)
        self.choose_mode_label = Label("Choose Mode", 40, (0, 0, 0),
                                       (255, 255, 255), width/2, 150)
        self.add_label = Label("Addition", 25, (0, 0, 0),
                               (255, 255, 255), width/5, 550)
        self.subtract_label = Label("Subtraction", 25, (0, 0, 0),
                                    (255, 255, 255), 2*(width/5), 550)
        self.multiply_label = Label("Multiplication", 25, (0, 0, 0),
                                    (255, 255, 255), 3*(width/5), 550)
        self.divide_label = Label("Division", 25, (0, 0, 0),
                                  (255, 255, 255), 4*(width/5), 550)
        self.end_label = Label("You ended up with " + str(self.points) + " points.", 35, (0, 0, 0),
                               (255, 255, 255), width/2, 150)
        self.play_again_label = Label("Play Again", 25, (0, 0, 0),
                                      (255, 255, 255), width/2, 650)
        self.add1_label = Label("1 Digit Addition", 20, (0, 0, 0),
                                (255, 255, 255), width/5, 550)
        self.stage = "start"
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
                    if (self.xbetween**2+self.ybetween**2)**0.5 < 200:
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
                        if (self.xbetween**2+self.ybetween**2)**0.5 < 200:
                            for k in range(len(self.circlelist)):
                                self.circlelist[k].changepos()
                            self.tooclose = True
                            break

        self.mousenotpressed = True

    def drawgame(self):
        if self.stage == "start":
            self.game_title_label.draw(win)
            self.play_label.draw(win)

        if self.stage == "choose mode":
            self.choose_mode_label.draw(win)
            self.add_label.draw(win)
            self.subtract_label.draw(win)
            self.multiply_label.draw(win)
            self.divide_label.draw(win)

        if self.stage == "game":
            for circle in self.circlelist:
                circle.draw()
            self.qlabel.draw(win)
            for label in self.answerLabels:
                label.draw(win)
            self.points_label.draw(win)
            self.timer_label.draw(win)

        if self.stage == "end":
            self.end_label.draw(win)
            self.play_again_label.draw(win)

    def set_timer(self):
        self.start_time = pygame.time.get_ticks()
        self.timer_label = Label("Time Left: " + str(int(30)), 25, (0, 0, 0),
                                 (255, 255, 255), width*0.1, 25)

    def rungame(self):
        self.checkcircledistance()
        while self.run:
            win.fill(self.bg_color)
            pygame.time.delay(10)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    self.run = False
            self.x, self.y = pygame.mouse.get_pos()

            if self.stage == "start":
                pygame.event.get()
                if pygame.mouse.get_pressed() == (0, 0, 0):
                    self.mousenotpressed = True
                if pygame.mouse.get_pressed() == (1, 0, 0) and self.mousenotpressed:
                    self.mousenotpressed = False
                    if self.play_label.in_rect:
                        self.stage = "choose mode"

                elif pygame.mouse.get_pressed() == (1, 0, 0):
                    self.mousenotpressed = False
                self.play_label.checkcursor(self.x, self.y, (128, 128, 128))

            if self.stage == "choose mode":
                pygame.event.get()
                if pygame.mouse.get_pressed() == (0, 0, 0):
                    self.mousenotpressed = True
                if pygame.mouse.get_pressed() == (1, 0, 0) and self.mousenotpressed:
                    self.mousenotpressed = False
                    if self.add_label.in_rect:

                        self.mode = "addition"
                        self.question, self.answer, self.answerList = self.math.get_question(
                            self.mode)
                        self.qlabel = Label(self.question, 30, (0, 0, 0),
                                            (255, 255, 255), width/2, 25)
                        for i in range(len(self.circlelist)):
                            self.answerLabels.append(Label(str(self.answerList[i]), 25, (0, 0, 0), (
                                23, 230, 216), self.circlelist[i].x, self.circlelist[i].y))
                        self.stage = "game"
                        self.set_timer()
                    if self.subtract_label.in_rect:

                        self.mode = "subtraction"
                        self.question, self.answer, self.answerList = self.math.get_question(
                            self.mode)
                        self.qlabel = Label(self.question, 30, (0, 0, 0),
                                            (255, 255, 255), width/2, 25)
                        for i in range(len(self.circlelist)):
                            self.answerLabels.append(Label(str(self.answerList[i]), 25, (0, 0, 0), (
                                23, 230, 216), self.circlelist[i].x, self.circlelist[i].y))
                        self.stage = "game"
                        self.set_timer()
                    if self.multiply_label.in_rect:

                        self.mode = "multiplication"
                        self.question, self.answer, self.answerList = self.math.get_question(
                            self.mode)
                        self.qlabel = Label(self.question, 30, (0, 0, 0),
                                            (255, 255, 255), width/2, 25)
                        for i in range(len(self.circlelist)):
                            self.answerLabels.append(Label(str(self.answerList[i]), 25, (0, 0, 0), (
                                23, 230, 216), self.circlelist[i].x, self.circlelist[i].y))
                        self.stage = "game"
                        self.set_timer()
                    if self.divide_label.in_rect:

                        self.mode = "division"
                        self.question, self.answer, self.answerList = self.math.get_question(
                            self.mode)
                        self.qlabel = Label(self.question, 30, (0, 0, 0),
                                            (255, 255, 255), width/2, 25)
                        for i in range(len(self.circlelist)):
                            self.answerLabels.append(Label(str(self.answerList[i]), 25, (0, 0, 0), (
                                23, 230, 216), self.circlelist[i].x, self.circlelist[i].y))
                        self.stage = "game"
                        self.set_timer()
                elif pygame.mouse.get_pressed() == (1, 0, 0):
                    self.mousenotpressed = False
                self.add_label.checkcursor(self.x, self.y, (128, 128, 128))
                self.subtract_label.checkcursor(
                    self.x, self.y, (128, 128, 128))
                self.multiply_label.checkcursor(
                    self.x, self.y, (128, 128, 128))
                self.divide_label.checkcursor(
                    self.x, self.y, (128, 128, 128))

            if self.stage == "game":
                self.time_now = pygame.time.get_ticks()
                self.time_diff = (self.time_now-self.start_time)/1000
                self.timer_label = Label("Time Left: " + str(int(30 - self.time_diff)), 25, (0, 0, 0),
                                         (255, 255, 255), width*0.1, 25)
                if 30 - self.time_diff <= 0:
                    self.stage = "end"
                    self.end_label = Label("You ended up with " + str(self.points) + " points.", 35, (0, 0, 0),
                                           (255, 255, 255), width/2, 150)

                pygame.event.get()
                if pygame.mouse.get_pressed() == (0, 0, 0):
                    self.mousenotpressed = True
                if pygame.mouse.get_pressed() == (1, 0, 0) and self.mousenotpressed:
                    self.mousenotpressed = False
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
                            self.question, self.answer, self.answerList = self.math.get_question(
                                self.mode)
                            self.points_label = Label("Points: "+str(self.points), 25, (0, 0, 0),
                                                      (255, 255, 255), width*0.9, 25)
                            self.qlabel = Label(self.question, 30, (0, 0, 0),
                                                (255, 255, 255), width/2, 25)
                            self.answerLabels = []
                            for i in range(len(self.circlelist)):
                                self.answerLabels.append(Label(str(self.answerList[i]), 25, (0, 0, 0), (
                                    23, 230, 216), self.circlelist[i].x, self.circlelist[i].y))

                elif pygame.mouse.get_pressed() == (1, 0, 0):
                    self.mousenotpressed = False

            if self.stage == "end":
                pygame.event.get()
                if pygame.mouse.get_pressed() == (0, 0, 0):
                    self.mousenotpressed = True
                if pygame.mouse.get_pressed() == (1, 0, 0) and self.mousenotpressed:
                    self.mousenotpressed = False
                    if self.play_again_label.in_rect:
                        self.stage = "choose mode"
                        self.points = 0
                        for circle in self.circlelist:
                            circle.changepos()
                        self.checkcircledistance()
                        self.answerLabels = []
                        self.play_again_label.in_rect = False
                        self.add_label.in_rect = False
                        self.subtract_label.in_rect = False
                        self.multiply_label.in_rect = False
                        self.divide_label.in_rect = False
                elif pygame.mouse.get_pressed() == (1, 0, 0):
                    self.mousenotpressed = False
                self.play_again_label.checkcursor(
                    self.x, self.y, (128, 128, 128))

            self.drawgame()

            pygame.display.update()
        pygame.quit()


game = Game()
game.rungame()
