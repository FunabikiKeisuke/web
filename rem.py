import sys
import re
# function format macro
REM_MAX = 100 # until 100rem
FLOAT_REM = 1.0 # 2rem to 2.0rem
REM_MIN = 0.1 # from 0.1rem
REM_CHANGE = 10 # 2.0rem to (2.0/REM_CHANGE)rem
# command line arguments
args = sys.argv
# file open
fr = open(sys.argv[1], 'r')
fw = open(sys.argv[2], 'w')
# file reading
contents = fr.read()
# variable declaration
num = REM_MAX
# format conversion
for i in range(REM_MAX):
    if num == REM_MAX:
        txt = (contents.replace(' ' + str(num) + 'rem', ' ' + str(float(num/FLOAT_REM)) + 'rem'))
        txt = (contents.replace(':' + str(num) + 'rem', ': ' + str(float(num/FLOAT_REM)) + 'rem'))
        txt = (contents.replace(' -' + str(num) + 'rem', ' -' + str(float(num/FLOAT_REM)) + 'rem'))
        txt = (contents.replace(':-' + str(num) + 'rem', ': -' + str(float(num/FLOAT_REM)) + 'rem'))
        num -= 1
    else:
        txt = (txt.replace(' ' + str(num) + 'rem', ' ' + str(float(num/FLOAT_REM)) + 'rem'))
        txt = (txt.replace(':' + str(num) + 'rem', ': ' + str(float(num/FLOAT_REM)) + 'rem'))
        txt = (txt.replace(' -' + str(num) + 'rem', ' -' + str(float(num/FLOAT_REM)) + 'rem'))
        txt = (txt.replace(':-' + str(num) + 'rem', ': -' + str(float(num/FLOAT_REM)) + 'rem'))
        num -= 1
        print(num)
# variable declaration
num = REM_MIN
# unit conversion
for i in range(10000):
    if num == REM_MIN:
        txt = (txt.replace(str(round(num, 2)) + 'rem', str(round((num/REM_CHANGE), 3)) + 'rem'))
        num += 0.01
        round(num, 2)
    else:
        txt = (txt.replace(str(round(num, 2)) + 'rem', str(round((num/REM_CHANGE), 3)) + 'rem'))
        num += 0.01
        round(num, 2)
        print(round(num, 2))
# file writing
fw.write(txt)
# file close
fr.close()
fw.close()
