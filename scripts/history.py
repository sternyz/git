import sqlite3
import csv
from datetime import datetime, timedelta

def convert_time(webkit_time):
    # Webkit timestamp is in microseconds since Jan 1, 1601
    epoch_start = datetime(1601, 1, 1)
    return epoch_start + timedelta(microseconds=webkit_time)

conn = sqlite3.connect(r"C:\!Fit_Admin\wort\investigation\FrontDesk-2400\FDesk\Chrome\History")
cursor = conn.cursor()

cursor.execute("SELECT url, title, visit_count, last_visit_time FROM urls ORDER BY last_visit_time DESC")
history_rows = cursor.fetchall()
conn.close()


with open("Chrome_history.csv", mode="w", newline='', encoding="utf-8") as file:
    writer = csv.writer(file)
    writer.writerow(["Timestamp", "URL", "Title", "Visit Count"])
    for row in history_rows:
        url, title, visits, last_time = row
        date_time = convert_time(last_time)
        print(f"{date_time} | {url} | {title} | Visits: {visits}")
        writer.writerow([date_time.strftime("%Y-%m-%d %H:%M:%S"), url, title, visits])

