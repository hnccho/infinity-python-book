import os, random

dir = 'scripts/py4fun/' if os.getcwd().find('sl4a') > 0 else ''
txt = open(dir + 'wordlist.txt').read()
words = filter(lambda x: len(x) > 0 and not x.startswith('#'), txt.splitlines())

while True:
    print(random.choice(words))
    raw_input()