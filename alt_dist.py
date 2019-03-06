#!/usr/bin/env python
import matplotlib.pyplot as plt
import numpy as np
import csv

plt.style.use('ggplot')

alts, pops, comuni = [], [], []

with open('./data/comuni-alti.tsv', 'r') as f:
    for r in csv.DictReader(f, delimiter='\t'):
        pop, alt = int(r['POPOLAZIONE']), int(r['ALTITUDINE'])
        comuni.append((unicode(r['COMUNE'], 'utf-8'), pop, alt))
        pops += [pop]
        alts += [alt] * pop

comuni.sort(key=lambda (c,p,alt): alt)

pop_mean, pop_median, pop_std = np.median(pops), np.mean(pops), np.std(pops)
pop_max = max(pops)

plt.hist(alts, orientation='horizontal', normed=False, bins=50, color='r')
plt.xlabel('Popolazione')
plt.ylabel('Altitudine (mslm)')
plt.title('Distribuzione popolazione')

y = 200
for comune, pop, alt in comuni:
    if pop < 2000: continue
    y += 100
    plt.annotate(comune,
           xy=(pop, alt),
           xytext=(min(pop*2, pop_max), y),
           arrowprops=dict(arrowstyle='->', color='b'))

plt.text(20000, 1720, "Altitudine media: %.2f" % np.mean(alts), size=16)
plt.text(20000, 1600, "Altitudine mediana: %d" % np.median(alts), size=16)

plt.show()
