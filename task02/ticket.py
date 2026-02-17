

class Ticket:
    def __init__(self, seat, user):
        self.seat = seat
        self.user = user

    def __str__(self):
        return f"{self.user} -> Seat {self.seat.number}"
