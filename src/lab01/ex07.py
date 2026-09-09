stroka = input()
f = 0
word = ''
index1 = 0
index2 = 0
index0 = 0
for i in range(len(stroka)):
    if f==0:
        if 'A' <= stroka[i] <= 'Z':
            word += stroka[i]
            f = 1
            index1 = i
    elif f == 1:
        if '0' <= stroka[i] <= '9':
            word += stroka[i+1]
            index2 = i+1
            index0 = i+1
            f = 2
    else:
        if i-index0 == index2-index1:
            index0 = i
            word += stroka[i]
print(word)
    

