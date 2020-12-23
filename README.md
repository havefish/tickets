# Tickets
Manages parking lot ticketing system.

# Install
### System Requirements
* Python 3.6+
* Works on any operating system
* Has no third-party dependencies
### Set up
* Clone the repo
* Create a virtual environment and activate it. This is optional, as no third-party dependencies as of yet.
    ```bash
    cd tickets
    python3 -m venv venv
    source venv/bin/activate
    ```
## Usage
Once inside the repo

```bash
python3 -m tickets <commands-file>
```

### Example
Let `commands.txt` be a text file that contains the inputs as below:
```
Create_parking_lot 6
Park KA-01-HH-1234 driver_age 21
Park PB-01-HH-1234 driver_age 21
Slot_numbers_for_driver_of_age 21
Park PB-01-TG-2341 driver_age 40
Slot_number_for_car_with_number PB-01-HH-1234
Leave 2
Park HR-29-TG-3098 driver_age 39
Vehicle_registration_number_for_driver_of_age 21
```

Running the following

```bash
python3 -m tickets commands.txt
```

produces the following output

```
Car with vehicle registration number "KA-01-HH-1234" has been parked at slot number 1
Car with vehicle registration number "PB-01-HH-1234" has been parked at slot number 2
1, 2
Car with vehicle registration number "PB-01-TG-2341" has been parked at slot number 3
2
Slot number 2 vacated, the car with vehicle registration number "PB-01-HH-1234" left the space, the driver of the car was of age 21
Car with vehicle registration number "HR-29-TG-3098" has been parked at slot number 2
KA-01-HH-1234, HR-29-TG-3098
```