COMMITNUM = $(shell git log --pretty=oneline --abbrev-commit --abbrev=8|head -1 | awk '{print $$1}')
DATETIME = $(shell date  +'%Y%m%d%H%M%S')
GITTIME = $(shell git log -1 --date=iso-strict --pretty=%cd)
PROJECT = zest
PYTHON = python3

pdf:
	kicad-cli sch export pdf $(PROJECT).kicad_sch

fab: scripts/gerber.py
	mkdir -p fab
	cp License fab
	$(PYTHON) scripts/gerber.py zest.kicad_pcb fab -gerber -drill -bom -xypos

scripts/gerber.py:
	mkdir -p scripts
	wget https://gitlab.com/lbl-bids/kicad_library/-/raw/f0649040c631f607d80040bc28f9726b902a2629/scripts/gerber.py -O scripts/gerber.py
	echo "1b6c5d99b7cb82a72ffd64895578e01f1f96e2d3fc03a86a395eebeef724e1ae  scripts/gerber.py" | sha256sum -c

tarball: fab qrsn
	echo $(GITTIME)
	tar --sort=name --mtime=$(GITTIME)  --owner=0 --group=0 --numeric-owner -czf $(PROJECT)_$(DATETIME)_$(COMMITNUM).tar.gz fab qrsngbr
	sha256sum $(PROJECT)_$(DATETIME)_$(COMMITNUM).tar.gz

zip: fab qrsn
	touch -d $(GITTIME) fab/* qrsngbr/*
	zip -X -o $(PROJECT)_$(DATETIME)_$(COMMITNUM).zip fab/* qrsngbr/*
	sha256sum $(PROJECT)_$(DATETIME)_$(COMMITNUM).zip

SNSTART = 1
SNSTOP = 2
qrsn: scripts/gerber.py
	$(PYTHON) qrsn.py -proj $(PROJECT)_qrsn -start $(SNSTART) -stop $(SNSTOP) -outputdir qrsngbr

.PHONY: fab qrsn zip pdf
