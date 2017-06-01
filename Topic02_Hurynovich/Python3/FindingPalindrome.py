"""Program for checking the phrase on palindrome."""
PHRASE = input('Write a phrase below:\n')


def reverse_phrase(string):
    """Function to get a reverse phrase."""
    return ''.join(reversed(string))
print("This phrase is a palindrome" if PHRASE == reverse_phrase(PHRASE)
      else "This phrase is not a palindrome")
