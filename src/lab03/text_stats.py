
from ..lib.text import normalize, tokenize, count_freq, top_n

stroka = input("Введите строку: ")

stroka = tokenize(normalize(stroka))

print("Всего слов: ", len(stroka))
stroka = count_freq(stroka)
print("Уникальных слов: ", len(stroka))
print("Топ-5:")
for i in top_n(stroka):
    print(f'{i[0]}:{i[1]}')


