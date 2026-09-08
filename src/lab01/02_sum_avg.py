a = input('a: ')
b = input('b: ')
print(f'sum={round(float(a.replace(',', '.')) + float(b.replace(',', '.')),2)}; avg={round((float(a.replace(',', '.')) + float(b.replace(',', '.'))) / 2 , 2)}')