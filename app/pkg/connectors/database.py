import asyncpg
from contextlib import asynccontextmanager
from asyncpg import Connection

from .base_connector import BaseConnector

__all__ = ["Database"]


class Database(BaseConnector):
    def __init__(self, dsn: str):
        self.dsn = dsn

    async def connect(self) -> Connection:
        """Initialize the connection."""
        return await asyncpg.connect(dsn=self.dsn)

    @asynccontextmanager
    async def get_connection(self) -> Connection:
        """Acquire a connection."""
        conn = await self.connect()
        yield conn
        await conn.close()
