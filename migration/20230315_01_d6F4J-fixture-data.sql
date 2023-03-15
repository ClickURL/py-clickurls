-- Fixture data
-- depends: 

CREATE TABLE IF NOT EXISTS users (
    user_id SERIAL,
    username VARCHAR(100) NOT NULL,
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP,
    deleted_at TIMESTAMP,
    PRIMARY KEY (user_id)
);
INSERT INTO users (username) VALUES ('Anton'), ('Oleg'), ('Kaban');

CREATE TABLE IF NOT EXISTS urls (
    url_id SERIAL,
    original_url TEXT NOT NULL,
    token VARCHAR(20),
    created_at TIMESTAMP DEFAULT NOW(),
    updated_at TIMESTAMP,
    deleted_at TIMESTAMP,
    creator_id INTEGER,
    PRIMARY KEY (url_id),
    FOREIGN KEY (creator_id) REFERENCES users(user_id) ON DELETE RESTRICT
);
INSERT INTO urls (original_url, token, creator_id) VALUES 
('first url', 'test-token-1', 1),
('second url', 'test-token-2', 2),
('fourth url', 'test-token-3', 3);