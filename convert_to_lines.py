#!/usr/local/bin/python
# coding: utf-8
import sys
import svg
import os
from mkdir_p import mkdir_p

if len(sys.argv) < 2:
    print 'requires input folder of svg to convert'
    exit()

lineDir = 'line_svgs'
width, height = (128, 128)


def convert_svg(inputFilename, outputFilename):
    mySvg = svg.Svg(inputFilename)
    f = open(outputFilename, 'w')
    f.write('<svg xmlns="http://www.w3.org/2000/svg" >')
    bounds = mySvg.bbox()
    mySvg.translate((-bounds[0].x, -bounds[0].y))
    mySvg.scale(min(width / (bounds[1].x - bounds[0].x), height / (bounds[1].y - bounds[0].y)))
    strokeColor = 'currentcolor'
    fillColor = 'none'
    for path in mySvg.flatten():
        for stroke in path.simplify(100, 1):
            f.write('<path d="')
            f.write(''.join(
                ['M{} {}'.format(stroke[0].x, stroke[0].y), ' '.join(['L{} {}'.format(i.x, i.y) for i in stroke[1:]])]))
            f.write('" style="stroke: {}; fill: {}"></path>'.format(strokeColor, fillColor))
    f.write('</svg>')
    f.close()


def convert_dir(oldDir, newDir):
    mkdir_p(newDir)
    for svgFile in os.listdir(oldDir):
        try:
            convert_svg(os.path.join(oldDir, svgFile), os.path.join(newDir, svgFile))
        except Exception:
            print 'Could not convert {}'.format(svgFile)


if __name__ == '__main__':
    arg = sys.argv[1]
    filename = os.path.basename(arg)
    if os.path.isdir(arg):
        oldDir = sys.argv[1]
        newDir = '{}/{}'.format(lineDir, filename)
        print 'Saving line glyphs to', newDir
        convert_dir(oldDir, newDir)
    elif os.path.isfile(arg):
        print 'converting svg', arg, 'to file', filename
        convert_svg(arg, filename)
