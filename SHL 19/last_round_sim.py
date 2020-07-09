import pandas as pd
import numpy as np
import random, statistics
from scipy.stats import poisson

stats = pd.read_csv('shl_clean-7.csv')
stats = stats.iloc[:,1:]
stats.set_index("team", inplace = True)
games = pd.read_csv('games-7.csv')
games = games.iloc[:,1:]

# Poission regression
def pois (df, team, max_g, avg_g):
    avg = df.loc[team, avg_g]
    ma = df.loc[team, max_g]
    pois = [poisson.pmf(i, avg) for i in range(ma+1)]
    return(pois)

# How to decide a winner in a game
def win(df, home_team, away_team):
    home = pois(df, home_team, "home_max", "home_avg")
    away = pois(df, away_team,"away_max", "away_avg")
    matrix = np.multiply.outer(home, away)
    home_prob = np.sum(np.tril(matrix, -1))/np.sum(matrix)
    away_prob = np.sum(np.triu(matrix, 1))/np.sum(matrix)
    tie_prob = np.sum(np.diagonal(matrix))/np.sum(matrix)
    res = random.randrange(1, 100)
    if res > (away_prob + tie_prob)*100:
        return home_team
    elif res > tie_prob*100:
        return away_team
    else:
        return "Tie"

games["winner"] = games.apply(lambda x: "tie" if x["tie?"] == "y" else (x["home"] if x["home_goals"] > x["away_goals"] else x["away"]), axis=1)

test = games.tail(7)
test = test.assign(home_win=0, away_win=0, tie=0, sim_winner="")

test = test.reset_index(drop=True)

def sim_games(df, num_sim):
    result = []
    sim_count = 0
    while sim_count < num_sim:
        for index, row in df.iterrows():
            h = row["home"]
            a = row['away']
            winner = win(stats, h, a)
            if winner == h:
                df.at[index,'home_win'] += 1
                df.at[index,'sim_winner'] = h
            elif winner == a:
                df.at[index,'away_win'] += 1
                df.at[index,'sim_winner'] = a
            else:
                df.at[index,'tie'] += 1
                df.at[index,'sim_winner'] = "tie"
            df["correct"] = df.apply(lambda x: 1 if x["winner"] == x["sim_winner"] else 0, axis = 1)
            accuracy = sum(df.correct)/len(df)
            result.append(accuracy)
            sim_count += 1
    return statistics.mean(result)

print(sim_games(test, 1000))

#print(test)
#print("The model predicted the right results in {} out of {} games ({:.2%})".format(sum(test.correct), len(test), sum(test.correct)/len(test)))


