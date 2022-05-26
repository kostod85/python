edibles = ["отбивные", "пельмени", "яйца", "орехи"]

for food in edibles:
    if food == "пельмени":
        print("Я не ем пельмени!")
        break
    print("Отлично, вкусные " + food)
else:
    print("Хорошо, что не было пельменей!")
print("Ужин окончен.")