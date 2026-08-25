import os
import time
from fastapi import FastAPI
import psycopg2

app = FastAPI()

def get_db_connection():
    return psycopg2.connect(
        host=os.getenv("DB_HOST", "db"),
        database=os.getenv("DB_NAME", "postgres"),
        user=os.getenv("DB_USER", "postgres"),
        password=os.getenv("DB_PASSWORD", "secret")
    )

time.sleep(2)
conn = get_db_connection()
cur = conn.cursor()
cur.execute("""
    CREATE TABLE IF NOT EXISTS visits (
        id SERIAL PRIMARY KEY,
        timestamp TIMESTAMP DEFAULT CURRENT_TIMESTAMP
    );
""")
conn.commit()
cur.close()
conn.close()

@app.get("/api/visit")
def visit():
    conn = get_db_connection()
    cur = conn.cursor()
    
    cur.execute("INSERT INTO visits DEFAULT VALUES;")
    conn.commit()
    
    cur.execute("SELECT COUNT(*) FROM visits;")
    count = cur.fetchone()[0] 
    
    cur.close()
    conn.close()
    
    return {"status": "success", "total_visits": count}
