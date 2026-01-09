palindrome= str(input("Mot: "))
if palindrome == palindrome[::-1]:
    print(palindrome,"est un palindrome.")
else:
    print(palindrome," n'est pas un palindrome.")