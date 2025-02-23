CREATE TABLE news_headlines (
    id SERIAL PRIMARY KEY,
    headline TEXT NOT NULL,
    conspiracy_score FLOAT NOT NULL,
    suspicious_words JSONB,
    created_at TIMESTAMP DEFAULT CURRENT_TIMESTAMP
);
