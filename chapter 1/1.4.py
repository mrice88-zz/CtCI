# Palindrome Permutation: given a string write a function to check if it is a permutation of a palindrome.


def ispalindromepermutation(s):
    charcount = {}
    oddcount = 0

    # One pass through the string.
    for c in s:
        if not c.isalnum():
            continue
        c = c.lower()  # lets ignore case.
        try:
            charcount[c] += 1
        except KeyError:
            charcount[c] = 1

        if charcount[c] % 2 is 1:
            oddcount += 1
        else:
            oddcount -= 1
    return oddcount < 2


test1 = 'Tacoz cat'
test2 = ''
test3 = 'Palindrome'
test4 = 'taco cat'
test5 = 'TACO CAT'

print(ispalindromepermutation(test1))
print(ispalindromepermutation(test2))
print(ispalindromepermutation(test3))
print(ispalindromepermutation(test4))
print(ispalindromepermutation(test5))


