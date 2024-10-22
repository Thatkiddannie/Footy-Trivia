import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('coaches_db.sqlite')
cursor = conn.cursor()

# Create the eu_coaches table
cursor.execute('''CREATE TABLE IF NOT EXISTS eu_coaches (
                    id INTEGER PRIMARY KEY AUTOINCREMENT,
                    name TEXT NOT NULL,
                    nationality TEXT NOT NULL,
                    teams_countries_coached TEXT NOT NULL,
                    active BOOLEAN NOT NULL)''')

# Insert data (example data, you can add more entries)
coaches_data = [
    ("Sir Alex Ferguson", "Scottish", "Manchester United, Aberdeen", False),
    ("Pep Guardiola", "Spanish", "Barcelona, Bayern Munich, Manchester City", True),
    ("José Mourinho", "Portuguese", "Chelsea, Real Madrid, Manchester United, Tottenham, Roma", True),
    ("Johan Cruyff", "Dutch", "Ajax, Barcelona", False),
    ("Carlo Ancelotti", "Italian", "AC Milan, Chelsea, Real Madrid, Bayern Munich", True),
    ("Arrigo Sacchi", "Italian", "AC Milan, Italy", False),
    # Add more coaches as needed
]

# Insert all data into the table
cursor.executemany('''INSERT INTO eu_coaches (name, nationality, teams_countries_coached, active)
                      VALUES (?, ?, ?, ?)''', coaches_data)

# Commit changes
conn.commit()

# Example query to retrieve all coaches
cursor.execute('SELECT * FROM eu_coaches')
all_coaches = cursor.fetchall()

# Print the results
for coach in all_coaches:
    print(coach)

# Close the connection
conn.close()
