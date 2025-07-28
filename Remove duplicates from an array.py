n=int(input())
l=list(map (int, input().split()))
arr= (sorted (list (set(l))))
print(*arr)
