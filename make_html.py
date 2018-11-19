#!/usr/local/bin/python
import os
import sys

HEADER = '''
<style>
img {
  width: 256px;
  height: auto
}
</style>

'''

line_svg_dirname = os.path.join(os.path.dirname(os.path.realpath(__file__)), 'line_svgs')


def generate_duplicates_file():
    line_svg_htmlname = 'duplicates.html'
    dirs = os.listdir(line_svg_dirname)

    html_path = '{}/{}'.format(line_svg_dirname, line_svg_htmlname)
    html_fd = open(html_path, 'w')
    html_fd.write(HEADER)
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


def generate_index_files(forDir=None):
    dirs = os.listdir(line_svg_dirname)
    for dirname in dirs:
        if forDir and dirname != forDir:
            continue
        dirpath = os.path.join(line_svg_dirname, dirname)
        if os.path.isdir(dirpath):
            html_path = '{}/{}.html'.format(line_svg_dirname, dirname)
            html_fd = open(html_path, 'w')
            html_fd.write(HEADER)
            for filename in sorted(os.listdir(dirpath)):
                html_fd.write('<img src="{}/{}" />'.format(dirpath, filename))
            html_fd.close()
            print 'generated index file {}'.format(html_path)


def print_usage():
    print 'usage: ./make_html.py <index|dups>'
    exit()


if __name__ == '__main__':
    if len(sys.argv) == 1:
        print_usage()
    if sys.argv[1] == 'index':
        dirname = sys.argv[2] if len(sys.argv) == 3 else None
        generate_index_files(forDir=dirname)
    elif sys.argv[1] == 'dups':
        generate_duplicates_file()
    else:
        print_usage()
