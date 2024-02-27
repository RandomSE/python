import time

print(time.ctime(1700000000))  # converts a time expressed in seconds sice epoch began to a readable string
# epoch: when your computer thinks time began/ reference point
# print(time.time())  # returns current seconds since epoch
# print(time.ctime(time.time()))

# formatting:   https://docs.python.org/3/library/time.html#time.strftime
'''
current_time = time.localtime()
string_time = time.strftime("%B %d %Y %H: %M %S", current_time)
print(string_time)
utc_time = time.gmtime(0)  # epoch for most systems
str_utc_time = time.strftime("%B %d %Y %H: %M %S", utc_time)
print(str_utc_time)

time_string = "7 February, 2023"
time_object = time.strptime(time_string, "%d %B, %Y")  # the punctuation and order is VERY important.
print(time_object)
'''

# year, month, day, hours, minutes, seconds, day of week, day of year, daylights saving
time_tuple = (2023, 11, 15, 0, 13, 20, 2, 0, -1)
time_tuple_string = time.asctime(time_tuple)
time_mk_tuple = time.mktime(time_tuple)
print(time_tuple_string)
print(time_mk_tuple)