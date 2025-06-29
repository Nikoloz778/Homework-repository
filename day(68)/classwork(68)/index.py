def just_function(string):
    # string="apple$banana$mango$peach"
    string= string.split("$")
    return print(string)

just_function("The$world$is$yours")