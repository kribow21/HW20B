import dbcreds
import mariadb

conn= None
cursor=None

def login_hacker():
    print("Please Login")
    alias_name = input("Enter username:")
    user_password = input("Enter password:")
    cursor.execute("SELECT * FROM hackers WHERE alias=?, password=?",[alias_name,user_password,])
    hacker_login = cursor.fetchone()
    print(hacker_login)
    if(hacker_login.length != 0):
        print('sucess login')
        hacker_choices()
    else:
        print('failed to login')

def hacker_choices():
    print('Select an option:')
    print('1: Enter a new exploit')
    print('2: See all your exploits')
    print('3: See all exploits by others')
    print('4: Exit application')
    hacker_choice = input()
    while hacker_choice.length == 1:
        if(hacker_choice == '1'):
            print('Enter new exploit:')
            exploit = input()
            cursor.execute("INSERT INTO exploits(content) VALUES (?)",[exploit])
            conn.commit()
            print('exploit created')
        elif(hacker_choice == '2'):
            cursor.execute("SELECT * FROM exploits WHERE user_id=")
            exploit_list = cursor.fetchall()
            for ex in exploit_list:
                print(ex)
        elif(hacker_choice == '3'):
            cursor.execute("SELECT * FROM exploits WHERE user_id!=")
            others_exploits = cursor.fetchall()
            for others in others_exploits:
                print(others)
        else:
            print('exited')
            break


try:
    conn=mariadb.connect(
                    user=dbcreds.user,
                    password=dbcreds.password,
                    host=dbcreds.host,
                    port=dbcreds.port,
                    database=dbcreds.database)
    cursor=conn.cursor()
    login_hacker()


except mariadb.DataError: 
    print('Something went wrong with your data')
except mariadb.OperationalError:
    print('Something wrong with the connection')
except mariadb.ProgrammingError:
    print('Your query was wrong')
except mariadb.IntegrityError:
    print('Your query would have broken the database and we stopped it')
except mariadb.InterfaceError:
    print('Something wrong with database interface')
except:
    print('Something went wrong')
finally:
    if(cursor != None):
        cursor.close()
        print('cursor closed')
    else:
        print('no cursor to begin with')
    if(conn != None):   
        conn.rollback()
        conn.close()
        print('connection closed')
    else:
        print('the connection never opened, nothing to close')
