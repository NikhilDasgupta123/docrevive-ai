from sqlalchemy import text
from database import engine


with engine.connect() as connection:
    result = connection.execute(
        text("SELECT current_database();")
    )

    print("Database connected successfully")
    print("Database:", result.scalar())