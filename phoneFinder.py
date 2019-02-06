#given a feature, returns all of the phones that have those features
def phoneFinder(givenFeatures):
    featureDict = {"p": ["+consonantal", "-sonorant", "-continuant", 
                         "-delayed release", "-approximant", "-tap", 
                         "-trill", "-nasal", "-voice", "-spread glottis",
                         "-constricted glottis", "+labial", "-round", "-labiodental",
                         "-coronal", "0anterior", "0distributed", "0strident", "-lateral",
                         "dorsal", "0ALLVOWEL"], 
                   "b" : ["+consonantal", "-sonorant", "-continuant", 
                         "-delayed release", "-approximant", "-tap", 
                         "-trill", "-nasal", "+voice", "-spread glottis",
                         "-constricted glottis", "+labial", "-round", "-labiodental",
                         "-coronal", "0anterior", "0distributed", "0strident", "-lateral",
                         "dorsal", "0ALLVOWEL"],
                   "m" : ["+consonantal", "+sonorant", "-continuant", 
                         "0delayed release", "-approximant", "-tap", 
                         "-trill", "+nasal", "+voice", "-spread glottis",
                         "-constricted glottis", "+labial", "-round", "-labiodental",
                         "-coronal", "0anterior", "0distributed", "0strident", "-lateral",
                         "dorsal", "0ALLVOWEL"],
                   #labiodental
                   "f" : ["+consonantal", "-sonorant", "+continuant", 
                         "+delayed release", "-approximant", "-tap", 
                         "-trill", "-nasal", "-voice", "-spread glottis",
                         "-constricted glottis", "+labial", "-round", "+labiodental",
                         "-coronal", "0anterior", "0distributed", "0strident", "-lateral",
                         "dorsal", "0ALLVOWEL"],
                   "v" : ["+consonantal", "-sonorant", "+continuant", 
                         "+delayed release", "-approximant", "-tap", 
                         "-trill", "-nasal", "+voice", "-spread glottis",
                         "-constricted glottis", "+labial", "-round", "+labiodental",
                         "-coronal", "0anterior", "0distributed", "0strident", "-lateral",
                         "dorsal", "0ALLVOWEL"],
                   #alveolar
                   "t" : ["+consonantal", "-sonorant", "-continuant", 
                         "-delayed release", "-approximant", "-tap", 
                         "-trill", "-nasal", "-voice", "-spread glottis",
                         "-constricted glottis", "-labial", "-round", "-labiodental",
                         "+coronal", "+anterior", "-distributed", "-strident", "-lateral",
                         "dorsal", "0ALLVOWEL"],
                   "d" : ["+consonantal", "-sonorant", "-continuant", 
                         "-delayed release", "-approximant", "-tap", 
                         "-trill", "-nasal", "+voice", "-spread glottis",
                         "-constricted glottis", "-labial", "-round", "-labiodental",
                         "+coronal", "+anterior", "-distributed", "-strident", "-lateral",
                         "dorsal", "0ALLVOWEL"],
                  "s" : ["+consonantal", "-sonorant", "+continuant", 
                         "+delayed release", "-approximant", "-tap", 
                         "-trill", "-nasal", "-voice", "-spread glottis",
                         "-constricted glottis", "-labial", "-round", "-labiodental",
                         "+coronal", "+anterior", "-distributed", "+strident", "-lateral",
                         "dorsal", "0ALLVOWEL"],
                   #TO REPRESENT ESH SYMBOL IPA
                   "esh" : ["+consonantal", "-sonorant", "+continuant", 
                         "+delayed release", "-approximant", "-tap", 
                         "-trill", "-nasal", "-voice", "-spread glottis",
                         "-constricted glottis", "-labial", "-round", "-labiodental",
                         "+coronal", "-anterior", "+distributed", "+strident", "-lateral",
                         "dorsal", "0ALLVOWEL"],
                  "z" : ["+consonantal", "-sonorant", "+continuant", 
                         "+delayed release", "-approximant", "-tap", 
                         "-trill", "-nasal", "+voice", "-spread glottis",
                         "-constricted glottis", "-labial", "-round", "-labiodental",
                         "+coronal", "+anterior", "-distributed", "+strident", "-lateral",
                         "dorsal", "0ALLVOWEL"],
                  "n" : ["+consonantal", "+sonorant", "-continuant", 
                         "0delayed release", "-approximant", "-tap", 
                         "-trill", "+nasal", "+voice", "-spread glottis",
                         "-constricted glottis", "-labial", "-round", "-labiodental",
                         "+coronal", "+anterior", "-distributed", "-strident", "-lateral",
                         "dorsal", "0ALLVOWEL"],
                  "l" : ["+consonantal", "+sonorant", "+continuant", 
                         "0delayed release", "+approximant", "-tap", 
                         "-trill", "-nasal", "+voice", "-spread glottis",
                         "-constricted glottis", "+labial", "-round", "-labiodental",
                         "+coronal", "+anterior", "-distributed", "-strident", "+lateral",
                         "dorsal", "0ALLVOWEL"], 
                  #vowels
                  "a" : ["0ALLCONSONANT", "-high", "+low", "0tense", "-front", "-back", "-round"],
                  "e" : ["0ALLCONSONANT", "-high", "-low", "+tense", "+front", "-back", "-round"],
                  "i" : ["0ALLCONSONANT", "+high", "-low", "+tense", "+front", "-back", "-round"],
                  "o" : ["0ALLCONSONANT", "-high", "-low", "+tense", "-front", "+back", "+round"],
                  "u" : ["0ALLCONSONANT", "+high", "-low", "+tense", "-front", "+back", "+round"],}
    phonesWithTheFeature = []
    for keyPhone, valueFeatures in featureDict.items():
        goodPhoneValue = 0
        for f1 in valueFeatures:
            for f2 in givenFeatures:
                if f2 == f1:
                    goodPhoneValue = goodPhoneValue + 1
        if goodPhoneValue == len(givenFeatures):
            phonesWithTheFeature.append(keyPhone)
    return phonesWithTheFeature
        