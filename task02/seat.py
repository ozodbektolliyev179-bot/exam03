class Seat:
    def __init__(self, number: int):
        self.number = number
        self.is_taken = False

    def __str__(self):
        return f"Seat {self.number}: {'X' if self.is_taken else 'O'}"
