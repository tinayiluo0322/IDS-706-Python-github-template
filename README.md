[![CI](https://github.com/nogibjj/python-template/actions/workflows/cicd.yml/badge.svg)](https://github.com/nogibjj/python-template/actions/workflows/cicd.yml)
## Template for Python Projects 

IDS 706 Mini-Project 1

This Python GitHub template includes a `Makefile`, `requirements.txt`, `.devcontainer`, `.gitignore`, `GitHubActions`, and `Readme`.

### Goals

The purpose of this project is to create a Python template to use for later projects in IDS 706 Data Engineering. It sets up an environment on codespaces and uses GitHub Actions to run a Makefile for the following: `make install`, `make test`, `make format`, `make lint`, and `make all`. 

### Overview 
+ `.devcontainer`: define and set up containerized development environments, providing a consistent and isolated workspace for coding and testing applications. It includes a Dockerfile and a devcontainer.json file.
  + `Dockerfile`: set up a development container for Python and optionally Node.js development within Visual Studio Code.
  + `devcontainer.json`: configure and define a development container environment for use with Visual Studio Code's Remote - Containers extension. 

+ `.github/workflows`: a special directory used to store workflow configuration files for GitHub Actions(CI/CD). It includes a ci.yml file, which automates the CI process for a code repository.
  + `ci.yml`: triggers code pushes to the "main" branch, pulls requests to the "main" branch, and allows manual triggering. The workflow includes steps to check out code, install dependencies, perform linting, run tests, and apply code formatting. This automation helps maintain code quality and ensures that code changes are continuously tested and validated.

+ `.gitignore`: specify patterns of files and directories that should be ignored by Git when tracking changes and making commits in a project.
+ `Makefile`: contains a set of rules that define how to automate common development tasks related to a Python project, including installing dependencies, running tests, and maintaining code formatting and code quality standards in a Python project.
+ `requirements.txt`: specify Python package dependencies that are required to run the project.
+ `main.py`: defines a simple function positive_real_number that checks if a given number is greater than 0 and returns True if it is.
+ `test_main.py`: test the functionality of the positive_real_number function defined in the main.py module.
  
### Check Format and Test Approval Image
+ install code `make install'
+ lint code `make lint`
+ format code `make format`
+ test code `make test`
+ code `make all` executes install, lint, format, and test targets

<img width="1133" alt="Screen Shot 2023-09-07 at 7 48 01 PM" src="https://github.com/tinayiluo0322/IDS-706-Python-github-template/assets/143360909/8cfef660-84e3-4dad-a491-ce6fd0d567d8">

<img width="1111" alt="Screen Shot 2023-09-07 at 7 47 21 PM" src="https://github.com/tinayiluo0322/IDS-706-Python-github-template/assets/143360909/cb74e5ac-7d40-413b-b6b6-bef0809f99f6">

### [References](https://github.com/nogibjj/python-template)

