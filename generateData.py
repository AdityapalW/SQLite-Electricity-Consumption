import sqlite3
import random

# Connect to the SQLite database (or create it if it doesn't exist)
conn = sqlite3.connect('neighborhood_electricity.db')
cursor = conn.cursor()

# Create the table if it doesn't exist already
cursor.execute('''
    CREATE TABLE IF NOT EXISTS electricity_consumption (
        id INTEGER PRIMARY KEY AUTOINCREMENT,
        household_name TEXT NOT NULL,
        consumption_kwh REAL NOT NULL
    )
''')

# Function to generate random electricity consumption for households
def generate_random_consumption(num_households):
    data = []
    for i in range(1, num_households + 1):
        household_name = f'Household_{i}'
        consumption_kwh = round(random.uniform(100, 1000), 2)  # Random consumption between 100 and 1000 kWh
        data.append((household_name, consumption_kwh))
    return data

# Generate random data for 50 households
num_households = 50
households_data = generate_random_consumption(num_households)

# Insert the generated data into the database
cursor.executemany('''
    INSERT INTO electricity_consumption (household_name, consumption_kwh)
    VALUES (?, ?)
''', households_data)

# Commit the transaction and close the connection
conn.commit()
conn.close()

print(f"Inserted electricity consumption data for {num_households} households.")


