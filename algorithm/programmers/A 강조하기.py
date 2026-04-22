import sys
sys.stdin = open('r', 'input.txt')

myString = input()

def solution(myString):
    answer = []
    for i in myString:
        if i == 'a' or i == 'A':
            answer.append('A')
        else:
            b = i.lower()
            answer.append(b)
    result = ''.join(answer)
    return result
