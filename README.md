## StackOverflow-v1 
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)  [![PRs Welcome](https://img.shields.io/badge/PRs-welcome-brightgreen.svg?style=flat-square)](http://makeapullrequest.com)  [![Build Status](https://travis-ci.com/jonathanmusila/StackOverflow-v1.svg?branch=develop)](https://travis-ci.com/jonathanmusila/StackOverflow-v1)  [![Coverage Status](https://coveralls.io/repos/github/kwanj-k/storemanager-v2/badge.svg?branch=ch-readme-%23161404824)]

## Summary

StackOverflow-lite is a platform in which users can as questions and get answers. 

## NOTE
* The project is managed using PivotalTracker board [click here](https://www.pivotaltracker.com/n/projects/2202775)

* THe documentation is not yet created

* The app is not yet hosted on heroku

* Some of the app's adge cases are not yet catched

## Getting Started 

* Clone the repository: 

    ```https://github.com/jonathanmusila/StackOverflow-v1.git```

* Navigate to the cloned repo.

### Prerequisites

```
1. Python3
2. Flask
3. Postman
```

## Installation 
After navigating to the cloned repo;

Create a virtualenv and activate it ::

    create a directory 
    cd into the directory
    virtualenv -p python3 venv
    source venv/bin activate

Install the dependencies::

    pip install -r requirements.txt 

## Configuration

After activativating the virtualenv, run:

    ```
    export FLASK_APP="run.py"
    export FLASK_DEBUG=1
    export FLASK_ENV="development"

    ```
## Running Tests
Run:
```
pytest --cov-report term-missing --cov=app
```

### Testing on Postman
Fire up postman and start the development server by:
  ```
  $ flask run
  ```