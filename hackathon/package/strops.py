import string

def getspan(s, ss):
   
    try:
        start = s.index(ss)
        end = start + len(ss)
        return (start, end)
    except ValueError:
        return (-1, -1)  

def reverseWords(s):
    words = s.split()
    return ' '.join(reversed(words))

def removePunctuation(s):
    return ''.join(c for c in s if c not in '.,!?":;()[]{}')

def countWords(s):
    return len(s.split())

def characterMap(s):
    return {char: s.count(char) for char in set(s)}

def makeTitle(s):
    return s.title()

def normalizeSpaces(s):
    return ' '.join(s.split())

def transform(s):
    return s[::-1].swapcase()

def getPermutations(s):
    if len(s) == 1:
        return [s]
    return [s[i] + p for i in range(len(s)) for p in getPermutations(s[:i] + s[i+1:])]