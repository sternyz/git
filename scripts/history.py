"""
Browser History Extraction Script
================================

This script extracts browser history from Chrome/Edge SQLite database files
and exports the data to a CSV file for analysis.

Author: [Your Name]
Purpose: Extract browser history for forensic analysis or data migration
"""

import sqlite3
import csv
from datetime import datetime, timedelta

def convert_time(webkit_time):
    """
    Convert Webkit timestamp to human-readable datetime
    
    Webkit timestamps are stored as microseconds since January 1, 1601
    (the start of the Webkit epoch). This function converts them to
    standard Python datetime objects.
    
    Args:
        webkit_time (int): Webkit timestamp in microseconds
        
    Returns:
        datetime: Converted datetime object
    """
    # Webkit epoch starts on January 1, 1601
    epoch_start = datetime(1601, 1, 1)
    # Add the microseconds to get the actual timestamp
    return epoch_start + timedelta(microseconds=webkit_time)

# Database connection
# Note: Update this path to point to the correct browser history file
# Chrome: C:\Users\[Username]\AppData\Local\Google\Chrome\User Data\Default\History
# Edge: C:\Users\[Username]\AppData\Local\Microsoft\Edge\User Data\Default\History
conn = sqlite3.connect(r"C:\!Fit_Admin\wort\investigation\FrontDesk-2400\FDesk\Chrome\History")
cursor = conn.cursor()

# Execute SQL query to fetch browser history
# This query selects:
# - url: The visited webpage URL
# - title: The page title
# - visit_count: Number of times the page was visited
# - last_visit_time: Timestamp of the most recent visit
# Results are ordered by most recent visits first
cursor.execute("SELECT url, title, visit_count, last_visit_time FROM urls ORDER BY last_visit_time DESC")
history_rows = cursor.fetchall()

# Close database connection to free up resources
conn.close()

# Export data to CSV file
# The CSV will contain: Timestamp, URL, Title, and Visit Count
with open("Chrome_history.csv", mode="w", newline='', encoding="utf-8") as file:
    writer = csv.writer(file)
    
    # Write header row for better readability
    writer.writerow(["Timestamp", "URL", "Title", "Visit Count"])
    
    # Process each history entry
    for row in history_rows:
        # Unpack the row data
        url, title, visits, last_time = row
        
        # Convert the Webkit timestamp to readable datetime
        date_time = convert_time(last_time)
        
        # Print to console for immediate feedback
        print(f"{date_time} | {url} | {title} | Visits: {visits}")
        
        # Write formatted data to CSV
        # Format timestamp as YYYY-MM-DD HH:MM:SS for easy reading
        writer.writerow([date_time.strftime("%Y-%m-%d %H:%M:%S"), url, title, visits])

print(f"\nExport complete! {len(history_rows)} history entries saved to Chrome_history.csv")

