
# coding: utf-8

# In[16]:

import re


# In[17]:

def longest_substring(s):
    '''
    My docstring
    '''
    
    a=str(s)
    b = list(a)
    
    c = []
    
    for number in range(0,len(b)):
        d = []
        for letter in b[number:]:
            d.append(letter)
            if len(d) > 1:
                c.append(''.join(d))
    
    e = list(set(c))
    e.sort(key = lambda s: len(s))
    
    result = []
    
    for end in e[::-1]:
        for front in e:
            if len(re.findall(re.escape(front),end))>1:
                verdict = False
                break
            else:
                verdict = True
                continue
        if len(result) < 1:
            if verdict:
                result.append((end, len(end)))
        else:
            if verdict:
                if len(end) >= len(result[0][0]):
                    result.append((end, len(end)))
                else:
                    break
                    
    return result

