import csv

MAX_PLAYERS = 18
CUR_PLAYERS = 0
TEAM = []

def show_players():
    players = []
    with open('players.csv') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        next(reader, None) # skip the header
        for column in reader:
            players.append(column[1])
    print("These are the players you can draft:")
    for player in players:
        print(player)

def check_drafted(player):
    with open('players.csv') as csv_file:
        reader = csv.reader(csv_file, delimiter=',')
        next(reader, None) # skip the header
        for row in reader:
            if row[1] == player and row[4] == '0':
                return True
            else:
                return False


def draft(player, CUR_PLAYERS):
    if check_drafted(player):
        TEAM.append(player)
        print("You drafted %s" % player)






def main():
    show_players()
    draft('Lionel Messi', CUR_PLAYERS)
    print(TEAM)
    print(CUR_PLAYERS)
if __name__ == "__main__": main()