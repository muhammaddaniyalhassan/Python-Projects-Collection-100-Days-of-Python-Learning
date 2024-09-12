from random import choice

import art
print(art.logo)


def add(n1, n2):
    return n1 + n2


#sub
def sub(n1, n2):
    return n1 - n2

#divide
def divide(n1, n2):
    return n1 / n2

#multiply
def mul(n1, n2):
    return n1 * n2

operation={
     '+': add,
     '-': sub,
     '/': divide,
    '*':  mul
}
def calculator():
    case=True
    while case!=False:

        nn1=float(input("Enter your first number: "))
        nn2=float(input("Enter your second number: "))

        m_choice=str(input("Enter a mathematical operator from the choice of +, -, * or /"))
        answer=operation[m_choice](nn1,nn2)
        print(answer)
        case_ = str(input("Do you want to perform further calculations? y or no")).lower()
        if case_ == "n":
            case = False
            return answer
        else:
            continue_ = str(input("Do you wish to continue with the previous result? y or no")).lower()
            if continue_=="n":
                answer=0
            else:
                answer=nn1
                nn2=float(input("Enter your second number: "))











