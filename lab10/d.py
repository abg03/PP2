import psycopg2

config = psycopg2.connect(
    host='localhost', 
    database='postgres',
    user='postgres',
    password='Iman2422&'
)

current = config.cursor()


sql = '''
    SELECT * FROM phonebook ORDER BY name DESC
'''

sql2 = '''
    SELECT * FROM phonebook ORDER BY id DESC
'''

current.execute(sql2)
final = current.fetchall()
print(final)
current.close()
config.commit()
config.close()