# Description: Convert Titatic dataset to ARFF format
# Author: Hoang NT
# Created: 2016-06-17
# History: v0.0 - File created. Custom for the titatic dataset.

import csv
import sys

def main():
    # Check command format
    if not len(sys.argv) == 2:
        print('\nUsage: %s <filename.csv>' % sys.argv[0])
        return
    # Try to open csv file
    try :
        csv_file = open(sys.argv[1])
    except IOError:
        print('Unable to open [%s], please check file location.' % sys.argv[1])
    else :
        print('Unexpected error:', sys.exc_info()[0])
        raise
    # Read csv file to list
    try :
        csv_data = csv.reader(csv_file)
    except csv.Error :
        print('Error reading CSV file.')
        raise
    data = list(csv_data)

    # TODO: Add a class contains ARFF data structure
    # instead of hard-coding or asking user about datatype.

    # The first line is attributes and the rest is csv
    attr_list = data[0]
    data = data[1:]

    # List of available ARFF datatypes:
    arff_datatypes = ['numeric', 'class', 'string', 'date']

    # Query user for datatype:
    print('\nPlease provide datatype of each attributes:\n (numeric, class, string, date)')
    type_array = []
    for attr_name in attr_list :
        attr_type = 'none'
        while attr_type not in arff_datatypes:
            attr_type = raw_input('\nEnter type for [%s]: ' % attr_name)
        type_array.append(attr_type)



