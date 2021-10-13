import sys,re,os,numpy
startspace='\s*'
oneint='(?P<%s>[-\d]+)\s+'
endint='(?P<%s>[-\d]+)\s*'
onechar='(?P<%s>\S+)\s+'
endchar='(?P<%s>\S+)\s*'
twointpair='(?P<%s>[-\d]+),(?P<%s>[-\d]+)\s*'
next_re='\s*(?P<next>[\s\S]*)';

v_para=('version','fileformat_version');
v_re=(startspace+oneint+endint+next_re)#%v_para;
L_para=('x1','y1','x2','y2','color','width','capstyle','dashstyle','dashlength','dashspace')
L_re=(startspace+9*oneint+endint+next_re)#%L_para;
G_para=('x','y','width','height','angle','mirrored','embedded')
G_re=(startspace+5*oneint+2*onechar+next_re)#%G_para;
B_para=('x','y','width','height','color','linewidth','capstyle','dashstyle','dashlength','dashspace','filltype','fillwidth','angle1','pitch1','angle2','pitch2');
B_re=(startspace+15*oneint+endint+next_re)#%B_para
V_para=('x','y','radius','color','width','capstyle','dashstyle','dash_length','dashspace','filltype','fillwidth','angle1','pitch1','angle2','pitch2')
V_re=(startspace+14*oneint+endint+next_re)#%V_para;
A_para=('x','y','radius','startangle','sweepangle','color','width','capstyle','dashstyle','dashlength','dashspace')
A_re=(startspace+10*oneint+endint+next_re)#%A_para;
T_para=('x','y','color','size','visibility','show_name_value','angle','alignment','num_lines')
T_re=(startspace+8*oneint+endint+next_re)#%T_para
N_para=('x1','y1','x2','y2','color')
N_re=(startspace+4*oneint+endint+next_re)#%N_para
U_para=('x1','y1','x2','y2','color','ripperdir')
U_re=(startspace+5*oneint+endint+next_re)#%U_para
P_para=('x1','y1','x2','y2','color','pintype','whichend')
P_re=(startspace+6*oneint+endint+next_re)#%P_para;
C_para=('x','y','selectable','angle','mirror','basename')
C_re=(startspace+5*oneint+endchar+next_re)#%C_para;
H_para=('color','width','capstyle','dashstyle','dashlength','dashspace','filltype','fillwidth','angle1','pitch1','angle2','pitch2','num_lines')
H_re=(startspace+12*oneint+endint+next_re)#%H_para;
F_para=('character','width','flag')
F_re=(startspace+onechar+oneint+endint+next_re)#%F_para
a_para=('attributes')
a_re=(startspace+'(?P<%s>[\s\S]*?)}'+next_re)#%a_para;
M_para=('x','y','contents','endz')
M_re=(startspace+twointpair+'(?P<%s>[\s\S]*?)'+'(?P<%s>\n[zZ])\s*'+next_re)#%M_para;
type_para=('type')
type_re=(startspace+'(?P<%s>[vLGBVATNMUPCHF{])'+next_re)#%type_para;
np_para=('netname','pinstxt')
np_re=(startspace+'(?P<%s>\S+):(?P<%s>.*)')
class gaf_format:
	def __init__(self,type_str,f_re_string,f_para):
		self.f_re_string=(f_re_string%f_para);
		self.f_para=f_para
		self.groupdict={};
		self.type_str=type_str
		self.attrdict={};
	def textline_re(self,linenums):
		return linenums*r'(.*)\n'+'\s*(?P<next>[\s\S]*)';
	def setattrdict(self,attrdict):
		self.attrdict.update(attrdict)
	def parse_gaf(self,line):
		m=re.match(self.f_re_string,line)
		if (m):
			self.groupdict=m.groupdict();
	def next_str(self):
		return self.groupdict['next']
	def output_mainline(self):
		mainline=[str(self.groupdict[item]) for item in self.f_para] 
		mainline.insert(0,self.type_str)
		mainline_str= ' '.join(mainline)
		return mainline_str
	def output_attrline(self):
		attrline=''
		if (len(self.attrdict)!=0):#groupdict.has_key('attributes'):
			#			print str(self.groupdict['attributes'])
			attrline='\n{\n'
			for attr in self.attrdict.keys():#groupdict['attributes']:
				attrline+=(self.attrdict[attr].output_str()+'\n')
			attrline+='}'
		return attrline
	def output_str(self):
		return self.output_mainline()+self.output_attrline();
	def findsym(self,symbolname):
		dirlist=['.']# ?? parse gafrc for dirlists
		dirlist.append('../txgls/submodule/hardware/')
		symbolpath=None
		for dirs in dirlist:
			for dirpath,dirnames,filenames in os.walk(dirs):
				for filename in [f for f in filenames if f==symbolname]:
					symbolpath=os.path.join(dirpath,filename)
		if (symbolpath==None):
			print '%s not found'%symbolname
		return symbolpath;


class version(gaf_format):
	def __init__(self,line):
		gaf_format.__init__(self,'v',v_re,v_para)
		self.parse_gaf(line)
		self.version=self.groupdict['version']
		self.fileformat_version=self.groupdict['fileformat_version']
class line(gaf_format):
	def __init__(self,line):
		gaf_format.__init__(self,'L',L_re,L_para)
		self.parse_gaf(line)
		self.x1=self.groupdict['x1']
		self.y1=self.groupdict['y1']
		self.x2=self.groupdict['x2']
		self.y2=self.groupdict['y2']
		self.color=self.groupdict['color']
		self.width=self.groupdict['width']
		self.capstyle=self.groupdict['capstyle']
		self.dashstyle=self.groupdict['dashstyle']
		self.dashlength=self.groupdict['dashlength']
		self.dashspace=self.groupdict['dashspace']

class picture(gaf_format):
	def __init__(self,line):
		gaf_format.__init__(self,'G',G_re,G_para)
		self.parse_gaf(line)
		self.x =self.groupdict['x']
		self.y =self.groupdict['y']
		self.width =self.groupdict['width']
		self.height =self.groupdict['height']
		self.angle =self.groupdict['angle']
		self.mirrored =self.groupdict['mirrored']
		self.embeded =self.groupdict['embeded']

class box(gaf_format):
	def __init__(self,line):
		gaf_format.__init__(self,'B',B_re,B_para)
		self.parse_gaf(line)
		self.x =self.groupdict['x']
		self.y =self.groupdict['y']
		self.width =self.groupdict['width']
		self.height =self.groupdict['height']
		self.color =self.groupdict['color']
		self.linewidth =self.groupdict['linwidth']
		self.capstyle =self.groupdict['capstyle']
		self.dashstyle =self.groupdict['dashstyle']
		self.dashlength =self.groupdict['dashlength']
		self.dashspace =self.groupdict['dashspace']
		self.filltype =self.groupdict['filltype']
		self.fillwidth =self.groupdict['fillwidth']
		self.angle1 =self.groupdict['angle1']
		self.pitch1 =self.groupdict['pitch1']
		self.angle2 =self.groupdict['angle2']
		self.pitch2 =self.groupdict['pitch2']
class circle(gaf_format):
	def __init__(self,line):
		gaf_format.__init__(self,'V',V_re,V_para)
		self.parse_gaf(line)
		self.x=self.groupdict['x']
		self.y=self.groupdict['y']
		self.radius=self.groupdict['radius']
		self.color=self.groupdict['color']
		self.width=self.groupdict['width']
		self.capstyle=self.groupdict['capstyle']
		self.dashstyle=self.groupdict['dashstyle']
		self.dash_length=self.groupdict['dash_length']
		self.dashspace=self.groupdict['dashspace']
		self.filltype=self.groupdict['filltype']
		self.fillwidth=self.groupdict['fillwidth']
		self.angle1=self.groupdict['angle1']
		self.pitch1=self.groupdict['pitch1']
		self.angle2=self.groupdict['angle2']
		self.pitch2=self.groupdict['pitch2']
class arc(gaf_format):
	def __init__(self,line):
		gaf_format.__init__(self,'A',A_re,A_para)
		self.parse_gaf(line)
		self.x=self.groupdict['x']
		self.y=self.groupdict['y']
		self.radius=self.groupdict['radius']
		self.startangle=self.groupdict['startangle']
		self.sweepangle=self.groupdict['sweepangle']
		self.color=self.groupdict['color']
		self.width=self.groupdict['width']
		self.capstyle=self.groupdict['capstyle']
		self.dashstyle=self.groupdict['dashstyle']
		self.dashlength=self.groupdict['dashlength']
		self.dashspace=self.groupdict['dashspace']
class text(gaf_format):
	def __init__(self,line):
		gaf_format.__init__(self,'T',T_re,T_para)
		gaf_format.parse_gaf(self,line)
		self.parse_gaf(line)
		self.x=self.groupdict['x']
		self.y=self.groupdict['y']
		self.color=self.groupdict['color']
		self.size=self.groupdict['size']
		self.visibility=self.groupdict['visibility']
		self.show_name_value=self.groupdict['show_name_value']
		self.angle=self.groupdict['angle']
		self.alignment=self.groupdict['alignment']
		self.num_lines=self.groupdict['num_lines']
		self.attr_name=None
		self.attr_value=None
	def parse_gaf(self,line):
		self.num_lines=int(self.groupdict['num_lines'])
		m=re.match(self.textline_re(self.num_lines),self.groupdict['next'])
		#print m.groups()
		self.groupdict['string_lines']=m.groups()[0:-1]
		self.groupdict['next']=m.group('next')
	def output_str(self):
		mainline=self.output_mainline()
		textline='\n'.join(self.groupdict['string_lines'])
		return mainline+'\n'+textline
	def isattr(self):
		self.parse_oneline_attribute_text()
		return self.attr
	def parse_oneline_attribute_text(self):
		m=re.match('\s*(?P<attr_name>.+)\s*=\s*(?P<attr_value>.+)\s*',self.groupdict['string_lines'][0]);
		self.attr=True if m else False
		if (m):
			self.attr_name=m.group('attr_name')
			self.attr_value=m.group('attr_value')
		return m	
	def getattrname(self):
		return self.attr_name
	def getattrvalue(self):
		return self.attr_value
	def setvalue(self,value):
		self.attr_value
	def output_str(self):
		mainline=self.output_mainline()
		attrline=str(self.groupdict['attr_name'])+'='+str(self.groupdict['attr_value'])
		return mainline+'\n'+attrline
class net(gaf_format):
	def __init__(self,line):
		gaf_format.__init__(self,'N',N_re,N_para)
		self.parse_gaf(line)
		self.x1=self.groupdict['x1']
		self.y1=self.groupdict['y1']
		self.x2=self.groupdict['x2']
		self.y2=self.groupdict['y2']
		self.color=self.groupdict['color']
		x1=int(self.groupdict['x1'])
		y1=int(self.groupdict['y1'])
		x2=int(self.groupdict['x2'])
		y2=int(self.groupdict['y2'])
		self.p1=(x1,y1)
		self.p2=(x2,y2)
	def get_netxy(self):
		xylist=[(int(self.groupdict['x1']),int(self.groupdict['y1'])),(int(self.groupdict['x2']),int(self.groupdict['y2']))]
		return xylist
	def point_on_net(self,xy):
		online=False
		c=numpy.cross(self.p2-self.p1,self.p1-xy)
		xin=min(self.p1[0],self.p2[0])<=xy[0] and max(self.p1[0],self.p2[0])>=xy[0] 
		yin=min(self.p1[1],self.p2[1])<=xy[1] and max(self.p1[1],self.p2[1])>=xy[1]
		if (c==0 and xin and yin):
			online=True
		return online
class bus(gaf_format):
	def __init__(self,line):
		gaf_format.__init__(self,'U',U_re,U_para)
		self.parse_gaf(line)
		self.x1	=self.groupdict['x1']
		self.y1	=self.groupdict['y1']
		self.x2	=self.groupdict['x2']
		self.y2	=self.groupdict['y2']
		self.color	=self.groupdict['color']
		self.ripperdir	=self.groupdict['ripperdir']
class pin(gaf_format):
	def __init__(self,line,netpin=False):
		self.init_para()
		gaf_format.__init__(self,'P',P_re,P_para)
		self.parse_gaf(line)
		self.x1	=self.groupdict['x1']
		self.y1	=self.groupdict['y1']
		self.x2	=self.groupdict['x2']
		self.y2	=self.groupdict['y2']
		self.color	=self.groupdict['color']
		self.pintype	=self.groupdict['pintype']
		self.whichend	=self.groupdict['whichend']
		self.location()

	def init_para(self):
		self.x=None;
		self.y=None;
		self.component=None;
		self.net={}
		self.whichend=None;
		#self.net=None
	def getpinseq(self):
		return self.attrdict['pinseq'][-1].attr_value
	def set_comp(self,comp):
		self.component=comp;
		for value in self.net.values():
			value['comp']=comp
	def getxy(self):
		return (self.x,self.y)
	def location(self):
		x=None
		y=None
		if (self.groupdict.has_key('whichend') and self.groupdict.has_key('x1') and self.groupdict.has_key('y1') and self.groupdict.has_key('x2') and self.groupdict.has_key('y2')):
			if (int(self.groupdict['whichend'])==0):
				x=int(self.groupdict['x1'])
				y=int(self.groupdict['y1'])
			elif (int(self.groupdict['whichend'])==1):
				x=int(self.groupdict['x2'])
				y=int(self.groupdict['y2'])
			else:
				x=0
				y=0
		self.x=x
		self.y=y
		#print int(obj.groupdict['whichend'])
		return (x,y)
	def setseq(self,newseq,label=None,number=None):
		self.attrdict['pinseq'].setvalue(newseq)
		self.attrdict['pinlabel'].setvalue(newseq)
		self.attrdict['pinnumber'].setvalue(newseq)

		#print len(self.attrdict),self.attrdict.keys()
		#print len(self.groupdict),self.groupdict.keys()
class netpin(pin):
	def __init__(self,net,pinseq):
		self.attrdict={}
		self.attrdict['net']=net
		self.attrdict['pinseq']=pinseq
		self.type_str='np'

		#gaf_format.__init__(self,'np',np_re,np_para)
		#self.parse_gaf(line)
		#for pinseq in self.groupdict['pinstxt'].split(','):
		#	self.attrdict['pinseq']=pinseq
		self.init_para()
	def getpinseq(self):
		return self.attrdict['pinseq']
			#self.setseq(pinseq)
class component(gaf_format):
	def __init__(self,line):
		gaf_format.__init__(self,'C',C_re,C_para)
		self.parse_gaf(line)
		self.x	=self.groupdict['x']
		self.y	=self.groupdict['y']
		self.selectable	=self.groupdict['selectable']
		self.angle	=self.groupdict['angle']
		self.mirror	=self.groupdict['mirror']
		self.basename	=self.groupdict['basename']
		self.pinxy={}
		self.update_attr()
	def update_attr(self):
		if self.attrdict.has_key('refdes'):
			self.refdes=self.attrdict['refdes'][-1].groupdict['attr_value']
		else:
			self.refdes='UNKNOWN?'

	def get_refdes(self):
		return self.refdes
	def get_pinxy(self):
		symbol_path=self.findsym(self.basename)
		if symbol_path:
			self.symbol=geda_symbol(symbol_path)
			sympinxy=self.symbol.getpinxy()
			for pin in sympinxy.keys():
				key={'comp':self,'pin':pin}
				x=int(sympinxy[pin][0])+int(self.x)
				y=int(sympinxy[pin][1])+int(self.y)
				self.pinxy.update({key:(x,y)})
				print key
		print self.pinxy

class path(gaf_format):
	def __init__(self,line):
		gaf_format.__init__(self,'H',H_re,H_para)
		self.parse_gaf(line)
		self.color	=self.groupdict['color']
		self.width	=self.groupdict['width']
		self.capstyle	=self.groupdict['capstyle']
		self.dashstyle	=self.groupdict['dashstyle']
		self.dashlength	=self.groupdict['dashlength']
		self.dashspace	=self.groupdict['dashspace']
		self.filltype	=self.groupdict['filltype']
		self.fillwidth	=self.groupdict['fillwidth']
		self.angle1	=self.groupdict['angle1']
		self.pitch1	=self.groupdict['pitch1']
		self.angle2	=self.groupdict['angle2']
		self.pitch2	=self.groupdict['pitch2']
		self.num_lines	=self.groupdict['num_lines']
class font(gaf_format):
	def __init__(self,line):
		gaf_format.__init__(self,'F',F_re,F_para)
		self.parse_gaf(line)
		self.character	=self.groupdict['character']
		self.width	=self.groupdict['width']
		self.flag	=self.groupdict['flag']
class attributes(gaf_format):
	def __init__(self,line):
		gaf_format.__init__(self,'{',a_re,a_para)
		self.parse_gaf(line)
		self.attributes	=self.groupdict['attributes']
		self.attrdict={}
		self.parse_attributes()
	def getattrdict(self):
		return self.attrdict
	def parse_attributes(self):
		attrsobj=gaf_string(self.groupdict['attributes']);
		self.attrdict.update(attrsobj.attrdict)
		return attrsobj.getattrdict()
#		attrs=attrsobj.parse_string()
#		attrtextobjs=[text(attr) for attr in attrsobj.objects]
#		for attr in attrtextobjs:
#			self.attrdict[attr.groupdict['attr_name']]=attr
#		self.attrdict.update(attrsobj.getattrdict()
#		return attrtextobjs
class pathdata(gaf_format):
	def __init__(self,line):
		gaf_format.__init__(self,'M',M_re,M_para)
		self.parse_gaf(line)
		self.x	=self.groupdict['x']
		self.y	=self.groupdict['y']
		self.contents	=self.groupdict['contents']
		self.endz	=self.groupdict['endz']
	def output_str(self):
		#this is a temporary solution before I understand the detail structure
		outstr="%s %s,%s\n%s%s"%(self.type_str,self.groupdict['x'],self.groupdict['y'],self.groupdict['contents'],self.groupdict['endz'])
		return outstr
class gaf_string:
	def __init__(self,string):
		self.s_gaf=string
		self.objects=[]
		self.attrdict={}
		self.parse_string()
		self.nets=[]
	def getattrdict(self):
		return self.attrdict
	def parse_string(self,string=None):
		if (string==None):
			string=self.s_gaf;
		m=re.match(type_re%type_para,string);
		gaf_object=None;
		if (m):
			type_str=m.group('type');
			next_str=m.group('next');
			if type_str=='v':
				gaf_object=version(next_str);
			elif type_str=='M':
				gaf_object=pathdata(next_str);
			elif type_str=='L':
				gaf_object=line(next_str);
			elif type_str=='G':
				gaf_object=picture(next_str);
			elif type_str=='B':
				gaf_object=box(next_str);
			elif type_str=='V':
				gaf_object=circle(next_str);
			elif type_str=='A':
				gaf_object=arc(next_str);
			elif type_str=='T':
				gaf_object=text(next_str);
			elif type_str=='N':
				gaf_object=net(next_str);
			elif type_str=='U':
				gaf_object=bus(next_str);
			elif type_str=='P':
				gaf_object=pin(next_str);
			elif type_str=='C':
				gaf_object=component(next_str);
			elif type_str=='H':
				gaf_object=path(next_str);
			elif type_str=='F':
				gaf_object=font(next_str);
			elif type_str=='{':
				gaf_object=attributes(next_str);
			else:
				print "don't know ----------",next_str;
		if (gaf_object):
			if (gaf_object.type_str=='{'):#__class__.__name__=='attributes'):
				self.objects[-1].setattrdict(gaf_object.getattrdict());
			elif (gaf_object.type_str=='T' and gaf_object.isattr()):
				attrobj=[gaf_object]
				attrname=gaf_object.getattrname()
				attrvalue=gaf_object.getattrvalue()
				newattr=attrobj
				if self.attrdict.has_key(attrname):
					print 'has_key',attrname,self.attrdict[attrname],newattr
					self.attrdict[attrname].extend(newattr)
				else:
					self.attrdict[attrname]=newattr
					print 'new',attrname,self.attrdict[attrname],newattr
			else:	
				self.objects.append(gaf_object);
			next_str=gaf_object.next_str();
			self.parse_string(next_str);
		else:
			next_str=None
		return self.objects

class geda_schematic(gaf_string):
	def __init__(self,filename):
		string=open(filename).read()
		gaf_string.__init__(self,string)
		self.components=[]
		self.nets=[];
		self.buses=[];
		self.node=[];
		for obj in self.objects:
			if (obj.type_str=='C'):
				self.components.append(obj)
			elif (obj.type_str=='N'):
				self.nets.append(obj)
			elif (obj.type_str=='U'):
				self.buses.append(obj)
			else:
				pass
#		for obj in self.components:
#			self.node.update(obj.get_pinxy())
#		for obj in self.nets:
#			self.node.
	def merge_nets(self):
		processed=[];
		#self.netlists=[{net:None} for net in self.nets]
		for net1 in self.netlists:
			for net2 in self.netlists:
				if (net1 != net2):
					print net1.get_netxy()
					print net2.get_netxy()
					if net1.connected_net(net2):
						net.append(newnet)
						processed.append(newnet)
		unprocessed=[net for net in self.nets]

		for newcomponent in self.components:
			print newcomponent.get_pinxy()

#netlist.update(component=component)
			#xy= net.get_netxy():
			#for netlist in self.netlists:
			#	if xy[0] in netlist or xy[1] in netlist:
#self.netlists=[{((x0,y0),(x1,y1),(x2,y2)):name},....]

				
#				print xy
	#			self.netlist.append(xy)
			

	def available_part_list(self):
		pass
	def apply_parts(self):
		pass
	def RF_sim(self):
		pass
	def netlist(self):
		pass
	def generate_symbol_from_sch(self):
		pass


class geda_symbol(gaf_string):
	def __init__(self,filename):
		self.pins=[]
		string=open(filename).read()
		gaf_string.__init__(self,string)
		self.gennetpin()
		self.update_pins()
		self.genpindict()
		self.genpinxy()
	def gennetpin(self):
		if self.attrdict.has_key('net'):
			print self.attrdict['net']
			for np in self.attrdict['net']:
				print np
				nptxt=np.attr_value
				print 'nptxt is ',nptxt
				m=re.match(np_re%np_para,nptxt)
				if (m):
					npdict=m.groupdict();
					
					print npdict['pinstxt'].split(',')

					for pinseq in npdict['pinstxt'].split(','):
						newpin=netpin(npdict['netname'],pinseq)
						self.objects.append(newpin)
	#			newpin=netpin(np.groupdict['attr_value'])#,netpin=True)
	#			self.objects.append(newpin)
			#	print np.groupdict['attr_value']#['attrvalue']
			#	if net not in self.nets:
			#		self.nets.append(net)
			#	else:
			#		pass # should add pin to net?

	def derive_vendor_part_symbol(self):
		pass
	def add_attr(self,attrdict):
		pass
	def pin_map(self,oldnewdict):
		for pin in oldnewdict.keys():
			if self.pindict.has_key(pin):
				self.pindict[pin].setseq(oldnewdict[pin])


		pass
	def RF_sim(self):
		pass
	def generate_from_verilog(self,verilogfile):
		pass
	def update_pins(self):
		print 'update_pins',self.pins
		for obj in self.objects:
			if (obj.type_str=='P' or obj.type_str=='np'):
				self.pins.append(obj)
		if self.attrdict.has_key('net'):
			print [net.__class__.__name__ for net in self.attrdict['net']]

	def genpindict(self):
		self.pindict={}
		for obj in self.objects:
			if (obj.type_str=='P' or obj.type_str=='np'):
				print obj.type_str
				print obj.getpinseq()
				self.pindict.update({obj.getpinseq():obj})
	def getpindict(self):
		return self.pindict
	def genpinxy(self):
		self.pinxy={}
		for p in self.pindict.keys():
			self.pinxy.update({p:self.pindict[p].getxy()})
	def getpinxy(self):
		return self.pinxy
		


if __name__=="__main__":
	if (0):
		sym=geda_symbol(sys.argv[1])
		print sym.getpindict()
#	for o in sym.objects:
#		print o.output_str()
		#sym.pin_map({'1':'2','2':'1'})
		for o in sym.objects:
			print o.output_str()
		print sym.getpindict()
		print sym.getpinxy()	
	filename=sys.argv[1]
	ext=os.path.basename(filename).split('.')[-1]
	if ext=='sym':
		sym=geda_symbol(filename)
		print '''usage:
		-x symbol filename apply vendor specification in json file'''
		print 'obj class name',[obj.__class__.__name__ for obj in sym.objects]
		print 'key,length for attrdict',[(key,len(sym.attrdict[key])) for key in sym.attrdict.keys()]
		print '# of pins: ',len(sym.pins)
		print filename,len(sym.pins),'pins'
		for pin in sym.pins:
			print 'pin',pin.attrdict,pin.getxy()
	elif ext=='sch':
		sch=geda_schematic(sys.argv[1])
		print sch.components
		print 'usage'

#	sch.merge_nets()
#	print [o.groupdict['basename'] if o.__class__.__name__=='component' else o.__class__.__name__ for o in sgaf.objects]
#	for o in sgaf.objects:
#		print o.output_str()
# http://wiki.geda-project.org/geda:file_format_spec#path_data
