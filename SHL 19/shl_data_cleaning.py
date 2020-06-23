import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
from scipy.stats import poisson, skellam

shl_og = pd.read_csv("shl.csv")

shl = shl_og[["home", "away", "home_goals", "away_goals"]]
shl_mean = shl.mean()
home_max = shl["home_goals"].max()
away_max = shl["away_goals"].max()
n_games = int(len(shl)/len(shl.home.unique()))
print(n_games)
# Create a new df with stats per team
# Home stats
shl_stats_home = shl.groupby(["home"]).sum()
shl_stats_home.reset_index(level = 0, inplace = True)
shl_stats_home.home = shl_stats_home.home.str.strip()
shl_stats_home.rename(columns = {"home": "team", "away_goals": "home_ga"}, inplace = True)
#Away stats
shl_stats_away = shl.groupby(["away"]).sum()
shl_stats_away.reset_index(level = 0, inplace = True)
shl_stats_away.away = shl_stats_away.away.str.strip()
shl_stats_away.rename(columns = {"home_goals": "away_ga"}, inplace = True)
#concat
shl_stats = pd.concat([shl_stats_home, shl_stats_away], axis=1)
shl_stats.drop(["away"], inplace = True, axis=1)

# Average for each stat
shl_stats["home_avg"] = shl_stats.home_goals/(n_games/2)
shl_stats["away_avg"] = shl_stats.away_goals/(n_games/2)
shl_stats["home_ga_avg"] = shl_stats.home_ga/(n_games/2)
shl_stats["away_ga_avg"] = shl_stats.away_ga/(n_games/2)


"""
# Fiter
shl.home = shl.home.str.strip()
is_fbk = shl.home == "Färjestad BK"
fbk = shl[is_fbk]
print(fbk)
print(shl_stats)
# team_mean = shl.groupby(["home"]).mean()
"""

"""def home_prob(team):
    avg = team_mean.loc[team_mean["home"] == team, "home_goals"]
    prob_goals = np.column_stack()
"""


"""
#Poisson
prob_goals = np.column_stack([[poisson.pmf(i, shl_mean[j]) for i in range(home_max)] for j in range(2)])

# Plot histogram of actual goals
plt.hist(shl[["home_goals", "away_goals"]].values, range(home_max+1), label=["Home", "Away"], density=True, color=["#061324", "#A8C9DA"])

# Plot Poission
pois_1 = plt.plot([i-0.5 for i in range(1,home_max+1)], prob_goals[:,0],marker = "o", label = "Home", color = "#49738C")
pois_2 = plt.plot([i-0.5 for i in range(1,home_max+1)], prob_goals[:,1],marker = "o", label = "Away", color = "#DB5756")

leg=plt.legend(loc='upper right', fontsize=13, ncol=2)
leg.set_title("Poisson           Actual        ", prop = {'size':'14', 'weight':'bold'})

plt.xticks([i-0.5 for i in range(1,home_max+1)],[i for i in range(home_max+1)])
plt.xlabel("Goals per Match",size=13)
plt.ylabel("Proportion of Matches",size=13)
plt.title("Number of Goals per Match (SHL 2019/20 Season)",size=14,fontweight='bold')
plt.ylim([-0.004, 0.4])
plt.tight_layout()
plt.show()
#Probability of a draw
draw_prob = skellam.pmf(0.0, shl_mean[0], shl_mean[1])
"""