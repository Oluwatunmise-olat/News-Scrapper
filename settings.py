from dotenv import dotenv_values

config = dotenv_values(".env")

News_API_KEY = config.get("NEWS_AUTH_KEY", None)
