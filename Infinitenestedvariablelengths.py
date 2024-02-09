
def Multlens(lists):
    lens = [len(lst) for lst in lists]
    prod = 1
    for i in lens:
        prod *= i
    return prod

lists = [['a','b'],['1','2','3','4'],['c','d','e']]

def returnallperms(lists):
    strings = []
    length = len(lists)
    for count in range(Multlens(lists)):
        string = ""
        for index in range(length):
            if index != 0 and index != length-1:
                letterindex = int((count%(Multlens(lists[index:])))/(Multlens(lists[index+1:])))
                # print(letterindex)
            elif index == 0:
                letterindex = int(count/(Multlens(lists[index+1:])))
            else:
                letterindex = int(count%(Multlens(lists[index:])))
            # print(letterindex)
            string += lists[index][letterindex]
        strings.append(string)
    return strings

# print(returnallperms(lists))

