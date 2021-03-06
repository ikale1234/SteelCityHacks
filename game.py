import pygame
import random
import time
from label_class import Label
from math_class import Math
from circle_class import Circle
width = 1280
height = 768
win = pygame.display.set_mode((width, height))
pygame.display.set_caption("Quick Maths")
pygame.init()


class Game:
    def __init__(self):
        self.run = True
        self.circlelist = []
        self.bg_color = (255, 255, 255)
        self.hover_color = (66, 167, 245)
        self.circle_color = (23, 230, 216)
        self.bg = pygame.image.load("background.jpg")
        self.tooclose = False
        self.math = Math()
        self.points = 0
        self.points_label = Label("Points: "+str(self.points), 25, (0, 0, 0),
                                  (255, 255, 255), width*0.9, 25)

        self.game_title_label = Label("Quick Maths", 40, (0, 0, 0),
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
        self.choose_diff_label = Label("Choose Level", 32, (0, 0, 0),
                                       (255, 255, 255), width/2, 500)
        self.diff_1_label = Label("1", 30, (0, 0, 0),
                                  (255, 255, 255), width*0.35, 600)
        self.diff_2_label = Label("2", 30, (0, 0, 0),
                                  (255, 255, 255), width*0.45, 600)
        self.diff_3_label = Label("3", 30, (0, 0, 0),
                                  (255, 255, 255), width*0.55, 600)
        self.diff_4_label = Label("4", 30, (0, 0, 0),
                                  (255, 255, 255), width*0.65, 600)

        self.stage = "start"
        for i in range(5):
            self.circlelist.append(Circle(width, height))
        self.allcircles = Circle(width, height)
        self.allcircles.changepos(self.circlelist)
        self.allcircles.tp()
        self.answerLabels = []
        self.mousenotpressed = True
        self.circlemove = False
        self.circlesteps = 0
        self.new_question = False
        self.wrongsound = pygame.mixer.Sound("wrong.wav")
        self.rightsound = pygame.mixer.Sound("correct.wav")

    def drawgame(self):
        win.blit(self.bg, [0, 0])
        if self.stage == "start":
            self.game_title_label.draw(win)
            self.choose_diff_label.draw(win)
            self.diff_1_label.draw(win)
            self.diff_2_label.draw(win)
            self.diff_3_label.draw(win)
            self.diff_4_label.draw(win)

        if self.stage == "choose mode":
            self.choose_mode_label.draw(win)
            self.add_label.draw(win)
            self.subtract_label.draw(win)
            self.multiply_label.draw(win)
            self.divide_label.draw(win)

        if self.stage == "game":
            for circle in self.circlelist:
                circle.draw(win)
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

    def startgame(self, mode):
        self.mode = mode
        self.question, self.answer, self.answerList = self.math.get_question(
            self.mode, self.difficulty)
        random.shuffle(self.answerList)
        for i in range(len(self.answerList)):
            if self.answerList[i] == self.answer:
                self.index = i
        self.qlabel = Label(self.question, 30, (0, 0, 0),
                            (255, 255, 255), width/2, 25)
        for i in range(len(self.circlelist)):
            self.answerLabels.append(Label(str(self.answerList[i]), 25, (
                0, 0, 0), self.circle_color, self.circlelist[i].x, self.circlelist[i].y))
        self.stage = "game"
        self.set_timer()

    def rungame(self):
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
                    if self.diff_1_label.in_rect:
                        self.stage = "choose mode"
                        self.difficulty = 1
                    if self.diff_2_label.in_rect:
                        self.stage = "choose mode"
                        self.difficulty = 2
                    if self.diff_3_label.in_rect:
                        self.stage = "choose mode"
                        self.difficulty = 3
                    if self.diff_4_label.in_rect:
                        self.stage = "choose mode"
                        self.difficulty = 4

                elif pygame.mouse.get_pressed() == (1, 0, 0):
                    self.mousenotpressed = False
                self.diff_1_label.checkcursor(self.x, self.y, self.hover_color)
                self.diff_2_label.checkcursor(self.x, self.y, self.hover_color)
                self.diff_3_label.checkcursor(self.x, self.y, self.hover_color)
                self.diff_4_label.checkcursor(self.x, self.y, self.hover_color)
            if self.stage == "choose mode":
                pygame.event.get()
                if pygame.mouse.get_pressed() == (0, 0, 0):
                    self.mousenotpressed = True
                if pygame.mouse.get_pressed() == (1, 0, 0) and self.mousenotpressed:
                    self.mousenotpressed = False
                    if self.add_label.in_rect:
                        self.startgame("addition")

                    if self.subtract_label.in_rect:
                        self.startgame("subtraction")
                    if self.multiply_label.in_rect:
                        self.startgame("multiplication")
                    if self.divide_label.in_rect:

                        self.startgame("division")
                elif pygame.mouse.get_pressed() == (1, 0, 0):
                    self.mousenotpressed = False
                self.add_label.checkcursor(self.x, self.y, self.hover_color)
                self.subtract_label.checkcursor(
                    self.x, self.y, self.hover_color)
                self.multiply_label.checkcursor(
                    self.x, self.y, self.hover_color)
                self.divide_label.checkcursor(
                    self.x, self.y, self.hover_color)

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
                    for i in range(len(self.circlelist)):
                        self.xdiff = abs(self.x-self.circlelist[i].x)
                        self.ydiff = abs(self.y-self.circlelist[i].y)
                        if (self.xdiff**2+self.ydiff**2)**0.5 < 50 and self.circlemove == False:
                            if self.circlelist[i] == self.circlelist[self.index]:
                                self.points += 1
                                self.circlelist[i].changecolor((0, 255, 0))
                                self.answerLabels[i] = Label(str(self.answerList[i]), 25, (0, 0, 0), (
                                    0, 255, 0), self.circlelist[i].x, self.circlelist[i].y)
                                self.rightsound.play()

                            else:
                                if self.points > 0:
                                    self.points -= 1
                                self.circlelist[i].changecolor((255, 0, 0))
                                self.answerLabels[i] = Label(str(self.answerList[i]), 25, (0, 0, 0), (
                                    255, 0, 0), self.circlelist[i].x, self.circlelist[i].y)
                                self.circlelist[self.index].changecolor(
                                    (0, 255, 0))
                                self.answerLabels[self.index] = Label(str(self.answerList[self.index]), 25, (0, 0, 0), (
                                    0, 255, 0), self.circlelist[self.index].x, self.circlelist[self.index].y)
                                self.wrongsound.play()
                            self.allcircles.changepos(self.circlelist)
                            self.circlemove = True

                if self.circlemove:
                    self.allcircles.slide(45)
                    self.circlesteps += 1
                    for i in range(len(self.answerLabels)):
                        self.answerLabels[i].changepos(
                            self.circlelist[i].x, self.circlelist[i].y)
                    if self.circlesteps == 45:
                        self.circlemove = False
                        self.circlesteps = 0
                        self.new_question = True
                if self.new_question:
                    for circle in self.circlelist:
                        circle.changecolor(self.circle_color)

                    self.new_question = False
                    self.question, self.answer, self.answerList = self.math.get_question(
                        self.mode, self.difficulty)
                    random.shuffle(self.answerList)
                    for i in range(len(self.answerList)):
                        if self.answerList[i] == self.answer:
                            self.index = i

                    self.points_label = Label("Points: "+str(self.points), 25, (0, 0, 0),
                                              (255, 255, 255), width*0.9, 25)
                    self.qlabel = Label(self.question, 30, (0, 0, 0),
                                        (255, 255, 255), width/2, 25)
                    self.answerLabels = []
                    for i in range(len(self.circlelist)):
                        self.answerLabels.append(Label(str(self.answerList[i]), 25, (
                            0, 0, 0), self.circle_color, self.circlelist[i].x, self.circlelist[i].y))

                elif pygame.mouse.get_pressed() == (1, 0, 0):
                    self.mousenotpressed = False

            if self.stage == "end":
                pygame.event.get()
                if pygame.mouse.get_pressed() == (0, 0, 0):
                    self.mousenotpressed = True
                if pygame.mouse.get_pressed() == (1, 0, 0) and self.mousenotpressed:
                    self.mousenotpressed = False
                    if self.play_again_label.in_rect:
                        self.stage = "start"
                        self.points = 0
                        self.allcircles.changepos(self.circlelist)
                        self.answerLabels = []
                        self.play_again_label.in_rect = False
                        self.add_label.in_rect = False
                        self.subtract_label.in_rect = False
                        self.multiply_label.in_rect = False
                        self.divide_label.in_rect = False
                        self.diff_1_label.in_rect = False
                        self.diff_2_label.in_rect = False
                        self.diff_3_label.in_rect = False
                        self.diff_4_label.in_rect = False
                elif pygame.mouse.get_pressed() == (1, 0, 0):
                    self.mousenotpressed = False
                self.play_again_label.checkcursor(
                    self.x, self.y, self.hover_color)

            self.drawgame()

            pygame.display.update()
        pygame.quit()


game = Game()
game.rungame()
