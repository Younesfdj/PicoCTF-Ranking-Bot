import csv

def orderLeaderboard(leaderboard:list)->list:
    # sort the leaderboard
    leaderboard.sort(key=lambda x: x[1], reverse=True)
    return leaderboard

def extractLeaderboard(csvFile)->list:
    rows = []
    # read the csv file
    with open(csvFile, 'r') as csvfile:
        csvreader = csv.reader(csvfile)
        # get the rows of the csv file
        for row in csvreader:
            rows.append(row)
    # get the starting index of the leaderboard
    for i in range(len(rows)-1):
        if '(Total)' in rows[i]:
            startingIndex = i
            break

    # get the leaderboard
    leaderboard = []
    for row in rows[startingIndex+1:] :
        neuRow = list(filter(None,row))
        neuRowLength = len(neuRow)-1
        leaderboard.append([neuRow[0],int(neuRow[neuRowLength])])

    return orderLeaderboard(leaderboard)

def getUserRank(leaderboard:list, user:str)->int|list:
    for i in range(len(leaderboard)):
        if user in leaderboard[i]:
            return leaderboard[i]
    return -1

