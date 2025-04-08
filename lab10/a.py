import psycopg2

config = psycopg2.connect(
    host='localhost', 
    database='postgres',
    user='postgres',
    password='Iman2422&'
)
current = config.cursor()
sql1 = '''
    CREATE TABLE phonebook(
        id INTEGER PRIMARY KEY,
        name VARCHAR(200),
        number VARCHAR(200)
    )
'''

current.execute(sql1)

# final = current.fetchall()
# print(final)

current.close()
config.commit()
config.close()
