-- Table definitions for the tournament project.
--
-- Put your SQL 'create table' statements in this file; also 'create view'
-- statements if you choose to use it.
--
-- You can write comments in this file by starting them with two dashes, like
-- these lines here.


DROP DATABASE IF EXISTS tournament;
CREATE DATABASE tournament;

-- Connecting to the database tournament
\c tournament


CREATE TABLE players(
    -- tournament varchar(3),
    id serial PRIMARY KEY,
    name TEXT NOT NULL,
    wins integer NOT NULL,
    losses integer NOT NULL
);

CREATE TABLE matches(
    id serial PRIMARY KEY,
    round_number serial,
    player_one_id serial NOT NULL REFERENCES players (id), -- referential integrity with the playerstable
    player_two_id serial NOT NULL REFERENCES players (id),
    winner_id serial NOT NULL REFERENCES players (id)
);


-- view for standings

CREATE VIEW standings as
    select
        id,
        name,
        wins,
        (wins + losses) as match_total

    from players
    order by wins;

-- view for ranking and deciding the bye distribution based on the wins and id of the players

CREATE VIEW ranking as
    select
        id,
        name,
        wins,
        RANK() OVER (ORDER BY wins DESC, id ASC) as rank
    from players
    order by rank;


-- swiss pairing for the fixture of matches along with the ranking view
create view swiss_pair as
    select
        a.id,
        a.name,
        b.id as opp_id,
        b.name as opp_win
    from
        ranking as a,
        ranking as b
    where
        a.id != b.id
        and
        a.rank = (b.rank - 1)
        and
        mod(a.rank, 2) = 1
    order by
        a.rank,
        a.id;





