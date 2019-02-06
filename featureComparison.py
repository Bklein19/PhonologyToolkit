#compares n matrices and returns the notable feature differences that the first matrix has that 
#are different from the others
def featureComparison(matrices):
    differentFeatures = []
    matrixIndex = 0
    for matrixIndex in range(len(matrices)):
        for feature in matrices[0]:
            containsfeature = False;
            for otherFeature in matrices[matrixIndex]:
                if otherFeature == feature:
                    containsfeature = True;
                    break
            if containsfeature == False:
                differentFeatures.append(feature)
                differentFeatures.append(phoneFinder(matrices[matrixIndex]))
        matrixIndex = matrixIndex + 1
    return differentFeatures
