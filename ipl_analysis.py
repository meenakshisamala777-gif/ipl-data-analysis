import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# -------------------------------
# Load Dataset
# -------------------------------

matches = pd.read_csv("matches.csv")
deliveries = pd.read_csv("deliveries.csv")

print("Matches Dataset Shape:", matches.shape)
print("Deliveries Dataset Shape:", deliveries.shape)

# -------------------------------
# Basic Dataset Information
# -------------------------------

print("\nMatches Dataset Info")
print(matches.info())

print("\nMissing Values")
print(matches.isnull().sum())

# -------------------------------
# Most Winning Teams
# -------------------------------

wins = matches['winner'].value_counts()

print("\nTop Winning Teams")
print(wins.head(10))

plt.figure(figsize=(10,6))
sns.barplot(
    x=wins.values[:10],
    y=wins.index[:10]
)
plt.title("Most Winning Teams in IPL")
plt.xlabel("Number of Wins")
plt.ylabel("Teams")
plt.show()

# -------------------------------
# Top Run Scorers
# -------------------------------

# Some datasets use batter, others use batsman
if 'batter' in deliveries.columns:
    top_runs = deliveries.groupby('batter')['batsman_runs'].sum().sort_values(ascending=False).head(10)
else:
    top_runs = deliveries.groupby('batsman')['batsman_runs'].sum().sort_values(ascending=False).head(10)

print("\nTop Run Scorers")
print(top_runs)

plt.figure(figsize=(10,6))
sns.barplot(
    x=top_runs.values,
    y=top_runs.index
)
plt.title("Top 10 IPL Run Scorers")
plt.xlabel("Runs")
plt.ylabel("Players")
plt.show()

# -------------------------------
# Most Popular Stadiums
# -------------------------------

venue_count = matches['venue'].value_counts().head(10)

print("\nTop Stadiums")
print(venue_count)

plt.figure(figsize=(12,6))
sns.barplot(
    x=venue_count.values,
    y=venue_count.index
)
plt.title("Top 10 IPL Stadiums by Matches Hosted")
plt.xlabel("Matches Hosted")
plt.ylabel("Venue")
plt.show()

# -------------------------------
# Toss Winners Analysis
# -------------------------------

toss = matches['toss_winner'].value_counts().head(10)

plt.figure(figsize=(8,8))
plt.pie(
    toss.values,
    labels=toss.index,
    autopct='%1.1f%%'
)
plt.title("Toss Winners Distribution")
plt.show()

# -------------------------------
# Toss Winner vs Match Winner
# -------------------------------

matches['toss_match_win'] = (
    matches['toss_winner'] == matches['winner']
)

result = matches['toss_match_win'].value_counts()

plt.figure(figsize=(6,6))
plt.pie(
    result.values,
    labels=['Won Match After Winning Toss',
            'Lost Match After Winning Toss'],
    autopct='%1.1f%%'
)
plt.title("Impact of Toss on Match Result")
plt.show()

# -------------------------------
# Matches Played Each Season
# -------------------------------

if 'season' in matches.columns:

    season_matches = matches.groupby('season').size()

    plt.figure(figsize=(10,6))
    season_matches.plot(marker='o')
    plt.title("IPL Matches Per Season")
    plt.xlabel("Season")
    plt.ylabel("Matches")
    plt.grid(True)
    plt.show()

# -------------------------------
# Top Players with Most Sixes
# -------------------------------

if 'batter' in deliveries.columns:

    sixes = deliveries[deliveries['batsman_runs'] == 6]
    top_sixers = sixes.groupby('batter').size().sort_values(ascending=False).head(10)

else:

    sixes = deliveries[deliveries['batsman_runs'] == 6]
    top_sixers = sixes.groupby('batsman').size().sort_values(ascending=False).head(10)

plt.figure(figsize=(10,6))
sns.barplot(
    x=top_sixers.values,
    y=top_sixers.index
)
plt.title("Top 10 Six Hitters in IPL")
plt.xlabel("Number of Sixes")
plt.ylabel("Players")
plt.show()

print("\nIPL Analysis Completed Successfully!")