import spacy
nlp = spacy.load('en_core_web_md')

tokens = nlp('cat apple monkey banana')

for token1 in tokens:
    for token2 in tokens:
        print(token1.text, token2.text, token1.similarity(token2))

#Note:  monkey and cat have a high similarity because they are both animals
#       apple and banana have a high similarity becuase they are both fruits
#       monkey and banana have a high simiarity because monkeys eat bananas

"""When using 'en_core_web_sm' instead of 'en_core_web_md' the follwing warning is issued: 

UserWarning: [W007] The model you're using has no word vectors loaded, so the result of 
the Doc.similarity method will be based on the tagger, parser and NER, which may not
give useful similarity judgements. This may happen if you're using one of the small 
models, e.g. `en_core_web_sm`, which don't ship with word vectors and only use 
context-sensitive tensors. You can always add your own word vectors, or use one of 
the larger models instead if available.

The similarities are lower when using 'en_core_web_sm' instead of 'en_core_web_md'"""