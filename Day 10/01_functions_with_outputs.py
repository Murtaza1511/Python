# This function converts full name into title case e.g. Murtaza Tinwala
def format_name(first_name, last_name):
    """Take first and last name and format it to return a title case version of 
    the name
    """
    if first_name == "" or last_name == "":
        return "You didn't provide valid inputs"
    f_name = first_name.title()
    l_name = last_name.title()
    return (f_name + " "+l_name)


full_name = format_name(input("What is your first name? "), input("What is your last name? "))
print(full_name)
