# python interpreter sets special variables, one of which is __main__
# python assigns the __name__ variable a value of __main__ if it's the initial module being run
# used to add flexibility, and module can be used and imported by other modules.

import mod_2

# print(__name__)
# print(mod_2.__name__)


def hello():
    print(hello)


if __name__ == "__main__":
    print("Running this module directly")
else:
    print("Running the module indirectly")
