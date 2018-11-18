# coding: utf-8
import sys
import svg

width, height = (128, 128)
if len(sys.argv) < 3:
    print 'usage: simplify <svg old> <svg new>'
    exit()
mySvg = svg.Svg(sys.argv[1])
f = open(sys.argv[2], 'w')
f.write('<svg xmlns="http://www.w3.org/2000/svg" >')
bounds = mySvg.bbox()
mySvg.translate((-bounds[0].x, -bounds[0].y))
mySvg.scale(min(width / (bounds[1].x - bounds[0].x), height / (bounds[1].y - bounds[0].y)))
path = mySvg.flatten()[0].simplify(100, 1)
strokeColor = 'currentcolor'
fillColor = 'white'
for path in mySvg.flatten():
    for stroke in path.simplify(100, 1):
        f.write('<path d="')
        f.write(''.join(['M{} {}'.format(stroke[0].x, stroke[0].y), ' '.join(['L{} {}'.format(i.x, i.y) for i in stroke[1:]])]))
        f.write('" style="stroke: {}; fill: {}"></path>'.format(strokeColor, fillColor))
f.write('</svg>')
f.close()


