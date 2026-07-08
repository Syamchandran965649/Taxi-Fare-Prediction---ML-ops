import sys

class CustomException(Exception):

    def __init__(self, error_message):

        super().__init__(error_message)

        _, _, exc_tb = sys.exc_info()

        self.line = exc_tb.tb_lineno if exc_tb else None

    def __str__(self):

        return f"Error at line {self.line}: {super().__str__()}"