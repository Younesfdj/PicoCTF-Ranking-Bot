from utils.csv_utils import extractLeaderboard, getUserRank
from utils.message_formatters import leaderboard_formatter


def generate_response(user_message:str,csvFile)->str:
    input = user_message.split("/picoCTF")[1].strip().split()
    if "leaderboard" in input: 
        leaderboard = extractLeaderboard(csvFile)
        return leaderboard_formatter(leaderboard)
    return "hello there"