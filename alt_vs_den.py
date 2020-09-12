#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np
import csv

plt.style.use('ggplot')

comuni = []

x_field = 'POPOLAZIONE'
y_field = 'ALTITUDINE'
z_field = 'DENSITA'

with open('./data/comuni-alti.tsv', 'r') as f:
    for r in csv.DictReader(f, delimiter='\t'):
        r['POPOLAZIONE'] = int(r['POPOLAZIONE'])
        r['DENSITA'] = float(r['DENSITA'])
        r['ALTITUDINE'] = int(r['ALTITUDINE'])
        r['COMUNE'] = unicode(r['COMUNE'], 'utf-8')
        comuni.append(r)

comuni.sort(key=lambda c: c['POPOLAZIONE'])
x = [c[x_field] for c in comuni]
y = [c['ALTITUDINE'] for c in comuni]
z = [c[z_field] for c in comuni]


plt.scatter(x, y, s=z, alpha=0.4)
plt.xlabel(x_field)
plt.ylabel(y_field)
plt.title("O = " + z_field)

y = 200
for c in comuni:
    #if c['POPOLAZIONE'] > 2000 or c['ALTITUDINE'] > 1400:
    if c['POPOLAZIONE'] > 1000 or c['ALTITUDINE'] > 600:
        plt.text(c[x_field], c[y_field], c['COMUNE'])

plt.show()
