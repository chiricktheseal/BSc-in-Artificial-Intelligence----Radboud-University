# your code here
import nltk
from nltk.corpus import wordnet as wn

# car = lemma ;  n=noun  ;  01= number of def
synset = wn.synset('car.n.01')

print("Synset:", synset)
print("Synonims:", synset.lemma_names())
print("Definition:", synset.definition())
print("Examples of usage:", synset.examples())

# Гиперонимы (более общие понятия)
print("Гиперонимы:")
for hypernym in synset.hypernyms():
    print(hypernym.name(), "-", hypernym.definition())

# Гипонимы (более конкретные понятия)
print("\nГипонимы:")
for hyponym in synset.hyponyms():
    print(hyponym.name(), "-", hyponym.definition())

# Меронимы (части целого)
print("\nМеронимы:")
for part in synset.part_meronyms():
    print(part.name(), "-", part.definition())

# Холонимы (целое, частью которого является сунсет)
print("\nХолонимы:")
for whole in synset.part_holonyms():
    print(whole.name(), "-", whole.definition())
    
#-------------------------------------------------------------
bank_synsets = wn.synsets('bank') #get all synsets for 'bank'

print("Synsets for word 'bank':", bank_synsets)
for synset in bank_synsets:
    print(synset.name())