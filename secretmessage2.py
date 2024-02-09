import math
from Infinitenestedvariablelengths import returnallperms
from Infinitenestedvariablelengths import Multlens

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z',' ','?',',','.','!','\"','\'','’','‘','A','B','C','D','E','F','G','H','I','J','K','L','M','N','O','P','Q','R','S','T','U','V','W','X','Y','Z','`','~','(',')']
# print(len(letters))
# startings = {"d":['b','l','p'],'k':['c','g'],'p':['d','j','r'],'a':['a','e'],'h':['f','v'],'z':['n','z'],'y':['q','y'],'w':['s','w'],'e': 'i', 'i': 'm', 'm': 'u', 'o': 'o', 'r': 't', 's': 'k', 'v': 'h', ' ': ' ', '?': '?'}

def primes(min,max):
    total = []
    for i in range(min,max+1):
        prime = True
        for div in range(2,int(math.sqrt(i))+1):
            if i%div == 0:
                prime = False
                break
        if prime:
            total.append(i)
    return total

def modinverse(prime,residue,mod):
    possiblevalues = []
    for n in range(mod):
        if n*prime%mod == residue:
            possiblevalues.append(n)
    if len(possiblevalues) > 0:
        return possiblevalues
    return None

def startingletters(encrypted):
    totals = []
    for i in letters:
        if encrypted == encrypt(i):
            totals.append(i)
    return totals

def numprimes(start,amount):
    nums = []
    i = start
    while len(nums) < amount:
        prime = True
        for div in range(2,int(math.sqrt(i))+1):
            if i%div == 0:
                prime = False
                break
        if prime:
            nums.append(i)
        i += 1
    return nums

def encrypt(msg):
    newmsg = ""
    nums = numprimes(letters.index(msg[0])+2,len(msg))
    numindex = 0
    for char in msg:
        # if char != " ":
        charindex = letters.index(char)
        newmsg += letters[(nums[numindex]*charindex)%len(letters)]
        numindex += 1
        # else:
        #     newmsg += " "
    return newmsg

def decrypt(msg):
    newmsg = ""
    totallist = []
    for startingletter in startingletters(msg[0]):
        done = True
        # print(startingletter)
        tmplist = []
        primes = numprimes(letters.index(startingletter)+2,len(msg))
        # print(primes)
        tmplist.append([startingletter])
        # print(tmplist)
        for index in range(1,len(msg)):
            possible = modinverse(primes[index],letters.index(msg[index]),len(letters))
            # print(possible)
            if possible is not None:
                tmplist.append([letters[i] for i in possible])
            else:
                done = False
                break
        if done:
            totallist.append(tmplist)
    return [returnallperms(totallist[i]) for i in range(len(totallist))]
# print(letters.index("u"))
# print(encrypt("we will attack the stronghold in the morning. get troops ready."))
# print(startingletters('v'))
# print(decrypt("ieccohnean.aiuenrwwmr.elyxorjwer .biomcthergtws tc.lwipywr,a?mb"))
# print(modinverse(13,20,len(letters)))
# print(letters[8])
# print(primes(70,100))
# print(numprimes(90,2))

# for i in letters:
#     print(i,letters[(letters.index(i)*numprimes(letters.index(i)+2,1)[0])%len(letters)])

# x = {}
# for i in letters:
#     n = input(i+" ")
#     if n != "no":
#         x[i] = n
# print(x)

# msg = "Create a variable to store the new encrypted message.Change your code to store the user's message and not just one character.Add a for loop to your code, and indent the rest of the code so that it is repeated for each character in the message.Test your code. You should see that each character in the message is encrypted and printed one at a time.Let’s add each encrypted character to your newMessage variable.You can print the newMessage as it is being encrypted. Some characters aren’t in the alphabet, which causes an error.Test out your code with some characters that aren’t in the alphabet.For example, you could use the message hi there!!Notice that the space and the ! characters are all encrypted as the letter ‘c’!It would be better if your code didn’t encrypt anything not in the alphabet, but just used the original character."
# msg = "Hi!"
msg = input("Enter the message you want to encrypt: ")
encrypted = encrypt(msg)
print("This is your encrypted message:",encrypted,'\n')
print("These are the possible messages you could have sent:",decrypt(encrypted))