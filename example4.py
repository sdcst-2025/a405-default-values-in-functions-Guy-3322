#!python3

# EXTENSION

# You may sometimes see the use of * in the function input parameters.
# This indicates that multi[ple values are ex[ected, and that they will be
# used to create a tuple

# There is also a **kwargs input parameter (for KeyWord Arguments)
# that creates a dictionary object, which we will see in Grade 12

# What is the difference between a Tuple and a List?

def argsExample(*args):
    print(f"The input is a variable of type {type(args)}" )
    print(f"The value of the variable is {args}")
    print(f"The variable has a length of {len(args)}")

def main():
    print("A function call with 4 inputs:")
    argsExample(1,2,3,"hello")
    print("")
    print("")
    print("")
    print("A function call with 6 inputs:")
    argsExample(1,2,3,"hello",True,1.3)
    print("")
    print("")
    print("")


if __name__ == "__main__":
    main()
    