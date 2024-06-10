from utils.csv_utils import extractLeaderboard, getUserRank
from utils.message_formatters import leaderboard_formatter, user_rank_formatter


def generate_response(user_message:str,csvFile)->str:
    input_text = user_message.split("/picoCTF")[1].strip().split()
    leaderboard = extractLeaderboard(csvFile)
    if "leaderboard" in input_text: 
        return leaderboard_formatter(leaderboard)
    elif "rank" in input_text:
        i = input_text.index("rank")
        user = input_text[i+1]
        user_rank = getUserRank(leaderboard,user)
        return user_rank_formatter(user_rank)
    return "Hello there! I am a bot that can help you with the picoCTF leaderboard. You can ask me for the leaderboard or your rank."