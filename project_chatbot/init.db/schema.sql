CREATE TABLE chat_history (
    session_id VARCHAR(255) PRIMARY KEY,
    msg_type VARCHAR(50) NOT NULL,
    message TEXT NOT NULL,
    regdate DATETIME DEFAULT CURRENT_TIMESTAMP
);