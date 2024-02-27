# zip function: zip(*iterables) aggregate elements from two or more iterables (list, tuple, dictionary etc.)
# and creates a zip object with paired values stored in tuples for each element/

usernames = ["Anon", "Big Jim", "Small Jim"]
passwords = ["'#PQ,AIDB&y['5]iaag8,ssm5gz4ee9^uf0{M~-k((HZZQMU", "Pam_the_lamb", "Solitary_Turtle37^"]
last_login = ["7 January 2021", "9 December 2023", "8 September 2023"]
users = zip(usernames, passwords, last_login)
for i in users:
    print(i)

print(type(users))
