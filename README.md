# SHL_Predictions: Project Overview
- Creating a model for predicting results in the Swedish Hockey League (SHL)
- This is a work in progress and will be updated continuously

## Code and resources used:
**Python:** 3.7

**Packages:** Pandas, Numpy, Matplotlib, Scipy, Seaborn


## Data Cleaning
The data was collected from [here](https://stats.swehockey.se/ScheduleAndResults/Schedule/10371). To get going quickly i copied all the games and pasted them in an excel-sheet.

- Created new columns for home and away goals
- Created a column to show if a game ended in a tie after full time or not
- Created a a dataset with stats for each team based on the game data (total number of goals home/away, max/min goals home/away, avg. number of goals /home/away, avg. number of goals against home/away)
- Exported the data to two seperate csv files, ["shl_clean.csv"](https://github.com/tlondahl/SHL_Predictions/blob/master/SHL%2019/shl_clean.csv) (team stats) and ["games.csv"](https://github.com/tlondahl/SHL_Predictions/blob/master/SHL%2019/games.csv) (all the games and results)

## Model building:
- My model is based on Poission regression.
- Currently the model uses the variables of how many goals the home and away team is expected to score combined with how many goals they are expected to give up.
- Since it is usually an advantage to be on home ice the variables are home/away specific, i.e. only data from how a team has perforemd at home is used for calculating the  probability of the said home team scoring/giving up a goal
- To be able to predict a winner the sum of all the probabilites of a team scoring more, less or equal amount of goals are used and combined with a random factor (otherwise the favourite would always win, and that is not always the case)
### Future plans:
- Later I plan to test develop the model further by using team vs. team specific data, i.e. how team A have historically performed against Team B etc.
- I will also try to incorporate how a team has performed lately. For instance, the results of the last 10 games will be valued higher.

## Testing:
in order to testthe model I excluded the last 7 games from the data set and the sats calculations and exported the same type of files as described above but called them ["shl_clean-7.csv"](https://github.com/tlondahl/SHL_Predictions/blob/master/SHL%2019/shl_clean-7.csv) (team stats) and ["games-7.csv"](https://github.com/tlondahl/SHL_Predictions/blob/master/SHL%2019/games-7.csv) (all the games and results)
- When simulating the last round 1000 times my model had a mean accuracy per simulation of **_(43.19%)_**.
- The code for this simulation can be found [here](https://github.com/tlondahl/SHL_Predictions/blob/master/SHL%2019/last_round_sim.py)

### To do:
- Calculate the standings of each simulation
- Do a Monte Carlo simulation of a season

## Conclusion (so far)
There are three possible results to a hockey game, home team win, away team win or a tie. Having an accuracy of **_43.19%_** is at least better than chosing a result by random **_(1/3, 33,33%)_**. However, I would like to increase the accuracy. Hence, I will continue to devolp the model and try adding and/or removing some variables.


Later a would also like to build a more dynamic model to simulate an entire season where the results of each game have an effect on the probabity of the next game. 
