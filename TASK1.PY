# Початковий словник з назвами команд і їх очками (упорядкований за очками)
teams = {
    "Команда А": 45,
    "Команда B": 42,
    "Команда C": 38,
    "Команда D": 35,
    "Команда E": 33,
    "Команда F": 30,
    "Команда G": 28,
    "Команда H": 25,
    "Команда I": 22
}

# Функція для виведення всіх значень словника
def display_teams():
    print("\n> Список команд та їх очок:")
    for team, points in teams.items():
        print(f"{team}: {points}")

# Функція для додавання нової команди
def add_team():
    try:
        name = input("Введіть назву нової команди: ")
        if name in teams:
            print("> Помилка: команда з такою назвою вже існує.")
            return

        points = int(input("Введіть кількість набраних очок: "))
        teams[name] = points
        print("> Команда успішно додана.")
    except ValueError:
        print("> Помилка: очки мають бути числом.")

# Функція для видалення команди
def remove_team():
    name = input("Введіть назву команди, яку потрібно видалити: ")
    if name in teams:
        del teams[name]
        print("> Команда успішно видалена.")
    else:
        print("> Помилка: команди з такою назвою не існує.")

# Функція для перегляду вмісту словника за відсортованими ключами
def display_sorted_teams():
    print("\n> Команди за алфавітним порядком:")
    for team in sorted(teams.keys()):
        print(f"{team}: {teams[team]}")

# Функція для визначення місця нової команди та команд, які набрали менше очок
def determine_team_position():
    try:
        points = int(input("Введіть кількість очок для нової команди: "))

        # Сортуємо команди за очками у зменшуваному порядку
        sorted_teams = sorted(teams.items(), key=lambda x: x[1], reverse=True)
        position = 1
        for i, (team, team_points) in enumerate(sorted_teams, start=1):
            if points > team_points:
                position = i
                break
            position = i + 1

        print(f"> Місце нової команди: {position}")

        # Виводимо команди, які набрали менше очок
        less_points_teams = [team for team, team_points in sorted_teams if team_points < points]
        print("\n> Команди, які набрали менше очок:")
        if less_points_teams:
            for team in less_points_teams:
                print(team)
        else:
            print("Немає команд з меншим результатом.")

    except ValueError:
        print("> Помилка: очки мають бути числом.")

# Діалог з користувачем
while True:
    print("\n\t* Навігаційне меню *")
    choice = input("> Введіть 1 для відображення всіх значень\n"
                   "> Введіть 2 для додавання нової команди\n"
                   "> Введіть 3 для видалення команди\n"
                   "> Введіть 4 для перегляду команд за алфавітом\n"
                   "> Введіть 5 для визначення місця нової команди\n"
                   "> Введіть 0 для виходу\n"
                   "> Ваш вибір: ")

    if choice == '1':
        display_teams()
    elif choice == '2':
        add_team()
    elif choice == '3':
        remove_team()
    elif choice == '4':
        display_sorted_teams()
    elif choice == '5':
        determine_team_position()
    elif choice == '0':
        print("> Програма завершена.")
        break
    else:
        print("> Помилка: незареєстрована дія. Спробуйте ще раз.")
