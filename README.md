# Tickets
Manages parking lot ticketing system.

## System Requirements
* Python 3.6+
* Works on any unix like operating systems
* Has no third-party dependencies

## Set up
* Clone the repo
* Create a virtual environment and activate it. This is optional, as no third-party dependencies as of yet.

```bash
git clone https://github.com/havefish/tickets.git
cd tickets
python3 -m venv venv
source venv/bin/activate
```

## Usage
The program can accept input from many different sources on the command line. All of the following will work.

```bash
# filename arguments
python3 -m tickets commands_1.txt commands_2.txt ...

# input redirection
python3 -m tickets < commands.txt

# piping from another command
cat commands.txt | python3 -m tickets

# read from stdin
python3 -m tickets
```

The program reads and processes inputs line by line and produces one line per input line. 
If there is an error with a certain line, the output will be of the format `ERROR: <reason>`, then the code moves on to process further lines.

A sample session is shown below

```bash
python3 -m tickets

leave 2
ERROR: cannot perform 'leave' before creating parking lot
create_parking_lot 2
Created parking of 2 slots
leave 2
ERROR: slot 2 is empty
park xxx 
ERROR: invalid usage for command 'park'
park xxx driver_age 12
Car with vehicle registration number "xxx" has been parked at slot number 1
park yyy driver_age 14
Car with vehicle registration number "yyy" has been parked at slot number 2
leave 1
Slot number 1 vacated, the car with vehicle registration number "xxx" left the space, the driver of the car was of age 12
park zzz driver_age 15
```

## Test Coverage

* To run all the tests
    
    ```
    python3 -m unittest tests/test_*
    ```

* Current test coverage report

    ```Name                   Stmts   Miss  Cover
    ------------------------------------------
    tests/test_cmds.py        15      0   100%
    tests/test_main.py        11      0   100%
    tests/test_models.py      72      0   100%
    tests/test_views.py       20      0   100%
    tickets/__init__.py        0      0   100%
    tickets/__main__.py       28      4    86%
    tickets/cmds.py           14      0   100%
    tickets/models.py         40      0   100%
    tickets/views.py          12      0   100%
    ------------------------------------------
    TOTAL                    212      4    98%
    ```

## Design
* The implementaion follows functional programming principles of localizing IO to the broundary of the system and maximizing the number of pure functions.

    The `__main__` module take an input stream, processes it and produces to stdout. The processing code constitues majority (98%, as evident from the above coverage report) of the whole code; it consists of pure functions and is fully tested.

* The implementaion trades space efficiency for better performance; it will take comparatively more memory but all required operations are O(1):
    
    * finding the next available slot closest to the entrance (by using a heap)
    * aggregations based on age, car registration number (by maintaining in-memory indices)

* The code is easily extensible. Adding one more command involves the following:
    * add an entry to `cmds.CMDS` dict
    * add a method in the `models.ParkingLot` class
    * add a corresponding view function in `views.py`
    * the plumbing is already taken care of.
