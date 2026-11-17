
import pandas as pd
from sqlalchemy import create_engine, text
from sqlalchemy.engine import URL
from getpass import getpass

# --------------------------------
# 1. MySQL Server Configuration
# --------------------------------

username = input("Enter MySQL username: ")
password = getpass("Enter MySQL password: ")

host = "localhost"
port = 3306
database = "cybershield"

# --------------------------------
# 2. Connect to MySQL Server
# --------------------------------

server_url = URL.create(
    "mysql+pymysql",
    username=username,
    password=password,
    host=host,
    port=port
)

server_engine = create_engine(server_url)

# --------------------------------
# 3. Create CyberShield Database
# --------------------------------

with server_engine.connect() as connection:
    connection.execute(
        text("CREATE DATABASE IF NOT EXISTS cybershield")
    )
    connection.commit()

print("CyberShield database created successfully!")

# --------------------------------
# 4. Connect to CyberShield Database
# --------------------------------

database_url = URL.create(
    "mysql+pymysql",
    username=username,
    password=password,
    host=host,
    port=port,
    database=database
)

engine = create_engine(database_url)

# --------------------------------
# 5. Load CSV Files
# --------------------------------

df_veris = pd.read_csv(
    "veris_incidents_clean.csv",
    parse_dates=["Incident_Date"]
)

df_kev = pd.read_csv(
    "cisa_kev_clean.csv",
    parse_dates=["dateAdded", "dueDate"]
)

print("Both CSV files loaded successfully!")

# --------------------------------
# 6. Upload VERIS Dataset
# --------------------------------

df_veris.to_sql(
    name="veris_incidents",
    con=engine,
    if_exists="replace",
    index=False,
    chunksize=500,
    method="multi"
)

print("VERIS dataset uploaded successfully!")

# --------------------------------
# 7. Upload CISA KEV Dataset
# --------------------------------

df_kev.to_sql(
    name="cisa_kev",
    con=engine,
    if_exists="replace",
    index=False,
    chunksize=500,
    method="multi"
)

print("CISA KEV dataset uploaded successfully!")

# --------------------------------
# 8. Verify Uploaded Tables
# --------------------------------

with engine.connect() as connection:

    tables = connection.execute(
        text("SHOW TABLES")
    )

    print("\nTables in CyberShield Database:")

    for table in tables:
        print(table[0])

print("\nBoth datasets uploaded successfully!")
