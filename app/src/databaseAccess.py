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

fetch_session_data()