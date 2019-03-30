try:
    x = int(input("Input a num: "))
    if x < 0:
        raise ValueError("Number must be postive")
    if x > 1000:
        raise ValueError("Number may not exceed 1000")
except ValueError as ex:
    print(ex)
