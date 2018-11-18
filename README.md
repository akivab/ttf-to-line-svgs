ttf to line svg
===============

*Requirements*

[fontforge](https://fontforge.github.io/en-US/), to convert files to SVG format
[svg](https://github.com/akivab/svg), a Python SVG parser (included as submodule)

Explodes a TTF font into a set of SVGs that only use move-to and line-to instructions.

Used in conjunction with the AxiDraw v3 to allow us to write with any font.

Usage:

```
  ./ttf_to_line_svgs.sh <ttf or otf file>
```

The output directory is currently ```line_svgs```, where a directory with 
