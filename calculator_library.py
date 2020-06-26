from calculator.simple import SimpleCalculator


class InputSyntaxError(Exception):
    def __init__(self):
        # TODO: Add more information regarding the input error to ease debugging.
        pass


def calculate(statement):
    calculator = SimpleCalculator()
    calculator.run(statement)
    print(f'simplecalculator log: {calculator.log}')
    if calculator.log[-1] == 'result: Error':
        raise InputSyntaxError
    # The calculator.log is a list of string. The result is the last element.
    return calculator.log[-1].split(' ')[1]
