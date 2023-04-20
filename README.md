# Data Quality check tools for GitHub Actions

Usage:
```
    py dupe_key_check.py {csv filename}
```
Run the above command to check for duplicates in the key-startv-endv columns. If checking for multiple .csv files, separate filenames with a space.

If duplicates are found in any of the csv files, an exit code of 1 will be returned from the python program.