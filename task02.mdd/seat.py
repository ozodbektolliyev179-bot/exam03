class Seat:
    def ___init__(self, number: int):
        if not isinstance(number, int) or number <= 0:
            raise ValueError("number musbat butun son bo'lishi kerak")

        self.number = number
        self.is_taken = False