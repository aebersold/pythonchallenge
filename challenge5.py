import pickle

f = open('challenge5.txt', 'r')
deserialized = pickle.Unpickler(f).load()
print deserialized

