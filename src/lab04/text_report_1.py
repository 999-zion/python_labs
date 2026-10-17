import sys
from src.lib.text import normalize, tokenize, count_freq, top_n
from src.lab04.io_txt_csv import read_text, write_csv

def main():
    try:
        raw_text = read_text("data/lab04/input.txt", encoding="utf-8")
    except FileNotFoundError:
        print("Ошибка: файл не найден")
        return

    clean = normalize(raw_text)
    tokens = tokenize(clean)
    unique = len(set(tokens))
    freq_dict = count_freq(tokens)

    all_rows = sorted(freq_dict.items(), key=lambda x: (-x[1], x[0]))
    top_5 = top_n(freq_dict)

    write_csv(all_rows, "data/lab04/report.csv", header = ("word", "count"))

    print(f"Всего слов: {len(tokens)}")
    print(f"Уникальных слов: {unique}")
    print("Топ-5:")
    for i in top_5:
        print(f"{i[0]}: {i[1]}")

if __name__ == "__main__":
    main()