def divide(a, b, floor = True):
    try:
        if floor == True:
            return round(a/b)
        else:
            return a/b
    except TypeError:
      # pass
        print("Values must be integers")