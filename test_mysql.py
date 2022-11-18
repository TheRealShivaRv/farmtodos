import mysql.connector as connector

config = {
    'user': 'root',
    'password': 'password',
    'host': '127.0.0.1',
    'database': 'farmtodos'
}

def db_conn(callback):
    try:
        conn = connector.connect(**config)    
        cursor = conn.cursor()  
        cursor.execute(callback)

    except connector.Error as error:
        print('Something went wrong:- ', error)

    finally:
        conn.close()  

def create_table_todos():
    db_conn('\
        CREATE TABLE Todos(\
            id INT AUTO_INCREMENT PRIMARY KEY,\
            title VARCHAR(255) NOT NULL,\
            is_done BOOLEAN DEFAULT(false),\
            date_created DATETIME DEFAULT(curtime())\
        );\
    ')
