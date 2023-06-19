# TODO: TASK 1
# people_file = open('files/people.txt ', 'r', encoding='UTF-8')
# c = 1
# for line in people_file:
#     print(f"{c}. {line}", end="")
#     c += 1


# TODO: TASK 2
# people_file = open('files/people.txt ', 'r', encoding='UTF-8')
# ages_file = open('files/ages.txt', 'r', encoding='UTF-8')
# people_list = []
# ages_list = []
# for name in people_file:
#     people_list.append(name.replace('\n', ''))
# for age in ages_file:
#     ages_list.append(age.replace('\n', ''))
# for i in range(len(people_list)):
#     print(f'{people_list[i]} - {ages_list[i]}')

# TODO: TASK 3
# cars_file = open('files/cars.txt', 'w', encoding='UTF-8')
# n = int(input('Сколько машин хотите ввести? '))
# for i in range(1, n+1):
#     model = input('Введите модель машины ')
#     color = input('Введите цвет машины ')
#     year = input('Введите год выпуска машины ')
#     cars_file.write(f'{i}. {model} {color} {year}\n')
#     print('Машина добавлена')

# #TODO: TASK 5
# marks_file = open('files/marks.txt', 'r', encoding='UTF-8')
# marks_dict = {}
# for line in marks_file:
#     line_list = line.split()
#     name = line_list[0]
#     marks_list = list(map(int, line_list[1:]))
#     marks_dict[name] = marks_list
# marks_file.close()

# for name, marks in marks_dict.items():
#     print(f'{name} - {round(sum(marks) / len(marks), 2)}')

# for name, marks in marks_dict.items():
#     if 2 not in marks:
#         print(name)

# max_av = 0
# max_name = ''
# for name, marks in marks_dict.items():
#      if round(sum(marks) / len(marks), 2) > max_av:
#          max_av = round(sum(marks) / len(marks), 2)
#          max_name = name
#
# print(f'{max_name} - {max_av}')
# max_five = 0
# for el in marks_dict.values():
#     if el.count(5) > max_five:
#         max_five = el.count(5)
# for name, marks in marks_dict.items():
#     if marks.count(5) == max_five:
#         print(name)
#
#

# def average_season(season):
#     f = open(season + ".txt", "r", encoding="UTF-8")
#     s = 0
#     k = 0
#     for line in f.readlines():
#         temps_list = list(map(int, line.split()[1:]))
#         s += sum(temps_list)
#         k += len(temps_list)
#     return f"{season}: {round(s/k, 3)}"
#
#
# seasons = ["winter", "spring", "summer", "autumn"]
# seasons_file = open("all_seasons.txt", "w", encoding="UTF-8")
# for season in seasons:
#     seasons_file.write(average_season(season) + "\n")
# seasons_file.close()

#training_file = open('files/training.txt', 'r', encoding='UTF-8')
# 1
# s = 0
# for line in training_file:
#     s += int(line.split()[-2])
# print(s)
# 2
# week_dict = {}
# for line in training_file:
#     day = line.split()[0]
#     week_dict[day] = 0
# training_file.seek(0)
# for line in training_file:
#     day = line.split()[0]
#     hours = int(line.split()[-2])
#     week_dict[day] += hours
# print(week_dict)
# 3
# week_dict = {}
# for line in training_file:
#     day = line.split()[0]
#     week_dict[day] = [0, 0]
# training_file.seek(0)
# for line in training_file:
#     day = line.split()[0]
#     hours = int(line.split()[-2])
#     week_dict[day][0] += hours
#     week_dict[day][1] += 1
# av_dict = {}
# for day, data in week_dict.items():
#     av_dict[day] = data[0] / data[1]
# 4 (3)
# m = max(av_dict.values())
# for day, time in av_dict.items():
#     if time == m:
#         print(day)
# 5
# for line in training_file:
#     l = line.split()
#     if int(l[-2]) == 0:
#         print(l[1])

# week_dict = {}
# number_of_month = {'04': 'Апрель',
#                    '05': 'Май',
#                    '06': 'Июнь',
#                    '07': 'Июль',
#                    '08': 'Август'
#                    }
# for line in training_file:
#     month = line.split()[1].split('.')[1]
#     hour = int(line.split()[-2])
#     if hour == 0:
#         if month not in week_dict:
#             week_dict[month] = 1
#         else:
#             week_dict[month] += 1
# max_lazy_month = max(week_dict.values())
# lazy_list = []
# for month, lazy_days in week_dict.items():
#     if lazy_days == max_lazy_month:
#         lazy_list.append(month)
#
# for number in lazy_list:
#     print(number_of_month[number])


# def line_count(filename):
#     file = open(filename, 'r', encoding='UTF-8')
#     return len(file.readlines())
#
#
# print(line_count('test.txt'))