import requests
from collections import Counter

data = requests.get('http://dfedorov.spb.ru/python3/sport.txt')
data.encoding = 'cp1251'

sport_count = Counter()

lines = data.text.strip().split('\n')

for line in lines[1:]:
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
