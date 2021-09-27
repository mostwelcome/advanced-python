def main():
    # Merge two dicts with dict comprehension

    team1 = {'a': 20, 'b': 30, 'c': 40}
    team2 = {'d': 50, 'e': 60, 'f': 70}

    new_team = {k: v for team in (team1, team2) for k, v in team.items()}
    print(new_team)


if __name__ == "__main__":
    main()
