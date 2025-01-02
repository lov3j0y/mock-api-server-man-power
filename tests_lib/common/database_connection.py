import os
import psycopg2
from pathlib import Path
from dotenv import load_dotenv

class DatabaseConnection:
    """Class to handle database connections."""

    @staticmethod
    def get_connection():
        """Set up the database connection."""
        env_path = Path(__file__).resolve().parent.parent / "database.env"                  
        load_dotenv(dotenv_path=env_path)

        database_info = {
            "host": os.getenv('POSTGRES_HOST'),
            "port": os.getenv('POSTGRES_PORT'),
            "dbname": os.getenv('POSTGRES_DB'),
            "user": os.getenv('POSTGRES_USER'),
            "password": os.getenv('POSTGRES_PASSWORD')
        }

        return psycopg2.connect(**database_info)