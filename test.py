import sqlite3
from sqlite3.dbapi2 import connect

conn = sqlite3.connect('twitterInfo.db')

#if i dont want to save the database
#conn = sqlite3.connect(':memory:')

#cursor tells the database what to do
#create a cursor
c = conn.cursor()

# Create a Table
# c.execute("""CREATE TABLE Tweet (
#         username text,
#         description text,
#         location text,
#         following integer,
#         followers integer,
#         totaltweets integer,
#         retweetcount integer,
#         hashtags text
# )""")
c.execute("SELECT * FROM Tweet")
print(c.fetchall())

#Insert data into table
# c.execute("INSERT INTO customers VALUES ('John', 'Elder', 'john#codemy.com')")


# DataTypes
# NULL
# INTEGER
# REAL
# TEXT
# BLOB

# Commit our command
conn.commit()

# Close our connection
conn.close()

