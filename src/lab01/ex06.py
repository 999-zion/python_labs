n = int(input('in_1: '))
ochno , zaochno = 0 , 0 
for i in range(n):
    s = input(f'in_{i+2}: ').split()
    if s[3] == 'True':
        ochno +=1
    else: 
        zaochno+=1
print('out:',ochno,zaochno)
