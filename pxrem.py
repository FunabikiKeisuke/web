import sys
import re
# function format macro
PX_NUM = 10000
PX_REM= 100
# command line arguments
args = sys.argv
# file open
fr = open(sys.argv[1], 'r')
fw = open(sys.argv[2], 'w')
# file reading
contents = fr.read()
# variable declaration
num = PX_NUM
# unit conversion
for i in range(9999):
    if num == PX_NUM:
        txt = (contents.replace(str(num) + 'px', str(float(num/PX_REM)) + 'rem'))
        num -= 1
    else:
        txt = (txt.replace(str(num) + 'px', str(float(num/PX_REM)) + 'rem'))
        num -= 1
# file writing
fw.write(txt)
# file close
fr.close()
fw.close()
