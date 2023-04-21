"""
    Description: Checks for duplicate key and start-end pairs

    Author: William Lee

"""
import csv
import sys

check_failed_flag = False
failed_files = []
csv_files = sys.argv[1:]
for file in csv_files:
    # Input settings
    CSV_PATH = f'{file}'
    KEY_COLUMN_NAME = 'key_id'
    START_COLUMN_NAME = 'startv'
    END_COLUMN_NAME = 'endv'

    key_check = {}
    overlap_count = 0
    overlap_list = {}

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
                    overlap_count += 1
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
                if overlap_list.get(key):
                    append_index = overlap_list[key].append(value['line'])
                    overlap_list.update({
                        key: append_index
                    })
                else:
                    overlap_list.update({
                        key: value['line']
                    })

        print('[', file, ']')
        print('Number of version overlaps found:', overlap_count)

    if overlap_count > 0:
        print('List of overlapping versions for keys and their index:', overlap_list)
        check_failed_flag = True
        failed_files.append(file)

if check_failed_flag:
    print(f"Run ended. Version overlap found in dataset(s): {failed_files}")
    sys.exit("Checks failed.")
else:
    print("Run ended. No overlaps found: Checks passed.")
