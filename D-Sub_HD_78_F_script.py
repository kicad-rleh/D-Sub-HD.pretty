#!/bin/python3

from collections import namedtuple

Point = namedtuple('Point', ['x', 'y'])

num_rows = 4

x_delta = -2.41

y = [-6.24 / 2,
	 -2.08 / 2,
	 2.08 / 2,
	 6.24 / 2,
	 ]
y_cnt = [20, 19, 20, 19]
x_start = [-9.5 * x_delta,
		   -9 * x_delta,
		   -9.5 * x_delta,
		   -9 * x_delta,
		   ]

p = []

for y_i in range(num_rows):
	for x_i in range(y_cnt[y_i]):
		x = x_start[y_i] + (x_delta * x_i)
		p.append(Point(x, y[y_i]))
#		print('  x_i = {}'.format(x_i))
#	print(' y_i = {}'.format(y_i))

#print('# =========================================')

for pin in range(0,len(p)):
	print('  (pad {} thru_hole circle (at {:.2f} {:.2f}) (size 1.35 1.35) (drill 1.05) (layers *.Cu *.Mask))'.format(pin+1, p[pin].x, p[pin].y))
