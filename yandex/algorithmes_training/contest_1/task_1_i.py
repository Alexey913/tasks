# I. Расписание
# https://contest.yandex.ru/contest/59539/problems/I/


# Как же Илье надоело учиться! Сначала школа, потом университет...
# Вот, наконец, наступил тот долгожданный день, когда Илье утром
# не надо ехать на учебу. Но, к несчастью для Ильи, оказалось,
# что после окончания университета начинается самое трудное —
# надо устраиваться на работу.
# Во всемирно известной фирме «Goondex», в которую устроился Илья,
# принято очень много работать, в частности, для сотрудников
# установлена шестидневная рабочая неделя. Но, в качестве бонуса,
# «Goondex» каждый год предлагает своим сотрудникам выбрать любой
# день недели в качестве выходного. В свою очередь, оставшиеся
# шесть дней недели будут рабочими.
# Илья сообразил, что с учётом государственных праздников
# (которые всегда являются выходными) с помощью правильного выбора
# выходного дня недели можно варьировать количество рабочих дней
# в году. Теперь он хочет знать, какой день недели ему следует
# выбрать в качестве выходного, чтобы отдыхать как можно больше
# дней в году, или, наоборот, демонстрировать чудеса трудолюбия,
# работая по максимуму.


monthes = {'January': 31, 'February': 28,
           'March': 31, 'April': 30,
           'May': 31, 'June': 30,
           'July': 31, 'August': 31,
           'September': 30, 'October': 31,
           'November': 30, 'December': 31}

days_of_week = {1: 'Monday', 2: 'Tuesday',
        3: 'Wednesday', 4: 'Thursday',
        5: 'Friday', 6: 'Saturday',
        7: 'Sunday'}

all_days = {1: 0, 2: 0, 3: 0, 4: 0, 5: 0, 6: 0, 7: 0}

n = int(input())
year = int(input())
weekend = [input().split() for _ in range(n)]
start_day = input()
# print(weekend)
count_days = 365
if (year % 4 == 0 and year % 100 != 0) or (year % 100 == 0 and year % 400 == 0):
    monthes['February'] = 29
    count_days += 1
print(monthes)
for day in all_days:
    all_days[day] = count_days // 7
for k, day in days_of_week.items():
    if day == start_day:
        all_days[k] += 1
    elif count_days == 366 and start_day == day:
        all_days[k+1] += 1
if count_days == 366 and start_day == 'Sunday':
    all_days[1] += 1

count_start_day = 0
for k, day in days_of_week.items():
    if day == start_day:
        count_start_day = k
        break

for day in weekend:
    temp = 0
    for month in monthes:
        if month != day[1]:
            temp += monthes[month]
        else:
            temp += int(day[0])
            break
    print(temp)
    temp %= 7
    if temp + count_start_day == 1:
        day.append(7)
    elif temp + count_start_day <= 8:
        day.append(count_start_day + temp - 1)
    else:
        day.append(count_start_day + temp - 8)

print(weekend)


for day in weekend:
    for k in all_days:
        if day[2] != k:
            all_days[k] += 1
worst = min(all_days.values())
best = max(all_days.values())

for k, v in all_days.items():
    if v == best:
        best = days_of_week[k]
    if v == worst:
        worst = days_of_week[k]

print(all_days)
print(best, worst)