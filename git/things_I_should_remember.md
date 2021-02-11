## Use Case 1:
I needed to delete all the changes to one file and one file only

Command: `git checkout *filename*`

## Use Case 2:
I want to review all the actions I've taken on a repo

Command:`git reflog`

## Use Case 3:
I want to revert the changes I made to a file by checking out a version of that file from a different branch

Command: `git checkout [branch] -- [file]`

## Use Case 4:
I want to see just the changes that a commit made.

Command: `git diff COMMIT~ COMMIT`
