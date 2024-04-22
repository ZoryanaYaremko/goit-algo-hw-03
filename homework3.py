# Завдання 1
from datetime import datetime

def get_days_from_today(date):
    try:
        # Перетворення рядка дати у об'єкт datetime
        date_obj = datetime.strptime(date, '%Y-%m-%d')
        
        # Поточна дата
        today = datetime.today().date()
        
        # Рызниця між поточною датою та заданою датою
        delta = today - date_obj.date()
        
        # Кількість днів
        return delta.days
    except ValueError:
        # Обробка винятку неправильного формату вхідних даних
        return "Неправильний формат дати. Використовуйте формат 'РРРР-ММ-ДД'."

# Приклад використання
print(get_days_from_today("2021-10-09")) 

# Завдання 2
import random

def get_numbers_ticket(min_num, max_num, quantity):
    # Перевірка коректності вхідних параметрів
    if not (1 <= min_num <= max_num <= 1000 and 1 <= quantity <= (max_num - min_num + 1)):
        return []

    # Генерація унікальних випадкових чисел за діапазоном
    numbers_set = set()
    while len(numbers_set) < quantity:
        numbers_set.add(random.randint(min_num, max_num))

    # Відсортований список чисел
    return sorted(numbers_set)

# Приклад використання
lottery_numbers = get_numbers_ticket(1, 49, 6)
print("Ваші лотерейні числа:", lottery_numbers)


# Завдання 3
import re

def normalize_phone(phone_number):
    # Видаляємо всі символи, крім цифр та '+'
    phone_number = re.sub(r'\D', '', phone_number)
    
    # Перевіряємо, чи номер починається з міжнародного коду
    if not phone_number.startswith('+'):
        # Додаємо міжнародний код для України
        phone_number = '+38' + phone_number
    
    return phone_number

# Приклад використання
raw_numbers = [
    "067\\t123 4567",
    "(095) 234-5678\\n",
    "+380 44 123 4567",
    "380501234567",
    "    +38(050)123-32-34",
    "     0503451234",
    "(050)8889900",
    "38050-111-22-22",
    "38050 111 22 11   ",
]

sanitized_numbers = [normalize_phone(num) for num in raw_numbers]
print("Нормалізовані номери телефонів для SMS-розсилки:", sanitized_numbers)


# Завдання 4
from datetime import datetime, timedelta

def get_upcoming_birthdays(users):
    today = datetime.today().date()
    upcoming_birthdays = []

    for user in users:
        # Конвертуємо дату у datetime об'єкт
        birthday_date = datetime.strptime(user["birthday"], "%Y.%m.%d").date()
        
        # Перевіряємо, чи потрібно враховувати дату народження у наступному році
        if birthday_date < today:
            birthday_date = birthday_date.replace(year=today.year + 1)

        # Розраховуємо різницю між днем народження та сьогоднішнім днем
        days_until_birthday = (birthday_date - today).days

        # Перевіряємо, чи день народження випадає наступного тижня
        if 0 <= days_until_birthday <= 7:
            # Перевіряємо, чи день народження припадає на вихідний
            if birthday_date.weekday() >= 5:  # 5 та 6 - субота та неділя
                # Переносимо дату привітання на наступний понеділок
                days_until_birthday += (7 - birthday_date.weekday())

            congratulation_date = today + timedelta(days=days_until_birthday)
            congratulation_date_str = congratulation_date.strftime("%Y.%m.%d")

            # Додаємо ім'я та дату привітання до списку
            upcoming_birthdays.append({"name": user["name"], "congratulation_date": congratulation_date_str})

    return upcoming_birthdays

# Приклад використання
users = [
    {"name": "John Doe", "birthday": "1985.01.23"},
    {"name": "Jane Smith", "birthday": "1990.01.27"}
]

upcoming_birthdays = get_upcoming_birthdays(users)
print("Список привітань на цьому тижні:", upcoming_birthdays)
















