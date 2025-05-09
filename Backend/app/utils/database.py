import oracledb

def get_connection():
    try:
        connection = oracledb.connect(
            user="system",
            password="2003",
            dsn="localhost:1521/xe",
        )
        return connection
    except oracledb.DatabaseError as e:
        print("Database connection failed:", e)
        return None
