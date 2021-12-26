def crop(message, k):
    if len(message) <= k:
        return message
    else:
        return ' '.join(message[:k+1].split(' ')[0:-1])


def solution(P, S):
    N = range(1, 100000)
    P = range(1, 9)
    S = range(1, 9)

    for K in N - 1:
        print(K)
