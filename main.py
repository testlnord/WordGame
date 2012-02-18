#-------------------------------------------------------------------------------
# Name:        Р В РЎВР В РЎвЂўР В РўвЂР РЋРЎвЂњР В Р’В»Р РЋР Р‰1
# Purpose:
#
# Author:      hooloo
#
# Created:     02.01.2012
# Copyright:   (c) hooloo 2012
# Licence:     <your licence>
#-------------------------------------------------------------------------------
#!/usr/bin/env python
import random

def main():
    aFile = open ( 'usa', 'r' )
    WORDS = aFile.readlines();
    CountOfWords = len(WORDS)
    firstword = WORDS[random.randint(0,CountOfWords)]
    endofgame = 0
    humanturn = 1
    humanscore = 0;
    pcscore = 0;
    usednumbers = []

    while(endofgame < 1):
        print(firstword)
        if (humanturn > 0):
            secondword = input()
            humanturn = -humanturn;
        else:
            if (pcscore > humanscore):
                max_used_length = 2;
            else:
                max_used_length = 2 + round((humanscore - pcscore)/10);
            if (max_used_length>=len(firstword)):
                max_used_length = len(firstword)
            found_smth = 0;
            while (found_smth == 0):
                max_used_length = max_used_length - 1
                for word in WORDS:
                    if (word.startswith(firstword[len(firstword)-1-max_used_length:len(firstword)-1])):
                        found_smth = 1;

                        secondword = word[max_used_length:len(word)-1];
                        if (len(secondword)==0):
                            found_smth = 0;
                        break;

            humanturn = - humanturn
        if (secondword[0]=='0'):
            endofgame = 1;
            break;
        number = 0;
        #print(secondword)
        #print(len(secondword))
        for i in range(0,len(firstword)-1):
            find = 2;
            try:
                #print(firstword[i:len(firstword) - 1]+secondword+'\n')
                number = WORDS.index(firstword[i:len(firstword) - 1]+secondword + '\n')
                find = 1;
            except (ValueError):
                #print('notfound')
                number = 0;
                find = 0;

            if (find == 1):
                break;

        if (number != 0):
            oldword = 0
            for un in usednumbers:
                if (un == number ):
                    oldword=1
                    break
            if (oldword!=0):
                humanturn=-humanturn
                print("U`ve already used this word!")
            else:
                print( WORDS[number])
                head = len(firstword)-1 - i
                secondwordlength = head + len(secondword)
                if (humanturn < 0):
                    humanscore = humanscore+head*secondwordlength;
                else:
                    pcscore = pcscore + head*secondwordlength
                print("Get points: ",head*secondwordlength)
                print("YOUR SCORE: ",humanscore)
                print("MY SCORE: ",pcscore)
                firstword = WORDS[number]
                usednumbers.append(number)
        else:
            print("Sorry, but I don`t no this word.")
            humanturn = - humanturn
if __name__ == '__main__':
    main()

