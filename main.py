# Check if two words are anagrams
# Example:
# find_anagrams("hello", "check") --> False
# find_anagrams("below", "elbow") --> True


def find_anagram(word, anagram):
    # [assignment] Add your code here
    #word1 = "dictionary"
    #word2 = "indicatory"
    word1 = input("enter first word> ")
    word2 = input("enter second word> ")
    if(sorted(word1) == sorted(word2)):
        return True
    else:
        return False
print(find_anagram("dictionary", "indicatory"))