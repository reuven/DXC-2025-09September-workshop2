def cube(self, line):
    """Get the cube of a number"""
    numbers = self.line_to_numbers(line)
    result = numbers[0] ** 3
    print(f'{numbers[0]} ** 3 = {result}')
