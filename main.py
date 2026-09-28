from datetime import date

# Начальные данные (карточка документа)
doc_name = "Паспорт РФ"
doc_type = "Личные документы"

owner = "Не назначен"
expiration_year = None
status = "Новый"


# 1. Функция «Назначение владельца»
def assign_owner(user_name):
    if user_name != "":
        print("Владелец документа успешно привязан")
        return user_name
    return "Владелец не указан"


# 2. Функция «Установка срока действия»
def set_expiration_year(issue_year, validity_years):
    return int(issue_year) + int(validity_years)


# 3. Функция «Изменение статуса»
def check_status(exp_year):
    current_year = date.today().year
    if exp_year < current_year:
        return "Просрочен (Требуется замена)"
    elif exp_year == current_year:
        # Тема ПР1: ветвления if-elif-else
        return "Внимание! Истекает в этом году"
    else:
        return "Действителен"


# Основной сценарий
owner = assign_owner("Маргарита Гончарова")
expiration_year = set_expiration_year("2016", "10")  # Выдан в 2016 на 10 лет
status = check_status(expiration_year)

# вывод результата
print("\n=== СИСТЕМА УЧЕТА ДОКУМЕНТОВ ===")
print(f"Документ: {doc_name}")
print(f"Категория: {doc_type}")
print(f"Владелец: {owner}")
print(f"Год окончания действия: {expiration_year}")
print(f"Текущий статус: {status}")
