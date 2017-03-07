import argparse

from bdayreminder.actions import (
    syncdb,
    loadsampledata,
    loadexceldata,
    runallreminders,
    runemailreminder,
    runsmsreminder,
    runhangoutreminder
)

ACTIONS = {
    'syncdb': syncdb,
    'loadsampledata': loadsampledata,
    'loadexceldata': loadexceldata,
    'runallreminders': runallreminders,
    'runemailreminder': runemailreminder,
    'runsmsreminder': runsmsreminder,
    'runhangoutreminder': runhangoutreminder
}


def choicesDescriptions():
    return """
        Choices supports the following:
        syncdb              - Creates new sqlite DB with person table
        loadsampledata      - Loads sample data from db/sample_data.py
        loadexceldata       - loads excel data from db/data/yourexcel.xlsx
        runreminder         - Run reminder for email, sms and hangout
        runemailreminder    - Run reminder with only email
        runsmsreminder      - Run reminder with only sms
        runhangoutreminder  - Run reminder with only hangout message
    """


def main():
    parser = argparse.ArgumentParser(
        "Birthday Reminder",
        formatter_class=argparse.RawTextHelpFormatter,
        epilog=choicesDescriptions()
    )
    parser.add_argument('action', choices=ACTIONS.keys())

    args = parser.parse_args()
    action = ACTIONS[args.action]
    action()


if __name__ == "__main__":
    main()
