def isPalindrome(input):
    return input == input[::-1]

input = input()

if isPalindrome(input)==True:
    print("1")
else:
    print("0")