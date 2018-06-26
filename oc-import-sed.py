from random import *

prefix = 'oc import-image {} --from '
suffix = ':latest --confirm'

with open ('joel.txt', 'r') as src:
    with open('finish.txt', 'w') as dest:
        for line in src:
            x = randint(1, 10000)
            dest.write('oc import-image {} --from {}:latest --confirm\n'.format(x, line.rstrip('\n')))
