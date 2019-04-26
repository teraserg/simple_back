import psycopg2

conn = psycopg2.connect(dbname='mydb', user='admin', password='admin', host='localhost')
cursor = conn.cursor()

cursor.execute("insert into employee (username, surname, email) values ('john','connor','js@company.com');")
conn.commit()

cursor.execute('select * from employee')
records = cursor.fetchall()

print(f'Fetched {cursor}')
for row in records:
    print(row)

cursor.close()
conn.close()
