#!/usr/local/bin/python
import os
import sys

line_svg_dirname = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'line_svgs')
line_svg_htmlname = 'duplicates.html'
dirs = os.listdir(line_svg_dirname)

html_path = '{}/{}'.format(line_svg_dirname, line_svg_htmlname)
html_fd = open(html_path, 'w')
html_fd.write(open('html_header.txt', 'r').read())
set_of_all = None
for dirname in dirs:
    dirpath = os.path.join(line_svg_dirname, dirname)
    if os.path.isdir(dirpath):
        files = set(os.listdir(dirpath))
        if not set_of_all:
            set_of_all = files
        else:
            set_of_all = set_of_all.intersection(files)
for dup in set_of_all:
    for dirname in dirs:
        dirpath = os.path.join(line_svg_dirname, dirname)
        if os.path.isdir(dirpath):
            html_fd.write('<img src="{}/{}" />'.format(dirpath, dup))
    html_fd.write("<br>\n")
html_fd.close()