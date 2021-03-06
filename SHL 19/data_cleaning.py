import pandas as pd

df = pd.read_excel("shl.xlsx")

# Get home and away team
df[["home", "away"]] = df.Game.str.split("-", expand = True)
df.home = df.home.str.strip()
df.away = df.away.str.strip()

# Separate home and away goals from result
df[["home_goals", "away_goals"]] = df.Result.str.split("-", expand = True)
df.rename(columns= {"Unnamed: 4": "result2"}, inplace = True)
df["tie?"] = df.result2.apply(lambda x: "y" if len(x) >15 else "n")
df.home_goals = df.home_goals.str.strip().astype(int)
df.away_goals = df.away_goals.str.strip().astype(int)

# Calculate number of games played
n_games = int(len(df)/len(df.home.unique()))

# Create new dataframe with only the relevant information
games = df.iloc[:,7:]
# Create a new df with stats per team

# Home stats
shl_stats_home = games.groupby(["home"]).sum()
shl_stats_home.reset_index(level = 0, inplace = True)
shl_stats_home.rename(columns = {"home": "team", "away_goals": "home_ga"}, inplace = True)
max_home = df.groupby(["home"]).max()
max_home = max_home.filter(items=["home", "home_goals", "away_goals"])
max_home.rename(columns= {"home_goals": "home_max", "away_goals": "home_ga_max"}, inplace = True)
max_home.reset_index(level = 0, inplace = True)

#Away stats
shl_stats_away = df.groupby(["away"]).sum()
shl_stats_away.reset_index(level = 0, inplace = True)
shl_stats_away.rename(columns = {"home_goals": "away_ga"}, inplace = True)
max_away = df.groupby(["away"]).max()
max_away = max_away.filter(items=["away", "home_goals", "away_goals"])
max_away.rename(columns= {"home_goals": "away_ga_max", "away_goals": "away_max"}, inplace = True)
max_away.reset_index(level=0, inplace=True)

#concat
shl_stats = pd.concat([shl_stats_home, shl_stats_away, max_home, max_away], axis=1)
shl_stats.drop(["away", "home", "Spectators"], inplace = True, axis=1)
shl_stats = shl_stats.loc[:, ~shl_stats.columns.str.contains('^Unnamed')]


# Average for each stat
shl_stats["home_avg"] = shl_stats.home_goals/(n_games)
shl_stats["away_avg"] = shl_stats.away_goals/(n_games)
shl_stats["home_ga_avg"] = shl_stats.home_ga/(n_games)
shl_stats["away_ga_avg"] = shl_stats.away_ga/(n_games)

shl_stats.to_csv("shl_clean.csv")
games.to_csv("games.csv")
