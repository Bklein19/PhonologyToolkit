#compares n matrices and returns matching features from the given phones using a divide and conquer method
def matchingFeatures(matrices):
    if len(matrices) == 1:
        return matrices[0]
    elif len(matrices) == 2:
        return matchingFeaturesHelper(matrices[0], matrices[1])
    elif len(matrices) == 3:
        return matchingFeaturesHelper(matchingFeatures([matrices[0], matrices[1]]), matrices[2])
    else:
        tempSameFeatures = matchingFeaturesHelper(matrices[0], matrices[1]);
        matrixIndex = 2
        for matrixIndex in range(len(matrices) - 1):
            sameFeatures = matchingFeatures([tempSameFeatures, matchingFeaturesHelper(matrices[matrixIndex],
                                                                                     matrices[matrixIndex + 1])])
            matrixIndex = (matrixIndex + 2)
    return sameFeatures

#compares two feature matrices and returns their shared features
def matchingFeaturesHelper(matrix1, matrix2):
    sameFeatures = []
    for feature in matrix1:
        containsfeature = False;
        for otherFeature in matrix2:
            if otherFeature == feature:
                containsfeature = True;
        if containsfeature == True:
            sameFeatures.append(feature)
    return sameFeatures

print("TEST 1")
print(matchingFeatures([featureDispenser("m"), featureDispenser("k")]))

print("TEST 2")
print(matchingFeatures([featureDispenser("m"), featureDispenser("k"), featureDispenser("l")]))

print("TEST 3")
print(matchingFeatures([featureDispenser("m"), featureDispenser("k"),  featureDispenser("l"), featureDispenser("h")]))

print("TEST 4")
print(matchingFeatures([featureDispenser("m"), featureDispenser("k"),  featureDispenser("l"), featureDispenser("h"), featureDispenser("i")]))
