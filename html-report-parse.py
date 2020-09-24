from html.parser import HTMLParser
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
Classes
'''

class ReportHTMParser(HTMLParser):
    def handle_starttag(self, tag, attrs):
        if "table" in tag:
            print("Table ")
            for attr in attrs:
                print("attr:", attr)
            # print("New table")
        elif "tr" in tag:
            print("New row: ")
            for attr in attrs:
                print("attr:", attr)
        # elif "td"  in tag:
        #     print("New Cell")

    def handle_endtag(self, tag):
        pass

    def handle_data(self, data):
        # print(data)
        pass


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

fname = "./samples/Job 29 BARKER & STONEHOUSE OPEN modified.htm"

'''
Main
'''

# Open file to process and store in variable
report_contents = read_file(fname)


# Read data into pandas dataframe
data = pd.read_html(report_contents, header=0)
print(data[0].head())