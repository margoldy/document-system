import datetime

def valid_int(text):
    while True:
        to_int = input(text)
        try:
            value = int(to_int)
            return value
        except ValueError:
            print("Ошибка! Неверный формат")

print("=== Система учета личных документов (Проверка срока) ===")

doc_name = input("Введите название документа: ")
issue_year = valid_int("Введите год выдачи: ")
validity_years = valid_int("На сколько лет выдан документ: ")

expiration_year = issue_year + validity_years
today = datetime.date.today()
current_year = today.year

years_left = expiration_year - current_year

print("\n--- Результат проверки ---")
print("Документ:", doc_name)
print("Год окончания действия:", expiration_year)

if years_left < 0:
    years_overdue = abs(years_left)
    print("СТАТУС: Документ просрочен")
    print(f"Срок действия истек {years_overdue} лет назад")
elif years_left == 0:
    print("СТАТУС: Внимание! Срок действия документа истекает в этом году!")
elif years_left <= 2:
    print("СТАТУС: Документ действителен, но скоро потребуется замена.")
    print("Осталось лет:", years_left)
else:
    print("СТАТУС: Документ действителен.")
    print("Осталось лет:", years_left)