import dbcreds
import mariadb

try:
    conn=mariadb.connect(
                    user=dbcreds.user,
                    password=dbcreds.password,
                    host=dbcreds.host,
                    port=dbcreds.port,
                    database=dbcreds.database)
    cursor=conn.cursor()
    print('all good')
    cursor.close()
    conn.close()
except:
    print('something went wrong')