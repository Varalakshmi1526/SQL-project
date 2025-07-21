import sqlite3

# Connect to the database
conn = sqlite3.connect("railway.db")
cursor = conn.cursor()

# Create TRAINS table
cursor.execute("""
CREATE TABLE IF NOT EXISTS TRAINS (
    TRAIN_ID INTEGER PRIMARY KEY,
    TRAIN_NAME TEXT,
    SOURCE TEXT,
    DESTINATION TEXT,
    DATE TEXT,
    SEATS INTEGER
)
""")

# Create BOOKINGS table
cursor.execute("""
CREATE TABLE IF NOT EXISTS BOOKINGS (
    BOOKING_ID INTEGER PRIMARY KEY AUTOINCREMENT,
    TRAIN_ID INTEGER,
    USER_NAME TEXT,
    SEAT_NO INTEGER,
    STATUS TEXT
)
""")

# Check if TRAINS table is empty
cursor.execute("SELECT COUNT(*) FROM TRAINS")
train_count = cursor.fetchone()[0]

# Insert sample data only if no data exists
if train_count == 0:
    sample_trains = [
        (101, 'Shatabdi Express', 'Delhi', 'Lucknow', '2025-07-20', 150),
        (102, 'Rajdhani Express', 'Mumbai', 'Delhi', '2025-07-21', 200),
        (103, 'Duronto Express', 'Chennai', 'Kolkata', '2025-07-22', 180)
    ]
    cursor.executemany("""
        INSERT INTO TRAINS (TRAIN_ID, TRAIN_NAME, SOURCE, DESTINATION, DATE, SEATS)
        VALUES (?, ?, ?, ?, ?, ?)
    """, sample_trains)
    print("✅ Sample train data inserted.")
else:
    print("ℹ️ Train data already exists. No insert performed.")

# Commit and close
conn.commit()
conn.close()
print("✅ Database setup completed successfully.")
