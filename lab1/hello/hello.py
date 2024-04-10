
#Import libraries

#Global Variables

#Function Definitions
def say_hi():
    '''Takes in no arguments and returns a Hello World string'''
    return "Hello, world"
def generic_hi(name="world"):
    '''Takes in one argument and returns a "Hello, <argument>!" string. Default argument is world '''
    return f"Hello, {name}!"


if __name__ == "__main__":
    # Gather Inputs

    # Perform Calculations

    # Formatted Output

    #test say_hi()
    help(say_hi)
    print(say_hi())
    assert say_hi() == "Hello, world", "Test failed: say_hi() should return 'Hello, world'"

    #test generic_hi
    help(generic_hi)
    print(generic_hi())
    assert generic_hi() == "Hello, world!", "Test failed: generic_hi() with default arg should return 'Hello, world!'"

    ##Tests generic_hi() with "Art" as argument
    print(generic_hi("Art"))
    assert generic_hi("Art") == "Hello, Art!", "Test failed: generic_hi('Art') should return 'Hello, Art!'"
