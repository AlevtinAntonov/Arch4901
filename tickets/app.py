from tickets.account import Account
from tickets.buy_ticket import buy_ticket
from tickets.ticket import Ticket
from tickets.user import User

if __name__ == '__main__':
    # Создание пользователя, билета и аккаунта
    account = Account(1000)  # начальный баланс аккаунта
    user = User("Petr", 'User_1', "12345", account)
    ticket_1 = Ticket(1, 5, 33, '11.11.2023 10:00:00',
                      '11.11.2023 12:00:00', user.id_, 500, '10-A', )
    ticket_2 = Ticket(5, 3, 35, '11.11.2023 18:00:00',
                      '11.11.2023 19:00:00', user.id_, 200, '15-A', )
    # Проверка правильности пароля
    password_input = input("Введите пароль: ")
    if user.verify_password(password_input):
        print("Пароль верный.")
    else:
        print("Пароль неверный.")

    # Вывод информации о пользователе и его аккаунте
    print(f"Пользователь: {user.name}")
    print(f"Баланс аккаунта: {user.account.balance}")

    # Покупка билета 1
    buy_ticket(user, ticket_1)

    # Вывод обновленной информации о пользователе и аккаунте
    print(f"Пользователь: {user.name}")
    print(f"Баланс аккаунта: {user.account.balance}")
    print(f'Список купленных билетов: {user.get_tickets()}')

    # Покупка билета 2
    buy_ticket(user, ticket_2)

    # Вывод обновленной информации о пользователе и аккаунте
    print(f"Пользователь: {user.name}")
    print(f"Баланс аккаунта: {user.account.balance}")
    print(f'Список купленных билетов: {user.get_tickets()}')
