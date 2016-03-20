import sqlite3
import datetime
import xlrd


file_path = "/path/to/excel/file.xlsx"

wb = xlrd.open_workbook(file_path)
sheet = wb.sheet_by_index(0)


conn = sqlite3.connect('friends.db', detect_types=sqlite3.PARSE_DECLTYPES)
c = conn.cursor()
c.execute("DROP TABLE IF EXISTS friend")

# Create table
c.execute('''CREATE TABLE
             friend(name text, birth_date date, email text mobile text)''')

if __name__ == '__main__':
    for rownum in range(sheet.nrows):
        # read specific cell from excel
        name = sheet.row_values(rownum)[0]
        date = sheet.row_values(rownum)[1]
        formated_date = datetime.datetime(*xlrd.xldate_as_tuple(date, wb.datemode))
        email = sheet.row_values(rownum)[2]
        mobile = sheet.row_values(rownum)[3]

        actual_date = datetime.date(1987, formated_date.month, formated_date.day)
        c.execute(
            "INSERT INTO friend(name, birth_date, email, mobile) values (?, ?, ?)",
            (name, actual_date, email, mobile)
            )

    conn.commit()
    conn.close()
