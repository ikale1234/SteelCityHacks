import pygame
import random

pygame.init()
win = pygame.display.set_mode((1000, 1000))
pygame.display.set_caption("game")

run = True


class math():
    def __init__(self):
        self.num1 = random.randrange(11)
        self.num2 = random.randrange(11)
        self.question = ""
        self.answer = ""
        self.answerList = []

    def add(self):
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

    def anyMathQuestion(self):
        questionType = [self.add(), self.multi(), self.sub()]
        return questionType[random.randrange(3)]


font1 = pygame.font.SysFont("comicsans", 80, True)

run = math()
question = run.anyMathQuestion()
print(question)
while run:
    win.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if event.type == pygame.MOUSEBUTTONDOWN:
        run = math()
        question = run.anyMathQuestion()
        print(question)
    text = font1.render(question[0], 1, (235, 0, 0))
    win.blit(text, (500 - text.get_width()/2, 500))

    text2 = font1.render(str(question[2]), 1, (235, 0, 0))
    win.blit(text2, (500 - text.get_width()/2, 700))

    text3 = font1.render(str(question[1]), 1, (235, 0, 0))
    win.blit(text3, (500 - text.get_width()/2, 600))
    pygame.display.update()
