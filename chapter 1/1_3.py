#  Write a method to replace all spaces in a string with %20

# This needs to be WAY more effecient. But it is how I would work through it.
def urlify(url, urllen):
    newurl = url[::-1]
    lasturl = []
    for c in newurl:
        if not c == " ":
            lasturl.append(c)
        else:
            lasturl.append('%20')

    return ''.join(lasturl[::-1])


test1 = 'Hello this is a test'
test2 = ''
test3 = 'Thishasnospace'

print(urlify(test1, len(test1)))
print(urlify(test2, 14))
print(urlify(test3, 14))
