[![License: GPL v3](https://img.shields.io/badge/License-GPLv3-blue.svg)](https://www.gnu.org/licenses/gpl-3.0) [![Python 3.5](https://img.shields.io/badge/python-3.5-red.svg)](https://www.python.org/downloads/release/python-350/) [![PEP8](https://img.shields.io/badge/code%20style-pep8-orange.svg)](https://www.python.org/dev/peps/pep-0008/) [![PEP8](https://img.shields.io/badge/code%20framework-unittest-lightgrey.svg)](https://docs.python.org/3/library/unittest.html)

|**Service**|**Master**|**Devel**|
|:------------- |:------------- |:----- |
|CI status|[![Build Status](https://travis-ci.com/hkhbrus/AST-Project.svg?branch=master)](https://travis-ci.com/hkhbrus/AST-Project)|[![Build Status](https://travis-ci.com/hkhbrus/AST-Project.svg?branch=devel)](https://travis-ci.com/hkhbrus/AST-Project)|
|Test Coverage|[![codecov](https://codecov.io/gh/hkhbrus/AST-Project/branch/master/graph/badge.svg)](https://codecov.io/gh/hkhbrus/AST-Project)|[![codecov](https://codecov.io/gh/hkhbrus/AST-Project/branch/devel/graph/badge.svg)](https://codecov.io/gh/hkhbrus/AST-Project)|

# Object List Merger

The project involves the development of a program to merge input from mutiple sensors. To be more specific, each sensor is expected to provide a tuple list of the objects it perceives, where each tuple holds the object's name, id, and the confidence percentage with which the name of the object was determined. The objective is to merge these lists into a single list of all of the unique objects (based on the object ids) that were perceived, along with the most likely name of the object and the confidence with which the object is classified.

## Getting Started

These instructions will get you a copy of the project up and running on your local machine for development and testing purposes. See deployment for notes on how to deploy the project on a live system.

### Prerequisites

Python 3\
Numpy

### Installing

Run the following command on the terminal to install Git on a Linux (Ubuntu/Debian) system.
```
sudo apt-get install git
```
On the terminal, run the following command to clone the repository
```
git clone https://github.com/hkhbrus/AST-Project.git
```
Execute the following command on the terminal to run the [object_merger_sample.py](object_merger_sample.py) file. If everything is in order, the code should run without any errors.
```
python3 object_merger_sample.py
```

## Running the tests

The automated tests will be run by Travis CI whenever a new commit is made to the main GitHub repository. On a local repository, the following command can run on a terminal inside the repository to execute all the test cases.
```
python3 object_merger_test.py
```

### Break down into end to end tests

All of the testcases (Sensor input and the corresponding expected outputs) can be found tabulated in the [testcases.csv](testcases.csv) file.

## Deployment

The ["object_merger.py"](object_merger.py) file contains all the classes required to carry out an object list merger. The classes in the "object_merger.py" file can be imported from another python script in the same directory using the following line of code.
```
from object_merger import *
```
The code below provides an example of how the classes and methods in the "object_merger.py" file could be used carry out an object list merger on two sensor inputs. The input must be provided in the form of a tuple list, where each tuple represents an object and consists of the object's name(type string), number(type int), confidence(type int). An "ObjectListMerger" object could be created with the tuple lists from the sensors provided as the input parameters. The "combined_tuple_list" method could then be call on the "ObjectListMerger" object to return the merged object list as a list of tuples.
```
sensor_1 = [('knife',1, 99), ('scissor', 2, 65), ('spoon', 3, 33), ('spoon', 4, 80), ('keys', 5, 95)]
sensor_2 = [('knife',1, 55), ('scissor', 2, 95), ('fork', 3, 99), ('spoon', 4, 99), ('keys', 5, 95) ]
actual = ObjectListMerger(sensor_1,sensor_2).combined_tuple_list()
print ('Input sensor readings:\n' , sensor_1 , '\n' , sensor_2)
print ('Obtained merged result:\n' , actual, '\n')
```

## Authors

* **Heruka Andradi**
* **Carlo Wiesse**

## License

This project is licensed under the GNU General Public License v3.0
