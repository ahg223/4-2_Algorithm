N, M, K = map(int, input().split())
print(min(min(N//2,M),(N+M-K)//3))
