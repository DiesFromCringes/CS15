def palindrome(text):
    if len(text)<1:
        return "This is a palindrome."
    else :
        if text[0] == text[-1]:
            return palindrome(text[1:-1])
        else:
            return "This is not a palindrome." 
print(palindrome("HANAH"))
def palindrome2(text):
    if text == text[::-1]:
        return "This is a palindrome."
    return "This is not a palindrome." 
print(palindrome2("HANAH1"))