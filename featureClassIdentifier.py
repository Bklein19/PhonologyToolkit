#given a set of phones and a subset of those phones, return the (TODO non) minimal feature matrix that 
#defines the natural class that is the subset of the phones
def featureClassIdentifier(phoneSet, phoneSubSet):
    phoneIndex = 0
    subSetFeatures = []
    for phone in phoneSubSet:
        subSetFeatures.append(featureDispenser(phone))
        phoneIndex = phoneIndex + 1
    matchingFeaturesOfSubSet = matchingFeatures(subSetFeatures)
    #want to return the matching features of the subset that arent matching in the main set
    phoneIndex = 0
    features = []
    for phone in phoneSet:
        features.append(featureDispenser(phone))
        phoneIndex = phoneIndex + 1
    matchingFeaturesOfSet = matchingFeatures(features)
    return nonMatchingFeatures([matchingFeaturesOfSubSet, matchingFeaturesOfSet])


print("TEST 1")
print(featureClassIdentifier(["p", "b", "f", "n", "m"], ["p", "b"]))

print("TEST 2")
print(featureClassIdentifier(["p", "b", "f", "n",], ["p", "b"]))

print("TEST 3")
print(featureClassIdentifier(["p", "b", "n", "k", "g"], ["p", "b"]))
