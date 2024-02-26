import random


class Player:
    def __init__(self, name, rank, total_points,old_rank,desc):
        self.rank = rank
        self.name = name
        self.total_points = total_points
        self.old_rank = old_rank
        self.desc=desc
    def __str__(self):
        return f"Player: {self.name}, Rank: {self.rank}, Total Points: {self.total_points}, Old Rank: {self.old_rank}, desc order = {self.desc}"


def chances(player1, player2, drow):
    tmp = (1 - drow) / 2
    reverse_ratio = 1 - (player1.rank / player2.rank)
    player2_chace = tmp + reverse_ratio
    player1_chace = tmp - reverse_ratio
    return player1_chace, player2_chace


def calculate_update(player1, player2):  ##player2 winner
    print("the game between " + player1.name + " and " + player2.name)
    if player1.rank <= player2.rank:
        player1_chace, player2_chace = chances(player1, player2, 0.2)
    else:
        player1_chace, player2_chace = chances(player2, player1, 0.2)
    random_number = random.random()
    # print(player1.name + " " + str(player1_chace))
    # print(player2.name + " " + str(player2_chace))
    # print(random_number)
    if random_number > player2_chace:
        player2.rank+=50
        player1.rank-=50
        print("the winner is "+ player2.name)
        player2.total_points+=1
    elif random_number < player2_chace:
        player2.rank -= 50
        player1.rank += 50
        player1.total_points += 1
        print("the winner is "+ player1.name)
    else:
        print("no winner in this game ")



def rounds(players, match_pairs):
    round_number = 1
    for index, (match, result) in enumerate(match_pairs.items(), start=1):
        if index % 2 == 1:
            print("Round", round_number)
            round_number += 1
        first_player, second_player = match
        calculate_update(players[first_player], players[second_player])


if __name__ == "__main__":
    match_pairs = {
        (0, 1): None,
        (2, 3): None,
        (0, 2): None,
        (1, 3): None,
        (0, 3): None,
        (1, 2): None
    }
    players = []
    for i in range(4):
        tmp=random.randint(1500, 2000)
        if i==0:
            tmp=1500
        if i==1:
            tmp=1600
        players.append(Player("Player:" + str(i), tmp, 0,tmp,0))

    players.sort(key=lambda x: x.rank)
    for player in players:
        print(player)
    print("##########################################")
    rounds(players, match_pairs)
    players.sort(key=lambda x: x.total_points)
    print("##########################################")
    for i in range(4):
        print(players[i])
    print("##########################################")
    print("The winner of the tournament is: " +players[3].name)
    for i in range(4):
        players[i].desc=players[i].rank-players[i].old_rank
    players.sort(key=lambda x: x.desc)
    print("##########################################")
    for i in range(4):
        print(players[i])