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
    short_Url TEXT NOT NULL,
    token uuid,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP,
    deleted_at TIMESTAMP,
    creator_id INTEGER,
    PRIMARY KEY (url_id),
    FOREIGN KEY (creator_id) REFERENCES users(user_id) ON DELETE RESTRICT
);
INSERT INTO urls (original_url, short_url, token, creator_id) VALUES 
('first url', 'first_short_code', 'a8098c1a-f86e-11da-bd1a-00112444be1e', 1),
('second url', 'second_short_code', 'a8098c1a-f86e-11da-bd1a-00112444be2e', 2),
('third url', 'third_short_code', 'a8098c1a-f86e-11da-bd1a-00112444be3e', 3);