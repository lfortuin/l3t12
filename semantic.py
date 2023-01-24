import spacy
nlp = spacy.load('en_core_web_md')

tokens = nlp('cat apple monkey banana')

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

#Note:  monkey and cat have a high similarity because they are both animals
#       apple and banana have a high similarity becuase they are both fruits
#       monkey and banana havea  high simiarity because monkeys eat bananas