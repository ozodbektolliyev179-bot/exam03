from seat import Seat
from ticket import Ticket

class CinemaSession:
    def __init__(self, movie_title: str, total_seats: int):
        if not isinstance(movie_title, str) or not movie_title.strip():
            raise ValueError("Film nomi bo'sh bo'lmasligi kerak")
        if not isinstance(total_seats, int) or total_seats <= 0:
            raise ValueError("Jami o'rinlar musbat butun son bo'lishi kerak")

        self.movie_title = movie_title
        self.total_seats = total_seats
        self.seats = [Seat(i + 1) for i in range(total_seats)]
        self.bookings = []

    def available_seats(self) -> list[int]:
        return [seat.number for seat in self.seats if not seat.is_taken]

    def book_seat(self, seat_number: int, user: str) -> Ticket:
        if not (1 <= seat_number <= self.total_seats):
            raise ValueError("Noto'g'ri o'rin raqami")
        seat = self.seats[seat_number - 1]
        if seat.is_taken:
            raise RuntimeError("Bu o‘rin band")
        seat.is_taken = True
        ticket = Ticket(seat, user)
        self.bookings.append(ticket)
        return ticket

    def __str__(self):
        return f"CinemaSession: {self.movie_title} ({self.total_seats} seats)"
