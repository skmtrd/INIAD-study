gym = ["JPN", "RUS", "CHN",  "GBR", "USA", "BRA", "GER", "UKR"]

gym_rank = {gym[i]: i + 1 for i in range(len(gym))}

gym_rank = {country : index + 1 for index, country in enumerate(gym)}

print(gym_rank(["USA"]))
