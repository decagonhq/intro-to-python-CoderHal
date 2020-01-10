def divide(number1, number2, floor = True):
    try:
        if floor == True:
            return round(number1/number2)
        else:
            return number1/number2
    except TypeError:
        raise TypeError("Values must be integers")
