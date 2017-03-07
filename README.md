Birthday Reminder
=================

This module helps to send birthday reminder to all DB members. Currently this module allows you to send reminder using email, sms and hangout messages.

Setup:
------

```shell
$ git clone https://github.com/asifpy/python-bdayreminder
$ cd bdayreminder
```

Install Requirements
--------------------
```
- Create your seperate virtual env and activate it
- Install requirements: pip install -r requirements.txt
```

Usage
-----

```shell
$ python3 bdayreminder/manage.py --help

usage: Birthday Reminder [-h]

optional arguments:
  -h, --help            show this help message and exit

        Choices supports the following:
        syncdb              - Creates new sqlite DB with person table
        loadsampledata      - Loads sample data from db/sample_data.py
        loadexceldata       - loads excel data from db/data/yourexcel.xlsx
        runallreminders     - Run reminder for email, sms and hangout
        runemailreminder    - Run reminder with only email
        runsmsreminder      - Run reminder with only sms
        runhangoutreminder  - Run reminder with only hangout message
```

Init DB
-------
Use the below command to create sqlite DB with `Person`.

```shell
$ python3 bdayreminder/manage.py syncdb
```

Load Sample Data
----------------

Update the `bdayreminder/db/loader.py` for your own sample data and then run the below command.

```shell
$ python3 bdayreminder/manage.py loadsampledata
```

Send Email Reminder
-------------------

Run the below command to send Email reminder

```shell
$ python3 bdayreminder/manage.py runemailreminder
```

Send Hangout Reminder
---------------------

Run the below command to send hangout reminder

```shell
$ python3 bdayreminder/manage.py runhangoutreminder
```

Send SMS Reminder
-----------------

Run the below command to send sms reminder

```shell
$ python3 bdayreminder/manage.py runsmsreminder
```


Send all reminders
------------------

Run the below script to send reminders using email, sms and hangout:

```shell
$ python3 bdayreminder/manage.py runallreminders
```

