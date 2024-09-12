# def format_name(f_name, l_name):
#     formated_f_name = f_name.title()
#     formated_l_name = l_name.title()
#     return f"{formated_f_name} {formated_l_name}"
#
#
# formatted_name = format_name("AnGeLa", "YU")
#
# length = len(formatted_name)
#
#
#

def is_leap_year(current_year):
    # Write your code here.
    # Don't change the function name.
    current_year = int(input("Which year are you in?: "))
    leap = True
    if current_year % 4 == 0:
        if current_year % 100 != 0:
            print("This is a leap year")
        elif current_year % 400 == 0:
            print("This is a leap year")
        else:
            print("This is not a leap year")
            leap = False
    else:
        print("This is not a leap year")
        leap = False
    return leap


is_leap_year(2024)