TOP := $(dir $(abspath $(lastword $(MAKEFILE_LIST))))
GAF_VERSION := $(shell gaf --version 2>/dev/null)

FOOTGEN_DIR = $(TOP)geda_library/footprint
DJBOXSYM_DIR = $(TOP)/geda_library/symbol
SCRIPT_DIR = /usr/share/gEDA/scheme/
#$(TOP)script

# AUTHOR=`git log --pretty="%an" -1 logen.sch`; sed -e 's/\$Author\$/'"$AUTHOR"'/g' logen.sch > logen_git.sch
GIT_AUTHOR_CMD = git log --pretty="%an"
GIT_DATE_CMD   = git log --pretty="%ad" --date=short
GIT_REV_CMD    = git log --pretty="%h"

.PHONY: all clean geda_lib clean_dep
#$(FOOTGEN_DIR)/elements:
#	make -C $(FOOTGEN_DIR)

%_bom.txt: %.sch
	gnetlist -g bom -Oattribs=refdes,device,value,footprint,description,vendor,vendor_id,price $< -o $@

%_partslist3.txt: %.sch
	gnetlist -g partslist3 -Oattribs=refdes,device,value,footprint,description,vendor,vendor_id,price $< -o $@

%_bom2.txt: %.sch
	gnetlist -g bom2 -Oattribs=refdes,device,value,footprint,description,vendor,vendor_id,price $< -o $@

%_gbr.tar.gz: %.pcb
	mkdir -p gbr
	pcb -x gerber --gerberfile gbr/$*_gbr $<
	tar zcvf $@ gbr/
	rm -rf gbr

%.eps: %.pcb
	pcb -x eps --eps-file $@
%.ps: %.pcb
	pcb -x ps --psfile $@ $<
%.pdf: %.ps
	ps2pdf $<

%.eps: %.m
	octave -q $<
%.pdf: %.eps
	ps2pdf -dEPSCrop $< $@

ifdef GAF_VERSION
%_sch.pdf: %_git.sch
	refdes_renum $<
	gaf export -o $@  $<
else
%_sch.pdf: %_sch.ps
	ps2pdf $< $@
%_sch.ps: %_git.sch
	gschem -p -o $(notdir $@) -s $(SCRIPT_DIR)/print.scm $<
endif


%.cas: %.sch
	gnetlist -g cascade -o $@ $<

%_git.sch: %.sch
	FST_AUTHOR=`$(GIT_AUTHOR_CMD) $< | tail -n 1`; \
	FST_DATE=`$(GIT_DATE_CMD) $< | tail -n 1`; \
	LST_AUTHOR=`$(GIT_AUTHOR_CMD) -1 $<`; \
	LST_DATE=`$(GIT_DATE_CMD) -1 $<`; \
	LST_REV=`$(GIT_REV_CMD) -1 $<`; \
	sed -e 's/\$$LastAuthor\$$/'"$$LST_AUTHOR"'/g;s/\$$LastDate\$$/'"$$LST_DATE"'/g;s/\$$Revision\$$/'"$$LST_REV"'/g;s/\$$FirstDate\$$/'"$$FST_DATE"'/g;s/\$$FirstAuthor\$$/'"$$FST_AUTHOR"'/g;s#\$$FileName\$$#$<#g' $< > $@

geda_lib:
	make -C $(FOOTGEN_DIR)
	make -C $(DJBOXSYM_DIR)

%.sym: %.symdef
	$(TOP)geda_library/script/djboxsym $< > $@

clean: clean_dep
	rm -f *~ *- $(TARGET) $(CLEAN)
