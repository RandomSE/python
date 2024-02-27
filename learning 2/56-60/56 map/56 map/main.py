# map(): applies a function to each item in an iterable (such as tuples or lists) # map(function, iterable)

store = [("Hoodie", 22.00),
         ("Tie", 10.00),
         ("Jeans", 17),
         ("Socks", 13)]
to_euros = lambda data: (data[0], data[1] * 0.93)
to_USD = lambda data: (data[0], data[1] / 0.93)
store_euros = list(map(to_euros, store))
store_USD = list(map(to_USD, store_euros))
for i in store_USD:
    print(i)
