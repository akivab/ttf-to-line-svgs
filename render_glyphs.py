#!/usr/local/bin/python
# coding: utf-8
import os
import sys
from mkdir_p import mkdir_p
from xml.dom import minidom

DEFAULT_GLYPH_DIR = 'glyph_svgs'

if len(sys.argv) < 2:
    print 'specify svg input'
    exit(1)

doc = minidom.parse(sys.argv[1])

if len(sys.argv) == 3:
    outputDir = sys.argv[2]
else:
    outputDir = '{}/{}'.format(DEFAULT_GLYPH_DIR, os.path.basename(sys.argv[1]).split('.')[0])

print 'Saving glyphs to', outputDir

mkdir_p(outputDir)
glyphs = doc.getElementsByTagName('glyph')


format = '''
<svg xmlns="http://www.w3.org/2000/svg">
<path d="{}" transform="scale(1, -1)" style="fill: currentcolor;"></path>
</svg>'''

for glyph in glyphs:
    name = glyph.attributes['glyph-name'].value
    f = open('{}/{}.svg'.format(outputDir, name), 'w')
    if 'd' in glyph.attributes.keys():
        f.write(format.format(glyph.attributes['d'].value))
    f.close()
