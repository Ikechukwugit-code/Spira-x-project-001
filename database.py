import sqlite3
from app.config import DATABASE_NAME


def get_connection(database_name=None):
    if database_name is None:
        database_name=DATABASE_NAME
    return sqlite3.connect(DATABASE_NAME)


def initialize_database():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(""" CREATE TABLE IF NOT EXISTS business_requests (id INTEGER PRIMARY KEY AUTOINCREMENT, name TEXT NOT NULL, industry TEXT NOT NULL,problem TEXT NOT NULL, location TEXT NOT NULL,budget INTEGER NOT NULL,category TEXT NOT NULL)""")
    connection.commit()
    connection.close()

def save_request(request,category):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(""" INSERT INTO business_requests (name, industry,problem,location,budget,category)
    VALUES (?,?,?,?,?,?)""", (request.name,request.industry,request.problem,request.location,request.budget,category))
    request_id = cursor.lastrowid
    connection.commit()
    connection.close()
    return request_id

def get_all_requests():
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(""" SELECT id,name,industry,problem,location,budget,category FROM business_requests ORDER BY id DESC """)
    rows = cursor.fetchall()
    connection.close()
    requests = []
    for row in rows:
        requests.append({"id": row[0],"name": row[1],"industry": row[2],"problem": row[3],"location": row[4],"budget": row[5],"category": row[6]})
    return requests

def get_request_by_id(request_id):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(""" SELECT id,name,industry,problem,location,budget,category FROM business_requests WHERE id = ? """, (request_id,))

    row  = cursor.fetchone()
    connection.close()

    if row is None:
        return None

    return {
        "id": row[0],
        "name": row[1],
        "industry": row[2],
        "problem": row[3],
        "location": row[4],
        "budget": row[5],
        "category": row[6]
    }
def update_request(request_id,request, category):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(""" UPDATE business_requests SET name = ?, industry = ?, problem = ?, location = ?,budget = ?, category = ? WHERE id = ?""", (
        request.name,
        request.industry,
        request.problem,
        request.location,
        request.budget,
        category,
        request_id
    ))
    updated = cursor.rowcount
    connection.commit()
    connection.close()
    return updated > 0

def delete_request(request_id):
    connection = get_connection()
    cursor = connection.cursor()
    cursor.execute(""" DELETE FROM business_requests WHERE id = ? """, (request_id,))
    deleted = cursor.rowcount

    connection.commit()
    connection.close()
    return deleted


