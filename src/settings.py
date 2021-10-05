from dotenv import dotenv_values

config = dotenv_values(r"C:\Users\user\Desktop\projects\fast_api_redis\src\.env")

# NEWSAPI CONFIG
NEWS_API_KEY = config.get('NEWS_AUTH_KEY')

# REDDIT CONFIG
CLIENT_ID = config.get("REDDIT_CLIENT_ID")
SECRET_KEY = config.get("REDDIT_SECRET_KEY")

# REDDIT ACCOUNT DETAILS
USERNAME = config.get("USERNAME")
PASSWORD = config.get("PASSWORD")
