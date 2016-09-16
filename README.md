# RDBMS-tournament
A python module that uses the PostgreSQL database to keep track of players and matches in a game tournament.
The game tournament will use the Swiss system for pairing up players in each round: players are not eliminated, and each player should be paired with another player with the same number of wins, or as close as possible. Contains complete database schema for the above explained tournament.

## Code Templates
There are 3 files present in the VM's /vagrant directory

| Files              | Contains      |
| -------------      |:-------------:|
| tournament.sql     | This is the database used to store tournament records.|
| tournament.py      | This is the main Python file used to conduct the Swiss Style Tournament. |
| tournament_test.py | This is a python file created by Udacity and modified to perform essential tests on the tournament application.   |


## Installation

Prerequisites:
1. Git
2. Virtual Box
3. vagrant

##### Steps:

1. Open terminal
2. Move to the project folder
3. Clone the VM configuration of Udacity:
..* Run ```git clone http://github.com/udacity/fullstack-nanodegree-vm fullstack-nanodegree-vm```
4. cd into fullstack/vagrant directory created
5. Run ```https://github.com/harshitcodes/RDBMS-tournament```
6. Now you have a directory named tournament
7. Run ```vagrant up```
8. Log into vagrant VM: ```vagrant ssh```
9 cs into /vagrant/tournament/
10.Create tournament database by starting psql by running ```psql```
..* run ```\i tournament.sql```
11. Then come out of the psql and run ```python tournament_test.py``` to test the code.