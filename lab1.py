# Нужно поместить файл sport.txt в одну папку с программой и запустить

from collections import Counter

sport_count = Counter()

with open('sport.txt', 'r', encoding='cp1251') as file:
    next(file)
    
    for line in file:
        parts = line.strip().split('\t')
        if len(parts) < 4:
            continue
        
        sports_str = parts[3].strip()
        if not sports_str:
            continue
        
        sports = [s.strip() for s in sports_str.split(',') if s.strip()]
        
        sport_count.update(sports)

top_3_sports = sport_count.most_common(3)

print("Три наиболее популярных вида спорта по количеству объектов:")
for i, (sport, count) in enumerate(top_3_sports):
    print(f"{i}. {sport} — {count} объектов")
