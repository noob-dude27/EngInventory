set your root project folder to EngInventory then please run:
    python -m pip install -e . 

so that you can edit the project files and import stuff locally.
took me a while to figure out.

-Ezra

NOTES:
please clone the repo in VSCode by using the repo's main link:
    https://github.com/noob-dude27/EngInventory

how to use git/github commands:
to publish your own changes:
    create new branch: git branch 'new_branch'
    switch to branch: git switch 'new_branch'
    add changes: git add .
    commit to new_branch: git commit -m "your_message"
    push to new_branch: git push -u origin 'new_branch'
    create pull request & merge pull request (through github)

to update your local main branch in your computer:
    switch to your main branch: git switch 'main'
    update local main branch: git pull origin 'main'

to delete new branch:  git branch -d 'new_branch' (LOCAL)

clean up remote references: git fetch --prune
