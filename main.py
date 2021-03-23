import pyodbc,csv
conn = pyodbc.connect('Driver={SQL Server};'
                      'Server=127.0.0.1,49170;'
                      'Database=base3;'
                      'Trusted_Connection=yes;')

cursor = conn.cursor()
cursor.execute('SELECT code,code,type,code,code FROM base3.dbo.Table_1 WHERE code=111')

with open('//192.168.0.2/UserDisk/CustomData/employee_file.csv', mode='w', encoding='utf-8') as employee_file:
    employee_writer = csv.writer(employee_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL)
    for row in cursor:
        employee_writer.writerow(row)
        print(row)
