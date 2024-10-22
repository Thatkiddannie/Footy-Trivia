import sqlite3

# Connect to the database
conn = sqlite3.connect("eu_leagues.db")
cursor = conn.cursor()

# Step 1: Delete all rows from the 'leagues' table
cursor.execute('DELETE FROM leagues')

# Step 2: Reset the AUTOINCREMENT primary key counter for the 'leagues' table
cursor.execute('DELETE FROM sqlite_sequence WHERE name= "leagues"')

# Commit the transaction after deletion and resetting
conn.commit()

# Step 3: Insert the leagues data again
leagues_to_insert = [
    ('Premier League', 1, 'England'),
    ('Serie A', 2, 'Italy'),
    ('La Liga', 3, 'Spain'),
    ('Bundesliga', 4, 'Germany'),
    ('Ligue 1', 5, 'France'),
    ('Eredivisie', 6, 'Netherlands'),
    ('Liga Portugal Betclic', 7, 'Portugal'),
    ('Pro League', 8, 'Belgium'),
    ('Czech First League', 9, 'Czechia'),
    ('Trendyol Super Lig', 10, 'Turkiye'),
    ('Eliteserien', 11, 'Norway'),
    ('Israeli Premier League', 12, 'Israel'),
    ('Stoiximan Super League', 13, 'Greece'),
    ('Danish Superliga', 14, 'Denmark'),
    ('Austrian Bundesliga', 15, 'Austria'),
    ('Swiss Super League', 16, 'Switzerland'),
    ('Scottish Premiership', 17, 'Scotland'),
    ('Ekstraklasa', 18, 'Poland'),
    ('HNL', 19, 'Croatia'),
    ('Mozzart Bet Superliga', 20, 'Serbia'),
    ('Ukrainian Premier Legaue', 21, 'Ukraine'),
    ('Allsvenskan', 22, 'Sweden'),
    ('NB 1', 23, 'Hungary'),
    ('Cypriot First Division', 24, 'Cyprus'),
    ('Nike liga', 25, 'Slovakia'),
    ('Romanian Super Liga', 26, 'Romania'),
    ('Parva Liga', 27, 'Bulgaria'),
    ('Misli premier League', 28, 'Azerbaijan'),
    ('Russian Premier League', 29, 'Russia'),
    ('PrvaLiga', 30, 'Slovenia'),
# Honourable Mentions
    ('Championship', 31, 'England'),
    ('League One', 32, 'England'),
    ('League Two', 33, 'England'),
    ('South African Premier Division', 34, 'South Africa'),
    ('MLS', 35, 'USA'),
    ('Saudi Pro League', 36, 'Saudi Arabia'),
    ('A-League', 37, 'Australia'),
    ('Liga Profesional de Futbol', 38, 'Argentina'),
    ('Brasileirao Serie A', 39, 'Brazil'),
    ('Canadian Premier League', 40, 'Canada')
]

# Insert multiple rows at once
cursor.executemany('''
    INSERT INTO leagues ('name', rank, 'country')
    VALUES (?, ?, ?)
''', leagues_to_insert)

# Commit the transaction to save the new rows
conn.commit()

# Query and display the data to verify the IDs are reset correctly
cursor.execute('SELECT * FROM leagues')
rows = cursor.fetchall()

for row in rows:
    print(row)

# Close the connection
conn.close()