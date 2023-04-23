# its a good project. do some randimization so that it looks fun to play with

import random
Unanswered = []


class Question:
    def __init__(self, qNum):
        self.question = qNum
        self.result = 0
        self.Unanswered = []
        self.answered = ''

    def statement(self, statment=''):
        self.statement = statment

    def choices(self, ch1, ch2, ch3, answer):
        self.choice = {'a': ch1, 'b': ch2, 'c': ch3}
        self.answer = self.choice[answer]

    def showQuestion(self):
        print(self.statement)
        for key, choice in self.choice.items():
            print(f' {key}, {choice}')

    def receiveAnswer(self):
        self.answered = input("Answer? :- ")
        if self.choice[self.answered] == self.answer:
            self.result += 1
            print('CORRECT! 🎉😀😀')

        else:

            print('INCORRECT 😭 ')

    def checkAnswer(self):
        if self.choice[self.answered] == self.answer:
            self.result += 1
            return True
        else:
            return False


def rightAnswer(bool, q):
    if bool == True:
        pass
    else:
        Unanswered.append(q)


def rightAnswerOne(bool, q):
    if bool == True:
        Unanswered.remove(q)
    else:
        pass


q1 = Question(1)
q1.statement('What is the largest organ in the human body? ')
q1.choices('Liver', 'Skin', 'Brain', 'b')
q1.showQuestion()
q1.receiveAnswer()
rightAnswer(q1.checkAnswer(), q1)

q2 = Question(2)
q2.statement('Which planet is known as the Red Planet? ')
q2.choices('Mercury', 'Mars', 'Venus', 'b')
q2.showQuestion()
q2.receiveAnswer()
rightAnswer(q2.checkAnswer(), q2)

q3 = Question(3)
q3.statement('What is the capital city of Australia?')
q3.choices('Sydney', 'Melbourne', 'Canberra', 'c')
q3.showQuestion()
q3.receiveAnswer()
rightAnswer(q3.checkAnswer(), q3)

q4 = Question(4)
q4.statement('Who was the first person to walk on the moon?')
q4.choices('Buzz Aldrin', 'Neil Armstrong', 'Yuri Gagarin', 'b')
q4.showQuestion()
q4.receiveAnswer()
rightAnswer(q4.checkAnswer(), q4)

q5 = Question(5)
q5.statement('The richest man in the world as of today')
q5.choices('Mark Zukemberg - Facebook/meta',
           'Elon Musk- Tesla', 'Bernard Arnault - LVMH', 'c')
q5.showQuestion()
q5.receiveAnswer()
rightAnswer(q5.checkAnswer(), q5)

q6 = Question(6)
q6.statement('What is the largest mammal in the world?')
q6.choices(' Blue whale', ' Elephant', 'Giraffe', 'a')
q6.showQuestion()
q6.receiveAnswer()
rightAnswer(q6.checkAnswer(), q6)

if Unanswered != []:
    while Unanswered != []:

        for items in Unanswered:

            # num = random.randint(0, len(Unanswered))
            items.showQuestion()
            items.receiveAnswer()
            rightAnswerOne(items.checkAnswer(), items)
            if Unanswered == []:
                break
else:
    print("What a genuis, You did it all with NO MISTAKE! 🎉 🎉 🎉 🎉 ")
