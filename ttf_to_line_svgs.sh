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

./create_svg.sh $1
./render_glyphs.py $path_wo_ext.svg
./convert_to_lines.sh ./glyph_svgs/$filename_wo_ext
