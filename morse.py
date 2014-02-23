
AZ09 = ["A","B","C","D"]
MorseAZ09 = [".-","-...","-.-.","-.."]

def str2morse(string):
    string = string.upper()
    ret = ""
    for c in string:
        ret += MorseAZ09[AZ09.index(c)] +" "
    return ret


# alphanumeric to morse code dictionary
AN2Morse = {"A":".-",
            "B":"-...",
            "C":"-.-.",
            "D":"-..",
            "E":".",
            "F":"..-.",
            "G":"--.",
            "H":"....",
            "I":"..",
            "J":".---",
            "K":"-.-",
            "L":".-..",
            "M":"--",
            "N":"-.",
            "O":"---",
            "P":".--.",
            "Q":"--.-",
            "R":".-.",
            "S":"...",
            "T":"-",
            "U":"..-",
            "V":"...-",
            "W":".--",
            "X":"-..-",
            "Y":"-.--",
            "Z":"--..",
            
            "1":".----",
            "2":"..---",
            "3":"...--",
            "4":"....-",
            "5":".....",
            "6":"-....",
            "7":"--...",
            "8":"---..",
            "9":"----.",
            "0":"-----",
            
            " ":" "

            }
Morse2AN = {v:k for (k,v) in AN2Morse.items()}
splitLetter = " "
            
def an2morse(string):
    return [AN2Morse[c] for c in string.upper()]


def morse2bit(morseList):
    bitList = []
    
    for ch in morseList:
        for elem in ch:
            if elem == ".":
                bitList.append("1")
            elif elem == "-":
                bitList += ["1", "1", "1"]
            elif elem == " ":
                bitList.append("0")
            
            bitList.append("0") # end of dot or dash
        bitList += ["0", "0"] # end of character
    
    return bitList




def seq2tuple(onOffSeq):
    tupleList = []
    start0 = start1 = 0
    
    while True:
        try:
            start1 = onOffSeq.index('1', start0)
            tupleList.append(('0', start1-start0))
            start0 = onOffSeq.index('0', start1)
            tupleList.append(('1', start0-start1))
        except:
            if len(tupleList) > 0 and tupleList[0][0] == '0':
                tupleList = tupleList[1:]
            return tupleList

def tuple2bitData(tupleList):
    bitDataList = []  # ex: [('1',1), ('0',3), ('1',3), ...]
    
    lenOfDot = findLenOfDot(tupleList)
    newList = removeNoise(tupleList,lenOfDot)
    for e in newList:
        ref = e[1] / lenOfDot
        l = 7 if ref > 5 else 3 if ref > 2 else 1
        
        bitDataList.append((e[0], l))
    return bitDataList

def removeNoise(tupleList, lenOfDot):
    tmp = []
    for e in tupleList:
        if e[1] / lenOfDot > 0.5:
            tmp.append(e)
    if len(tmp) < 2:
        return tmp
    ret = [tmp[0]]
    for i in range(1, len(tmp)):
        if ret[-1][0] == tmp[i][0]:
            ret[-1] = (ret[-1][0], ret[-1][1] + tmp[i][1])
        else:
            ret.append(tmp[i])
    return ret

def findLenOfDot(tupleList):
    listOfOne = [e[1] for e in tupleList if e[0] == '1']
    avg = sum(listOfOne) / len(listOfOne)
    listOfDot = [e for e in listOfOne if e < avg]
    
    return sum(listOfDot) / len(listOfDot)

def bitData2morse(bitDataList):
    morseList = []
    ch = ''
    for e in bitDataList:
        if e[0] == '0' or e[0] == False:
            if e[1] != 1 and ch != '':
                morseList.append(ch)
                ch = ''
                if e[1] >= 6:
                    morseList.append(" ")
        elif e[0] == '1' or e[0] == True:
            if e[1] == 1:
                ch += '.'
            elif e[1] == 3:
                ch += '-'
                
    if ch != '':
        morseList.append(ch)
    return morseList

def morse2an(morseList):
    return "".join([Morse2AN[m] for m in morseList])




def an2bit(string):
    return morse2bit(an2morse(string))



def seq2an(onOffSeq):
    return morse2an(bitData2morse(tuple2bitData(seq2tuple(onOffSeq)))) 
