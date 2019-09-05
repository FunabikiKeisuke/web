import sys
import re
# function format macro
PX_NUM = 1000
PX_VW = 3.84
# command line arguments
args = sys.argv
# file open
fr = open(sys.argv[1], 'r', encoding="utf8", errors='ignore')
fw = open(sys.argv[2], 'w', encoding="utf8", errors='ignore')
# file reading
contents = fr.read()
# variable declaration
num = PX_NUM
# unit conversion
for i in range(999):
    if num == PX_NUM:
        txt = (contents.replace(str(num) + 'px', str(float(num/PX_VW)) + 'vw'))
        num -= 1
    else:
        txt = (txt.replace(str(num) + 'px', str(float(num/PX_VW)) + 'vw'))
        num -= 1
# file writing
fw.write(txt)
# file close
fr.close()
fw.close()
