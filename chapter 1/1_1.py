# Implement an algorithm to determine if a string has all unique characters.

# Would we consider capitalization as different letters?

def isunique(s):

    if len(s) > 256 or len(s) < 1:
        return False

    charmap = [False for _ in range(256)]  # assumes extended ASCII

    for c in s:
        if charmap[ord(c)]:
            return False
        else:
            charmap[ord(c)] = True
    return True


test1 = 'ABC'
test2 = 'AABC'
test3 = 'ABCC'
test4 = 'aA'
test5 = ''

print(isunique(test1))
print(isunique(test2))
print(isunique(test3))
print(isunique(test4))
print(isunique(test5))