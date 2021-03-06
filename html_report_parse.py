import os
import pandas as pd
import functools

'''
Decorators
'''

def replace_with_space(to_remove):

    def decorator(func):
        @functools.wraps(func)
        def wrapper(*args, **kwargs):

            result = func(*args, **kwargs)
            while result.count(to_remove) > 0:
                result = result.replace(to_remove, " ")

            return result

        return wrapper

    return decorator


'''
Functions
'''

@replace_with_space("  ")
@replace_with_space("&nbsp;")
def read_file(filename: str) -> str:

    rfile = open(filename, 'r')
    file_contents = rfile.read()
    rfile.close()

    return file_contents

'''
Variables
'''

fname = "./samples/Job 29 BARKER & STONEHOUSE OPEN, Step 1.htm"

'''
Main
'''

def process_report(fname):
    # Open file to process and store in variable
    report_contents = read_file(fname)

    # Read data into pandas dataframe
    data = pd.read_html(report_contents, header=0)
    print(data[0].head())


if __name__=='__main__':
    process_report(fname)