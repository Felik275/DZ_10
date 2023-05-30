#Task 3
# 3. Напишіть користувацький клас виключення з функціоналом на свій вибір. Викличте його за допомогою інструкції raise.

class CustomException(Exception):
    def __init__(self, message):
        self.message = message
        super().__init__(self.message)

    def __str__(self):
        return f"CustomException: {self.message}"


try:
    raise CustomException("Це є виключенням!")
except CustomException as e:
    print(e)