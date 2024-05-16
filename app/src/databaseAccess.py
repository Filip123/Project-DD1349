import sqlite3

def fetch_session_data():
    database_file = "app/src/database/database.db"
    
    conn = sqlite3.connect(database_file)
    cursor = conn.cursor()

   
    cursor.execute('SELECT session_key, country_key, year FROM session;')

   
    rows = cursor.fetchall()

    rowsDataList = []
    for row in rows:
        session_key = row[0]
        country_key = row[1]
        year = row[2]
        
       
        cursor.execute('SELECT country_name FROM country WHERE country_key=?', (country_key,))
        country_name_row = cursor.fetchone()
        
        if country_name_row:
            country_name = country_name_row[0]
        else:
            print("Country name not found for country key:", country_key)

        rowData = (session_key, country_name, year)
        rowsDataList.append(rowData)

    # Close the cursor and connection
    cursor.close()
    conn.close()
    return rowsDataList

def fetch_country_name(session_key):
    # Path to your database file

    database_file = "app/src/database/database.db"

    # Connect to the SQLite database
    conn = sqlite3.connect(database_file)
    cursor = conn.cursor()

    try:
        # Execute the query to fetch the country name based on session key
        cursor.execute('SELECT country_key FROM session WHERE session_key=?', (session_key,))
        # Fetch the result
        result = cursor.fetchone()
        if result:
            # If result is found, return the country key
            cursor.execute('SELECT country_name FROM country WHERE country_key=?', (result[0],))
            country_name = cursor.fetchone()
        
            if country_name:
                country_name = country_name[0]
            else:
                print("Country name not found for country key:", result[0])

            return country_name
        else:
            # If no result found, return None or raise an exception based on your requirement
            return None  # or raise Exception("Session key not found")
    finally:
        # Close the database connection
        conn.close()

def fetch_start_time(session_key):
    print(session_key)
    database_file =  "app/src/database/database.db"

    conn = sqlite3.connect(database_file)
    cursor = conn.cursor()

    cursor.execute('SELECT date_start FROM session WHERE session_key=?', (session_key,))
    result = cursor.fetchone()
    print("Result in satabase access" , result)
    # Close the cursor and connection
    cursor.close()
    conn.close()
    return result
    
