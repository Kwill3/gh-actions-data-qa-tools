# Data Quality check tools for GitHub Actions

## Using the Python file:
Run the python file using the code below
```
    py dupe_key_check.py {csv filename}
```
The python file checks for duplicates in the key-startv-endv columns. If checking for multiple .csv files, separate filenames with a space.
If duplicates are found in any of the csv files, an exit code of 1 will be returned from the python program.

## Using workflows in GitHub Actions:
Clone the .github/workflows/data_quality_check.yml to integrate checks into GitHub Actions.
Use this as a job to stop merging of a PR when test fails by setting branch protection rules in GitHub to 'require status checks to pass before merging'.
It is also worth to protect the branch to be merged into by requiring a PR before merging so that status checks cannot be bypassed.