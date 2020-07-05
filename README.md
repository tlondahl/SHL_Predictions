# SHL_Predictions: Project Overview
- Creating a model for predicting results in the Swedish Hockey League (SHL)
- This is a work in progress and will be updated continuously

## Code and resources used:
**Python:** 3.7

**Packages:** Pandas, Numpy, Matplotlib, Scipy, Seaborn


## Data Cleaning
The data was collected from https://stats.swehockey.se/ScheduleAndResults/Schedule/10371. To get going quickly i copied all the games and pasted them in an excel-sheet.

- Created new columns for home and away goals
- Created a column to show if a game ended in a tie after full time or not
- Created a a dataset with stats for each team based on the game data (total number of goals home/away, max/min goals home/away, avg. number of goals /home/away, avg. number of goals against home/away)
- Exported the data to two seperate csv files, "shl_clean.csv" (team stats) and "games.csv" (all the games and results)

## Model building:
- My model is based on Poission regression.
- Currently the model uses the variables of how many goals the home and away team is expected to score combined with how many goals they are expected to give up.
- Since it is usually an advantage to be on home ice the variables are home/away specific, i.e. only data from how a team has perforemd at home is used for calculating the  probability of the said home team scoring/giving up a goal
- To be able to predict a winner the sum of all the probabilites of a team scoring more, less or equal amount of goals are used and combined with a random factor (otherwise the favourite would always win, and that is not always the case)
### Future plans:
- Later I plan to test develop the model further by using team vs. team specific data, i.e. how team A have historically performed against Team B etc.
- I will also try to incorporate how a team has performed lately. For instance, the results of the last 10 games will be valued higher.

## Testing:
- When simulating the last round my model predicted the correct results in 5/7 games (71,42%)
- I have test the model above and simulated a season and checked the results from my model against the actual results. An initial test of one simulation showed that my model predicted the correct result in 52% of the games
### To do:
- Do a larger number of simulations
- Calculate the standings of each simulation
