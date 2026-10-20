import re
import pcbnew
import pyqrcode


def uuidinit(start=0):
    uuidincref = pcbnew.KIID(start)
    m = re.match(
        "(?P<head>[0-9a-f]{8}-[0-9a-f]{4}-[0-9a-f]{4}-[0-9a-f]{4})-000000000000",
        uuidincref.AsString(),
    )
    uuidreplacestr = m["head"]
    return uuidincref, uuidreplacestr


def uuidreplace(ofilename, uuidreplacestr, replacedby="00000000-0000-0000-0000"):
    with open(ofilename) as f:
        s = f.read()
    s1 = s.replace('"%s' % uuidreplacestr, '"%s' % replacedby)
    with open(ofilename, "w") as f:
        f.write(s1)


def uuidclone(src, dst, uuidinc=0):
    if isinstance(src, pcbnew.KIID):
        srcuuid = src
    elif hasattr(src, "m_Uuid"):
        srcuuid = src.m_Uuid
    elif src is None:
        srcuuid = pcbnew.KIID()
    else:
        exit("unknown uuid")
    for i in range(uuidinc):
        srcuuid.Increment()
    dst.m_Uuid.Clone(srcuuid)


def pcbtext(
    board,
    x,
    y,
    text,
    size=pcbnew.VECTOR2I(1000000, 2000000),
    layer=None,
    hjustify=pcbnew.GR_TEXT_H_ALIGN_CENTER,
    uuidincref=None,
):
    c = pcbnew.PCB_TEXT(board)
    # uuidinc(uuidincref,c)
    uuidclone(src=uuidincref, dst=c, uuidinc=1)
    c.SetPos(pcbnew.VECTOR2I(int(round(x, 10)), int(round(y, 10))))
    c.SetHorizJustify(hjustify)
    if layer is not None:
        c.SetLayer(board.GetLayerID(layer))
    c.SetText(text)
    c.SetTextSize(size)
    board.Add(c)


def qrpoint(center, step):
    xys = []
    xys.append((center.real, center.imag))
    xys.append((center.real, center.imag + step))
    xys.append((center.real + step, center.imag + step))
    xys.append((center.real + step, center.imag))
    xys.append((center.real, center.imag))
    return xys


def pcbfilledrect(board, xys, layer="F.Silkscreen", uuidincref=None):
    c = pcbnew.PCB_SHAPE(board)
    # uuidinc(uuidincref,c)
    uuidclone(src=uuidincref, dst=c, uuidinc=1)
    c.SetShape(pcbnew.SHAPE_T_POLY)
    polyset = pcbnew.SHAPE_POLY_SET()
    linechain = pcbnew.SHAPE_LINE_CHAIN()
    for x, y in xys:
        linechain.Append(int(round(x, 10)), int(round(y, 10)))
    linechain.SetClosed(True)
    polyset.AddOutline(linechain)
    c.SetPolyShape(polyset)
    c.SetFilled(True)
    c.SetWidth(0)
    c.SetLayer(board.GetLayerID(layer))
    board.Add(c)
    return c


def qrgen(stringin, quiet_zone=2):
    t = pyqrcode.create(stringin, error="Q")
    # t.svg('test.svg',scale=1)
    text = [i for i in t.text(quiet_zone).split("\n") if i]
    return text


def qrpcb(
    board,
    stringin,
    x0,
    y0,
    quiet_zone=2,
    stepnm=10 * 25400,
    layer="F.Silkscreen",
    uuidincref=None,
):
    text = qrgen(stringin, quiet_zone)
    # print("QR size %d" % len(text))
    # Checks that we got Version 2 (25x25) plus the quiet zone
    # succeeds with Alphanumeric input mode and error correction level 'Q'
    # Proper overall layout of the QR code in relation to the nearby text
    # on the silkscreen depends on this size being (about) 29.
    assert len(text) == 29
    cs = []
    text.reverse()
    for il, l in enumerate(text):
        for iw, w in enumerate(l):
            center = x0 + 1j * y0 + (iw - 1j * il) * stepnm
            xys = qrpoint(center, stepnm)
            if w == "0":
                p = pcbfilledrect(board, xys, layer=layer, uuidincref=uuidincref)
                uuidclone(src=uuidincref, dst=p, uuidinc=1)
                cs.append(p)
    #                print(iw,il,xys)
    v = pcbnew.PCB_GROUP(board)
    uuidclone(src=uuidincref, dst=v, uuidinc=1)
    for i in cs:
        v.AddItem(i)
    board.Add(v)


if __name__ == "__main__":
    import argparse
    import git
    import sys
    import os

    sys.path.append("./scripts/")
    import gerber

    parser = argparse.ArgumentParser(description=__doc__)
    #    parser.add_argument(dest='project', help='project name (used in saved gerber file name)')
    parser.add_argument(
        "-start", dest="start", type=int, default=1, help="serial number start"
    )
    parser.add_argument(
        "-stop", dest="stop", type=int, default=0, help="serial number stop"
    )
    parser.add_argument("-quiet", dest="quiet", type=int, default=2, help="quiet zone")
    parser.add_argument(
        "-keeppcb", dest="keeppcb", action="store_true", help="keep the pcb file"
    )
    parser.add_argument(
        "-projname", dest="projname", type=str, help="proj name", default="_qrsn"
    )
    parser.add_argument(
        "-outputdir",
        dest="outputdir",
        type=str,
        help="output directory",
        default="qrsngbr",
    )

    clargs = parser.parse_args()

    boardfilename = "%s.kicad_pcb" % clargs.projname
    for sn in range(clargs.start, clargs.stop):
        gitcommit8 = git.Repo(".").head.commit.hexsha[0:8].upper()
        if os.path.isfile(boardfilename):
            board = pcbnew.LoadBoard(boardfilename)
        else:
            board = pcbnew.NewBoard(boardfilename)
        #        qrpcb(board=board,stringin='https://gitlab.com/lbl-boards/zest commit:%s SN:%03d'%(gitcommit8,sn),x0=80000000,y0=-158000000,stepnm=15*25400,layer='B.Silkscreen')
        stringin = ("commit:%s SN:%03d" % (gitcommit8, sn)).upper()
        print(stringin)
        uuidincref, uuidreplacestr = uuidinit(start=0)
        qrpcb(
            board=board,
            stringin=stringin,
            x0=90000000,
            y0=-203000000,
            stepnm=13 * 25400,
            layer="F.Silkscreen",
            quiet_zone=clargs.quiet,
            uuidincref=uuidincref,
        )
        pcbtext(
            board=board,
            x=101000000,
            y=-211000000,
            text="COMMIT:\n%s\nSN:" % (gitcommit8),
            size=pcbnew.VECTOR2I(1500000, 1500000),
            layer="F.Silkscreen",
            hjustify=pcbnew.GR_TEXT_H_ALIGN_LEFT,
            uuidincref=uuidincref,
        )
        pcbtext(
            board=board,
            x=101000000,
            y=-204000000,
            text="%03d" % (sn),
            size=pcbnew.VECTOR2I(5000000, 5000000),
            layer="F.Silkscreen",
            hjustify=pcbnew.GR_TEXT_H_ALIGN_LEFT,
            uuidincref=uuidincref,
        )
        pcbnew.Refresh()
        board.Save(boardfilename)
        uuidreplace(boardfilename, uuidreplacestr, replacedby="00000000-0000-0000-0000")
        gerber.fab(
            pcbfile=boardfilename,
            outputdir=clargs.outputdir,
            gerber=True,
            drill=False,
            bom=False,
            xypos=False,
            keepdateveretc=False,
            debug=False,
            layers=["F.Silkscreen"],
        )
        gerbername = "%s/%s-%s.gbr" % (
            clargs.outputdir,
            clargs.projname,
            "F_Silkscreen",
        )
        gerbersnname = "%s/%s-%s_%03d.gbr" % (
            clargs.outputdir,
            clargs.projname,
            "F_Silkscreen",
            sn,
        )
        os.rename(gerbername, gerbersnname)
        if not clargs.keeppcb:
            for ext in ["pcb", "pro"]:
                os.remove("%s.kicad_%s" % (clargs.projname, ext))
