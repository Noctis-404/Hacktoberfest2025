L = int(input())
R = int(input())

for j in range(L, R + 1):
    num = j
    rev = 0
    while num > 0:
        digit = num % 10      
        rev = rev * 10 + digit   
        num //= 10               
    
    if rev == j:               
        
        if j > 1:
            for i in range(2, int(j ** 0.5) + 1):
                if j % i == 0:
                    break
            else:
                print(j, end=" ")
