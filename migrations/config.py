from dotenv import dotenv_values

env = dotenv_values()

class Config:
    """ environment variables """ 
    # MySQL connection
    DB_HOST = env.get('DB_HOST', 'localhost')
    DB_USER = env.get('DB_USER')
    DB_PASSWORD = env.get('DB_PASSWORD')
    DB_DATABASE = env.get('DB_DATABASE')
