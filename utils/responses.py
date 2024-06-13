from utils.leaderboard import extractLeaderboard, getUserRank, orderLeaderboard
from utils.message_formatters import leaderboard_formatter, user_rank_formatter
from dotenv import load_dotenv
from utils.api_request import getLeaderboard
import os 

load_dotenv()
DATA_FILE: str = os.getenv('DATA_FILE_PATH')
LEADERS_CLASSROOM_URL: str = os.getenv('LEADERS_CLASSROOM_URL')

def generate_response(user_message:str,csvFile=DATA_FILE)->str:
    input_text = user_message.split("/picoCTF")[1].strip().split()
    leaderboard = getLeaderboard()
    if leaderboard == -1:
        leaderboard = extractLeaderboard(csvFile)
    leaders_leaderboard = getLeaderboard(LEADERS_CLASSROOM_URL)
    if leaders_leaderboard != -1:
        leaderboard = orderLeaderboard([y for x in [leaderboard, leaders_leaderboard] for y in x])
    if "leaderboard" in input_text: 
        return leaderboard_formatter(leaderboard)
    elif "rank" in input_text:
        i = input_text.index("rank")
        user = input_text[i+1]
        user_rank = getUserRank(leaderboard,user)
        return user_rank_formatter(user_rank)
    return "Hello there! I am a bot that can help you with the picoCTF leaderboard. You can ask me for the leaderboard or your rank."