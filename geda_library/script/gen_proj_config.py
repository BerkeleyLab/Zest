#!/bin/python
import os
import re
import sys

def find_sch():
	pfile=os.popen('find . -name \'*.sch\'')
	sch_files=(pfile.read()).split()
	return sch_files

def locate_libtop(file_path):
	s = re.search("(.*/)sch/.*\.sch",file_path)
	if s:
		libtop_path = s.groups()[0]
		return libtop_path
	else:
		s = re.search("(.*/).*\.sch",file_path)
		if s:
			libtop_path = s.groups()[0]
			return libtop_path
		else:
			return './'

def file_name_without_sch(file_full_path):
	'''
		return the filename withou .sch
		for example:
			lock.sch --> lock
	'''
	s = re.search("([^/]*)\.sch",file_full_path)
	if s:
		name = s.groups()[0]
		return name
	else:
		print file_full_path, ' is not a schematic file'

def write_gsch2pcb(lib_path,out_name,geda_path):
	if lib_path[-4:]=='lib/':
		f_path=libtop+'sch/'+f_name+'.gsch2pcb'
		f_temp=open(f_path,'w')
		f_temp.write('schematics '+lib_path+'sch/'+out_name+'.sch\n')
		f_temp.write('output-name '+lib_path+'pcb/'+out_name+'\n')
		cmd = 'mkdir -p '+lib_path+'pcb'
		os.system(cmd)
		if geda_path:
			f_temp.write('elements-dir '+geda_path+'footprint/llrf5\n')
			f_temp.write('elements-dir '+geda_path+'footprint/elements')
		f_temp.close()
	else:
		f_path=libtop+f_name+'.gsch2pcb'
		f_temp=open(f_path,'w')
		f_temp.write('schematics '+lib_path+out_name+'.sch\n')
		f_temp.write('output-name '+lib_path+'pcb/'+out_name+'\n')
		cmd = 'mkdir -p '+lib_path+'pcb'
		os.system(cmd)
		if geda_path:
			f_temp.write('elements-dir '+geda_path+'footprint/llrf5\n')
			f_temp.write('elements-dir '+geda_path+'footprint/elements')
		f_temp.close()

	print f_path, ' Generated'

def gedalib_path():
	cmd = 'find \. -maxdepth 2 -name geda_library'
	p = os.popen(cmd)
	geda_path=p.read().strip()
	if geda_path:
		return geda_path+'/'
	else:
		print 'Warning: No geda_library'
		return None
def usage():
	print '''  Usage:
      gen_proj_config schematic.sch'''

if __name__=='__main__':
	if len(sys.argv)<2:
		usage()
		sys.exit()
	sch_files=sys.argv[1:]
	geda_path = gedalib_path()
	for f in sch_files:
		libtop = locate_libtop(f)
		if libtop:
			f_name = file_name_without_sch(f)
			write_gsch2pcb(libtop,f_name,geda_path)
		else:
			continue
