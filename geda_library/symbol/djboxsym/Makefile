.PHONY: all clean

SOURCE := $(wildcard *.symdef)
TARGET = $(SOURCE:%.symdef=%.sym)
DJBOXSYM = djboxsym
# http://www.gedasymbols.org/user/dj_delorie/tools/djboxsym
# 1a372fdef8e474119fae8acde38226f82271b62cd16b7f47b6b2408f0c0dd1ea  djboxsym

%.sym: %.symdef
	$(DJBOXSYM) $< > $@

all: $(TARGET)

clean:
	rm -f $(TARGET)
