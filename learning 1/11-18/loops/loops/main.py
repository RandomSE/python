
'''
name = None

while not name:
    name = input("What's your name?")

print("Hello, " + name)


for i in "abcdefghijklmnopqrstuvwxyz":
    print(i)

for seconds in range(10, 0, -1):
    print(seconds)
    time.sleep(1)
print("zero.")


rows = int(input("How many rows"))
columns = int(input("How many columns"))
# Not = int(input("Where in the row should there be an empty spot?"))
symbol = str(input("What symbol should be used?"))

for i in range(rows):
    for j in range(columns):
        print(symbol, end="")

    print()


while True:
    Name = input("What is your name?")
    if Name != "":
        break

print(Name)

phone_number = "079-332-7623"
for i in phone_number:
    if i == "-":
        continue
    print(i, end="")

'''

for i in range(1, 21):

    if i == 13:
        pass
    else:
        print(i)
