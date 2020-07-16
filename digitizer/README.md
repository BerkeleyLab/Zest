# LCLS-II LLRF Digitizer Board

This directory holds the schematics and associated files (but not the layout)
for the LCLS-II LLRF Digitizer Board, currently Rev. 1.1.
It is in gschem format; to work with it you
need [gschem](http://wiki.geda-project.org/geda:gaf) installed.
Tested on [Debian](https://www.debian.org) Jessie or Stretch, where
you simply `apt-get install geda-gschem`.

![Image of completed board](../../doc/digitizer_top_x.jpg) [block diagram](../../doc/digitizer_block.png)

The digitizer board features:

* 8 x transformer-coupled inputs sampled at 95 MS/s (2 x AD9653)
* 2 x transformer-coupled outputs sampled at 190 MS/s (AD9781)
* Input clock source up to 3 GHz (LMK01801, no on-board oscillator)
* Extra clock divider output
* 2 x Pmod digital I/O
* Interface to FPGA via dual-LPC-FMC connectors
* 181.8 x 110 mm, with notch to accommodate Xilinx FMC eval boards
* 4W power dissipation

## Schematics

To get PDF versions for reference,
simply `make` in this directory.  The result is digitizer_schematics.pdf.

## Artwork/Gerbers

Created by Kathy Pham at SLAC using PADS.  Latest is 20170519.
The PADS design imports the netlist exported from this gschem design.
These PADS files are _not_ kept in this git repository, but
their SHA256 signatures are kept in the
[layout_20170519.sha256sum](layout_20170519.sha256sum) file in this directory.

QR-code serial-number overlay Gerbers are generated with `qr_gen.py`.

## BOM

Get a copy of the `PC-379-396-15-C02_DIGITIZER BOARD_XY.xlsx` file exported from
the PADS design reference above, and place it in this directory.

Then `make merged_xy.csv` to merge the actual orderable part numbers (kept here
in the parts.data file) and get a usable xy assembly file for fabrication.

## Plastic Cover

One corner of the digitizer (by J3, clock input) has some fragile transformers
very close to where SMA wrenches are used.
It has proved helpful to have a protective cover in place to avoid damage.
This is designed in [OpenSCAD](http://www.openscad.org/) with a process that
matches up its features with the Gerber file; see covergen.py.
The OpenSCAD source file is cover1.scad.
OpenSCAD will export an STL file which is easily 3-D printed.

## References

 G. Huang, L. R. Doolittle, J. Yang, Y. Xu,
*``Low Noise Digitizer Design for LCLS-II LLRF,''* in NAPAC2016
[TUPOA40](http://accelconf.web.cern.ch/AccelConf/napac2016/papers/tupoa40.pdf).
