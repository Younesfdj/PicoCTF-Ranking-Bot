def leaderboard_formatter(leaderboard:list)->str:
    # format the leaderboard
    formatted_leaderboard = "**Leaderboard**\n```"
    for i in range(len(leaderboard)-1):
        rank = str(i+1)
        if i == 0:
            rank = "🥇"
        elif i == 1:
            rank = "🥈"
        elif i == 2:
            rank = "🥉"
        formatted_leaderboard += f"{rank}. {leaderboard[i][0]} - {leaderboard[i][1]}pts\n"
    formatted_leaderboard += "```"
    return formatted_leaderboard

def user_rank_formatter(user_rank:list | int)->str:
    # format the user rank
    return "```You are not on the leaderboard```" if user_rank == -1 else f"```🎖️. {user_rank[0]} - {user_rank[1]}pts```"