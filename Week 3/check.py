# def string(s):
#     print("Contains only letters:", s.isalpha())
#     print("Contains only uppercase:", s.isupper())
#     print("Contains only lowercase:", s.islower())
#     print("Contains only digits:", s.isdigit())
#     print("Contains letters and digits:", s.isalnum() and not s.isalpha() and not s.isdigit())
#     print("Starts with uppercase:", s[0].isupper() if s else False)
#     print("Ends with full stop:", s.endswith('.'))

# input_string = input("Enter a string: ")
# string(input_string)


def str_ing(st):
    print("The String contains only letters:",st.isalpha())
    print("The string contains only uppercase;", st.isupper())
    print("The string contains only lowercase;", st.islower())
    print("The string contains only digits;", st.isdigit())
    print("The string contains only letters and digits;", st.isalnum() and not st.isalpha() and not st.isdigit())
    print("The string starts uppercase;", st[0].isupper() if st else False)
    print("The string contains only uppercase;", st.endswith('.'))

input_string = input("Enter any stings:")
str_ing(input_string)