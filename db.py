import mysql.connector
import logging

def init_db():
    conn = mysql.connector.connect(host='mysqldb', # importante pois dentro da rede o serviço vai ter seu proprio IP
                                         user='root',
                                         password='p@ssw0rd1')
    with conn.cursor() as cursor:
        #
        cursor.execute("DROP DATABASE IF EXISTS logs")
        cursor.execute("CREATE DATABASE logs")
    print('Database criada com sucesso')

    execute_query("DROP TABLE IF EXISTS requests")
    execute_query('''CREATE TABLE requests (
                        input_x INTEGER,
                        pred_y INTEGER
                    )''')

        
    logging.warning('Tabela criada com sucesso')
    conn.close()

def execute_query(sql):
    conn = mysql.connector.connect(host='mysqldb', # importante pois dentro da rede o serviço vai ter seu proprio IP
                                        database='logs',
                                        user='root',
                                        password='p@ssw0rd1')
    cursor = conn.cursor()
    cursor.execute(sql)
    conn.commit() ### Notice the statement: mydb.commit(). It is required to make the changes, otherwise no changes are made to the table.
    cursor.close()
    conn.close()
    logging.warning(f'Query {sql} executada')



def store_log(request_dict):
    logging.warning(f'Inserindo log')
    x = int(request_dict['input_x'])
    y = int(request_dict['pred_y'])
    logging.warning(execute_query(f"INSERT INTO requests VALUES ({x},{y})") )

def get_log():
    conn = mysql.connector.connect(host='mysqldb', # importante pois dentro da rede o serviço vai ter seu proprio IP
                                        database='logs',
                                        user='root',
                                        password='p@ssw0rd1')
    myresult = []
    with conn.cursor() as cursor:
        cursor.execute("SELECT * FROM requests")
        myresult = cursor.fetchall()
        logging.warning(myresult)
    # pos processamento simples 
    response = []
    for t in myresult:
        response.append({'input_x':t[0],'pred_y':t[1]})
    
    return response