# Higher order function: A function that either accepts a function as an argument or returns a function.

'''

def loud(text):
    return text.upper()


def quiet(text):
    return text.lower()


def hello(func):
    text = func("Hello")
    print(text)


hello(quiet)
'''


def divisor(x):  # 7
    def dividend(y):  # 10
        return y / x
    return dividend


divide = divisor(7)
print(divide(10))
