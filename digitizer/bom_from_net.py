# coding: utf
import re, sys
exact = {}
apprx = {}
pfile = open('parts.data','r').read()
bom_id_set = {}
for line in pfile.split('\n'):
	a = line.split(':')
	if (len(a) is 2):
		d0 = re.sub('[Ω+]','',a[0])
		d = re.sub('  *',' ',d0)
		#print d
		exact[d]=a[1].strip()
		# PADS name
		b = re.sub('  *',' ',d0).split(' ')
		if len(b)>2: d = b[0]+'_'+b[1]+' '+b[2]
		else: d = b[0]+' '+b[1]
		d=d.upper()
		#print d
		#print d+':', a[1].strip()
		apprx[d]=a[1].strip()

def handle_pads(line):
	a = line.upper().split()
	if len(a) != 2: return
	b = a[1].split('@')
	if len(b) != 2: return
	#print b[0],b[1]
	if re.search('DNP',b[0]): return
	if b[0] == 'TP025': return
	if b[1] == 'ZXCT1009': b[1] = 'SOT23-3'  # total hack
	d = b[0]+' '+b[1]
	order = apprx[d]
	#print a[0], order
	o = re.sub('  *',' ',order).split(' ')
	digikey = o[1]
	if '@' in digikey:
		(distrib_part,distrib) = digikey.split('@')
		if distrib_part == '': distrib_part = o[0]
	else:
		distrib = 'Digi-Key'
		distrib_part = digikey
	orderable = ','.join([o[2], o[0], distrib, distrib_part])
	#print a[0],orderable
	bom_id = b[0]
	if ("CAPACITOR" in bom_id or "RESISTOR" in bom_id) and b[1] != "0603":
		#bom_id = bom_id + '_' + b[1]
		pass
	if orderable not in plist:
		plist[orderable] = []
		if bom_id in bom_id_set:
			sys.stderr.write("Warning: duplicate bom_id %s\n"%bom_id)
		bom_id_set[bom_id] = 1
	plist[orderable].append(a[0])
	psub[orderable] = bom_id

lfile = open('digitizer.net','r').read()
live = 0
plist={}
psub={}
for line in lfile.split('\n'):
	if len(line)>0: line = line[:-1]
	#line.replace(r'\r','')
	if line == "*PART*":
		live = 1
		continue
	if line == "":
		live = 0
	if live:
		handle_pads(line)

for p in sorted(plist, key=lambda key: psub[key]):
	print ','.join([psub[p], p, str(len(plist[p])), ' '.join(sorted(plist[p]))])
