import os
DB_USERNAME = "admin"
DB_PASSWORD = "IFT401_25"
DB_HOST = "my-rds-instance.cxq8kcsuioc3.us-east-2.rds.amazonaws.com"
DB_PORT = "3306"
DB_NAME = "project_stocks"
SQLALCHEMY_DATABASE_URI = f"mysql+pymysql://{DB_USERNAME}:{DB_PASSWORD}@{DB_HOST}:{DB_PORT}/{DB_NAME}"
SQLALCHEMY_TRACK_MODIFICATIONS = False