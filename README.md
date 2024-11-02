# Using [Markdown Guide](https://www.markdownguide.org/basic-syntax/)

## TELE6420: Infrastructure Automation and Design Course
### Assignment No. 4 

### Question 1:
1. Create a repository in Bitbucket/GitHub through the GUI.
2. Clone the created repository to your local system.
   - You may need to install Git and configure your account. Refer to the handouts provided by the Professor for setup.
3. On your local system, navigate to the cloned repository and create a file named `readme.md` (if you created your repo with a `readme.md` file, edit that file on your local system).
4. In the `readme.md` file, include the following information in the format shown below (you might need to use Markdown for formatting).
5. Push the changes to the remote repository.

### Question 2:
1. On your local system, inside the repository created in Question 1, add a file `show_time.py`.
2. In `show_time.py`, write Python code to display the current time.
3. Push the newly created `show_time.py` file to the remote master/main branch.
4. Create two additional developer branches in your project, each branched directly from master/main.
   - **TELE6420-Infrastructure Automation Design and Tools**
   - Due Date: November 2nd, 2024
5. Now using the `Developer-1` branch, modify the code to display time and date.
6. As `Developer-2`, modify the code to display time, date, and day.

For submission of Questions 1 and 2, show the CLI commands used with terminal outputs. Also, include screenshots of the commit timeline in Git.

**Note:** Other than creating the Git repo on Bitbucket/GitHub, do not perform any tasks directly through the GUI on Bitbucket/GitHub. All Git tasks should be performed on the local system using the CLI.

### Question 3:
1. Execute the below commands in a Linux terminal in the provided sequence.
2. Explain the executed command (only the first time you execute a new command).
3. Briefly explain what you inferred from the output of each executed command.
4. Answer the inlined questions.

mkdir learn_git
cd learn_git
git status
git init
touch afile.txt
git status
git add afile.txt
git status
git commit -m "first commit"
git log
ifconfig > afile.txt
git diff
git add afile.txt
git commit -m "second commit"
git log
