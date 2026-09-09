n = int(input())
ochno , zaochno = 0 , 0 
for i in range(n):
    s = input().split()
    if s[3] == 'True':
        ochno +=1
    else: 
        zaochno+=1
print(ochno,zaochno)
