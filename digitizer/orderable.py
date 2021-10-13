#!/usr/bin/python

# Big Fat Warning!
# For this program to work right, two files
#  gnet-partslist3.scm
#  partslist-common.scm
# in the gschem-1.8.2 backend need to be patched,
# so that capacitor dielectric values get printed out.
# See gschem-backend.patch.

import re
import sys
multiplier = 25
desc_col = 5   # number of columns in partslist3 containing part descriptions
  # unpatched partslist-common.scm produces 3

exact = {}
pfile = open('parts.data','r').read()
for line in pfile.split('\n'):
	a = line.split(':')
	if (len(a) is 2):
		d = re.sub('  *',' ',a[0])
		#print d
		exact[d]=a[1].strip()

lfile = open('partslist3.txt','r').read()
bom_line = 1
for line in lfile.split('\n'):
	a = line.split('\t')
	if len(a) < desc_col+1: continue
	if line[0] == '.': continue
	if a[1] == 'DNP': continue
	if a[0] == 'TP025': continue  # test point
	#d = '%s %s %s %s'%(a[0],a[1],a[2],a[3])
	d = ' '.join(a[0:desc_col])
	d = re.sub(' unknown','',d)
	if d in exact:
		if exact[d] is '':
			sys.stderr.write("Warning: need data on %s\n"%d)
			pass
		else:
			#print "OK: found %s"%exact[d]
			ee = exact[d].split()
			if ee[1][0] != '@':  # only Digi-Key items
				qty = int(a[desc_col])*multiplier
				print bom_line,'\t',ee[1],'\t',qty
				#print a[4],ee[1],ee[0],a[0],a[1]
			bom_line += 1
			a[0] == ee[0]
	else:
		sys.stderr.write("Warning: no entry for %s\n"%d)
	#print '\t'.join(a)
