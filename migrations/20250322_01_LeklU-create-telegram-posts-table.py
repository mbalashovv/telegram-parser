"""
create telegram_posts table
"""

from yoyo import step

__depends__ = {}

steps = [
    step("""
        CREATE TABLE telegram_posts (
          id SERIAL PRIMARY KEY,
          channel_id TEXT NOT NULL,
          message_id BIGINT NOT NULL,
          published_at TIMESTAMP NOT NULL,
          text TEXT,
          views INTEGER,
          collected_at TIMESTAMP DEFAULT NOW()
        );
    """,
    """
        DROP TABLE IF EXISTS telegram_posts;
    """)
]
