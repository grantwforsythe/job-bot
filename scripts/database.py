import sqlite3
import pandas as pd
from datetime import datetime

TODAY = datetime.today().strftime('%Y-%m-%d')


def apply(job: pd.Series, conn: sqlite3.Connection) -> None:
    title = job[0]
    company = job[1]
    data_applied = TODAY
    url = job[2]

    params = (title, company, data_applied, url)

    with conn:
        conn.execute("""INSERT INTO jobs VALUES(?, ?, ?, ?)""", params)


def view(conn: sqlite3.Connection):
    with conn:
        conn.execute("""SELECT * FROM jobs""")
        conn.fetchall()