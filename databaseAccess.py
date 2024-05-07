import sqlite3
def fetch_rows_with_country_name(database_file):
    
    conn = sqlite3.connect(database_file)
    cursor = conn.cursor()

   
    cursor.execute('SELECT session_key, country_key FROM session;')

   
    rows = cursor.fetchall()

    
    for row in rows:
        print(row)
        session_key = row[0]
        country_key = row[1]
        
       
        cursor.execute('SELECT country_name FROM country WHERE country_key=?', (country_key,))
        country_name_row = cursor.fetchone()
        
        if country_name_row:
            country_name = country_name_row[0]
            print(country_name)
        else:
            print("Country name not found for country key:", country_key)

    # Close the cursor and connection
    cursor.close()
    conn.close()

fetch_rows_with_country_name("database.db")