from seat import Seat


class Ticket:
    def __init__(self, seat: Seat, owner: str):
        if not isinstance(seat, Seat):
            raise ValueError("seat Seat tipida bo'lishi kerak")
        if not isinstance(owner, str) or not owner.strip():
            raise ValueError("owner bo'sh bo'lmasligi kerak")

        self.seat = seat
        self.owner = owner
        