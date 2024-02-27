# reduce() applies a function of choosing to an iterable, and reduces to a single cumulative value.
# performs function on first 2 elements and repeats process until 1 element remains. # reduce(function, iterable)
import functools
vowels = ["A", "E", "I", "O", "U"]
word = functools.reduce(lambda x, y: x + y, vowels)
print(word)

factorial = [5, 4, 3, 2, 1]
result = functools.reduce(lambda x, y: x * y, factorial)
print(result)
