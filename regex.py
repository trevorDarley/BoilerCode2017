def character():
    return "(" + raw_input("Enter the specific characters to search for:") + ")"
def characterSet():
    response2 = raw_input("1.) Any uppercase letter\n 2.) Any lowercase letter\n 3.) Any letter\n 4.) Any number\n 5.) Any number or letter\n 6.) Any character\n 7.) Custom character set\n")
    setVar=""
    if response2 == "1":
        setVar += "[A-Z]"
    elif response2 == "2":
        setVar += "[a-z]"
    elif response2 == "3":
        setVar += "[a-zA-Z]"
    elif response2 == "4":
        setVar += "[0-9]"
    elif response2 == "5":
        setVar += "[a-zA-Z0-9]"
    elif response2 == "6":
        setVar += "."
    elif response2 == "7":
        setVar += "[" + raw_input('Enter a set of characters. This can be a list of specific characters, like abcde, or it can be a range of characters, like A-Y.\n') + "]"
    
    response3 = raw_input("How many times may this character appear?\n 1.) any number of times\n 2.) exactly x times\n 3.) x or more times\n 4.) x to y times\n")
    if response3 == "1":
        setVar += "*"
    elif response3 == "2":
        setVar += "{"+ raw_input('Enter how many times this character or character set should appear: ') + "}"
    elif response3 == "3":
        setVar += "{" + raw_input('Enter the minimum number of times this character or character set should appear: ') + ",}"
    elif response3 == "4":
        setVar += "{" + raw_input('Enter the minimum number of times this character or character set should appear: ') + "," + raw_input('Enter the maximum number of times this character or character set should appear: ') + "}"
    return setVar

def menu():
    print "Build a custom pattern to search for in your files' contents."
    regex = ""
    while(1):
        response1 = raw_input("1.)Specific characters \n2.)Set of characters \n3.)Done\n")
        if response1 == "1":
              regex+=character()
        elif response1 == "2":
              regex+=characterSet()
        elif response1 == "3":
              return regex




