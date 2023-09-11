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

## Use Case 5:
I want to see the full history of a file including renames.

Command: `git log --follow {name_of_file}`

## Use Case 6:
I want to only apply the changes from a specific set of files from a stash

Command: `git checkout stash@{0} -- <filename>`
