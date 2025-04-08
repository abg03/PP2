import psycopg2

config = psycopg2.connect(
    host='localhost', 
    database='postgres',
    user='postgres',
    password='Iman2422&'
)
id = input()
name = input()
number = input()
current = config.cursor()
sql1 = '''
    INSERT INTO phonebook VALUES (%s, %s, %s)
'''

current.execute(sql1, (id, name, number))

# final = current.fetchall()
# print(final)

current.close()
config.commit()
config.close()
