# -*- coding: utf-8 -*-
import random

rolled = []
rolledtimes = 0;
biggest = []

freq = int(input('How many times would you like to roll the dice? '))

def roll():
    rand = random.randrange(1,7)
    return rand
def probability():
    for i in range(0,6):
        print('Calculation of probability:')
        percentage = "{:.2f}".format((count[i] / freq)*100)
        percent = str(percentage) + '%'
        print(' ', i + 1, ':', percent)
def theoretical():
    result = "{:.2f}".format((1/6)*freq)
    denominator = "{:.2f}".format(((1/6)*freq)*6)
    print('\nIn theory, each dice should roll {} out of {} times'.format(result,denominator))
def findBiggest():
    for i in range(1,7):
        biggest.append(rolled.count(i))
    print('\n', 'The most times a dice is rolled is', max(biggest), 'times')
def findSmallest():
    for i in range(1,7):
        biggest.append(rolled.count(i))
    print('\n', 'The least times a dice is rolled is', min(biggest), 'times')

for i in range(1,freq + 1):
    number = roll()
    rolled.append(number)
    rolledtimes+=1
count = [rolled.count(1),rolled.count(2),rolled.count(3),rolled.count(4),rolled.count(5),rolled.count(6)]
print('After being rolled {} times:\n\n1 is rolled {} times\n2 is rolled {} times\n3 is rolled {} times\n4 is rolled {} times\n5 is rolled {} times\n6 is rolled {} times\n'.format(rolledtimes,count[0],count[1],count[2],count[3],count[4],count[5]))

probability()
findBiggest()
findSmallest()
theoretical()
