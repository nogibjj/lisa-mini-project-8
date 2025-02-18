"""Query the database"""

import sqlite3


def query(conn):
    """Query the database for the top 5 rows of the GroceryDB table"""
    conn = sqlite3.connect(conn)
    cursor = conn.cursor()
    cursor.execute("SELECT COUNT(*) FROM OfferDB")
    print("Total number of observations in Offer table:")
    print(cursor.fetchall())
    conn.close()
    return "Success"
