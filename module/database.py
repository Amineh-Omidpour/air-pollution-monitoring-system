import os

import psycopg2
from dotenv import load_dotenv


load_dotenv()


class Database:
    def __init__(self):
        self.host = os.getenv("DB_HOST")
        self.port = os.getenv("DB_PORT")
        self.db_name = os.getenv("DB_NAME")
        self.user = os.getenv("DB_USER")
        self.password = os.getenv("DB_PASSWORD")


    def connect(self):
        try:
            connection = psycopg2.connect(
                host=self.host,
                port=self.port,
                dbname=self.db_name,
                user=self.user,
                password=self.password,
            )
            print("Database connection successful!")
            return connection
        except psycopg2.OperationalError as error:
            print(f"Database connection failed: {error}")
            raise  


    def create_table(self):
        connection = self.connect()
        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                    CREATE TABLE IF NOT EXISTS pollution_readings (
                        id SERIAL PRIMARY KEY,
                        region VARCHAR(50) NOT NULL,
                        pm25 REAL NOT NULL,
                        pm10 REAL NOT NULL,
                        no2 REAL NOT NULL,
                        co REAL NOT NULL,
                        timestamp TIMESTAMP NOT NULL
                    );
                """)
            connection.commit()
            print("Table 'pollution_readings' is ready.")
        except Exception:
            connection.rollback()
            raise
        finally:
            connection.close()  



    def insert_reading(self, region, pm25, pm10, no2, co, timestamp):
        connection=self.connect()              
        try:
           with connection.cursor() as cursor:
               cursor.execute(""" 
                    INSERT INTO pollution_readings 
                    (region, pm25, pm10, no2, co, timestamp) 
                    VALUES (%s, %s, %s, %s, %s, %s);
                    """, 
                    (region, pm25, pm10, no2, co, timestamp),
                    )
               connection.commit()
               print("Reading inserted successfully.")
        except Exception:
            connection.rollback()
            raise
        finally:
            connection.close()


    def fetch_recent_data(self, hours=24):  
        if not isinstance(hours, int) or isinstance(hours, bool) or hours<=0:
            raise ValueError("hours must be a positive integer.")      
        connection=self.connect()
        try:
            with connection.cursor() as cursor:
                cursor.execute(
                    """
                    select region, pm25, pm10, no2, co, timestamp
                    from pollution_readings
                    where timestamp >= NOW() - (%s * INTERVAL '1 hour')
                    order by timestamp DESC
                    """
                    ,(hours,),
                    )
                rows=cursor.fetchall()    
                return rows
        finally:
            connection.close()   

    def delete_old_data(self, days=7):
        if not isinstance(days, int) or isinstance(days, bool) or days <= 0:
         raise ValueError("days must be a positive integer.")
        connection=self.connect()       
        try:
            with connection.cursor() as cursor:
                cursor.execute("""
                delete from pollution_readings 
                where timestamp < now() - (%s * interval '1 day');
                """, (days,),
                )
            deleted_count = cursor.rowcount
            connection.commit()
            print(f"Deleted {deleted_count} old records.")
            return deleted_count
        except Exception:
            connection.rollback()
            raise
        finally:
            connection.close()

    def insert_many_readings(self, readings):
        if not readings:
           print(f"No readings to insert.") 
           return 0
        connection = self.connect()
        try:
            with connection.cursor() as cursor:
                cursor.executemany("""
                Insert into pollution_readings
                (region, pm25, pm10, no2, co, timestamp)
                values(%s, %s, %s, %s, %s, %s);
                """,
                readings,
                )
            inserted_count = cursor.rowcount
            connection.commit()
            print(f"Inserted {inserted_count} into readings.")
            return inserted_count
        except Exception:
            connection.rollback()
            raise
        finally:
            connection.close()



        

















