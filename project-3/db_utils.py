"""
This is the Database utility functions for the phishing domain checker API.
In this file you will find:
- Connection to the Mysql database
- Fetching, adding and removing the phishing domains.
- Handling database connection errors.
"""

import mysql.connector
from config import USER, PASSWORD, HOST, DATABASE

class DbConnectionError(Exception):
    pass

def _connect_to_db():
    """Establishes a connection to the database
    returns the connection object"""

    try:
        db_connection = mysql.connector.connect(
            host=HOST,
            user=USER,
            password=PASSWORD,
            auth_plugin='mysql_native_password',
            database=DATABASE
        )
        print ("Connected to DB successfully.")
        return db_connection
    except mysql.connector.Error as e:
        raise DbConnectionError(f"Database connection failed: {str(e)}")

def get_all_domains():
    #Fetching all phishing domains from the database.
    db_connection = None
    try:
        db = _connect_to_db()
        cur = db.cursor ()
        print ("Fetching all phishing domains.") # Debugging

        query = """SELECT * FROM phishing_domains"""
        cur.execute(query)
        result = cur.fetchall()

        cur.close()

        return result

    except Exception:

        raise DbConnectionError("Failed to read data from DB")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection is closed.")

def check_domain (domain):
    #Checks if a domain exists in the phishing database.
    db_connection = None
    try:
        db_connection = _connect_to_db()
        cur = db_connection.cursor()
        print (f"Checking if {domain} exists in the database") # debugging

        query = "SELECT * FROM phishing_domains WHERE domain = %s"
        cur.execute(query, (domain,))
        result = cur.fetchone()

        cur.close()
        return result

    except Exception as e:
        raise DbConnectionError(f"Failed to check domain: {str(e)}")

    finally:
        if db_connection:
            db_connection.close()
            print("DB connection closed.")

def add_domain (domain, reported_by):
    #Adds a new phishing domain to the database.
    db_connection = None
    try:
        db_connection= _connect_to_db()
        cur = db_connection.cursor()
        print(f"Adding domain: {domain}")

        query = """INSERT INTO phishing_domains (domain, reported_by, report_date) 
                 VALUES (%s, %s, NOW())"""
        cur.execute(query, (domain, reported_by,))

        db_connection.commit()
        cur.close()
        return "Domain added successfully"

    except Exception as e:
        raise DbConnectionError(f"Failed to add domain:{str(e)}")
    finally:
        if db_connection:
            db_connection.close()
            print("DB connection closed.")

def remove_domain (domain_id):
    #removes a phishing domain from the database by ID.
    db_connection = None
    try:
        db_connection= _connect_to_db()
        cur = db_connection.cursor()
        print(f"Removing domain with ID: {domain_id}")

        query = "DELETE FROM phishing_domains WHERE id = %s"
        cur.execute(query, (domain_id,))
        db_connection.commit()

        cur.close()
        return "Domain successfully removed."

    except Exception as e:
        raise DbConnectionError(f"Failed to remove domain:{str(e)}")
    finally:
        if db_connection:
            db_connection.close()
            print("DB connection closed.")


if __name__=="__main__":
    print("Testing DB CONNECTION")
    print(get_all_domains())




