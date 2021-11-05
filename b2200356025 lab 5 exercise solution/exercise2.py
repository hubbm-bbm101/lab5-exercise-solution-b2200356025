def is_mail(strng):
    if "@" in strng and "." in strng:
        return True
    return False

print(is_mail(input("enter your email")))