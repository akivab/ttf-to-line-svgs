#!/usr/bin/env bash
set -e
if [ "$#" -ne 1 ]
then
  echo "specify ttf file"
  exit
fi

filename=$(basename $1)
filename_wo_ext=$(echo "$filename" | cut -f 1 -d '.')
path_wo_ext=$(echo "$1" | cut -f 1 -d '.')
echo $filename
echo $filename_wo_ext
echo $path_wo_ext

GLYPH_DIR=/tmp/glyphs/$filename_wo_ext
echo 'Open($1)' > /tmp/convert.pe
echo 'Generate($1:r + ".svg")' >> /tmp/convert.pe
fontforge -script /tmp/convert.pe $1
./render_glyphs.py $path_wo_ext.svg $GLYPH_DIR
./convert_to_lines.py $GLYPH_DIR
./make_html.py index ./line_svgs/$filename_wo_ext
