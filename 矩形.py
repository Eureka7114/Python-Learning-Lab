n = eval(input())
d = 4*n-2
for i in range(1,n+1):
    k = 2*i-1
    print(k*"*"+(d-2*k)*" "+k*"*")
    print()
    