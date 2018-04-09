# One away: There are three types of edits that can be performed on strings: insert a char, delete a char, or replace
# a char. Given two strings, write a function to check if they are 1 or less edits away.


def isoneeditaway(a, b):
    if a is b:
        return True
    elif abs(len(a)-len(b)) > 1:
        return False

    elif abs(len(a)-len(b)) is 1:
        s1 = a if (len(a) < len(b)) else b
        s2 = (a, b)[(len(a) < len(b))]  # same as above, but I think it's an interesting way to do ternary in python

        s1_ind = 0
        s2_ind = 0

        # THere is a bug in here.
        for _ in range(len(s1)):
            if not s1[s1_ind] is s2[s2_ind] and s1_ind is s2_ind:
                s1_ind += 1
            elif s1[s1_ind] is s2[s2_ind]:
                s1_ind += 1
                s2_ind += 1
            else:
                return False

    else:
        count = 0
        for i in range(len(a)):
            if a[i] is b[i]:
                continue
            elif not a[i] is b[i]:
                count += 1

            if count > 1:
                return False
    return True






print(isoneeditaway('b', 'a'))
