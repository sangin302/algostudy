# 1차 풀이 방법
# 정확성 테스트는 통과했으나, 효율성 테스트에서 실패.
# 왜일까?
# 참여자 수가 100,000명이 넘어가고 거기서 최억의 경우를 생각하면 순회를 10,000,000,000번 해야함....
def solution(participant, completion):
    for i in completion:
        if i in participant:
            participant.remove(i)
    answer = "".join(participant)
    return answer

# 2차 풀이방법
# counter를 배워서 활용해보앗다.
from collections import Counter

def solution(participant, completion):
    return list(Counter(participant) - Counter(completion))[0]
