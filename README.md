Birthday Reminder
=================

This module helps to send birthday reminder to all DB members. Currently this module allows you to send reminder using email, sms and hangout messages.

Setup:
------

```shell
$ git clone https://github.com/asifpy/birthday_reminder.git 
$ cd bdayreminder
```

Install Requirements
--------------------
```
- Create your seperate virtual env and activate it
- Install requirements: pip install -r requirements.txt
```

Init DB
-------
Use the below command to create sqlite DB with `Person`.

```
python bdayreminder/db/makedb.py
```

Load Sample Data
----------------

Update the `bdayreminder/db/sample_data.py` for your own sample data and then run below command script to load.

```
python bdayreminder/db/sample_data.py
```


