"""
    Description: Checks for duplicate key and start-end pairs

    Author: William Lee

"""
import csv
import sys

def scan_file(filename:str, dupe_list)->int:
    CSV_PATH = filename
    KEY_COLUMN_NAME = 'key_id'
    START_COLUMN_NAME = 'startv'
    END_COLUMN_NAME = 'endv'

    key_check = {}
    dupe_count = 0

    with open(CSV_PATH, 'r', encoding='utf-8') as csv_in:
        csv_reader = csv.DictReader(csv_in, delimiter=',')
        line_count = 1
        for row in csv_reader:
            # Check if key exists
            key_value = row[KEY_COLUMN_NAME]
            start_value = row[START_COLUMN_NAME]
            end_value = row[END_COLUMN_NAME]
            if key_value in key_check:
                # Check if same start and end exists and is a duplicate
                if [start_value, end_value] in key_check[key_value]['start_end']:
                    key_check[key_value]['line'].append(line_count)
                    dupe_count += 1
                else:
                    key_check[key_value]['start_end'].append([start_value, end_value])
            else:
                key_check.update({
                    key_value: {
                        'start_end': [[start_value, end_value]],
                        'line': []
                    }
                })
            line_count += 1

        # Creates a list of only duplicates with their indices
        for key, value in key_check.items():
            if value['line']:
                if dupe_list.get(key):
                    append_index = dupe_list[key].append(value['line'])
                    dupe_list.update({
                        key: append_index
                    })
                else:
                    dupe_list.update({
                        key: value['line']
                    })

        print(f'[{filename}]')
        print('Number of duplicates found:', dupe_count)
    return dupe_count

dupe_count = 0
dupe_list = {}

csv_files = sys.argv[1:]
for file in csv_files:
    # Input settings
    dupe_count += scan_file(file, dupe_list)

if dupe_count > 0:
    print('List of duplicated keys and their index:', dupe_list)
    sys.exit("Program terminated: Duplicates found in dataset.")
