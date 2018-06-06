score_dict = {}
for char in "A,B,D,E,G,I,N,O,R,S,T,U".split(","):
    score_dict[char] = 1
for char in "C,F,H,L,M,P,V,W,Y".split(","):
    score_dict[char] = 2
for char in "J,K,Q,X,Z".split(","):
    score_dict[char] = 3

# return score of a word (int)
def calculate_score(word, request):
    score = 0
    if satisfied(word, request):
        for char in word:
            score += score_dict[char]
    return pow((score+1),2)

# return True if word is satisfied (boolean)
def satisfied(word, request):
    contains = False
    word = sorted(word)
    request = sorted(request)
    index = 0
    for char in request:
        if char == word[index]:
            index += 1
            if index == len(word):
                contains = True
                break
    return contains

def find_max(dictionary, request):
    if len(dictionary) == 1:
        return calculate_score(dictionary[0], request), dictionary[0]
    else:
        length = len(dictionary)
        max_left, word_left = find_max(dictionary[:int(length/2)], request)
        max_right, word_right = find_max(dictionary[int(length/2):], request)
        return (max_left, word_left) if max_left>max_right else (max_right, word_right)

# print(satisfied("abg", "abcsd"))
# request = "IZWWRBXFQRVDMALQ"
request = "rmdbqovsvdgbcoxj"
request = request.upper()
with open("./dictionary.words.txt", "r") as f:
    dictionary = [word.strip().upper().replace("QU", "Q") for word in f.readlines()]

score, result = find_max(dictionary, request)
print(score)
print(result.replace("Q", "QU"))