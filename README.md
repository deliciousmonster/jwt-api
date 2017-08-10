# Project Template

The Project Template is a base template used to create a new nio project with the recommended files and file structure.

## How to Use

  You can clone this project template using the nio command line interface (CLI) or git.

### Clone Using the nio CLI

You can create a new project directory with the nio-cli

  ```
    pip3 install nio-cli
    nio new <new_project_name>
  ```

### Clone Using git

To clone the project template using git
1. Clone the template and initialize the submodules which contain the blocks.
    ```
    git clone --depth=1 https://github.com/nioinnovation/project_template.git <new_project_name>
    cd <new_project_name>
    git submodule update --init --recursive
    ```
1. Remove the tracking link to the original template repository and reset ownership to yourself
    ```
    git remote remove origin
    git commit --amend --reset-author -m "Initial Commit"
    ```
To push your project to GitHub (or another remote repository)

1. Create a new online repository for your project.
1. You will be given a unique URL for your new repository. Copy this URL to your clipboard.
1. In your local repository, from the command line, set the remote tracking information to the new repository.
    ```
    git remote add origin <new_project_repo_URL>
    ```
1. Push to a branch (usually `master`).
    ```
    git push --set-upstream origin master
    ```

## File Reference

**blocks**<br>A directory that contains block types, as submodules. The project template comes with a few of the most commonly used block types. Block types can be added and removed, either from the block library or your own block types that you develop.

**etc**
<br>A folder containing project configurations and scripts.

**service_tests**<br>A submodule for service tests that includes `NioServiceTestCase` and other tools for service testing.

**tests**<br>A folder for your tests with an example set up for a service test.

**Dockerfile**<br>A script to create a docker image of the project. Docker can be used to ease deployment.

**docker-compose.yml**<br>A file that can be used with Docker to configure your application so that all its dependencies can be started with a single command.

**nio.conf**<br>A file that contains the nio project configuration. Default values are shown.

**nio.env**<br>A file containing environment variables for the project. If this file contains secrets, you will want to add it to the `.gitignore`.
