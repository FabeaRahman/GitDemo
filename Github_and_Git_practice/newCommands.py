
# first go to the desktop folder where you wanna practice and create a new folder
# go to another GitHub account and choose a repo and fork it (copy and download in your github)
# clone the forked repo in your folder and go in it
# check the branch (git remote -v)
# to add upstream
print ("type 'git remote add upstream 'the main person from whom you forked thtas repo link' '")
# again check the branch and create a new feature branch
# change something than add commit and push it
# after creating you have to pull the request in github where you will see a option (compare and pull request)
#===================================
# Stash Practice
# first go to the main branch and change something in any file but don't commit it
print("type 'git stash'")# disappear the changes just made
print(" type 'git stash list' ")# to check the hidden changes
# than go to another branch and again do some changes then add and commit it
# go to the main branch again than get back the first code
print(" type 'git stash pop' ") # again add and commit
#=========Tagging=========
# Lightweight and Annotated tagging
print("type - lightweight 'git tag v1.0' annotated 'git tag -a v1.1 -m 'First release version' '")
# to see all tags
print("type 'git tag' ")
# to see details log and push it
print(" 'git show v1.1 ' to push 'git push origin --tags ' ")
# to see the last commit changes
print("type 'git rebase -i HEAD~3 '")
# to edit the last commit 
print ("git commit --amend")
# to solve the merge conflict 
print ("git mergetool")
###
