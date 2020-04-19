T_cases = []
N_len = []
T = int(input())
for i in range(T):
    N_cases = []
    N_len.append(int(input()))
    for inp in map(int, input().split()):
        N_cases.append(inp)
    T_cases.append(N_cases)
    


for num_case in range(T):
    case = T_cases[num_case]
    
    count = 0
    for i in range(N_len[num_case]):
        if i > 0 and i < (N_len[num_case] - 1):
            if case[i] > case[i-1] and case[i] >case[i+1]:
                count += 1
    print("Case #{}: {}".format((num_case+1), count))