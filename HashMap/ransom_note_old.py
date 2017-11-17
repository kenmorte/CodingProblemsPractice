# second line = magazine
# third line = ransom note
# we can use the magazine to create the ransom note

# dictionary to keep track of the words and #occurrences (for both ransom and magazine)
#   iterate through the ransom note dictionary
#       if the word in ransom is not in the mag ---> return false
#       if the #ocurrences_in_ransom <= #ocurrences_in_mag --> perfect!
#       else --> return False
#   return True

def get_words(l: [str]) -> {str:int}:
    result = dict()
    for word in l:
        if word not in result:
            result[word] = 0
        result[word] += 1
    return result

def ransom_note(magazine, ransom):
    
    # keeping the number of occurrences for each word inside each list
    magazine_words = get_words(magazine)
    ransom_words = get_words(ransom)
    
    for word in ransom_words:
        if word not in magazine_words or ransom_words[word] > magazine_words[word]:
            return False
    return True
    

m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
answer = ransom_note(magazine, ransom)
if(answer):
    print("Yes")
else:
    print("No")
    
