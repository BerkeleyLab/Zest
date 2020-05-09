/* Digitizer cover to protect its transformers near J3 and J20 */
/* Obsolete, see cover2c.scad */
/* See also covergen.py */

/* 5 mm from board to attached SMA connector, which still fits in */
/* the 7.9 mm cutout for the board-mount SMA connector. */
/* 7 mm from board to the beginning of the hex section. */
/* Part is 5.5 mm thick, to avoid slight interference with SMA connectors found with a 6mm thick version. */

module cover()
{
  union() {
    difference() {
       union () {
          translate([0, -39.5, 2]) cube([40.5, 39.5, 3.5]);
          /* copper pad on board measures 5.8 mm dia */
          translate([37.55,-36.5, 0]) cylinder(r=2.9, h=4, $fn=30);
       }
       union () {
          /* 106.3 mil = 2.7 mm dia hole, tight clearance for 4-40 */
          translate([37.55, -36.5, -1]) cylinder(r=1.5, h=8, $fn=30);
          translate([ -1, -11.50, 0]) cube([10.6, 7.7, 8]);  /* J3  */
          translate([ -1, -26.75, 0]) cube([10.6, 7.7, 8]);  /* J20 */
          translate([ -1, -42.00, 0]) cube([10.6, 7.7, 8]);  /* J11 */
          /* TCM4-19 datasheet claims max height 4.06 mm, I measure 3.1 mm */
          translate([11.3, -15.2, 0]) cube([4.2, 4, 4.0]);  /* U34 */
          translate([17.3, -15.2, 0]) cube([4.2, 4, 4.0]);  /* T1 */
          translate([11.3, -26.0, 0]) cube([4.2, 4, 4.0]);  /* T1 */
          translate([39, -24, 1]) mirror(v=[1, 0, 0]) linear_extrude(height = 1.5) {
              text("LBNL", size = 6.2, font = "Liberation Sans");
          }
          translate([28, -34, 1]) mirror(v=[1, 0, 0]) linear_extrude(height = 1.5) {
              text("R3", size = 6.2, font = "Liberation Sans");
          }
       }
    }
    /* these are the stubs supposed to rest on the bare board */
    translate([0,    -3.6, 0]) cube([ 9.5, 3.6, 2]);
    translate([0,   -18.2, 0]) cube([ 9.5, 3.6, 2]);
    translate([0,   -33.1, 0]) cube([16.0, 5.2, 2]);
    translate([25.3, -6.1, 0]) cube([ 9.5, 6.1, 2]);
  }
}

cover();
