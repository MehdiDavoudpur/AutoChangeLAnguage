import sqlite3

# Connect to the database (or create it if it doesn't exist)
conn = sqlite3.connect('app_titles.db')

# Create a cursor object to execute SQL queries
cursor = conn.cursor()

table_name = 'app_titles'
col1_name = 'app_title'

# Create a table
cursor.execute(f'''CREATE TABLE IF NOT EXISTS {table_name}
                  (id INTEGER PRIMARY KEY, {col1_name} TEXT)''')


# Insert data into the table
def insert(title):
    cursor.execute(f"INSERT INTO {table_name} ({col1_name}) VALUES (?)", (title,))
    conn.commit()


def show():
    cursor.execute(f"SELECT {col1_name} FROM {table_name}")

    rows_list = []
    for row in cursor.fetchall():
        rows_list.append(row[0])
    return rows_list


def delete(record):
    # Execute the DELETE statement
    cursor.execute(f'DELETE FROM {table_name} WHERE app_title=?', (record,))

    # Commit the transaction
    conn.commit()


def delete_all():
    # Execute the DELETE statement
    cursor.execute(f'DELETE FROM {table_name}', ())

    # Commit the transaction
    conn.commit()
