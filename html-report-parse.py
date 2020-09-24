from html.parser import HTMLParser
import os
import pandas as pd
import functools

'''
Decorators
'''

def remove_nbsp(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):

        original_result = func(*args, **kwargs)
        modified_result = original_result.replace("&nbsp;", "")

        return modified_result

    return wrapper

def remove_extra_space(func):

    @functools.wraps(func)
    def wrapper(*args, **kwargs):

        modified_result = func(*args, **kwargs)
        while modified_result.count("  ") > 0:
            modified_result = modified_result.replace("  ", " ")

        return modified_result
    
    return wrapper

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

def remove_characters(doc_text: str, *args: str, **kwargs: str) -> str:
    cleaned_text = doc_text

    for kwarg in kwargs:
        if "space" in kwarg:
            cleaned_text = cleaned_text.replace(kwargs[kwarg], " ")

    for arg in args:
        cleaned_text = cleaned_text.replace(arg, "")
    
    return cleaned_text

@remove_nbsp
@remove_extra_space
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

# Clean extra characters
# cleaned_contents = remove_characters(report_contents,"<colgroup>", space_1="   ", space_2="  ", space_3="&nbsp;")

# Read data into pandas dataframe
data = pd.read_html(report_contents, header=0)
print(data[0].head())