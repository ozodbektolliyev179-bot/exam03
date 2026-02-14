from cinema_session import CinemaSession


session = CinemaSession("Avatar 2", 5)

print(session.available_seats())

t1 = session.book_seat(3, "Ali")
print(t1.owner, t1.seat.number)

print(session.available_seats())

t2 = session.book_seat(1, "Vali")

print(session.available_seats())

try:
    session.book_seat(3, "Sardor")
except RuntimeError:
    print("Joy band")

print(session)

print("Jami bron:", len(session.bookings))
for t in session.bookings:
    print(t.owner, "→", t.seat.number)
