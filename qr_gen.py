import numpy
import qrtools
import scipy.ndimage
import os

def qrpng2pcbpoly(qrpngfilename, x0=9600, y0=3200):
	im = scipy.ndimage.imread(qrpngfilename, flatten=True)
	ymax, xmax = im.shape
	y, x = numpy.where(im == 255)
	x0 = x0 - 450
	y0 = y0 + 430
	step = 14
	polygons = []
	for ix, xvalue in enumerate(x):
		x1 = x0+xvalue*step
		x2 = x0+xvalue*step+step
		y1 = y0-(ymax-y[ix])*step
		y2 = y0-(ymax-y[ix])*step+step
		polygons.append('''    Polygon("clearpoly")
	(
		[%.2fmil %.2fmil] [%.2fmil %.2fmil] [%.2fmil %.2fmil] [%.2fmil %.2fmil]
	)''' % (x1, y1, x2, y1, x2, y2, x1, y2))
	return '\n'.join(polygons)

# String length limits for Version 2 (25x25), assuming "Alphanumeric" encoding:
#  level='S'   40
#  level='M'   28
#  level='Q'   22
def qrgen(string, level='M'):
	print("qrgen: " + string)
	qr = qrtools.QR(string, pixel_size=1, margin_size=2, level=level)
	qr.encode(string)
	return string+'.png'

def pcbstring(x, y, size, s):
	return '''
	Text[%3.2fmil %3.2fmil 0 %d "%s" "clearline"]''' % (x, y, size, s)

def pcbstrings(l):
	return "".join([pcbstring(*ll) for ll in l])

def munge_size(l, xmax, ymax):
	if l[0:7] == 'PCB["" ':
		return 'PCB["" %.2fmil %.2fmil]' % (xmax, ymax)
	else:
		return l

def get_template(xmax=12000, ymax=10000):
	with open("template.pcb", "r") as f:
		template = f.read()
	lines = template.split('\n')
	return "\n".join([munge_size(l, xmax=xmax, ymax=ymax) for l in lines])


def pcbfile(silk, template):
	return template + '''Layer(10 "top silk" "silk")
(
'''+silk+'''
)'''

def infopcb(lines, sn, x0=9600, y0=3200):
	line_break = lines.split('\n')
	return pcbstrings([
		(x0, y0+0, 110, line_break[0]),
		(x0, y0+70, 110, line_break[1]),
		(x0, y0+140, 110, line_break[2]),
		(x0, y0+210, 200, 'S'),
		(x0, y0+320, 200, 'N'),
		(x0+100, y0+180, 500, '%03d' % sn)])

def oneboard(gerber_name="a.gbr", sn=1, qr_string="TEST 1", desc_string="", x0=3900, y0=1200, level="M", template="", lines=""):
	polys = qrpng2pcbpoly(qrgen(qr_string, level=level), x0=x0, y0=y0)
	pcbstr = pcbfile(silk=infopcb(lines, sn, x0=x0, y0=y0)+polys, template=template)
	pcb_name = 'test'
	with open(pcb_name+'.pcb', 'w') as f:
		f.write(pcbstr)
		f.close()
	os.system('pcb -x gerber %s.pcb && mv %s.%s.gbr %s' % (pcb_name, pcb_name, 'topsilk', gerber_name))


if __name__ == "__main__":
	setup = [3900, 7450, 'qr_sn_%03d.gbr', 'LBNL DIGITIZER V1.1 SN %03d', 'M', 'LBNL Digitizer\nLCLS-II LLRF\nRevision 1.1']
	# setup = [10000, 5360, 'qr_dn_sn_%03d.gbr', 'FNAL DOWNCVT REV C SN %03d', 'M', 'FNAL DOWNCVT\nLCLS-II LLRF\nRev C']
	# setup = [6900, 2300, 'qr_up_sn_%03d.gbr', 'FNAL UPCVT REV C SN %03d', 'M', 'FNAL UPCVT\nLCLS-II LLRF\nRev C']
	x0, y0, gerber_base, qr_base, level, lines = setup
	template = get_template(xmax=x0+1000, ymax=y0+1000)
	for sn in range(32, 57):
		gerber_name = gerber_base % sn
		qr_string = qr_base % sn
		desc_string = ''
		oneboard(gerber_name=gerber_name, sn=sn, qr_string=qr_string, desc_string=desc_string, x0=x0, y0=0, level=level, template=template, lines=lines)
