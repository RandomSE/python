# dictionary comprehension: way to create dictionary using an expression. can replace for loops and some lambda func
# dictionary = {key: expression for (key,value) in iterable}
# can also {key: expression for (key,value) in iterable if conditional } or {key: (if/else) for (key,value) in iterable}
# {key: function(value) for (key,value) in iterable}
Places_in_c = {"Milnerton": 28, "Goodwood": 31, "Bellville": 23, "Athlone": 17}
Weather_in_ct = {"Milnerton": "sunny", "Goodwood": "cloudy", "Bellville": "sunny", "Athlone": "sunny"}

Sunny_weather = {key: value for (key, value) in Weather_in_ct.items() if value == "sunny"}
Places_in_f = {key: ((value * 9/5) + 32) for (key, value) in Places_in_c.items()}
# Desc_cities = {key: ("Too warm" if value >= 24 else "Good") for (key, value) in Places_in_c.items()}
# print(Places_in_f)
# print(Sunny_weather)


def check_temp(value):
    if value >= 24:
        return "too warm"
    else:
        return "good"


Desc_cities = {key: check_temp(value) for (key, value) in Places_in_c.items()}
print(Desc_cities)
