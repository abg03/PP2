import psycopg2

config = psycopg2.connect(
    host='localhost', 
    database='postgres',
    user='postgres',
    password='Iman2422&'
)

current = config.cursor()


sql = '''
    UPDATE phonebook 
    SET number = %s
    WHERE name=%s
'''

current.execute(sql, ('87772121111', 'Darina'))




current.close()
config.commit()
config.close