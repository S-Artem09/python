# numbers = {"Artem": 89773424436, "Nikita": 89103335566}

# print(numbers.setdefault("Artem", 777))
# print(numbers)

# print(numbers.popitem())

# print(numbers.pop("Artem"))
#print(numbers)

# print(numbers["Artem"])
# print(numbers.get("Artem1"))

# name = input("Введите имя: ")
# number = input("Введите телефон: ")
# numbers[name] = number
# numbers.update({"1": 535353, "2": 5646456464})
# print(numbers)

# for name in numbers.keys():
#     print(name)

# for tel in numbers.values():
#     print(tel)

# for pair in numbers.items():
#     print(pair)

# a = [4, 5, 7]
# a[0] = 6
# print(a)

# a = "hello"
# a[0] = "j"
# print(a)


# numbers = {"Artem": 89773424436, "Nikita": 89103335566}
# numbers.update({"Vlad": 89153214455})
# print(numbers)
# for name, tel in numbers.items():
#     print(f"{name} - {tel}")
# name = input("Введите имя: ")
# print(numbers.setdefault(name, 7984324234242))

# a = {1: 'one', 2: 'two'}
# print(a.setdefault(7, 'seven'))
# print(a)

# a = {}
# while True:
#     s = input()
#     if s == '.':
#         break
#     l = s.split()
#     if len(l) == 2:
#         a[l[0]] = l[1]
#     else:
#         print(a[l[0]])

a = int(input())
i = 2
while i < a:
    print(i)
    i += 1