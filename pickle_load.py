import _pickle
with open('person.dat', 'rb') as f:
    person = _pickle.load(f)

print(person)