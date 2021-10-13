v 20110115 2
C 42300 78500 1 0 0 ltc6401.sym
{
T 46000 80900 5 10 0 0 0 0 1
device=ad driver
T 43800 80100 5 10 1 1 180 3 1
refdes=U1
T 42300 78500 5 10 0 0 0 0 1
footprint=QFN16_3_EP
T 42300 78500 5 10 0 0 0 0 1
value=LTC6401-14
}
C 45500 80900 1 0 0 resistor-1.sym
{
T 45800 81300 5 10 0 0 0 0 1
device=RESISTOR
T 45700 81200 5 10 1 1 0 0 1
refdes=R1
T 45500 80900 5 10 0 0 0 0 1
footprint=p0603
T 46100 81200 5 10 1 1 0 0 1
value=DNL
}
C 45500 79800 1 0 0 resistor-1.sym
{
T 45800 80200 5 10 0 0 0 0 1
device=RESISTOR
T 45700 80100 5 10 1 1 0 0 1
refdes=R3
T 45500 79800 5 10 0 0 0 0 1
footprint=p0603
T 46100 80100 5 10 1 1 0 0 1
value=0
}
C 42200 78200 1 0 0 gnd-1.sym
N 42300 78500 44800 78500 4
N 43200 81500 44500 81500 4
N 42300 79200 42300 78500 4
N 42300 80800 42000 80800 4
N 42000 80800 42000 80400 4
N 42000 80400 42300 80400 4
N 42300 80000 42000 80000 4
N 42000 80000 42000 79600 4
N 42000 79600 42300 79600 4
C 47100 79700 1 90 0 inductor-1.sym
{
T 46600 79900 5 10 0 0 90 0 1
device=INDUCTOR
T 46900 79900 5 10 1 1 90 0 1
refdes=L1
T 46400 79900 5 10 0 0 90 0 1
symversion=0.1
T 47100 79700 5 10 0 0 0 0 1
footprint=p0603
T 46900 80200 5 10 1 1 90 0 1
value=DNL
}
C 47800 79700 1 90 0 capacitor-1.sym
{
T 47100 79900 5 10 0 0 90 0 1
device=CAPACITOR
T 47300 79700 5 10 1 1 90 0 1
refdes=C5
T 46900 79900 5 10 0 0 90 0 1
symversion=0.1
T 47800 79700 5 10 0 0 0 0 1
footprint=p0603
T 47300 80100 5 10 1 1 90 0 1
value=12p_NPO
}
C 40200 81300 1 180 0 tc1-1-13m.sym
{
T 39200 80900 5 10 1 1 180 3 1
refdes=T1
T 40200 81300 5 10 0 0 0 0 1
footprint=AT224
T 40200 81300 5 10 0 0 0 0 1
value=TCM4-19
}
C 40400 80400 1 0 0 capacitor-1.sym
{
T 40600 81100 5 10 0 0 0 0 1
device=CAPACITOR
T 40600 80900 5 10 1 1 0 0 1
refdes=C2
T 40600 81300 5 10 0 0 0 0 1
symversion=0.1
T 40400 80400 5 10 0 0 270 0 1
footprint=p0603
T 41000 80900 5 10 1 1 0 0 1
value=0.1u_NPO
}
C 40400 79600 1 0 0 capacitor-1.sym
{
T 40600 80300 5 10 0 0 0 0 1
device=CAPACITOR
T 40600 80100 5 10 1 1 0 0 1
refdes=C3
T 40600 80500 5 10 0 0 0 0 1
symversion=0.1
T 40400 79600 5 10 0 0 270 0 1
footprint=p0603
T 41000 80100 5 10 1 1 0 0 1
value=0.1u_NPO
}
N 41300 80600 42000 80600 4
N 41300 79800 42000 79800 4
N 40400 80600 40200 80600 4
N 40400 79800 40200 79800 4
C 35500 79500 1 0 0 sma.sym
{
T 36500 81200 5 10 1 1 0 0 1
refdes=J1
T 35500 79500 5 10 0 0 0 0 1
footprint=SMA
T 35500 79500 5 10 0 0 0 0 1
value=SMA_right_angle
}
C 37900 79400 1 0 0 gnd-1.sym
N 38000 79700 38000 79800 4
N 38000 79800 38300 79800 4
C 35200 79700 1 0 0 gnd-1.sym
N 35300 80000 35300 80200 4
N 35300 80200 35500 80200 4
N 35500 79500 35500 81300 4
N 35500 79500 36500 79500 4
N 36500 81300 35500 81300 4
C 37400 80400 1 0 0 capacitor-1.sym
{
T 37600 81100 5 10 0 0 0 0 1
device=CAPACITOR
T 37500 80900 5 10 1 1 0 0 1
refdes=C1
T 37600 81300 5 10 0 0 0 0 1
symversion=0.1
T 37400 80400 5 10 0 0 270 0 1
footprint=p0603
T 37800 80900 5 10 1 1 0 0 1
value=0.1u_NPO
}
C 43400 81700 1 0 0 capacitor-1.sym
{
T 43600 82400 5 10 0 0 0 0 1
device=CAPACITOR
T 43600 82200 5 10 1 1 0 0 1
refdes=C4
T 43600 82600 5 10 0 0 0 0 1
symversion=0.1
T 43400 81700 5 10 0 0 270 0 1
footprint=p0603
T 44000 82200 5 10 1 1 0 0 1
value=0.1u
}
N 43100 81900 43400 81900 4
N 43200 81900 43200 81500 4
C 44500 81600 1 0 0 gnd-1.sym
N 44300 81900 44600 81900 4
L 35100 82600 35100 78100 3 0 0 0 -1 -1
L 35100 78100 49800 78100 3 0 0 0 -1 -1
L 35100 82600 49800 82600 3 0 0 0 -1 -1
L 49800 82600 49800 78100 3 0 0 0 -1 -1
C 34000 73800 0 0 0 title-B.sym
C 39500 83200 1 270 0 in-1.sym
{
T 39800 83200 5 10 0 0 270 0 1
device=INPUT
T 39800 83200 5 10 1 1 270 0 1
refdes=3P3V
}
C 42200 81800 1 0 0 inductor-1.sym
{
T 42400 82300 5 10 0 0 0 0 1
device=INDUCTOR
T 42400 82100 5 10 1 1 0 0 1
refdes=FB1
T 42400 82500 5 10 0 0 0 0 1
symversion=0.1
T 42200 81800 5 10 0 0 0 0 1
footprint=p0805
T 42200 81800 5 10 0 0 0 0 1
value=Murata BLM21PG221SN1D
}
T 41100 83400 9 20 1 0 0 0 1
pre-amp module
N 39600 82600 39600 81900 4
N 39600 81900 42200 81900 4
C 45500 80400 1 0 0 resistor-1.sym
{
T 45800 80800 5 10 0 0 0 0 1
device=RESISTOR
T 45700 80700 5 10 1 1 0 0 1
refdes=R2
T 45500 80400 5 10 0 0 0 0 1
footprint=p0603
T 46100 80700 5 10 1 1 0 0 1
value=0
}
C 45500 79300 1 0 0 resistor-1.sym
{
T 45800 79700 5 10 0 0 0 0 1
device=RESISTOR
T 45700 79600 5 10 1 1 0 0 1
refdes=R4
T 45500 79300 5 10 0 0 0 0 1
footprint=p0603
T 46100 79600 5 10 1 1 0 0 1
value=DNL
}
N 45500 80400 45500 80500 4
N 45500 79600 45500 79400 4
N 45500 80800 45500 81000 4
N 45500 80000 45500 79900 4
C 45400 78100 1 270 0 out-1.sym
{
T 45700 78100 5 10 0 0 270 0 1
device=OUTPUT
T 45700 78100 5 10 1 1 270 0 1
refdes=VOCM
}
C 49800 80900 1 0 0 out-1.sym
{
T 49800 81200 5 10 0 0 0 0 1
device=OUTPUT
T 49800 81200 5 10 1 1 0 0 1
refdes=OUT+
}
C 49800 79300 1 0 0 out-1.sym
{
T 49800 79600 5 10 0 0 0 0 1
device=OUTPUT
T 49800 79600 5 10 1 1 0 0 1
refdes=OUT-
}
N 45500 79200 45500 78100 4
C 48100 80900 1 0 0 resistor-1.sym
{
T 48400 81300 5 10 0 0 0 0 1
device=RESISTOR
T 48300 81200 5 10 1 1 0 0 1
refdes=R5
T 48100 80900 5 10 0 0 0 0 1
footprint=p0603
T 48700 81200 5 10 1 1 0 0 1
value=0
}
C 48100 79300 1 0 0 resistor-1.sym
{
T 48400 79700 5 10 0 0 0 0 1
device=RESISTOR
T 48300 79600 5 10 1 1 0 0 1
refdes=R6
T 48100 79300 5 10 0 0 0 0 1
footprint=p0603
T 48700 79600 5 10 1 1 0 0 1
value=0
}
N 46400 81000 48100 81000 4
N 46400 79400 48100 79400 4
N 49000 81000 49800 81000 4
N 49000 79400 49800 79400 4
N 47600 80600 47600 81000 4
N 47600 79700 47600 79400 4
N 47000 80600 47000 81000 4
N 47000 79700 47000 79400 4
N 46400 79700 46400 79900 4
N 46400 79700 47000 79700 4
N 46400 80500 46400 80700 4
N 46400 80700 47000 80700 4
C 38700 83200 1 270 0 in-1.sym
{
T 39000 83200 5 10 0 0 270 0 1
device=INPUT
T 39000 83200 5 10 1 1 270 0 1
refdes=GND
}
C 38700 82200 1 0 0 gnd-1.sym
N 38800 82500 38800 82600 4
C 40700 78500 1 90 0 capacitor-1.sym
{
T 40000 78700 5 10 0 0 90 0 1
device=CAPACITOR
T 40200 78700 5 10 1 1 90 0 1
refdes=C6
T 39800 78700 5 10 0 0 90 0 1
symversion=0.1
T 40700 78500 5 10 0 0 0 0 1
footprint=p0603
T 40200 79100 5 10 1 1 90 0 1
value=0.1u
}
N 40200 80200 40500 80200 4
N 40500 80200 40500 79400 4
C 40400 78200 1 0 0 gnd-1.sym
C 47800 78500 1 90 0 capacitor-1.sym
{
T 47100 78700 5 10 0 0 90 0 1
device=CAPACITOR
T 47300 78500 5 10 1 1 90 0 1
refdes=C7
T 46900 78700 5 10 0 0 90 0 1
symversion=0.1
T 47800 78500 5 10 0 0 0 0 1
footprint=p0603
T 47300 78800 5 10 1 1 90 0 1
value=8p_NPO
}
C 47500 78200 1 0 0 gnd-1.sym
C 47400 81900 1 270 0 capacitor-1.sym
{
T 48100 81700 5 10 0 0 270 0 1
device=CAPACITOR
T 47300 81200 5 10 1 1 90 0 1
refdes=C8
T 48300 81700 5 10 0 0 270 0 1
symversion=0.1
T 47400 81900 5 10 0 0 180 0 1
footprint=p0603
T 47300 81600 5 10 1 1 90 0 1
value=8p_NPO
}
C 47700 82200 1 180 0 gnd-1.sym
C 45500 78600 1 0 0 capacitor-1.sym
{
T 45700 79300 5 10 0 0 0 0 1
device=CAPACITOR
T 45700 79100 5 10 1 1 0 0 1
refdes=C9
T 45700 79500 5 10 0 0 0 0 1
symversion=0.1
T 45500 78600 5 10 0 0 270 0 1
footprint=p0603
T 46100 79100 5 10 1 1 0 0 1
value=0.1u
}
C 46300 78500 1 0 0 gnd-1.sym