# ЛР3 — Тексты и частоты слов (словарь/множество)

## Задание A — src/lib/text.py

## normalize

Нормализация. Преобразование строки s в norm(s):
1. Нормализует
2. заменяет все ё/Ё на е/Е
3. заменяет управляющие символы \\t, \\r, \\n на пробел
4. «схлопывает» последовательности пробелов в один

```python
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:

    '''
    Нормализация. Преобразование строки s в norm(s):
    1) Нормализует
    2) заменяет все ё/Ё на е/Е
    3) заменяет управляющие символы \\t, \\r, \\n на пробел
    4) «схлопывает» последовательности пробелов в один
    '''

    text = text.replace("\t"," ")
    text = text.replace("\n"," ")
    text = text.replace("\r"," ")

    if yo2e:
        text = text.replace("ё","е")
        text = text.replace("Ё","Е")

    if casefold:
        text = text.casefold()

    text = " ".join(text.split())
        
    return text.strip()
```



![taskA](images/lab03/img01.png)


## tokenize

Токенизация. Множество слов — это все подстроки, удовлетворяющие шаблону:
\w+(?:-\w+)*
(буквы/цифры/подчёркивание; допускается дефис внутри слова), разделённые любыми не-\w символами.

```python
def tokenize(text: str) -> list[str]:

    '''
    Токенизация. Множество слов — это все подстроки, удовлетворяющие шаблону \w+(?:-\w+)*
    (буквы/цифры/подчёркивание; допускается дефис внутри слова), разделённые любыми не-\w символами.
    '''

    tokens = re.findall('\w+(?:-\w+)*',text)
    return tokens
```

![taskA](images/lab03/img02.png)


## count_freq

Частоты. Для списка токенов T = [t₁, …, tₙ] частота слова w равна:
f(w) = |{ i : tᵢ = w }|.

```python
def count_freq(tokens: list[str]) -> dict[str, int]:

    '''
    Частоты. Для списка токенов T = [t₁, …, tₙ] частота слова w равна
    f(w) = |{ i : tᵢ = w }|.
    '''

    freq = {}

    for i in tokens:
        if i in freq:
            freq[i] += 1
        else:
            freq[i] = 1
            
    return freq
```

![taskA](images/lab03/img03.png)


## top_n

Топ-N. Отсортировать пары (слово, частота) по ключу (-частота, слово) и взять первые N.

```python
def top_n(freq: dict[str, int], n: int = 5) -> list[tuple[str, int]]:

    '''
    Топ-N. Отсортировать пары (слово, частота) по ключу (-частота, слово) и взять первые N.
    '''

    ans_freq = sorted(freq.items(), key=lambda x: (-x[1],x[0]))
    return ans_freq[:n]
```

![taskA](images/lab03/img04.png)


## Задание B — src/text_stats.py (скрипт со stdin)

Скрипт читает текст из stdin (до EOF), нормализует и токенизирует его с помощью функций из модуля text.py, считает общее количество слов, количество уникальных слов и выводит топ-5 самых частых слов. Добавлена возможность вывода красивой таблички(переменная tablet).

```python
from src.lib.text import normalize, tokenize, count_freq, top_n

tablet = 1
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
```


![taskB](images/lab03/img05.png)
![taskB](images/lab03/img06.png)

## Как запустить 

Вручную, с клавиатуры
В терминале из корня репозитория ввести

```python
python -m src.lab03.text_stats
```