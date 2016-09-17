-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dAShes, like
-- these lines here.


DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;

-- Connecting to the databASe tournament
\c tournament


CREATE TABLE players(
    -- tournament varchar(3),
    id serial PRIMARY KEY,
    name TEXT NOT NULL
);

CREATE TABLE matches(
    id serial PRIMARY KEY,
    player_one_id int NOT NULL REFERENCES players (id), -- referential integrity with the playerstable
    player_two_id int NOT NULL REFERENCES players (id),
    winner_id int DEFAULT 0
);


-- view for stANDings



-- view for ranking AND deciding the bye distribution bASed on the wins AND id of the players


create view wincounter AS
    SELECT
        players.id,
        players.name,
        count(matches.winner_id) AS wins
    FROM players
        LEFT JOIN matches
            on players.id = matches.winner_id
    GROUP BY
        players.id;

CREATE VIEW totalmatches AS
    SELECT players.id,
    players.name,
    count(matches.id) AS matches
   FROM (players
     LEFT JOIN matches ON (((players.id = matches.player_one_id) OR (players.id = matches.player_two_id))))
  GROUP BY players.id
  ORDER BY players.id;

CREATE VIEW standings AS
 SELECT players.id,
    players.name,
    wincounter.wins,
    totalmatches.matches
   FROM ((players
     JOIN wincounter ON ((players.id = wincounter.id)))
     LEFT JOIN totalmatches ON ((players.id = totalmatches.id)))
  ORDER BY wincounter.wins DESC;