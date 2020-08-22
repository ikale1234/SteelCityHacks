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

    def _addition1(self):
        self.answerList = []
        self.num1 = random.randrange(10)
        self.num2 = random.randrange(10)
        self.answer = self.num1+self.num2
        while self.answer > 9:
            self.num1 = random.randrange(10)
            self.num2 = random.randrange(10)
            self.answer = self.num1+self.num2
        self.answerList.append(self.answer)
        self.question = "what is " + \
            str(self.num1) + " + "+str(self.num2)+"?"
        for i in range(5):
            fakeAnswer = random.randrange(21)
            while fakeAnswer in self.answerList:
                fakeAnswer = random.randrange(21)
            self.answerList.append(fakeAnswer)
        return self.question, self.answer, self.answerList

    def _addition2(self):
        self.answerList = []
        self.num1 = random.randrange(10)
        self.num2 = random.randrange(10)
        self.answer = self.num1+self.num2
        while self.answer < 10:
            self.num1 = random.randrange(10)
            self.num2 = random.randrange(10)
            self.answer = self.num1+self.num2
        self.answerList.append(self.answer)
        self.question = "what is " + \
            str(self.num1) + " + "+str(self.num2)+"?"
        for i in range(5):
            fakeAnswer = random.randrange(21)
            while fakeAnswer in self.answerList:
                fakeAnswer = random.randrange(21)
            self.answerList.append(fakeAnswer)
        return self.question, self.answer, self.answerList

    def _addition3(self):
        self.answerList = []
        self.answer = random.randrange(10, 100)
        digit2 = self.answer % 10
        digit1 = self.answer//10
        numdigit1 = random.randrange(digit1+1)
        numdigit2 = random.randrange(digit2+1)
        self.num1 = (numdigit1 * 10) + numdigit2
        self.num2 = self.answer - self.num1
        self.answerList.append(self.answer)
        self.question = "what is " + \
            str(self.num1) + " + "+str(self.num2)+"?"
        for i in range(5):
            fakeAnswer = random.randrange(21)
            while fakeAnswer in self.answerList:
                fakeAnswer = random.randrange(21)
            self.answerList.append(fakeAnswer)
        return self.question, self.answer, self.answerList

    def _addition4(self):
        self.answerList = []
        digit2 = random.randrange(0, 9)
        digit1 = random.randrange(2, 10)
        self.answer = (digit1 * 10) + digit2
        numdigit1 = random.randrange(digit1)
        numdigit2 = random.randrange(digit2+1, 10)
        self.num1 = (numdigit1 * 10) + numdigit2
        self.num2 = self.answer - self.num1
        self.answerList.append(self.answer)
        self.question = "what is " + \
            str(self.num1) + " + "+str(self.num2)+"?"
        for i in range(5):
            fakeAnswer = random.randrange(21)
            while fakeAnswer in self.answerList:
                fakeAnswer = random.randrange(21)
            self.answerList.append(fakeAnswer)
        return self.question, self.answer, self.answerList

    def addition(self, difficulty):
        if difficulty == 1:
            return self._addition1()
        if difficulty == 2:
            return self._addition2()
        if difficulty == 3:
            return self._addition3()
        if difficulty == 4:
            return self._addition4()
        return self._addition1()

    def _multiplication1(self):
        multiplediff = [1, 10]
        self.num2 = random.randrange(1, 13)
        self.num1 = multiplediff[random.randrange(2)]
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

    def _multiplication2(self):
        multiplediff = [2, 5, 11]
        self.num2 = random.randrange(1, 13)
        self.num1 = multiplediff[random.randrange(3)]
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

    def _multiplication3(self):
        multiplediff = [3, 4, 6, 7]
        self.num2 = random.randrange(1, 13)
        self.num1 = multiplediff[random.randrange(4)]
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

    def _multiplication4(self):
        multiplediff = [8, 9, 12]
        self.num2 = random.randrange(1, 13)
        self.num1 = multiplediff[random.randrange(3)]
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

    def multiplication(self, difficulty):
        if difficulty == 1:
            return self._multiplication1()
        if difficulty == 2:
            return self._multiplication2()
        if difficulty == 3:
            return self._multiplication3()
        if difficulty == 4:
            return self._multiplication4()
        return self._multiplication1()

    def _subtraction1(self):
        self.answer = random.randrange(10)
        self.num1 = random.randrange(self.answer, 10)
        self.num2 = self.num1 - self.answer
        self.answerList = []
        print(self.num1, self.num2)
        if self.num1 > self.num2:
            self.question = "what is " + \
                str(self.num1) + " - "+str(self.num2)+"?"
        else:
            self.question = "what is " + \
                str(self.num2) + " - "+str(self.num1)+"?"
        self.answerList.append(self.answer)
        for i in range(5):
            fakeAnswer = random.randrange(11)
            while fakeAnswer in self.answerList:
                fakeAnswer = random.randrange(11)
            self.answerList.append(fakeAnswer)
        return self.question, self.answer, self.answerList

    def _subtraction2(self):
        self.num1 = random.randrange(10, 100)
        self.num2 = random.randrange(10)
        self.answerList = []
        if self.num1 > self.num2:
            self.question = "what is " + \
                str(self.num1) + " - "+str(self.num2)+"?"
            self.answer = self.num1 - self.num2
        else:
            self.question = "what is " + \
                str(self.num2) + " - "+str(self.num1)+"?"
            self.answer = self.num2 - self.num1
        self.answerList.append(self.answer)
        for i in range(5):
            fakeAnswer = random.randrange(11)
            while fakeAnswer in self.answerList:
                fakeAnswer = random.randrange(11)
            self.answerList.append(fakeAnswer)
        return self.question, self.answer, self.answerList

    def _subtraction3(self):
        self.answer = random.randrange(100)
        digit2 = self.answer % 10
        digit1 = self.answer//10
        numdigit1 = random.randrange(digit1, 10)
        numdigit2 = random.randrange(digit2, 10)
        self.num1 = (numdigit1 * 10) + numdigit2
        self.num2 = self.num1 - self.answer
        self.answerList = []
        print(self.num1, self.num2)
        if self.num1 > self.num2:
            self.question = "what is " + \
                str(self.num1) + " - "+str(self.num2)+"?"
        else:
            self.question = "what is " + \
                str(self.num2) + " - "+str(self.num1)+"?"
        self.answerList.append(self.answer)
        for i in range(5):
            fakeAnswer = random.randrange(11)
            while fakeAnswer in self.answerList:
                fakeAnswer = random.randrange(11)
            self.answerList.append(fakeAnswer)
        return self.question, self.answer, self.answerList

    def _subtraction4(self):
        self.answerList = []
        digit2 = random.randrange(1, 10)
        digit1 = random.randrange(0, 9)
        print(digit1, digit2)
        self.answer = (digit1 * 10) + digit2
        numdigit1 = random.randrange(digit1+1, 10)
        numdigit2 = random.randrange(digit2)
        self.num1 = (numdigit1 * 10) + numdigit2
        self.num2 = self.num1 - self.answer
        self.answerList = []
        print(self.num1, self.num2)
        if self.num1 > self.num2:
            self.question = "what is " + \
                str(self.num1) + " - "+str(self.num2)+"?"
        else:
            self.question = "what is " + \
                str(self.num2) + " - "+str(self.num1)+"?"
        self.answerList.append(self.answer)
        for i in range(5):
            fakeAnswer = random.randrange(11)
            while fakeAnswer in self.answerList:
                fakeAnswer = random.randrange(11)
            self.answerList.append(fakeAnswer)
        return self.question, self.answer, self.answerList

    def subtraction(self, difficulty):
        if difficulty == 1:
            return self._subtraction1()
        if difficulty == 2:
            return self._subtraction2()
        if difficulty == 3:
            return self._subtraction3()
        if difficulty == 4:
            return self._subtraction4()
        return self._subtraction1()

    def _division1(self):
        divideBy = [1, 10]
        self.num2 = random.randrange(1, 13)
        self.num1 = divideBy[random.randrange(2)]
        self.answerList = []
        self.answer = self.num1*self.num2
        self.num2 = self.answer
        self.answer = self.num2/self.num1
        self.answerList.append(self.answer)
        self.question = "what is " + str(self.num2) + " / "+str(self.num1)+"?"
        for i in range(5):
            fakeAnswer = random.randrange(100)
            while fakeAnswer in self.answerList:
                fakeAnswer = random.randrange(100)
            self.answerList.append(fakeAnswer)
        return self.question, self.answer, self.answerList

    def _division2(self):
        divideBy = [2, 5, 11]
        self.num2 = random.randrange(1, 13)
        self.num1 = divideBy[random.randrange(3)]
        self.answerList = []
        self.answer = self.num1*self.num2
        self.num2 = self.answer
        self.answer = self.num2/self.num1
        self.answerList.append(self.answer)
        self.question = "what is " + str(self.num2) + " / "+str(self.num1)+"?"
        for i in range(5):
            fakeAnswer = random.randrange(100)
            while fakeAnswer in self.answerList:
                fakeAnswer = random.randrange(100)
            self.answerList.append(fakeAnswer)
        return self.question, self.answer, self.answerList

    def _division3(self):
        divideBy = [3, 4, 6, 7]
        self.num2 = random.randrange(1, 13)
        self.num1 = divideBy[random.randrange(4)]
        self.answerList = []
        self.answer = self.num1*self.num2
        self.num2 = self.answer
        self.answer = self.num2/self.num1
        self.answerList.append(self.answer)
        self.question = "what is " + str(self.num2) + " / "+str(self.num1)+"?"
        for i in range(5):
            fakeAnswer = random.randrange(100)
            while fakeAnswer in self.answerList:
                fakeAnswer = random.randrange(100)
            self.answerList.append(fakeAnswer)
        return self.question, self.answer, self.answerList

    def _division4(self):
        divideBy = [8, 9, 12]
        self.num2 = random.randrange(1, 13)
        self.num1 = divideBy[random.randrange(3)]
        self.answerList = []
        self.answer = self.num1*self.num2
        self.num2 = self.answer
        self.answer = self.num2/self.num1
        self.answerList.append(self.answer)
        self.question = "what is " + str(self.num2) + " / "+str(self.num1)+"?"
        for i in range(5):
            fakeAnswer = random.randrange(100)
            while fakeAnswer in self.answerList:
                fakeAnswer = random.randrange(100)
            self.answerList.append(fakeAnswer)
        return self.question, self.answer, self.answerList

    def division(self, difficulty):
        if difficulty == 1:
            return self._division1()
        if difficulty == 2:
            return self._division2()
        if difficulty == 3:
            return self._division3()
        if difficulty == 4:
            return self._division4()
        return self._division1()


font1 = pygame.font.SysFont("comicsans", 80, True)

run = math()
question = run.division(4)
# print(question)
while run:
    win.fill((0, 0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            run = False

    if event.type == pygame.MOUSEBUTTONDOWN:
        question = run.division(4)
        # print(question)
    text = font1.render(question[0], 1, (235, 0, 0))
    win.blit(text, (500 - text.get_width()/2, 500))

    text2 = font1.render(str(question[2]), 1, (235, 0, 0))
    win.blit(text2, (500 - text.get_width()/2, 700))

    text3 = font1.render(str(question[1]), 1, (235, 0, 0))
    win.blit(text3, (500 - text.get_width()/2, 600))
    pygame.display.update()
