import json

from controller import menu_json


# Модель пользователя
class User:
    def __init__(self, name, age, pin, is_admin=False):
        self.name = name
        self.age = age
        self.pin = pin
        self.is_admin = is_admin
        self.orders = []  # Список заказов пользователя


# Список пользователей (вместо базы данных)
users = []

# Регистрация админа
admin_user = User("admin", 30, "admin123", is_admin=True)
users.append(admin_user)


# Декоратор для проверки возраста
def age_check(func):
    def wrapper(*args, **kwargs):
        age = args[0]  # Предполагаем, что возраст передается первым аргументом
        if age < 18:
            print("Извините, вы должны быть старше 18 лет, чтобы заказывать.")
            return None
        return func(*args, **kwargs)

    return wrapper


# Функция для генерации чека
def generate_receipt(order_items, total_price):
    print("\n--- Чек ---")
    for item in order_items:
        print(f"{item['название']}: {item['цена']}р")
    print(f"Общая сумма: {total_price}р")
    print("Спасибо за ваш заказ!")


# Декоратор для проверки оплаты
def check_after_payment(func):
    def wrapper(*args, **kwargs):
        # Выполняем оплату
        payment_successful = func(*args, **kwargs)

        # Проверяем, успешна ли оплата
        if payment_successful:
            print("Оплата прошла успешно. Выполняем чек.")
            return True
        else:
            print("Оплата не прошла. Чек не будет выдан.")
            return False

    return wrapper


@check_after_payment
def process_payment(amount):
    # Здесь должна быть логика обработки платежа
    if amount > 0:
        print(f"Обработка платежа на сумму: {amount} рублей.")
        return True  # Платеж успешен
    return False  # Платеж не успешен


# Функция для аутентификации
def authenticate_user(name, pin):
    for user in users:
        if user.name == name and user.pin == pin:
            return user
    return None


# Функция для отображения заказов
def display_orders():
    print("\n--- Заказы ---")
    for user in users:
        if user.orders:
            for order in user.orders:
                print(f"{user.name} заказал: {order['название']} за {order['цена']}р")


# Запрос информации у пользователя
name = input("Придумайте ник: ")
if name.lower() == 'admin':
    pin = input("Введите пароль администратора: ")
    if pin == "admin123":  # Проверка пароля администратора
        print("Добро пожаловать, администратор!")
        display_orders()  # Отображаем заказы
    else:
        print("Неверный пароль администратора.")#айяйяй.....
else:
    age = int(input("Сколько вам лет: "))
    pin = input("Придумайте пароль: ")

    # Создание пользователя
    user = User(name, age, pin)
    users.append(user)

    # Проверка возраста и вывод соответствующего меню
    if age >= 18:
        print("Вы можете заказывать.")
    else:
        print("Вы не можете заказывать.")

    # Запрос у пользователя, хочет ли он что-либо заказать
    order = input("Хотите что-либо заказать? (да/нет): ")


    @age_check
    def process_order(user):
        # Загружаем JSON в Python-объект
        menu = json.loads(menu_json)

        # Функция для поиска цены продукта
        def find_price(product_name):
            for category, items in menu['menu'].items():
                for item in items:
                    if item['название'].lower() == product_name.lower():
                        return item['цена']
            return None

        order_items = []
        total_price = 0

        while True:
            user_input = input("Введите название продукта (или 'выход' для завершения): ")