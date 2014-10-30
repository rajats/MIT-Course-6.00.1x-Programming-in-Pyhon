# credits MITx 6.00.1x course edx

from ps4a import *
import time


#
#
# Problem #6: Computer chooses a word
#
#
def compChooseWord(hand, wordList, n):
    """
    Given a hand and a wordList, find the word that gives 
    the maximum value score, and return it.

    This word should be calculated by considering all the words
    in the wordList.

    If no words in the wordList can be made from the hand, return None.

    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)

    returns: string or None
    """
    score=0
    temp=0
    p_word,store_word='',''
    for word in wordList:
        if isValidWord(word, hand, wordList):
            temp=score
            p_word=store_word
            score=getWordScore(word, n)
            store_word=word
            if temp>score:
                score=temp
                store_word=p_word
    if score==0:
            return None
    else:       
        return store_word



#
# Problem #7: Computer plays a hand
#
def compPlayHand(hand, wordList, n):
    """
    Allows the computer to play the given hand, following the same procedure
    as playHand, except instead of the user choosing a word, the computer 
    chooses it.

    1) The hand is displayed.
    2) The computer chooses a word.
    3) After every valid word: the word and the score for that word is 
    displayed, the remaining letters in the hand are displayed, and the 
    computer chooses another word.
    4)  The sum of the word scores is displayed when the hand finishes.
    5)  The hand finishes when the computer has exhausted its possible
    choices (i.e. compChooseWord returns None).
 
    hand: dictionary (string -> int)
    wordList: list (string)
    n: integer (HAND_SIZE; i.e., hand size required for additional points)
    """
    score=0
    total=0
    while(sum(hand.values()) > 0):
        print "Current Hand: ",
        displayHand(hand)
        c_word=compChooseWord(hand, wordList, n)
        if c_word!=None:
            score=getWordScore(c_word, n)
            total +=score
            hand=updateHand(hand, c_word)
            print '"',c_word,'" earned', score, 'points. Total:', total, 'points.'
        elif c_word==None:
            print 'Total score: ',
            print total,' points.'
            break 
        if calculateHandlen(hand)==0:
            print 'Total score: ',
            print total,' points.'
            break 
        print ''

    
#
# Problem #8: Playing a game
#
#
def playGame(wordList):
    """
    Allow the user to play an arbitrary number of hands.
 
    1) Asks the user to input 'n' or 'r' or 'e'.
        * If the user inputs 'e', immediately exit the game.
        * If the user inputs anything that's not 'n', 'r', or 'e', keep asking them again.

    2) Asks the user to input a 'u' or a 'c'.
        * If the user inputs anything that's not 'c' or 'u', keep asking them again.

    3) Switch functionality based on the above choices:
        * If the user inputted 'n', play a new (random) hand.
        * Else, if the user inputted 'r', play the last hand again.
      
        * If the user inputted 'u', let the user play the game
          with the selected hand, using playHand.
        * If the user inputted 'c', let the computer play the 
          game with the selected hand, using compPlayHand.

    4) After the computer or user has played the hand, repeat from step 1

    wordList: list (string)
    """
    total=0
    score=0
    p_hand={}
    while(True):
        choice=raw_input('Enter n to deal a new hand, r to replay the last hand, or e to end game: ')
        if (choice=='n'):
            while(True):
                c_or_u=raw_input('Enter u to have yourself play, c to have the computer play: ')
                if c_or_u=='u':
                    c_hand=dealHand(HAND_SIZE)
                    p_hand=c_hand
                    playHand(c_hand, wordList, HAND_SIZE)
                    break
                elif c_or_u=='c':
                    c_hand=dealHand(HAND_SIZE)
                    p_hand=c_hand
                    compPlayHand(c_hand, wordList, HAND_SIZE)
                    break
                else:
                    print 'Invalid command.'
                    print ''
            
            
        elif choice=='r':
            if p_hand=={}:
                print 'You have not played a hand yet. Please play a new hand first!'
                print ''
            else:
                while(True):
                    c_or_u=raw_input('Enter u to have yourself play, c to have the computer play: ')
                    if c_or_u=='u':
                        playHand(p_hand, wordList, HAND_SIZE)
                        break
                    elif c_or_u=='c':
                        compPlayHand(p_hand, wordList, HAND_SIZE)
                        break
                    else:
                        print 'Invalid command.'
                        print ''
                 
        elif choice=='e':
            break
        else:
            print 'Invalid command.'
            print ''
            

        
#
# Build data structures used for entire session and play game
#
if __name__ == '__main__':
    wordList = loadWords()
    playGame(wordList)


