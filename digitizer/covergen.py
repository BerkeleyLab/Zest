# 3D-printed plastic cover for the Digitizer board

# To test the alignment of its features with the Gerbers of the PCB:
# python covergen.py > foo.pcb && pcb -x gerber foo.pcb && gerbv foo.top.gbr foo.bottom.gbr foo.group2.gbr ref1.gbr ref2.gbr
# where the .gbr files come from Kathy Pham and PADS.

# To create the 3D model for printing:
# python covergen.py openscad > cover2_layers.dat && openscad cover2c.scad

use_openscad = False


def base_cube(x1, y1, dx, dy, h):
	# h is only for compatibility with openscad routine
	if use_openscad:
		vv = (x1, y1, dx, dy, h)
		return '    base_cube(%6.2f, %6.2f, %5.2f, %5.2f, %5.2f);\n' % vv
	x1 = x1 + 27.1
	y1 = 16.3 - y1
	x2 = x1 + dx
	y2 = y1 - dy
	return '''    Polygon("clearpoly")
	(
		[%.2fmm %.2fmm] [%.2fmm %.2fmm] [%.2fmm %.2fmm] [%.2fmm %.2fmm]
	)''' % (x1, y1, x2, y1, x2, y2, x1, y2)


# these are the stubs supposed to rest on the bare board
def layer1():
	r = ""
	r += base_cube(0,    -3.6,  9.5, 3.6, 2)
	r += base_cube(0,   -18.2,  9.5, 3.6, 2)
	r += base_cube(25.3, -6.1,  9.5, 6.1, 2)
	for ix in range(10):
		y = -33.10 - 15.24*ix
		r += base_cube(0, y, 16.0, 5.2, 2)
	return r


# stay-clear for transformers
def layer2():
	r = ""
	# TCM4-19 datasheet claims max height 4.06 mm, I measure 3.1 mm
	r += base_cube(11.3, -15.2, 4.2, 4, 4.0)  # U34
	r += base_cube(17.3, -15.2, 4.2, 4, 4.0)  # T1
	r += base_cube(11.3, -26.0, 4.2, 4, 4.0)  # T2
	for ix in range(9):
		y = -39.12 - 15.24*ix
		r += base_cube(15.09, y, 4.2, 4.4, 4.0)  # UxT1
	r += base_cube(15.09, -178.7, 4.2, 4.4, 4.0)  # U13T1
	# These next holes just reduce the amount of material needed for printing
	# keep the edge for stiffness
	r += base_cube(22.0,  -73.0, 15.0, 32.0, 4.0)
	r += base_cube(22.0, -143.0, 15.0, 61.0, 4.0)
	r += base_cube(22.0, -177.0, 15.0, 26.0, 4.0)
	return r


# holes for SMA connectors and the mounting screw
def layer3():
	r = ""
	# J3 J20 J11 J10 J9 J8 ...
	for ix in range(12):
		y = -11.52 - 15.24*ix
		r += base_cube(-1, y, 10.6, 7.7, 8)  # J3
	r += base_cube(-1, -184.16, 10.6, 12.7, 8)  # it would break off anyway
	# now 3 mounting screws
	if not use_openscad:
		r += base_cube(37.55-2.1,  -36.50-2.1, 4.2, 4.2, 2)
		r += base_cube(38.69-2.1,  -77.90-2.1, 4.2, 4.2, 2)
		r += base_cube(32.47-2.1, -146.99-2.1, 4.2, 4.2, 2)
	return r


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


def pcb_file(top_items, bot_items, mid_items):
	template = get_template(xmax=5236.11, ymax=9638.89)
	return template + '''Layer(1 "top" "copper")
(
'''+top_items+'''
)
Layer(2 "ground" "copper")
(
)
Layer(3 "signal2" "copper")
(
'''+mid_items+'''
)
Layer(4 "signal3" "copper")
(
)
Layer(5 "power" "copper")
(
)
Layer(6 "bottom" "copper")
(
'''+bot_items+'''
)
Layer(7 "outline" "copper")
(
)
Layer(8 "spare" "copper")
(
)
Layer(9 "bottom silk" "silk")
(
)
Layer(10 "top silk" "silk")
(
)'''


def infogbr(filename, layer='top'):
	from os import system
	system('pcb -x gerber test.pcb')
	f = open('%s.%s.gbr' % (filename, layer))
	s = f.read()
	f.close()
	return s


def gbrcombine(s1, s2):
	return '\n'.join(['\n'.join(s1.split('\r\n')[:-2]), s2])


def openscad_file(top_items, bot_items, mid_items):
	r = ""
	r += "module layer1()\n{\n" + top_items + "}\n\n"
	r += "module layer2()\n{\n" + bot_items + "}\n\n"
	r += "module layer3()\n{\n" + mid_items + "}\n\n"
	return r

if __name__ == "__main__":
	from sys import argv
	if len(argv) > 1 and argv[1] == "openscad":
		use_openscad = True
		print openscad_file(layer1(), layer2(), layer3())
	else:
		print pcb_file(layer1(), layer2(), layer3())
