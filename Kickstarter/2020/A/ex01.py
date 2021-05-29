T = int(input())
for ind in range(T):
    N, K = map(int, input().split())
    S = input()
    left = 0
    right = N - 1 if N % 2 == 0 else N - 2
    res = 0
    while left < right:
        if S[left] != S[right]:
            res += 1
        left += 1
        right -= 1

    print(f"Case #{ind + 1}: {0 if res >= K else K - res}")
