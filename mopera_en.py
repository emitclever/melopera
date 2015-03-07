#-*-coding:utf8;-*-
# qpy:2
# qpy:console
# My very first program on python for my daughter first math problems.
# Need qpython3 application for android (python3 mac or windows)
# Lets play
from random import randint
import random
correct = 0
rng = 10
print("Hello Melissa")
for i in range (rng):  # (number of questions)
    n1 = randint(0,6)   # (numbers to choose randomly)
    n2 = randint(0,n1)
    opera = random.choice(r'+-') # random operation choosing could be '+-*/' depend on complexity
    resultat = eval(str(n1) + opera + str(n2))
    print(n1,opera,n2,end="")
    inp=(input(" = "))
    if inp.isdigit(): # check if valid integer not empty
        ans = int(inp)
    else:
        ans = 0
    if ans == resultat:
        print("TRUE. :) \n\n")
        correct = correct + 1
    else:
        print("FALSE :( , Answer is %d.\n\n" % resultat)
print("\n %d / %d." % (rng,correct))
print("End")

