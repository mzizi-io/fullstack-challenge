import os
from sqlalchemy import create_engine
from sqlalchemy_utils import database_exists, create_database
from dotenv import load_dotenv
from logging import getLogger
import pandas as pd

logger = getLogger(__name__)

load_dotenv()

DB_USER = os.getenv("DB_USER")
DB_PASSWORD = os.getenv("DB_PASSWORD")
DB_HOST = os.getenv("DB_HOST")
DB_PORT = os.getenv("DB_PORT")
DB_NAME = os.getenv("DB_NAME")
DB_URL = f"postgresql://{DB_USER}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}" # noqa

engine = create_engine(DB_URL)


def create_database_if_not_exists():
    if not database_exists(engine.url):
        logger.info(f"Creating database '{DB_NAME}'...")
        create_database(DB_URL)
        logger.info("Database created successfully!")
    else:
        logger.info("Database already exists.")


def ingest_excel_data():
    df = pd.read_excel("./dev_setup/data.xlsx")
    df.columns = map(lambda x: str.lower(x).replace(" ", "_"), df.columns)
    df = df.rename(columns={
        "zip": "zip_code",
        "dir": "direction"
    })
    df['id'] = df.index
    df.replace(r"^ +$", None, inplace=True, regex=True)
    df.to_sql(name='assets', con=engine, if_exists='replace', index=False)


if __name__ == "__main__":
    create_database_if_not_exists()
    ingest_excel_data()
