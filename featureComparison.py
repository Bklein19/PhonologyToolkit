#compares two feature matrices and returns the notable feature differences the first has but the second doesn't.
def featureComparison(matrix1, matrix2):
    differentFeatures = []
    for feature in matrix1:
        containsfeature = False;
        for otherFeature in matrix2:
            if otherFeature == feature:
                containsfeature = True;
                break
        if containsfeature == False:
            differentFeatures.append(feature)
    return differentFeatures
