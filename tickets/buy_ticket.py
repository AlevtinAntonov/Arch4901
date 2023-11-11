from tickets.ticket import Ticket
from tickets.user import User


def buy_ticket(user: User, ticket: Ticket):
    if user.account.balance >= ticket.price:
        user.account.withdraw(ticket.price)
        user.add_ticket(ticket)
        print(f"Билет на маршрут № {ticket.route_number} от зоны № {ticket.departure_zone} до зоны № "
              f"{ticket.arrival_zone} - время отправления {ticket.departure_time} успешно куплен.")
    else:
        print("Недостаточно средств на счете для покупки билета.")