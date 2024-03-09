import os
from dotenv import load_dotenv
from openai import OpenAI
import pyupbit

load_dotenv()
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
upbit = pyupbit.Upbit(os.getenv("UPBIT_ACCESS_KEY"), os.getenv("UPBIT_SECRET_KEY"))


completion = client.chat.completions.create(
  model="gpt-3.5-turbo",
  messages=[
    {"role": "system", "content": "You are a helpful assistant."},
    {"role": "user", "content": "Hello!"}
  ]
)

print(completion.choices[0].message)
print(upbit.get_balance("KRW-BTC"))
krw = upbit.get_balance("KRW")
print(krw)