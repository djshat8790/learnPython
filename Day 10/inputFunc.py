
first_name = input()
last_name = input()


def format_name(f_name, l_name):
    formated_name = f_name.title()+" "+l_name.title()
    return formated_name


print(format_name(first_name, last_name))

