import random


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
