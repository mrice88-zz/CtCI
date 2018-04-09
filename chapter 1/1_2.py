# Given two strings, write a method to decide if one is a permutation of the other.


def checkpermutation(a,b):
    try:  # Handles weird input being handed to it.
        return sorted(a) == sorted(b)
    except TypeError:
        return False



test1 = ['', 'a']
test2 = ['abc', 'acb']
test3 = ['', '']
test4 = ['abc', 'def']
test5 = [1, '1']

print(checkpermutation(test1[0], test1[1]))
print(checkpermutation(test2[0], test2[1]))
print(checkpermutation(test3[0], test3[1]))
print(checkpermutation(test4[0], test4[1]))
print(checkpermutation(test5[0], test5[1]))

