#!/usr/local/bin/python
# coding: utf-8
import sys
import os
import errno
from xml.dom import minidom

GLYPH_DIR = 'glyph_svgs'
def mkdir_p(path):
    try:
        os.makedirs(path)
    except OSError as exc:  # Python >2.5
        if exc.errno == errno.EEXIST and os.path.isdir(path):
            pass
        else:
            raise
1
if len(sys.argv) < 2:
    print 'specify svg input'
    exit(1)
doc = minidom.parse(sys.argv[1])
outputDir = sys.argv[2] if len(sys.argv) == 3 else '{}/{}'.format(GLYPH_DIR, os.path.basename(sys.argv[1]).split('.')[0])
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
