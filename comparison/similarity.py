import spacy
nlp = spacy.load('en_core_web_lg') #python -m spacy download en_core_web_lg

a = nlp(u'')
b = nlp(u'')

sim = a.similarity(b)

print(sim)
