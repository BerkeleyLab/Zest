s/_unknown//
s/\+@/@/
s/Ω//

s,/,,g
# Getting rid of the "/" is a crude way to remove hierarchy.
#   -e '2,/^\*NET\*/s/[.-]/_/g'
# Converting "." and "-" to "_" applies only to line 2 through *NET*, so as not to
# mess with "." that's used as the pin number separator in the netlist proper.

s/U29U1	LT1763IDE-1.8@DFN-12/U29U1	LT1763IDE-3.3@DFN-12/g
s/U32R1	RESISTOR_422k@0603/U32R1	RESISTOR_191k@0603/g
s/ZXCT1009QFTA@SOT23-3/ZXCT1009QFTA@ZXCT1009/g
