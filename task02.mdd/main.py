from cinema_session import CinemaSession

session = CinemaSession("Avatar 2", 5)

print("Bo'sh joylar:", session.available_seats())

t1 = session.book_seat(3, "Ali")
print(t1)

print("Bo'sh joylar:", session.available_seats())

t2 = session.book_seat(1, "Vali")
print(t2)

print("Bo'sh joylar:", session.available_seats())
