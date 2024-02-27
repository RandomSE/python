import os, random, shutil
'''
 
# random, requires the import random
x = random.randint(1, 6)
y = random.random
rps = ["Rock", "Paper", "Scissors"]
z = random.choice(rps)
print(z)

cards = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "J", "Q", "K", "A"]
random.shuffle(cards)
print(cards)



# exceptions : events found during execution, alter the flow of a program. *** important

try:
    numerator = int(input("Put a number: "))
    denominator = int(input("Put  a number to divide by: "))
    result = numerator / denominator
except ZeroDivisionError as e:
    print("You cannot divide by zero.")
    print(e)

except ValueError as e:
    print("You cannot divide by a string literal.")
    print(e)

except Exception as e:
    print("An error occurred.")
    print(e)
else:
    print(result)
finally:
    print("The program has run.")



# file reading, requires the import os
path = "C:\\Users\\the11\\PycharmProjects\\learning\\Random-exception\\Test_folder"

if os.path.exists(path):
    print("That location exists.")
    if os.path.isfile(path):
        print("That is a file.")
    elif os.path.isdir(path):
        print("That is a directory.")
else:
    print("That location does not yet exist.")


try:
    with open('Test.txt') as file:
        print(file.read())
except FileNotFoundError as e:
    print(u"\u001b[32m File not found.")
    print("Error: " + str(e))
finally:
    try:
        print(file.closed)
    except NameError as e:
        print(e)
        

# file writing
text = "Robert^Smith^54"  # \n adds a line  after
with open("Test2.txt", "w") as file:  # "w" changes into write mode. "a" will append.
    file.write(text)
    
'''
# file copying, requires import shutil : copyfile() copies contents of a file, copy() copyfile + permission
# + destination can be directory. copy2() = copy() + copies metadata (file creation and modification times)
the_path = "C:\\Users\\the11\\PycharmProjects\\learning\\Random-exception\\Copy.txt"
if not os.path.exists(the_path):
    shutil.copy2("Test.txt", the_path)
else:
    print("File has already been copied to requested location.")

# moving files, requires import os module.
source = "Copy.txt"
destination = "C:\\Users\\the11\\PycharmProjects\\learning\\Random-exception\\Moved folder\\Copy.txt"

try:
    if os.path.exists(destination):
        print("File already exists there.")
        # figure out how to (safely) delete a file with pyton
    else:
        os.replace(source, destination)
        print(source + " was moved.")

except FileNotFoundError as e:
    print(source + " Was not found.")
