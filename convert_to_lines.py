#!/usr/local/bin/python
# coding: utf-8
import sys
import svg
import os
from mkdir_p import mkdir_p
import json

if len(sys.argv) < 2:
    print 'requires input folder of svg to convert'
    exit()

lineDir = 'line_svgs'
width, height = (128, 128)


def convert_svg(inputFilename, outputFilename, dataWriter=None):
    mySvg = svg.Svg(inputFilename)
    f = open(outputFilename, 'w')
    f.write('<svg xmlns="http://www.w3.org/2000/svg" >')
    bounds = mySvg.bbox()
    mySvg.translate((-bounds[0].x, -bounds[0].y))
    mySvg.scale(min(width / (bounds[1].x - bounds[0].x), height / (bounds[1].y - bounds[0].y)))
    strokeColor = 'currentcolor'
    fillColor = 'none'
    f.write('<path d="')
    for path in mySvg.flatten():
        for stroke in path.simplify(100, 1):
            data = ''.join(
                ['M{:.2f} {:.2f}'.format(stroke[0].x, stroke[0].y), ' '.join(['L{:.2f} {:.2f}'.format(i.x, i.y) for i in stroke[1:]])])
            f.write(data)
            if dataWriter:
                dataWriter.write(data)
    f.write('" style="stroke: {}; fill: {}"></path>'.format(strokeColor, fillColor))
    f.write('</svg>')
    f.close()
    return data

def convert_dir(oldDir, newDir):
    dat = open('{}.dat'.format(newDir), 'w')
    mkdir_p(newDir)
    for svgFile in os.listdir(oldDir):
        try:
            dat.write('{}: '.format(svgFile))
            convert_svg(os.path.join(oldDir, svgFile), os.path.join(newDir, svgFile), dataWriter=dat)
            dat.write('\n')

        except Exception:
            print 'Could not convert {}'.format(svgFile)

    dat.close()

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
