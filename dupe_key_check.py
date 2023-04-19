"""
    Description: Checks for duplicate key and start-end pairs

    Author: William Lee

"""
import csv

# Input settings
CSV_PATH = './test.csv'
KEY_COLUMN_NAME = 'key_id'
START_COLUMN_NAME = 'startv'
END_COLUMN_NAME = 'endv'

key_check = {}
dupe_count = 0
dupe_list = {}

with open(CSV_PATH, 'r', encoding='utf-8') as csv_in:
    csv_reader = csv.reader(csv_in, delimiter=',')
    line_count = 0
    key_index = start_index = end_index = None
    for row in csv_reader:
        if line_count == 0:
            for i, items in enumerate(row):
                if items == KEY_COLUMN_NAME:
                    key_index = i
                elif items == START_COLUMN_NAME:
                    start_index = i
                elif items == END_COLUMN_NAME:
                    end_index = i
        else:
            # Check if key exists
            key_value = row[key_index]
            start_value = row[start_index]
            end_value = row[end_index]
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

    print('Number of duplicates found:', dupe_count)
    print('List of duplicated keys and their index:', dupe_list)
