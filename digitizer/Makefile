LINKS=digitizer_05_se2diff.sch digitizer_06_diff2se.sch digitizer_07_thermo_bridge.sch digitizer_08_LDO-B.sch digitizer_09_LT6655-ref.sch digitizer_10_TPS62210-ps.sch digitizer_11_LT1763-ps.sch
SOURCE := $(sort $(wildcard ./digitizer_*.sch))
SOURCE += $(LINKS)
SOURCE_PDF = $(SOURCE:%.sch=%_sch.pdf)
GEDA_LIBRARY=../geda_library
OPENSCAD = openscad

TOP_SCH = digitizer_01_adda.sch digitizer_02_fmc.sch digitizer_03_housekeeping.sch digitizer_04_power.sch

TARGET = $(SOURCE_PDF) digitizer_schematics.pdf

all: $(TARGET)
CLEAN += digitizer_schematics.pdf *.ps partslist3.txt bom.txt bom2.txt digitizer.net digitizer.net1 digitizer.drc orderable.txt digitizer_schematics.pdf parts1.csv merged_xy.csv pads.csv cover2_layers.dat *.stl gnet-pads2.scm
include ./rules.mk


links:$(LINKS)

digitizer_05_se2diff.sch: $(GEDA_LIBRARY)/pcblib/schem/se2diff.sch
	ln -s $< $@
digitizer_06_diff2se.sch:$(GEDA_LIBRARY)/pcblib/schem/diff2se.sch
	ln -s $< $@
digitizer_07_thermo_bridge.sch:$(GEDA_LIBRARY)/pcblib/schem/thermo_bridge.sch
	ln -s $< $@
digitizer_08_LDO-B.sch:$(GEDA_LIBRARY)/pcblib/schem/LDO-B.sch
	ln -s $< $@
digitizer_09_LT6655-ref.sch:$(GEDA_LIBRARY)/pcblib/schem/LT6655-ref.sch
	ln -s $< $@
digitizer_10_TPS62210-ps.sch: $(GEDA_LIBRARY)/pcblib/schem/TPS62110-ps.sch
	ln -s $< $@
digitizer_11_LT1763-ps.sch: $(GEDA_LIBRARY)/pcblib/schem/LT1763-ps.sch
	ln -s $< $@


digitizer_schematics.pdf: $(SOURCE_PDF)
	pdfunite $^ $@

digitizer.drc: $(TOP_SCH)
	gnetlist -g drc2 -o $@ $^

digitizer_02_fmc.sch: digital_pin.py digitizer_digital_pin.txt
	python $^ > $@.$$ && mv $@.$$ $@

gnet-pads2.scm: make-pads2
	sh $<

digitizer.net1: $(TOP_SCH) gnet-pads2.scm
	gnetlist -L . -g pads2 $(filter-out gnet-pads2.scm, $^) -o $@

# See netlist_adjust.sed for explanation of how the raw gnetlist output needs to be fixed up
digitizer.net: digitizer.net1
	sed -f netlist_adjust.sed < $< > $@

partslist3.txt: $(TOP_SCH)
	gnetlist -g partslist3 -Oattribs=refdes,device,value,footprint,dielectric,voltage -o $@ $^
bom.txt: $(TOP_SCH)
	gnetlist -g bom -Oattribs=refdes,device,value,footprint,dielectric,voltage -o $@ $^
bom2.txt: $(TOP_SCH)
	gnetlist -g bom2 -Oattribs=refdes,device,value,footprint,dielectric,voltage -o $@ $^

orderable.txt: orderable.py partslist3.txt
	python $^ > $@

# Experimental
parts1.csv: digitizer.net parts.data
	python bom_from_net.py > $@

pads.csv: PC-379-396-15-C02_DIGITIZER\ BOARD_XY.xlsx
	libreoffice --headless --convert-to csv --outdir . "$<"
	mv PC-379-396-15-C02_DIGITIZER\ BOARD_XY.csv $@

merged_xy.csv: pads.csv parts.data
	python merge.py > $@

cover2_layers.dat: covergen.py
	python $< openscad > $@

cover2c.stl: cover2c.scad cover2_layers.dat
	$(OPENSCAD) -o $@ $<

myclean: clean
	    rm -f $(LINKS) *.pdf
