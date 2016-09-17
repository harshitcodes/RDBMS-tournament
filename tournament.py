#!/usr/bin/env python
#
# tournament.py -- implementation of a Swiss-system tournament
#

import psycopg2


def connect():
    """Connect to the PostgreSQL database.  Returns a database connection."""
    return psycopg2.connect("dbname=tournament")


def deleteMatches():
    """Remove all the match records from the database."""
    DB = connect()
    db_cursor = DB.cursor()
    db_cursor.execute("DELETE FROM matches;")
    DB.commit()
    DB.close()


def deletePlayers():
    """Remove all the player records from the database."""
    DB = connect()
    db_cursor = DB.cursor()
    db_cursor.execute("DELETE FROM players;")
    DB.commit()
    DB.close()


def countPlayers():
    """Returns the number of players currently registered."""
    DB = connect()
    db_cursor = DB.cursor()
    db_cursor.execute("SELECT count(*) FROM players;")
    num = db_cursor.fetchone()[0]
    db_cursor.close()
    DB.close()
    return num


def registerPlayer(name):
    """Adds a player to the tournament database.

    The database assigns a unique serial id number for the player.  (This
    should be handled by your SQL database schema, not in your Python code.)

    Args:
      name: the player's full name (need not be unique).
    """
    DB = connect()
    db_cursor = DB.cursor()
    # inserting the player with name wins and losses(initialized)
    db_cursor.execute("INSERT INTO players (name)" "VALUES" "(%s);", (name,))
    DB.commit()


def playerStandings():
    """Returns a list of the players and their win records, sorted by wins.

    The first entry in the list should be the player in first place, or a player
    tied for first place if there is currently a tie.

    Returns:
      A list of tuples, each of which contains (id, name, wins, matches):
        id: the player's unique id (assigned by the database)
        name: the player's full name (as registered)
        wins: the number of matches the player has won
        matches: the number of matches the player has played
    """
    DB = connect()
    db_cursor = DB.cursor()
    db_cursor.execute("SELECT * FROM standings;")
    standing_list = db_cursor.fetchall()
    DB.close()
    return standing_list


def reportMatch(winner, loser):
    """Records the outcome of a single match between two players.

    Args:
      winner:  the id number of the player who won
      loser:  the id number of the player who lost
    """

    DB = connect()
    cursor = DB.cursor()
    cursor.execute("INSERT INTO matches(player_one_id,player_two_id,winner_id)"
    " VALUES (%s,%s,%s)" , (winner,loser,winner))
    DB.commit()
    cursor.close()
    DB.close()

    # DB = connect()
    # db_cursor = DB.cursor()
    # db_cursor.execute("select MAX(round_number) FROM matches;")
    # max = db_cursor.fetchall()[0][0]
    # if max is None:
    #     max = 0

    # # insert info about the match results
    # db_cursor.execute("INSERT INTO matches("
    #           "round_number, player_one_id, player_two_id, winner_id)"
    #           "VALUES"
    #           "(%s, %s, %s, %s);",
    #           (int(max+1), int(winner), int(loser), int(winner),))

    # # updating the players table using the results
    # db_cursor.execute("UPDATE players " "SET wins = wins + 1 " "WHERE id = %s;", (int(winner),))  #sanitized
    # db_cursor.execute("UPDATE players " "SET losses = losses + 1 " "WHERE id = %s;", (int(loser),))
    # DB.commit()
    # DB.close()


def swissPairings():
    """Returns a list of pairs of players for the next round of a match.

    Assuming that there are an even number of players registered, each player
    appears exactly once in the pairings.  Each player is paired with another
    player with an equal or nearly-equal win record, that is, a player adjacent
    to him or her in the standings.

    Returns:
      A list of tuples, each of which contains (id1, name1, id2, name2)
        id1: the first player's unique id
        name1: the first player's name
        id2: the second player's unique id
        name2: the second player's name
    """
    DB = connect()
    db_cursor = DB.cursor()
    db_cursor.execute("SELECT ID,name,wins FROM standings ORDER BY wins DESC;")
    rows = db_cursor.fetchall()
    DB.close()
    i=0
    pairings = []
    while i < len(rows):
        playerAid = rows[i][0]
        playerAname = rows[i][1]
        playerBid = rows[i+1][0]
        playerBname = rows[i+1][1]
        pairings.append((playerAid,playerAname,playerBid,playerBname))
        i=i+2

    return pairings


