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



![task1](images/lab03/img01.png)