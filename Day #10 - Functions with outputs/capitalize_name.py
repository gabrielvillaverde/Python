# Exercise to format any first name and last name with an initial capital letter and the rest in lowercase.

def get_name():
    while True:
        name = input("What is your name? ")
        if name.isalpha():
            name = name.capitalize()
            return name
        else:
            print("Please enter alphabetic characters only for your name.")
            
def get_last_name():
    while True:
        last_name = input("What is your last name? ")
        if last_name.isalpha():
            last_name = last_name.capitalize()
            return last_name
        else:
            print("Please enter alphabetic characters only for your last name.")

def format_name():
    f_name = get_name()
    l_name = get_last_name()
    return f"{f_name} {l_name}" # The format_name() function uses f"{f_name} {l_name}" to create a formatted string that combines the first name and last name with a space in between.

complete_name = format_name()
print(complete_name)
