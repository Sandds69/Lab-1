str = input("Enter a palindrome: ")
str = str.lower().replace(" ", "")
rev = ''.join(reversed(str))
# print(rev, str)
print(f"Is palindrome: {rev == str}")