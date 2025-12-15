import requests
import matplotlib.pyplot as plt
import sys

try:
    data = requests.get("https://raw.githubusercontent.com/dm-fedorov/python_basic/master/data/opendata.stat").text
    err_404 = "404: Not Found"
    if data == err_404:
        print(f"Ошибка при загрузке данных: {err_404}")
        sys.exit(1)
except requests.exceptions.RequestException as e:
    print(f"Ошибка при загрузке данных: {e}")
    sys.exit(1)

lines = data.strip().split("\n")
lines = lines[1::]
pensions_2018 = []

dates = []
values = []

for line in lines:
    parts = line.split(",")
    
    name = parts[0]
    region = parts[1]
    date = parts[2][:-3:]
    value = int(parts[3])
    if len(parts) < 4: # строка может содержать недостаточно данных
        continue 
    
    if name == "Средняя пенсия" and region == "Забайкальский край" and date[:4:] == "2018":
        pensions_2018.append(value)
        dates.append(date)
        values.append(value)

average_pension = sum(pensions_2018) / len(pensions_2018)
print("Средняя пенсия в Забайкальском крае за 2018 год:", round(average_pension, 2))

plt.plot(dates, values)
plt.title("Изменение средней пенсии в Забайкальском крае за 2018 год")
plt.xlabel("Дата")
plt.ylabel("Пенсия")
plt.xticks(rotation=45) # чтоб  по оси абсцисс не было текста друг на друге
plt.grid(True)
plt.tight_layout() # чтоб не было обрезанного окна (добавил из-за xticks)
plt.show()
