"""Program for checking the phrase on palindrome."""
PHRASE = raw_input('Write a phrase below:\n').decode("utf-8")
REVERSE_PHRASE = PHRASE[::-1]
print "This phrase is a palindrome" if PHRASE == REVERSE_PHRASE \
    else "This phrase is not a palindrome"
