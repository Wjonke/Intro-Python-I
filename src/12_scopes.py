# Experiment with scopes in Python.
# Good reading: https://www.programiz.com/python-programming/global-local-nonlocal-variables

# When you use a variable in a function, it's local in scope to the function.
# This prints 12. What do we have to modify in change_x() to get it to print 99?
x = 12
# ^^^^^-----this is a global variable
print("Original global x----->", x)
def change_x():
    global x
    #  ^^^^-----by using global we are changing x globally be redefining it locally
    x = 99
change_x()
print("Global X(12) changed to 99 inside function by calling 'global' keyword--------->", x)


# This nested function has a similar problem.

def outer():
    y = 120
    print("Original local y ----->", y)

    def inner():
        nonlocal y
        y = 999

    inner()

    # This prints 120. What do we have to change in inner() to get it to print
    # 999?
    # Note: Google "python nested function scope".
    print("Local y(120) changed to 999 inside function by calling 'nonLocal' keyword in nested function--------->", y)


outer()
