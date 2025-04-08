import psycopg2
import csv
config = psycopg2.connect(
    host='localhost', 
    database='postgres',
    user='postgres',
    password='Iman2422&'
)

current = config.cursor()
a = []
with open('1.csv') as f:
    read = csv.reader(f)
    for i in read:
        a.append(i)

sql1 = '''
    INSERT INTO phonebook VALUES (%s, %s, %s)
'''

for i in a:
    current.execute(sql1, i)

current.close()
config.commit()
config.close()
