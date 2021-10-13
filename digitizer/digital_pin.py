import re
def gnd(x0,y0):
	return '''C %d %d 1 270 1 gnd-1.sym'''%(x0,y0)
def input(x0,y0,xt0,yt0,xt1,yt1,refdes):
	return '''C %d %d 1 0 0 in-1.sym
{
T %d %d 5 10 0 0 90 0 1
device=INPUT
T %d %d 5 10 1 1 90 0 1
refdes=%s
}'''%(x0,y0,xt0,yt0,xt1,yt1,refdes)

def pin(x0,y0,x1,y1,xt1,yt1,xt2,yt2,label,xt3,yt3,number,xt4,yt4,seq):
	return '''P %d %d %d %d 1 0 0
{
T %d %d 5 10 0 0 0 0 1
pintype=unknown
T %d %d 5 10 0 1 0 0 1
pinlabel= %s
T %d %d 5 10 1 1 0 6 1
pinnumber=%s
T %d %d 5 10 0 0 0 0 1
pinseq=%s
}'''%(x0,y0,x1,y1,xt1,yt1,xt2,yt2,label,xt3,yt3,number,xt4,yt4,seq)

def net(x0,y0,x1,y1,name):
	return '''N %d %d %d %d 4
{
T %d %d 5 10 1 1 0 0 1
netname=%s
}'''%(x0,y0,x1,y1,x1,y1,name)


if __name__=="__main__":
	head='''v 20130925 2
T 7000 20200 9 40 1 0 0 0 1
LPC FMC P1
C 5000 2000 1 0 0 fmc_lpc_mzn.sym
{
T 8795 1995 5 10 1 1 0 0 1
refdes=P1
T 5000 2000 5 10 1 1 0 0 1
device=ASP-134604-01
T 5000 2000 5 10 1 1 0 0 1
footprint=FMC_LPC_MEZ
}
T 17700 20000 9 40 1 0 0 0 1
LPC FMC P2
C 15000 2000 1 0 0 fmc_lpc_mzn.sym
{
T 19495 1895 5 10 1 1 0 0 1
refdes=P2
T 15000 2000 5 10 1 1 0 0 1
device=ASP-134604-01
T 15000 2000 5 10 1 1 0 0 1
footprint=FMC_LPC_MEZ
}
C -100 0 0 0 0 lbl-title-bordered-A1.sym
{
T 30700 1200 15 10 1 1 0 0 1
title=TITLE
T 27200 1000 15 10 1 1 0 0 1
file=$FileName$
T 27200 300 15 10 1 1 0 0 1
author=$LastAuthor$
T 27200 600 15 10 1 1 0 0 1
date=$LastDate$
T 27200 1300 15 10 1 1 0 0 1
revision=$Revision$
T 30700 600 15 10 1 1 0 0 1
date=$FirstDate$
T 30700 300 15 10 1 1 0 0 1
author=$FirstAuthor$
}'''
	print head
	abcdef=['C','D','G','H'];
	nets={};
	duplicate=[]
	p=open('digitizer_digital_pin.txt').read().split('\n')
	for line in p:
		#		print line
		m=re.match('(P1|P2)\s(\S)(\d*)\s*([\s\S]*)',line)
		if m:
			netname=m.group(4)
			if nets.has_key(netname):
				duplicate.append(netname)
			else:
				nets[netname]=[m.group(2),m.group(3)]

#			print m.groups()
			if m.group(1)=='P1':			
#				print m.groups()
				name=abcdef.index(m.group(2))
				index=eval(m.group(3))
				x0=6200+name*2000;
				y0=19500-400*index;
				x1=x0-700;
				y1=y0;
				print net(x0,y0,x1,y1,m.group(4))
			elif m.group(1)=='P2':			
#				print m.groups()
				name=abcdef.index(m.group(2))
				index=eval(m.group(3))
				x0=16200+name*2000;
				y0=19500-400*index;
				x1=x0-700;
				y1=y0;
				print net(x0,y0,x1,y1,m.group(4))
#	print duplicate
				
'''	abcdef=['A','B','C','D','E','F','G','H','J','K'];
	gndpins=[];
	hpcpin=[line.split(' ') for line in open('fmchpc.pins').read().split('\r')];
	for name in range(len(abcdef)):
		for index in range(40):
			label=abcdef[name]+str(index+1)
			#print index,10-name,label,hpcpin[index][10-name],hpcpin[index][10-name]=='GND'
			if hpcpin[index][10-name]=='GND':
			#	print label
				gndpins.append(label)
#	print gndpins
	for name in range(len(abcdef)):
		for index in range(40):
			x0= 1200+name*2000;
			y0= 17300-400*index;
			label=abcdef[name]+str(index+1)
			if (label in gndpins):
				pass
				#print gnd(x0,y0)
			else:	
				#xt0=x0-300; yt0=y0;
				#xt1=x0-300; yt1=y0;
				#print input(x0-300,y0,xt0,yt0,xt1,yt1,label)
				x0= 1200+name*2000;
				y0= 17300-400*index;
				x1=x0+800;y1=y0;
				xt1=x0;yt1=y0;
				xt2=x0+1145; yt2=y0-5;
				label=abcdef[name]+str(index+1)
				xt3=x0+705;yt3=y0+45;
				number=label;
				xt4=x0;yt4=y0;
				seq=label;
				print pin(x0,y0,x1,y1,xt1,yt1,xt2,yt2,label,xt3,yt3,number,xt4,yt4,seq)
				
	
#			x0= 1200+name*2000;
#			y0= 17300-400*index;
#			x1=x0+800;y1=y0;
#			xt1=x0;yt1=y0;
#			xt2=x0+1145; yt2=y0-5;
#			label=abcdef[name]+str(index+1)
#			xt3=x0+705;yt3=y0+45;
#			number=label;
#			xt4=x0;yt4=y0;
#			seq=label;
#			print pin(x0,y0,x1,y1,xt1,yt1,xt2,yt2,label,xt3,yt3,number,xt4,yt4,seq)
##1200,17300,2000,17300,1200,17300,2345,17295,label,1905,17345,number,1200,17300,seq)
'''
