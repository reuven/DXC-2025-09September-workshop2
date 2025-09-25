def square(self, line):
    """Get the square of a number"""
    numbers = self.line_to_numbers(line)
    result = numbers[0] ** 2
    print(f'{numbers[0]} ** 2 = {result}')
