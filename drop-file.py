import sys
import os
from html_report_parse import process_report
from test import test_me

if len(sys.argv) > 0:
    orig_stdout = sys.stdout

    script_loc = os.path.dirname(os.path.abspath(__file__))

    with open(os.path.join(script_loc,'report_output.txt'), 'a') as f:
        sys.stdout = f

        for i in range(1,len(sys.argv)):
            process_report(sys.argv[i])

        sys.stdout = orig_stdout
