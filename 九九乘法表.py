for i in range(1,10,1):
    for j in range(1,10-i,1):
        print(6*" ",end=" ")
    for j in range(10-i,10,1):
        print(f"{i}*{j}={i*j:2d}",end=" ")
    print()