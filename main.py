import tkinter as tk
from tkinter import ttk
import random
import math


class BasketballTeam:
    def __init__(self, name):
        self.name = name
        self.wins = 0
        self.loses = 0
        self.total_points = 0


class Championship:
    def __init__(self, teams):
        self.teams = teams
        self.table = []

    def play_match(self, team1, team2):
        score1, score2 = model_match()
        team1.total_points += score1
        team2.total_points += score2

        if score1 > score2:
            team1.wins += 1
            team2.loses += 1
        else:
            team2.wins += 1
            team1.loses += 1

        self.update_table()

    def play_championship(self):
        for i in range(len(self.teams)):
            for j in range(i + 1, len(self.teams)):
                team1 = self.teams[i]
                team2 = self.teams[j]
                self.play_match(team1, team2)

    def update_table(self):
        sorted_teams = sorted(self.teams, key=lambda team: (-team.wins, team.loses))
        #sorted_teams = self.teams
        for i, team in enumerate(sorted_teams):
            self.table.append((i + 1, team.name, team.wins, team.loses))


def poisson(lam, m, s):
    while s >= -1 * lam:
        s += math.log(random.random())
        m += 1
    return m


def model_match():
    lam = 100
    return poisson(lam, 0, 0), poisson(lam, 0, 0)



championship = Championship([
    BasketballTeam("Чигаго Булз"),
    BasketballTeam("Бостон Селтикс"),
    BasketballTeam("Милуоки Бакс"),
    BasketballTeam("Майами Хит"),
    BasketballTeam("Бруклин Нетс"),
    BasketballTeam("Денвер Наггетс")
])

championship.play_championship()

root = tk.Tk()
tree = ttk.Treeview(root, columns=("Rank", "Team", "Wins", "Losses", "AVG PTS"), show="headings")
tree.heading("Rank", text="Rank")
tree.heading("Team", text="Team")
tree.heading("Wins", text="Wins")
tree.heading("Losses", text="Losses")
tree.heading("AVG PTS", text="AVG PTS")
tree.pack()

sorted_teams = sorted(championship.teams, key=lambda team: (-team.wins, team.loses))
for i, team in enumerate(sorted_teams):
    team_avg_points = team.total_points / (len(championship.teams) - 1)
    tree.insert("", "end", values=(i + 1, team.name, team.wins, team.loses,
                                   round(team_avg_points, 2)))

root.mainloop()