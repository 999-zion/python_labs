import sys
from pathlib import Path
from src.lib.text import normalize, tokenize, count_freq, top_n
from src.lab04.io_txt_csv import read_text, write_csv
            
def main():
    files = sys.argv[1:]
    if not files:
        print("Ошибка: не указаны входные файлы")
        return

    per_file_rows = []
    total_freq = {}
    total_tokens = 0
    total_unique_words = set()

    for path in files:
        try:
            raw_text = read_text(path, encoding="utf-8")
        except FileNotFoundError:
            print(f"Ошибка: файл не найден: {path}")
            return

        tokens = tokenize(normalize(raw_text))
        freq = count_freq(tokens)

        file_name = Path(path).name

        for word, cnt in freq.items():
            per_file_rows.append((file_name, word, cnt))
            total_freq[word] = total_freq.get(word, 0) + cnt

        total_tokens += len(tokens)
        total_unique_words.update(freq.keys())

        top_5 = top_n(freq)
        max_len = max([len(i[0]) for i in top_5])
        print(file_name)
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

    per_file_rows.sort(key=lambda r: (r[0], -r[2], r[1]))
    write_csv(per_file_rows, "data/lab04/report_per_file.csv", header=("file", "word", "count"))

    
    total_rows = sorted(total_freq.items(), key=lambda r: (-r[1], r[0]))
    write_csv(total_rows, "data/lab04/report_total.csv", header=("word", "count"))
    print()
    print("Информация по всем файлам:")
    print(f"Всего слов: {total_tokens}")
    print(f"Уникальных слов: {len(total_unique_words)}")
    print("Топ-5:")

    top_5 = top_n(total_freq)
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

if __name__ == "__main__":
    main()

