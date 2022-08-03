# task 1
## Question 1


GIT WORKFLOW FUNDAMENTALS 

· Working Directory: Repositories created with git init is called working directory.  

· Staging Area： Files are added using git add. It is where files are going to be committed. We can treat staging area as the area between current commit and next commit. 

· Local Repo (head): Files will be add to local repo after git commiting. 

· Remote repo (master): Files can be pushed to remote repo when they are already committed to local repo.  
 
WORKING DIRECTORY STATES: 

· Staged: The changes made to files have been saved to staging area but not committed .

· Modified: There are some changes made to files since last commit and can stage these files which ultimately can be committed.

· Committed: Files have been committed to local repo. 
 
GIT COMMANDS:

· Git add: take modified files in working directory and put them in staging area

· Git commit: take files in staging area and make a permanent snapshot of current state of repository.

· Git push: push committed files to remote repo.

· Git fetch: download contents from remote repo.

· Git merge: changes made in another branch can be added to the main branch when merge happens.

· Git pull: fetch and download files from remote repo and update the local repo.
