# Phishing Domain Checker API

This guide explains how to use the **Phishing Domain Checker**.
It consists of a backend server built with Flask and a MySQL database to store and query phishing domains. 

---

## **Overview**
The Phishing Domain Checker API allows users to:
**View** all known phishing domains.
**Check** if a specific domain is a phishing site.
**Add** a new phishing domain to the database.
**Remove** a domain from the database.

---

## **Setting up the backend**

### 1. Create Configuration File
Create a file named **config.py** to store your database credentials:
```python
USER = "root"
PASSWORD = "Enter_your_password"
HOST = "localhost"
DATABASE = "phishing_checker"

```
### 2. Set up the database
- Ensure that your MySQL server is running. 
- Ensure your database is set up with the necessary tables and data from the db_utils file.

### 3. Install required packages
- Install the required Python packages (mysql-connector-python requests) so it connects with MySQL.

### 4. Start the Flask API
- Start the Flask API server you should see http://127.0.0.1:5000 you can also visit http://127.0.0.1:5000/domains to view the data. 

### 5. Test the API 
- Test the API using unittest to check if the API works.

### 6. Use the Command-line interface
- Run the client-side

Now the API is ready to use!


