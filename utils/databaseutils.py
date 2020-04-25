from dotenv import load_dotenv

load_dotenv()
ver = '0.1.0'


def connectToSQLDB():
    import os
    import mysql.connector as sqldb
    password = os.getenv('DB_PASSWORD')
    return sqldb.connect(user='root', password=password, database='team22demand', port=6022, buffered=True)


def getCustomerIDByCredentials(username):
    sqlConnection = connectToSQLDB()
    cursor = sqlConnection.cursor(buffered=True)

    statement = 'SELECT custid FROM customers WHERE username = %s OR email = %s'
    print(statement)
    print((username, username,))
    cursor.execute(statement, (username, username,))
    custid = cursor.fetchone()

    cursor.close()
    sqlConnection.close()

    return custid


def storeOrder(orderData):
    sqlConnection = connectToSQLDB()
    cursor = sqlConnection.cursor(buffered=True)

    statement = 'INSERT INTO orders VALUES (Null, %s, %s, %s, %s)'
    cursor.execute(statement, orderData)
    orderID = cursor.lastrowid
    sqlConnection.commit()

    cursor.close()
    sqlConnection.close()

    return orderID


def getOrderID(data):
    sqlConnection = connectToSQLDB()
    cursor = sqlConnection.cursor(buffered=True)

    statement = 'SELECT orderid FROM orders WHERE custid = %s AND date_ordered = %s'
    cursor.execute(statement, data)
    orderid = cursor.fetchone()[0]

    cursor.close()
    sqlConnection.close()

    return orderid
