import sqlite3
import logging


def database_connect():
    sqlite_connection = sqlite3.connect('/home/zero/Рабочий стол/db.db')
    cursor = sqlite_connection.cursor()
    return sqlite_connection, cursor


def database_disconnect(sqlite_connection, cursor):
    sqlite_connection.commit()
    cursor.close()
    sqlite_connection.close()


def create_notification(text, datetime, id):
    sqlite_connection, cursor = database_connect()
    query = f'''INSERT INTO Notifications (body, datetime, user_id)
            VALUES ("{text}", "{datetime}", {id})'''
    cursor.execute(query)
    database_disconnect(sqlite_connection, cursor)


def check_notifications():
    sqlite_connection, cursor = database_connect()
    #query = f'''SELECT * FROM Notification WHERE [datetime] = (SELECT datetime('now', '+1 day'))'''
    query = f'''SELECT * FROM Notifications WHERE [datetime] = (SELECT datetime('now'))'''# OR SELECT datetime('now', '+1 second') or SELECT datetime('now', '-1 second'))'''
    data = cursor.fetchall()
    for i in range(len(data)):
        print(data[i])
    cursor.execute(query)
    database_disconnect(sqlite_connection, cursor)
    return logging.info('checking...')
