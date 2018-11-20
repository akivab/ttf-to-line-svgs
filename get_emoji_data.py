import codepoints
import sys
if len(sys.argv) != 3:
    print 'provide file and emoji'
    exit()

filename = sys.argv[1]
c = sys.argv[2]
svgfile = hex(tuple(codepoints.from_unicode(c.decode('utf-8')))[0]).upper().replace('0X', 'u') + '.svg'
print 'looking for', svgfile
for line in open(filename, 'r').readlines():
    if svgfile in line:
        print line.split(':')[1].strip()
