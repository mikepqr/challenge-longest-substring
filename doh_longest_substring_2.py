
# coding: utf-8

def longest_substring(s):

    '''

    Arg:
        s = string to be evaluated for longest substring

    Output:
        len(substring) = length of the longest substring in int

    '''

    substrings = ''

    for number in range(0, len(set(s))+1)[::-1]:
        start = 0
        end = number
        while ((end <= len(s)) and (start != end)):

            if len(list(s[start:end])) == len(set(s[start:end])):
                substrings = s[start:end]
                break

            start += 1
            end += 1

        if len(substrings) > 0:
            break

    return len(substrings)
