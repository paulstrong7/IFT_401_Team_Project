import os
DB_USERNAME = "admin"
DB_PASSWORD = "IFT401_25"
DB_HOST = "my-rds-instance.cxq8kcsuioc3.us-east-2.rds.amazonaws.com"
DB_PORT = "3306"
DB_NAME = "project_stocks"
SQLALCHEMY_DATABASE_URI = 'mysql+pymysql://admin:IFT401_25@my-rds-instance.cxq8kcsuioc3.us-east-2.rds.amazonaws.com/project_stocks'
SQLALCHEMY_TRACK_MODIFICATIONS = False