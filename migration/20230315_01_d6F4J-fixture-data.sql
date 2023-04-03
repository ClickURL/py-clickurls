-- Fixture data
-- depends: 

CREATE TABLE IF NOT EXISTS users (
    user_id SERIAL,
    user_name VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP,
    deleted_at TIMESTAMP,
    PRIMARY KEY (user_id)
);
INSERT INTO users (user_name) VALUES ('Anton'), ('Oleg'), ('Kaban');

CREATE TABLE IF NOT EXISTS urls (
    url_id SERIAL,
    original_url TEXT NOT NULL,
    short_url TEXT NOT NULL,
    secret_access_token uuid,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP,
    deleted_at TIMESTAMP,
    creator_id INTEGER,
    PRIMARY KEY (url_id),
    FOREIGN KEY (creator_id) REFERENCES users(user_id) ON DELETE RESTRICT
);
INSERT INTO urls (original_url, short_url, secret_access_token, creator_id) VALUES 
('https://fastapi.tiangolo.com/', '12345', 'a8098c1a-f86e-11da-bd1a-00112444be1e', 1),
('https://plotly.com/graphing-libraries/', '54321', 'a8098c1a-f86e-11da-bd1a-00112444be2e', 2),
('https://docs.pydantic.dev/', 'qwert', 'a8098c1a-f86e-11da-bd1a-00112444be3e', 3);

CREATE TABLE IF NOT EXISTS prohibited_domain (
    domain_id SERIAL,
    domain TEXT NOT NULL,
    PRIMARY KEY (domain_id)
);
INSERT INTO prohibited_domain (domain) VALUES
('www.google.com'),
('www.facebook.com'),
('tsn.ua');

CREATE TABLE IF NOT EXISTS hour_views (
    view_id SERIAL,
    time TIMESTAMP DEFAULT NOW(),
    link_id INTEGER,
    PRIMARY KEY (view_id),
    FOREIGN KEY (link_id) REFERENCES urls(url_id) ON DELETE CASCADE
);
INSERT INTO hour_views (time, link_id) VALUES
('2023-03-01 19:10:25.176803', '1'),
('2023-03-02 19:10:25.176803', '1'),
('2023-03-03 19:10:25.176803', '1'),
('2023-03-03 19:11:25.176803', '1'),
('2023-03-04 19:11:25.176803', '1'),
('2023-03-04 19:12:25.176803', '1'),
('2023-03-05 19:10:25.176803', '1'),
('2023-03-06 19:11:25.176803', '1'),
('2023-03-07 19:11:25.176803', '1'),
('2023-03-07 19:14:25.176803', '1'),
('2023-03-07 20:11:25.176803', '1'),
('2023-03-07 21:11:25.176803', '1'),
('2023-03-07 22:11:25.176803', '1'),
('2023-03-08 10:12:25.176803', '1'),
('2023-03-08 11:12:25.176803', '1'),
('2023-03-08 12:12:25.176803', '1'),
('2023-03-08 13:12:25.176803', '1'),
('2023-03-08 14:12:25.176803', '1'),
('2023-03-13 10:12:25.176803', '1'),
('2023-03-13 11:12:25.176803', '1'),
('2023-03-13 12:12:25.176803', '1'),
('2023-03-14 13:12:25.176803', '1'),
('2023-03-15 14:12:25.176803', '1'),
('2023-03-16 10:12:25.176803', '1'),
('2023-03-16 11:12:25.176803', '1'),
('2023-03-16 12:12:25.176803', '1'),
('2023-03-16 13:12:25.176803', '1'),
('2023-03-16 14:12:25.176803', '1'),
('2023-03-17 12:12:25.176803', '1'),
('2023-03-18 13:12:25.176803', '1'),
('2023-03-19 14:12:25.176803', '1'),
('2023-03-20 14:12:25.176803', '1'),
('2023-03-20 14:12:25.176803', '1'),
('2023-03-21 14:12:25.176803', '1'),
('2023-03-22 14:12:25.176803', '1'),
('2023-03-23 14:12:25.176803', '1'),
('2023-03-24 14:12:25.176803', '1'),
('2023-03-25 14:12:25.176803', '1'),
('2023-03-26 14:12:25.176803', '1'),
('2023-03-26 15:12:25.176803', '1'),
('2023-03-26 16:12:25.176803', '1'),
('2023-03-26 17:12:25.176803', '1'),
('2023-03-27 14:12:25.176803', '1'),
('2023-03-27 15:12:25.176803', '1'),
('2023-03-27 16:12:25.176803', '1'),
('2023-03-27 17:12:25.176803', '1'),
('2023-03-27 18:12:25.176803', '1'),
('2023-03-27 19:12:25.176803', '1'),
('2023-03-27 20:12:25.176803', '1'),
('2023-03-27 21:12:25.176803', '1'),
('2023-03-27 21:13:25.176803', '1'),
('2023-03-27 21:23:25.176803', '1'),
('2023-03-27 21:25:25.176803', '1'),
('2023-03-27 21:44:25.176803', '1'),
('2023-03-27 22:12:25.176803', '1'),
('2023-03-27 22:22:25.176803', '1'),
('2023-03-27 22:32:25.176803', '1'),
('2023-03-27 22:42:25.176803', '1'),
('2023-03-28 15:12:25.176803', '1'),
('2023-03-28 16:12:25.176803', '1'),
('2023-03-29 17:12:25.176803', '1'),
('2023-03-29 18:12:25.176803', '1'),
('2023-03-29 19:12:25.176803', '1'),
('2023-03-30 11:12:25.176803', '1'),
('2023-03-31 11:12:25.176803', '1'),
('2023-03-31 11:16:25.176803', '1'),
('2023-03-31 11:18:25.176803', '1'),
('2023-03-31 11:40:25.176803', '1'),
('2023-03-01 19:10:25.176803', '2'),
('2023-03-02 19:10:25.176803', '2'),
('2023-03-03 19:10:25.176803', '3'),
('2023-03-03 19:11:25.176803', '2'),
('2023-03-04 19:11:25.176803', '2'),
('2023-03-04 19:12:25.176803', '3'),
('2023-03-05 19:10:25.176803', '2'),
('2023-03-06 19:11:25.176803', '2'),
('2023-03-07 19:11:25.176803', '2'),
('2023-03-07 19:14:25.176803', '3'),
('2023-03-07 20:11:25.176803', '3'),
('2023-03-07 21:11:25.176803', '3'),
('2023-03-07 22:11:25.176803', '2'),
('2023-03-08 10:12:25.176803', '3'),
('2023-03-08 11:12:25.176803', '2'),
('2023-03-08 12:12:25.176803', '3'),
('2023-03-08 13:12:25.176803', '2'),
('2023-03-08 14:12:25.176803', '3'),
('2023-03-13 10:12:25.176803', '2'),
('2023-03-13 11:12:25.176803', '3'),
('2023-03-13 12:12:25.176803', '2'),
('2023-03-14 13:12:25.176803', '3'),
('2023-03-15 14:12:25.176803', '2'),
('2023-03-16 10:12:25.176803', '3'),
('2023-03-16 11:12:25.176803', '2'),
('2023-03-16 12:12:25.176803', '3'),
('2023-03-16 13:12:25.176803', '2'),
('2023-03-16 14:12:25.176803', '3'),
('2023-03-17 12:12:25.176803', '3'),
('2023-03-18 13:12:25.176803', '3'),
('2023-03-19 14:12:25.176803', '3'),
('2023-03-20 14:12:25.176803', '3'),
('2023-03-20 14:12:25.176803', '2'),
('2023-03-21 14:12:25.176803', '2'),
('2023-03-22 14:12:25.176803', '2'),
('2023-03-23 14:12:25.176803', '2'),
('2023-03-24 14:12:25.176803', '3'),
('2023-03-25 14:12:25.176803', '3'),
('2023-03-26 14:12:25.176803', '3'),
('2023-03-26 15:12:25.176803', '2'),
('2023-03-26 16:12:25.176803', '2'),
('2023-03-26 17:12:25.176803', '2'),
('2023-03-27 14:12:25.176803', '2'),
('2023-03-27 15:12:25.176803', '2'),
('2023-03-27 16:12:25.176803', '3'),
('2023-03-27 17:12:25.176803', '2'),
('2023-03-27 18:12:25.176803', '2'),
('2023-03-27 19:12:25.176803', '2'),
('2023-03-27 20:12:25.176803', '2'),
('2023-03-27 21:12:25.176803', '2'),
('2023-03-27 21:13:25.176803', '2'),
('2023-03-27 21:23:25.176803', '3'),
('2023-03-27 21:25:25.176803', '2'),
('2023-03-27 21:44:25.176803', '3'),
('2023-03-27 22:12:25.176803', '3'),
('2023-03-27 22:22:25.176803', '3'),
('2023-03-27 22:32:25.176803', '3'),
('2023-03-27 22:42:25.176803', '3'),
('2023-03-28 15:12:25.176803', '3'),
('2023-03-28 16:12:25.176803', '3'),
('2023-03-29 17:12:25.176803', '3'),
('2023-03-29 18:12:25.176803', '2'),
('2023-03-29 19:12:25.176803', '2'),
('2023-03-30 11:12:25.176803', '2'),
('2023-03-31 11:12:25.176803', '2'),
('2023-03-31 11:16:25.176803', '3'),
('2023-03-31 11:18:25.176803', '3'),
('2023-03-31 11:40:25.176803', '2')