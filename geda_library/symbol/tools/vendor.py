import json,os,sys
def generate_vendor_symbol(filename='vendor.json',force=False):
	vendor_info=json.load(open(filename))
	location='T 0 0 1 1 0 1 0 0 1'
	dirname='vendors/'+vendor_info['vendor']
	if not os.path.exists(dirname):
		os.mkdir(dirname)
	for part in vendor_info['parts']:
		f_orig_name='general/'+part['device']+'.sym'
		s_orig=open(f_orig_name).read()
		s_att=''
		for attribs in part.keys():
			s_att+=location+'\n'+attribs+':'+part[attribs]+'\n'
		s_all=s_att+s_orig
		filename=part['device']+'_'+part['model']+'.sym'
		fullname=dirname+'/'+filename
		if (not os.path.isfile(fullname) or force):
			fout=open(fullname,'w+')
			fout.write(s_all)
		else:
			print fullname,"file existed"

if __name__=="__main__":
	if len(sys.argv)>2:
		force=sys.argv[2]
	else:
		force=False
	generate_vendor_symbol(sys.argv[1],force)
