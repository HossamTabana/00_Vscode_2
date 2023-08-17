# Comprehensive Git, GitHub, and GitLab Commands Guide

## Basic Git Commands:

1. `git init`
   - **Description**: Initialize a new Git repository.
   - **Example**: `git init`

2. `git clone [url]`
   - **Description**: Clone (or download) a repository from an existing URL.
   - **Usage**: `git clone https://github.com/user/repo.git`
   - **Example**: `git clone https://github.com/octocat/Hello-World.git`

3. `git add [file]`
   - **Description**: Add a file to the staging area.
   - **Usage**: `git add README.md`
   - **Example**: `git add .` (This command adds all files to the staging area.)

4. `git commit -m "[commit message]"`
   - **Description**: Commit changes in the staging area.
   - **Usage**: `git commit -m "Initial commit"`
   - **Example**: `git commit -m "Fixed typo"`

5. `git status`
   - **Description**: Show the status of changes as untracked, modified, or staged.
   - **Example**: `git status`

6. `git log`
   - **Description**: Show a log of all commits.
   - **Example**: `git log`

## Branching & Merging:

1. `git checkout -b [branch_name]`
   - **Description**: Create and switch to a new branch.
   - **Usage**: `git checkout -b feature-xyz`
   - **Example**: `git checkout -b feature-login`

2. `git merge [branch_name]`
   - **Description**: Merge changes from one branch into another.
   - **Usage**: `git merge feature-xyz`
   - **Example**: `git merge feature-login`

3. `git remote add origin [url]`
   - **Description**: Connect your local repository to a remote one.
   - **Usage**: `git remote add origin https://github.com/user/repo.git`
   - **Example**: `git remote add origin https://github.com/octocat/Hello-World.git`

## Extended Git Commands:

### Stashing & Cleaning:

1. `git stash`
   - **Description**: Temporarily saves changes that are not yet committed.
   - **Example**: `git stash`

2. `git stash list`
   - **Description**: List all stashed changesets.
   - **Example**: `git stash list`

3. `git stash apply`
   - **Description**: Apply the changes from the latest stashed changeset.
   - **Example**: `git stash apply`

4. `git clean`
   - **Description**: Remove untracked files from your working directory.
   - **Example**: `git clean -f`

### Remote Repositories:

1. `git remote`
   - **Description**: List all remotes for the current repository.
   - **Example**: `git remote`

2. `git remote add [alias] [url]`
   - **Description**: Add a remote repository.
   - **Usage**: `git remote add origin https://github.com/user/repo.git`
   - **Example**: `git remote add upstream https://github.com/otheruser/repo.git`

3. `git remote rm [alias]`
   - **Description**: Remove a remote repository.
   - **Usage**: `git remote rm origin`
   - **Example**: `git remote rm upstream`

4. `git fetch [remote]`
   - **Description**: Download objects and refs from another repository.
   - **Usage**: `git fetch origin`
   - **Example**: `git fetch upstream`

5. `git push origin [branch_name]`
   - **Description**: Upload local branch commits to the remote repository.
   - **Usage**: `git push origin feature-xyz`
   - **Example**: `git push origin feature-login`

### Rewriting History:

1. `git rebase [branch]`
   - **Description**: Reapply commits on top of another base tip.
   - **Usage**: `git rebase master`
   - **Example**: `git rebase feature-branch`

2. `git reset`
   - **Description**: Reset current HEAD to the specified state.
   - **Usage**: `git reset --hard HEAD~1`
   - **Example**: `git reset --soft HEAD~2`

3. `git revert [commit_id]`
   - **Description**: Revert some existing commits.
   - **Usage**: `git revert a123b4c`
   - **Example**: `git revert a123b4c`

4. `git cherry-pick [commit_id]`
   - **Description**: Apply the changes introduced by some existing commits.
   - **Usage**: `git cherry-pick a123b4c`
   - **Example**: `git cherry-pick d567e8f`

### Tagging:

1. `git tag`
   - **Description**: List all tags.
   - **Example**: `git tag`

2. `git tag [tag_name]`
   - **Description**: Create a new tag.
   - **Usage**: `git tag v1.0`
   - **Example**: `git tag v2.0`

3. `git push --tags`
   - **Description**: Push tags to remote.
   - **Example**: `git push --tags`

## GitLab Specific Commands:

1. `git clone [url]`
   - **Description**: Clone a repository from GitLab.
   - **Usage**: `git clone https://gitlab.com/user/repository.git`
   - **Example**: `git clone https://gitlab.com/johndoe/my-repo.git`

### GitLab Merge Requests:

1. `git checkout -b feature-branch`
   - **Description**: Create and switch to a new feature branch.
   - **Example**: `git checkout -b my-feature`

2. `git push origin feature-branch`
   - **Description**: Push the new feature branch to GitLab.
   - **Example**: `git push origin my-feature`

### GitLab CI/CD:

1. `gitlab-runner exec [executor] [.gitlab-ci.yml job]`
   - **Description**: Execute a GitLab CI job locally using GitLab runner (helpful for debugging).
   - **Usage**: `gitlab-runner exec shell test_job`

## GitHub Specific Commands:

1. `gh auth login`
   - **Description**: Authenticate with a GitHub instance.
   - **Example**: Follow the interactive prompts after running the command.

2. `gh issue list`
   - **Description**: List and filter issues in a repository.
   - **Example**: `gh issue list`

3. `gh issue view [issue_number]`
   - **Description**: View an issue in the browser or terminal.
   - **Usage**: `gh issue view 123`

4. `gh pr list`
   - **Description**: List and filter pull requests in a repository.
   - **Example**: `gh pr list`

5. `gh pr view [pr_number]`
   - **Description**: View a pull request in the browser or terminal.
   - **Usage**: `gh pr view 123`

6. `gh pr checkout [pr_number]`
   - **Description**: Check out a pull request locally.
   - **Usage**: `gh pr checkout 123`

7. `gh gist create [file...]`
   - **Description**: Create a new GitHub gist.
   - **Usage**: `gh gist create hello.py`

8. `gh gist list`
   - **Description**: List your gists.
   - **Example**: `gh gist list`

9. `gh repo create [name]`
   - **Description**: Create a new repository on GitHub.
   - **Usage**: `gh repo create my-new-repo`

10. `gh repo fork [repository]`
    - **Description**: Fork an existing repository.
    - **Usage**: `gh repo fork user/repo`

Always refer to the official documentation of [Git](https://git-scm.com/docs), [GitHub CLI](https://cli.github.com/manual/), and [GitLab](https://docs.gitlab.com) for more details. Ensure you have necessary permissions for operations and follow best practices.
