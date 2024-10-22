import sqlite3

# Connect to SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect("eu_teams.db")
cursor = conn.cursor()

# Function to create league tables and insert teams
def create_league_table(league_name, teams):
    # Sort the teams alphabetically before inserting
    teams.sort()

    # Create a table for the league with an auto-incrementing ID
    cursor.execute(f'''
        CREATE TABLE IF NOT EXISTS "{league_name}" (
            id INTEGER PRIMARY KEY AUTOINCREMENT,
            name TEXT NOT NULL
        )
    ''')

    # Clear existing data to avoid duplicates
    cursor.execute(f'DELETE FROM "{league_name}"')
    conn.commit()

    # Reset the auto-increment counter (for SQLite)
    cursor.execute(f'DELETE FROM sqlite_sequence WHERE name="{league_name}"')
    conn.commit()

    # Insert each team into the league table (which is already sorted)
    for team in teams:
        cursor.execute(f'INSERT INTO "{league_name}" (name) VALUES (?)', (team,))
    
    # Commit the transaction
    conn.commit()

    # Query and display the teams ordered by ID (which corresponds to alphabetical order)
    cursor.execute(f'SELECT * FROM "{league_name}" ORDER BY id ASC')
    league_sorted = cursor.fetchall()

    print(f"\n{league_name.replace('_', ' ')} Teams (24/25 Season):")
    for team in league_sorted:
        print(f"{team[0]} Team: {team[1]}")

# Teams for the 2024/25 season
premier_league_teams = [
    'Arsenal', 'Aston Villa', 'Bournemouth', 'Brentford', 'Brighton & Hove Albion',
    'Chelsea', 'Crystal Palace', 'Everton', 'Fulham', 'Ipswich', 'Leicester', 'Liverpool',
    'Manchester City', 'Manchester United', 'Newcastle United', 'Nottingham Forest',
    'Southampton', 'Tottenham Hotspur', 'West Ham United', 'Wolverhampton Wanderers'
]

serie_a_teams = [
    'AC Milan', 'Atalanta', 'Bologna', 'Cagliari', 'Empoli',
    'Fiorentina', 'Genoa', 'Inter Milan', 'Juventus', 'Lazio',
    'Lecce', 'Monza', 'Napoli', 'Roma', 'Salernitana',
    'Sassuolo', 'Torino', 'Udinese', 'Verona', 'Sampdoria'
]

la_liga_teams = [
    'Alaves', 'Almeria', 'Athletic Bilbao', 'Atletico Madrid', 'Barcelona',
    'Cadiz', 'Celta Vigo', 'Deportivo Alaves', 'Getafe', 'Girona',
    'Granada', 'Las Palmas', 'Mallorca', 'Osasuna', 'Rayo Vallecano',
    'Real Betis', 'Real Madrid', 'Real Sociedad', 'Sevilla', 'Valencia',
    'Villarreal'
]

bundesliga_teams = [
    'Augsburg', 'Bayern Munich', 'Bayer Leverkusen', 'Borussia Dortmund', 'Borussia Monchengladbach',
    'Eintracht Frankfurt', 'Freiburg', 'Hoffenheim', 'Koln', 'Mainz',
    'RB Leipzig', 'Union Berlin', 'VfB Stuttgart', 'Werder Bremen', 'Wolfsburg',
    'Darmstadt', 'Heidenheim'
]

ligue_1_teams = [
    'Paris Saint-Germain', 'Marseille', 'Monaco', 'Lyon', 'Lille',
    'Rennes', 'Lens', 'Nice', 'Strasbourg', 'Toulouse',
    'Montpellier', 'Reims', 'Nantes', 'Clermont Foot', 'Brest',
    'Lorient', 'Le Havre', 'Metz', 'Troyes', 'Ajaccio'
]

eredivisie_teams = [
    'Feyenoord', 'Psv', 'Ajax', 'AZ Alkmaar', 'FC Twente', 'FC Utrecht', 
    'NEC', 'SC Heerenveen', 'Fortuna Sittard', 'Vitesse', 'Heracles Almelo', 
    'Sparta Rotterdam', 'RKC Waalwijk', 'PEC Zwolle', 'Excelsior', 'Go Ahead Eagles', 
    'Almere City', 'FC Volendam', 
]

liga_portugal_teams = [
    'Benfica', 'Porto', 'Sporting CP', 'Sporting Braga', 'Vitoria SC', 
    'Rio Ave', 'Arouca', 'Famalicão', 'Farense', 'Chaves', 
    'Boavista', 'Estoril', 'Portimonense', 'Casa Pia', 'Estrela Amadora', 
    'Gil Vicente', 'Moreirense', 'Vizela'
]

pro_league = [
    'Anderlecht', 'Club Brugge', 'Antwerp', 'Genk', 'Gent', 
    'Standard Liege', 'Sporting Charleroi', 'Union Saint-Gilloise', 'Westerlo', 
    'OH Leuven', 'RWDM', 'Kortrijk', 'Mechelen', 'Cercle Brugge', 'AS Eupen', 'Sint-Truiden'
]

championship_teams = [
    'Sheffield United', 'Leeds United', 'Burnley', 'Luton Town', 'Norwich City', 
    'Middlesbrough', 'West Bromwich Albion', 'Watford', 'Millwall', 'Coventry City', 
    'Preston North End', 'Stoke City', 'Hull City', 'Cardiff City', 'Blackburn Rovers', 
    'Queens Park Rangers', 'Birmingham City', 'Sunderland', 'Bristol City', 'Swansea City', 'Sheffield Wednesday', 'Huddersfield Town', 'Rotherham United', 'Plymouth Argyle'
]

league_one_teams = [
    'Derby County', 'Bolton Wanderers', 'Charlton Athletic', 'Reading', 'Blackpool', 
    'Barnsley', 'Portsmouth', 'Wigan Athletic', 'Wycombe Wanderers', 'Peterbourough United', 
    'Oxford United', 'Shrewsbury Town', 'Lincoln City', 'Leyton Orient', 'Bristol Rovers', 
    'Burton Albion', 'Fleetwood Town', 'Exerter City', 'Stevenage', 'Carlisle United', 
    'Port Vale', 'Northampton Town', 'Cheltenham Town', 'Cambridge United'
]

league_two_teams = [
    'Wrexham', 'Milton Keynes Dons', 'Stockport County', 'Forrest Green Rovers', 'Gillingham', 
    'Bradford City', 'Mansfield Town', 'Salford City', 'Grimsby Town', 'Barrow', 
    'Walsall', 'Swindon Town', 'Colchester United', 'Notts County', 'Harrogate Town', 
    'AFC Wimbledon', 'Doncaster Rovers', 'Tranmere Rovers', 'Accrington Stanley', 
    'Sutton United', 'Crewe Alexandra', 'Morecambe', 'Crawley Town', 'Newport County'
]

brasileirao_Serie_A = [
    'Palmeiras', 'Flamengo', 'Atletico Mineiro', 'Athletico Paranense', 'Internacional', 
    'Bragantino', 'São Paulo', 'Corinthians', 'Santos', 'Fluminense', 
    'Botafogo', 'Fortaleza', 'América Mineiro', 'Goiás'
]

super_lig = [
    'Galatasaray', 'Fenerbahçe', 'Beşiktaş', 'Trabzonspor', 'Adana Demirspor', 
    'İstanbul Başakşehir', 'Samsunspor', 'Ankaragücü', 'Konyaspor', 'Fatih Karagümrük', 
    'Antalyaspor', 'Sivasspor', 'Gaziantep F.K.', 'Alanyaspor', 'Hatayspor', 
    'Rizespor', 'Kasımpaşa', 'İstanbulspor', 'Kayserispor'
]

major_league_soccer = [
    'Inter Miami', 'Los Angeles FC', 'Philadelphia Union', 'New England', 'LA Galaxy', 
    'Minnesota United', 'Portland Timbers', 'Seattle Sounders', 'San Jose Earthquakes', 'Cincinnati',  
    'Dallas', 'Sporting Kansas City', 'Real Salt Lake', 'Orlando City', 'New York City',
    'Atlanta United', 'Nashville SC', 'Columbus Crew', 'New York RB', 'Chicago Fire',
    'Colorado Rapids', 'Houston Dynamo', 'Vancouver Whitecaps', 'Toronto', 'Saint Louise City',
    'Austin', 'Charlotte', 'CF Montréal'
]

saudi_pro_league = [
    'Al Hilal', 'Al Ittihad', 'Al Nassr', 'Al Ahli Jeddah', 'Al Shabab', 
    'Al Ettifaq', 'Al Fateh', 'Al Wahda', 'Al Fayha', 'Damac', 
    'Abha', 'Al Raed', 'Al Taawon', 'Al Khaleej', 'Al Okhdood',
    'Al Tai', 'Al Riyadh', 'Al Hazem'
]

# Create and populate tables for each league
create_league_table('Premier_League', premier_league_teams)
create_league_table('Serie_A', serie_a_teams)
create_league_table('La_Liga', la_liga_teams)
create_league_table('Bundesliga', bundesliga_teams)
create_league_table('Ligue_1', ligue_1_teams)
create_league_table('Eredivisie', eredivisie_teams)
create_league_table('Liga_Portugal', liga_portugal_teams)
create_league_table('Pro_League', pro_league)
create_league_table('Championship_', championship_teams)
create_league_table('League_One', league_one_teams)
create_league_table('League_Two', league_two_teams)
create_league_table('Brasileirao_Serie_A', brasileirao_Serie_A)
create_league_table('Super_Lig', super_lig)
create_league_table('Major_League_Soccer', major_league_soccer)
create_league_table('Saudi_Pro_League', saudi_pro_league)
# Close the connection
conn.close()
