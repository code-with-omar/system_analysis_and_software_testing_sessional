# string = input("Please Enter a Number or String: ")
# reversedString = string[::-1]
# if string == reversedString:
#     print(f"{string} is a Palindrome")
# else:
#     print(f"{string} is not a Palindrome")


def is_palindrome(value):
    convert_string = str(value)
    start = 0
    end = len(value) - 1
    while start < end:
        if convert_string[start] != value[end]:
            return False
        start += 1
        end -= 1
    return True

input_str_or_num = input("Enter a number or string: ")
result = is_palindrome(input_str_or_num)
if result:
    print(f"{input_str_or_num} is a palindrome")
else:
    print(f"{input_str_or_num} is not palindrome")
