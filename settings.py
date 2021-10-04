from dotenv import dotenv_values

config = dotenv_values(".env")

# NEWSAPI CONFIG
NEWS_API_KEY = config.get('NEWS_AUTH_KEY')

# REDDIT CONFIG
CLIENT_ID = config.get("REDDIT_CLIENT_ID")
SECRET_KEY = config.get("REDDIT_SECRET_KEY")
