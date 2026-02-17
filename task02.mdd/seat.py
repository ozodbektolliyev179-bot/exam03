
class Seat:
    def __init__(self, number: int):
        self.number = number
        self.is_taken = False   # Bu bo‘sh/band holatini saqlaydi

    def __str__(self):
        return f"Seat {self.number}: {'X' if self.is_taken else 'O'}"
