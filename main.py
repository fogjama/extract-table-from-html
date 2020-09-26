import sys
from html_report_parse import process_report

if len(sys.argv) > 1:
    process_report(sys.argv[1])
else:
    print('Syntax error: main.py <filename>')