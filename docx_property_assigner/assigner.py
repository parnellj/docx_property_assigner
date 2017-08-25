from docx import Document
from pptx import Presentation

from datetime import datetime
import os
import csv

"""
This script requires the following packages:
    python-docx
    python-pptx

This script takes a CSV file, 'property_reassignment', which contains the following
data for each document to be recast:

    variable            data type

    filepath	        string
    filename	        string
    filetype	        string
    author	            string
    category	        string
    comments	        string
    content_status	    string
    created	            datetime
    identifier	        string
    keywords	        string
    language	        string
    last_modified_by    string
    last_printed	    datetime
    modified	        datetime
    revision	        integer
    subject	            string
    title	            string
    version	            string

Where 'filepath' is the full Windows filepath, filename, and extension, and 'datetime'
values are entered as 'yyyy-mm-dd'.
    To preserve the current value, enter 'Keep'
    To set the value to blank, enter '' (blank cell).
        Blank dates resolve to 1970-01-01, 12:00:00 AM UTC.
"""

OUTPATH = os.path.join('.', 'outputs')
INPATH = os.path.join('.', 'inputs')

# Read the CSV file
with open(os.path.join(INPATH, 'property_reassignment.csv')) as f:
    reader = csv.reader(f)
    headers = reader.next()
    valtypes = {headers[i]:v for i, v in enumerate(reader.next())}
    entries = [{headers[i]:v for i, v in enumerate(row)} for row in reader]

# Iterate through the CSV file
for entry in entries:

    # Skip a document if its type is not '.docx' or '.pptx'
    if entry['filetype'] == '.docx':
        d = Document(entry['filepath'])
    elif entry['filetype'] == '.pptx':
        d = Presentation(entry['filepath'])
    else:
        continue

    for variable_name, value in entry.iteritems():
        # Skip (retain) values labeled 'Keep'
        if value == 'Keep': continue

        # Special treatment for datetime and integer values per python-docx
        if valtypes[variable_name] == 'datetime':
            try:
                value = datetime.strptime(value, '%Y-%m-%d')
            except ValueError:
                value = datetime(1970, 1, 1, 0, 0, 0)
        elif valtypes[variable_name] == 'integer':
            value = int(value)
        else: value = value.encode('utf-8')

        setattr(d.core_properties, variable_name, value)

    d.save(os.path.join(OUTPATH, entry['filename']))

    print 'finished'
