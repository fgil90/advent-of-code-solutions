# from collections import Counter

words = [line.strip() for line in open('2015-05.txt', 'r')]

niceWords = 0

def isNice(word):
    check1 = [word[i] == word[i+2] for i in range(len(word)-2)]
    if not any(check1):
        return False
    check2 = [word.count(word[i:i+2])>1 for i in range(len(word)-2)]
    return any(check2)


# def isNice1(word):
#     if ("ab" in word or "cd" in word or "pq" in word or "xy" in word):
#         return False

#     vowelCount = word.count("a") + word.count("e") + word.count("i") + word.count("o") + word.count("u")
#     if vowelCount < 3:
#         return False

#     prevChar=''
#     for character in word:
#         if (prevChar == character):
#             return True
#         prevChar = character

# def isNice2(word):
#     counter = Counter()
#     prevChar = '0'
#     prevPrevChar = '0'
#     inBetween = False
#     for character in word:
#         charPair = prevChar + character
#         inBetween = inBetween or (prevPrevChar == character)
        
#         if not (prevPrevChar == prevChar and prevChar == character):
#             counter[charPair] += 1
#             prevPrevChar = prevChar
#         else:
#             prevPrevChar = '0'
#         prevChar = character
#     return (inBetween and counter.most_common(1)[0][1] > 1)


for word in words:
    if (isNice(word)):
        niceWords+=1 




