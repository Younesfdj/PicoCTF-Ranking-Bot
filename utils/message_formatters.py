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