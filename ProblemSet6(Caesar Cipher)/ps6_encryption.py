# credits MITx 6.00.1x course edx
# 6.00x Problem Set 6
#
# Part 1 - HAIL CAESAR!

import string
import random

WORDLIST_FILENAME = "words.txt"

# -----------------------------------
# Helper code
# (you don't need to understand this helper code)
def loadWords():
    """
    Returns a list of valid words. Words are strings of lowercase letters.
    
    Depending on the size of the word list, this function may
    take a while to finish.
    """
    print "Loading word list from file..."
    inFile = open(WORDLIST_FILENAME, 'r')
    wordList = inFile.read().split()
    print "  ", len(wordList), "words loaded."
    return wordList

def isWord(wordList, word):
    """
    Determines if word is a valid word.

    wordList: list of words in the dictionary.
    word: a possible word.
    returns True if word is in wordList.

    Example:
    >>> isWord(wordList, 'bat') returns
    True
    >>> isWord(wordList, 'asdf') returns
    False
    """
    word = word.lower()
    word = word.strip(" !@#$%^&*()-_+={}[]|\\:;'<>?,./\"")
    return word in wordList

def randomWord(wordList):
    """
    Returns a random word.

    wordList: list of words  
    returns: a word from wordList at random
    """
    return random.choice(wordList)

def randomString(wordList, n):
    """
    Returns a string containing n random words from wordList

    wordList: list of words
    returns: a string of random words separated by spaces.
    """
    return " ".join([randomWord(wordList) for _ in range(n)])

def randomScrambled(wordList, n):
    """
    Generates a test string by generating an n-word random string
    and encrypting it with a sequence of random shifts.

    wordList: list of words
    n: number of random words to generate and scamble
    returns: a scrambled string of n random words

    NOTE:
    This function will ONLY work once you have completed your
    implementation of applyShifts!
    """
    s = randomString(wordList, n) + " "
    shifts = [(i, random.randint(0, 25)) for i in range(len(s)) if s[i-1] == ' ']
    return applyShifts(s, shifts)[:-1]

def getStoryString():
    """
    Returns a story in encrypted text.
    """
    return open("story.txt", "r").read()


# (end of helper code)
# -----------------------------------


#
# Problem 1: Encryption
#
def buildCoder(shift):
    """
    Returns a dict that can apply a Caesar cipher to a letter.
    The cipher is defined by the shift value. Ignores non-letter characters
    like punctuation, numbers and spaces.

    shift: 0 <= int < 26
    returns: dict
    """
    dict={'A': 'A', 'C': 'C', 'B': 'B', 'E': 'E', 'D': 'D', 'G': 'G', 'F': 'F', 'I': 'I', 'H': 'H', 'K': 'K', 'J': 'J', 'M': 'M', 'L': 'L', 'O': 'O', 'N': 'N', 'Q': 'Q', 'P': 'P', 'S': 'S', 'R': 'R', 'U': 'U', 'T': 'T', 'W': 'W', 'V': 'V', 'Y': 'Y', 'X': 'X', 'Z': 'Z', 'a': 'a', 'c': 'c', 'b': 'b', 'e': 'e', 'd': 'd', 'g': 'g', 'f': 'f', 'i': 'i', 'h': 'h', 'k': 'k', 'j': 'j', 'm': 'm', 'l': 'l', 'o': 'o', 'n': 'n', 'q': 'q', 'p': 'p', 's': 's', 'r': 'r', 'u': 'u', 't': 't', 'w': 'w', 'v': 'v', 'y': 'y', 'x': 'x', 'z': 'z'}
    for keys in dict:
        if ord(keys)>=65 and ord(keys)<=90:
            ascii_value=ord(keys)
            new_ascii=shift+ascii_value
            if new_ascii>90:
                new_ascii=new_ascii+13
                new_ascii=new_ascii%26
                new_ascii += 65
            dict[keys]=chr(new_ascii)
                
        if ord(keys)>=97 and ord(keys)<=122:
            ascii_value=ord(keys)
            new_ascii=shift+ascii_value
            if new_ascii>122:
                new_ascii=new_ascii+7
                new_ascii=new_ascii%26
                new_ascii += 97
            dict[keys]=chr(new_ascii)
    return dict

def applyCoder(text, coder):
    """
    Applies the coder to the text. Returns the encoded text.

    text: string
    coder: dict with mappings of characters to shifted characters
    returns: text after mapping coder chars to original text
    """
    map_text=[]
    for letters in text:
        if (ord(letters)>=65 and ord(letters)<=90) or (ord(letters)>=97 and ord(letters)<=122):
            map_text.append(coder[letters])
        else:
            map_text.append(letters)
    return ''.join(map_text)            
    

def applyShift(text, shift):
    """
    Given a text, returns a new text Caesar shifted by the given shift
    offset. Lower case letters should remain lower case, upper case
    letters should remain upper case, and all other punctuation should
    stay as it is.

    text: string to apply the shift to
    shift: amount to shift the text (0 <= int < 26)
    returns: text after being shifted by specified amount.
    """
    return applyCoder(text, buildCoder(shift))

#
# Problem 2: Decryption
#
def findBestShift(wordList, text):
    """
    Finds a shift key that can decrypt the encoded text.

    text: string
    returns: 0 <= int < 26
    """
    shift=0
    bigcount=0
    final_count=0
    final_shift=0
    while(shift<26):
        count=0
        decrypted=applyShift(text, shift)
        dlist=decrypted.split(' ')
        for elements in dlist:
            l=len(elements)
            flag=False
            wordlist=list(elements)
            for letters in elements:
                if (ord(letters)>=65 and ord(letters)<=90) or (ord(letters)>=97 and ord(letters)<=122):
                    pass
                else:
                    flag=True
            if flag:
                wordlist=wordlist[:-1]
                word=''.join(wordlist)
            else:
                word=elements
            if isWord(wordList, word):
                count +=1
        if count>bigcount:
            bigcount=count
            final_shift=shift
        shift +=1
    return final_shift

def decryptStory():
    """
    Using the methods you created in this problem set,
    decrypt the story given by the function getStoryString().
    Use the functions getStoryString and loadWords to get the
    raw data you need.

    returns: string - story in plain text
    """
    wordList=loadWords()
    encrypted_story=getStoryString()
    shift_story=findBestShift(wordList, encrypted_story)
    return applyShift(encrypted_story, shift_story)

#
# Build data structures used for entire session and run encryption
#

if __name__ == '__main__':
    # To test findBestShift:
    #wordList = loadWords()
    #s = applyShift('Hello, world!', 8)
    #bestShift = findBestShift(wordList, s)
    #assert applyShift(s, bestShift) == 'Hello, world!'
    # To test decryptStory, comment the above four lines and uncomment this line:
    print decryptStory()
