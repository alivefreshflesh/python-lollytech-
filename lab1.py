# Нужно поместить файл sport.txt в одну папку с программой и запустить
# Программа была переписана с использованием requests, чтобы не было необходимости скачивать файл
# Пожалуйста, перейдите по ссылке ниже
# https://github.com/alivefreshflesh/python-lollytech-/blob/main/lab1_new.py

from collections import Counter

sport_count = Counter()

with open('sport.txt', 'r', encoding='cp1251') as file:
    next(file)
    
    for line in file:
        parts = line.strip().split('\t')
        sports_str = parts[3].strip()
        if not sports_str:
            continue
        sports = [s.strip() for s in sports_str.split(',')]
        sport_count.update(sports)

top_3_sports = sport_count.most_common(3)

print("Три наиболее популярных вида спорта по количеству объектов:")
for i, (sport, count) in enumerate(top_3_sports):
    print(f"{i + 1}. {sport} — {count} объектов")
