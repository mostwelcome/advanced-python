from collections import OrderedDict


def main():
    # list of teams with wins and losses
    teams = [
        ('a', (30, 20)),
        ('b', (20, 30)),
        ('c', (50, 0)),
        ('d', (25, 25))
    ]

    # sort the list by no of wins

    sorted_team = sorted(teams, key=lambda t: t[1][0], reverse=True)
    print(sorted_team)

    # create a orderdict from the list
    team_dict = OrderedDict(sorted_team)
    print(team_dict)

    # top team
    print(team_dict.popitem(last=False))


if __name__ == "__main__":
    main()
