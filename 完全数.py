N = eval(input())
for i in range(2,N):
    sum = 1
    for j in range(2,int(N**0.5)+1):
        if i%j == 0:
            sum += j
            sum += i//j
    if sum == i:
        print(i,end=" ")    