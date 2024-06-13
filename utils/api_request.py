#! ./.venv/bin/python3 
import requests
from dotenv import load_dotenv
import os
from loguru import logger

load_dotenv()
USERNAME: str = os.getenv('PICOCTF_USERNAME')
PASSWORD: str = os.getenv('PASSWORD')
CSRFTOKEN: str = os.getenv('CSRFTOKEN')

CLASSROOM_URL: str = os.getenv('CLASSROOM_URL')
LOGIN_URL: str = os.getenv('LOGIN_URL')

LOGIN_CRED = {
  "username":USERNAME,
  "password":PASSWORD
}

HEADERS = {"User-Agent" : "Mozilla/5.0 (X11; Linux x86_64; rv:109.0) Gecko/20100101 Firefox/115.0",
"X-CSRFToken" : CSRFTOKEN}

def login(url:str,cred:dict, headers:dict)->dict | int:
  try:
    res = requests.post(url, json=cred, headers=headers)
    cookies = res.cookies.get_dict()
    return cookies
  except Exception as e: 
    logger.error(f'Error: {e}')
    return -1

def getLeaderboard(url:str, headers:dict)->dict | int:
  try:
    cookies = login(LOGIN_URL,LOGIN_CRED,HEADERS)
    res = requests.get(url,cookies = cookies, headers=headers)
    return dict(res.json())
  except Exception as e:
    logger.error(f'Error: {e}')
    return -1
