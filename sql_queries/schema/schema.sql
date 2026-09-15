CREATE TABLE users (
    user_id VARCHAR(20) PRIMARY KEY,
    location VARCHAR(100),
    language VARCHAR(10),
    account_created DATE,
    follower_count INTEGER
);

CREATE TABLE posts (
    post_id VARCHAR(20) PRIMARY KEY,
    user_id VARCHAR(20) NOT NULL,
    platform VARCHAR(20),
    text_content TEXT,
    timestamp TIMESTAMP NOT NULL,
    likes NUMERIC,
    shares INTEGER NOT NULL,
    comments INTEGER NOT NULL,
    CONSTRAINT fk_posts_user
        FOREIGN KEY (user_id)
        REFERENCES users(user_id)
);