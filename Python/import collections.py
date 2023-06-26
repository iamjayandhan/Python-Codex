import collections

string = "Hello world"
frequencies = collections.Counter(string)
repeated = {}

for key, value in frequencies.items():
#iterate through frequencies dictionary

    if value > 1:
        repeated[key] = value
#if character repeats, add to repeated dictionary


print(repeated)
#OUTPUT
#{'l': 3, 'o': 2}