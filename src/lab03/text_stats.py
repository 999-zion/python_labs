
from src.lib.text import normalize, tokenize, count_freq, top_n

tablet = ""
stroka = input("Введите строку: ")

clean = normalize(stroka)
tokens = tokenize(clean)
unique = len(set(tokens))
freq_dict = count_freq(tokens)
top_5 = top_n(freq_dict)

if tablet:
    max_len = max([len(i[0]) for i in top_5])
    if max_len > 5:
        print("слово"+(max_len-4)*" "+"|"+" частота")
        print("-"*(10+max_len))
        for i in top_5:
            print(f"{i[0]:<{max_len}} | {i[1]}")
        print("-"*(10+max_len))
    else: 
        print("слово | частота")
        print("-"*15)
        for i in top_5:
            print(f"{i[0]:<{5}} | {i[1]}")
        print("-"*15)
else:
    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {unique}")
    print("Топ-5:")
    for i in top_5:
        print(f"{i[0]}:{i[1]}")

