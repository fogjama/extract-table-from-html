import sys
from html_report_parse import process_report

if len(sys.argv) == 2:
    # print('Process file: ' + str(sys.argv))
    process_report(sys.argv[1])
elif len(sys.argv) > 2:
    filename = './samples/'
    for i in range(1,len(sys.argv)):
        filename += sys.argv[i]
        filename += ' '
    process_report(filename)
    # print('Process file: ' + filename)
else:
    print('Syntax error: main.py <filename>')