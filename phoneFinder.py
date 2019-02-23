#given a feature, returns all of the phones that have those features
def phoneFinder(givenFeatures):
    phonesWithTheFeature = []
    for keyPhone, valueFeatures in featureCreator().items():
        goodPhoneValue = 0
        for f1 in valueFeatures:
            for f2 in givenFeatures:
                if f2 == f1:
                    goodPhoneValue = goodPhoneValue + 1
        if goodPhoneValue == len(givenFeatures):
            phonesWithTheFeature.append(keyPhone)
    return phonesWithTheFeature
        
print(phoneFinder(["-sonorant", "+dorsal"]))
