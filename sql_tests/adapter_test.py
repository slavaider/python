import psycopg2
from psycopg2.extras import RealDictCursor, execute_values

if __name__ == '__main__':
    connection = psycopg2.connect(dbname='test_database', user='postgres', password='admin')  # host,port default
    cursor = connection.cursor()
    cursor.execute('DROP TABLE IF EXISTS super_heroes,traffic_light;')
    connection.commit()
    cursor.execute("""CREATE TABLE super_heroes
                (
                 hero_id serial PRIMARY KEY,
                 hero_name varchar ,
                 strength int
                );""")
    # строго нельзя
    # cur.execute('INSERT INTO super_heroes(hero_name,strength) VALUES (%s,%s)' % ('super_man', 100))
    cursor.execute('INSERT INTO super_heroes(hero_name,strength) VALUES (%s,%s);', ('super_man', 100))
    cursor.execute("""INSERT INTO super_heroes(hero_name,strength)
                    VALUES (%(name)s,%(strength)s);""", {'name': 'Green Arrow', 'strength': 50})
    cursor.execute("""INSERT INTO super_heroes(hero_name,strength)
                        VALUES (%(name)s,%(strength)s);""", {'name': 'Flash', 'strength': 999})
    connection.commit()
    cursor.execute("""CREATE TABLE traffic_light(
                   traffic_id serial PRIMARY KEY,
                   light text);
                   """)
    cursor.execute("INSERT INTO traffic_light(light) VALUES (%s);", ('red',))
    cursor.execute("SELECT * FROM super_heroes")
    one_line = cursor.fetchone()
    print(one_line)
    other_lines = cursor.fetchall()
    for i in other_lines:
        print(i)
    connection.commit()
    cursor.close()
    connection.close()

    with psycopg2.connect(dbname='test_database', user='postgres', password='admin') as connection:
        with connection.cursor(cursor_factory=RealDictCursor) as cursor:
            execute_values(cursor, 'INSERT INTO traffic_light(light) VALUES %s', [('green',), ('blue',)])
            cursor.execute('SELECT * FROM traffic_light')
            record = cursor.fetchall()
            print(record)
            print(record[0]['light'])
    connection = psycopg2.connect(dbname='test_database', user='postgres', password='admin')
    with connection:
        with connection.cursor() as cursor:
            cursor.execute("""UPDATE super_heroes SET strength = %s WHERE hero_name  = %s""", (90, 'super_man'))
    with connection:
        with connection.cursor() as cursor:
            cursor.execute("""SELECT * FROM super_heroes""")
            record = cursor.fetchall()
            for i in record:
                print(i)
    connection.close()
