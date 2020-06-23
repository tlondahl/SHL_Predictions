import pandas as pd

df = pd.read_excel("shl.xlsx")

# Get home and away team
df[["home", "away"]] = df.Game.str.split("-", expand = True)
df.home = df.home.str.strip()
df.away = df.away.str.strip()

# Separate home and away goals from result
df[["home_goals", "away_goals"]] = df.Result.str.split("-", expand = True)
df.home_goals = df.home_goals.str.strip().astype(int)
df.away_goals = df.away_goals.str.strip().astype(int)

# Calculate number of games played
n_games = int(len(df)/len(df.home.unique()))

# Remove irrelevant columns
df.drop(["Spectators"], inplace = True, axis = 1)
# Create a new df with stats per team

# Home stats
shl_stats_home = df.groupby(["home"]).sum()
shl_stats_home.reset_index(level = 0, inplace = True)
shl_stats_home.rename(columns = {"home": "team", "away_goals": "home_ga"}, inplace = True)
#Away stats
shl_stats_away = df.groupby(["away"]).sum()
shl_stats_away.reset_index(level = 0, inplace = True)
shl_stats_away.rename(columns = {"home_goals": "away_ga"}, inplace = True)
#concat
shl_stats = pd.concat([shl_stats_home, shl_stats_away], axis=1)
shl_stats.drop(["away"], inplace = True, axis=1)

# Average for each stat
shl_stats["home_avg"] = shl_stats.home_goals/(n_games/2)
shl_stats["away_avg"] = shl_stats.away_goals/(n_games/2)
shl_stats["home_ga_avg"] = shl_stats.home_ga/(n_games/2)
shl_stats["away_ga_avg"] = shl_stats.away_ga/(n_games/2)

shl_stats.to_csv("shl_clean.csv")