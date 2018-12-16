## Continous Integration with Travis
The following steps can be followed to automatically run tests on a GitHub repository, every time a new commit is made.

1. Sign in with GitHub at [travis-ci.com](https://travis-ci.com/).
2. Accept authorization of Travis CI.
3. Once re-directed to GitHub, click "Accept" and choose the repository for CI.
4. Creat a file named ".travis.yml" inside the repository. 
5. Inside the ".travis.yml" file, the programing language and it's version must be defined. The test code that need to be run must also be defined. In the following example, Python 3.5 is used, and all 'unittest' tests are executed. 

```
language: python
python:
  - 3.5
script:
- python -m unittest
```

## Travis Build Status Badge
The following steps can be followed to add a travis build status badge to the README.md of a GitHub repository.

1. Click the ![Build](https://img.shields.io/badge/build-passing-brightgreen.svg) icon on the Travis CI repository page.
2. Select the required branch.
3. Select the type as 'Markdown'.
4. Copy the generated Markdown code and paste in the README.md file of the GitHub repository to display the Travis CI build status.

## Code Coverage Badge using Codecov
The following steps can be followed to add a code coverage badge to the README.md of a GitHub repository.

1. Append the .travis.yml file with the following. The name of the test code ('test_code.py' in the example below) must be specified under 'script'
```
install:
  - pip install codecov
script:
  - coverage run test_code.py
after_success:
  - codecov
```
2. Sign up with GitHub at [codecov.io](https://codecov.io/).
3. Choose the repository, and go to 'Settings'.
4. Click 'Badge' and copy the Markdown code.
5. Paste the Markdown code in the README.md file of the GitHub repository to display the code coverage

## Custom Badges
Custome badges could be made at [shields.io](https://shields.io/#/). The following Markdown code could be used with the '< SUBJECT >', '< STATUS >', and '< COLOR >' specified as required. 
```
https://img.shields.io/badge/<SUBJECT>-<STATUS>-<COLOR>.svg
```
