def minPairFinder(strArray):
    result = []
    for i in range(len(strArray)):
        j = i + 1
        while j < len(strArray):
            if (isMinimalPair(strArray[i], strArray[j])):
                result.append([strArray[i], strArray[j]])
            j = j + 1
    return(result)

def isMinimalPair(str1, str2):
    discrepancy = False
    if len(str1) != len(str2):
        return False
    for i in range(len(str1)):
        #first discrepancy
        if str1[i] != str2[i] and discrepancy == False:
            discrepancy = True
        #case of two discrepancies
        elif str1[i] != str2[i] and discrepancy == True:
            return False
        #case of same word
        elif i == len(str1) - 1 and discrepancy == False:
            return False
    return True

#--------------------------------------------------------------------------------------------------

print(minPairFinder(["sad", "cad", "bad", "bar", "tall", "fall", "doll", "mall"]))

#--------------------------------------------------------------------------------------------------

#To be added upon
def isNearMinimalPair(str1, str2):
    discrepancy = False
    for i in range(len(str1)):
        j = 0
        while j < i + 1 and j != (len(str1)):
            #first discrepancy
            if str1[i] != str2[i] and discrepancy == False:
                discrepancy = True
            #case of two discrepancies
            elif str1[i] != str2[i] and discrepancy == True:
                return False
            #case of same word
            elif i == len(str1) - 1 and discrepancy == False:
                return False
    return True
