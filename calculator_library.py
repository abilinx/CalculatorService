from calculator.simple import SimpleCalculator


class InputSyntaxError(Exception):

    def __init__(self):
        pass


def calculate(statement):
    calculator = SimpleCalculator()
    calculator.run(statement)
    print(f'calculator log: {calculator.log}')
    if calculator.log[-1] == 'result: Error':
        raise InputSyntaxError
    return calculator.log[-1].split(' ')[1]
