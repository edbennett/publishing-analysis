#!/usr/bin/env python

import matplotlib.pyplot as plt

positions = [0.5, 1.5, 2.5, 3.5, 4.5, 5.5]
countries = ['India', 'Brazil', 'USA', 'China', 'EU', 'Argentina']
cattle_numbers = [3.03e8, 2.44e8, 9.44e7, 9.14e7, 8.70e7, 5.37e7]

plt.bar(positions, cattle_numbers, tick_label=countries)
plt.xlabel('Country/Region')
plt.ylabel('Population')
plt.title('Cattle population by country or region')
plt.savefig('cattle.pdf')
plt.close()
