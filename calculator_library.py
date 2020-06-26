from calculator.simple import SimpleCalculator


def calculate(statement):
    calculator = SimpleCalculator()
    calculator.run(statement)
    return calculator.log[-1].split(' ')[1]
