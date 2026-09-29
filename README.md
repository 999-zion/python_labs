# ЛР3 — Тексты и частоты слов (словарь/множество)

## Задание A — src/lib/text.py

## normalize

- `*` означает, что `casefold` и `yo2e` можно передать только по имени
- `casefold()` приводит к нижнему регистру корректнее, чем `lower()`, для Юникода
- `yo2e` склеивает `ё` и `е`, иначе «ёжик» и «ежик» считались бы разными словами



```python
def normalize(text: str, *, casefold: bool = True, yo2e: bool = True) -> str:
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