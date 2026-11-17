import os
from dotenv import load_dotenv

load_dotenv()

key = os.getenv("MY_API_KEY")
if not key:
    raise SystemExit("MY_API_KEY не задан: создайте .env по образцу .env.example")

# сам ключ никогда не печатаем и не логируем
print(f"Ключ загружен, длина: {len(key)} символов")
