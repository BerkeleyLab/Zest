# coding: utf

# pads.csv is the XY file from PADS, translated from .xlsx to .csv using
# LibreOffice (tested: LibreOffice 3.5.4.2 on Debian Wheezy)

# parts.data is the llrf5 cross-reference file from specifier to orderable
# part number.

# This Python script merges the two, adding manufacurer and manufacturer part
# to the end of each row.

import re
exact = {}
apprx = {}
pfile = open('parts.data', 'r').read()
for line in pfile.split('\n'):
	a = line.split(':')
	# a = re.sub('[Ω+]', '', line).split(':')
	if (len(a) is 2):
		d0 = re.sub('[Ω+]', '', a[0])
		d = re.sub('  *', ' ', d0)
		# print d
		exact[d] = a[1].strip()
		# PADS name
		b = re.sub('  *', ' ', d0).split(' ')
		if len(b) > 2: d = b[0]+'_'+b[1]+' '+b[2]
		else: d = b[0]+' '+b[1]
		# print d
		d = d.upper()
		# print d+':', a[1].strip()
		apprx[d.upper()] = a[1].strip()

lfile = open('pads.csv', 'r').read()
for line in lfile.split('\n'):
	a = line.split(',')
	if len(a) < 3: continue
	if a[0] == 'PartType':
		print line+',Manufacturer,Part'
		continue
	# Eliminate confusion on SMA vertical
	if a[0] == '142-0701-301':
		line = re.sub('142-0701-301', '142-0701-201', line)
	if a[0] == 'MT230_107_PLT': continue  # mounting holes?
	if a[0] == 'TP025': continue  # test points
	if re.search('DNP', a[0]): continue
	if a[2] == 'ZXCT1009': a[2] = 'SOT23-3'  # total hack
	# print a[0],a[2]
	d = a[0]+' '+a[2]
	order = apprx[d]
	# print d, order
	o = re.sub('  *', ' ', order).split(' ')
	print ','.join([line, o[2], o[0]])
