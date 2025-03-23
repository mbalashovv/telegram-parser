from contextlib import asynccontextmanager
from asyncpg import Connection

from app.pkg.connectors import Connectors
from app.pkg.connectors.database import Database
from app.pkg.di import inject

__all__ = ["get_connection"]


@asynccontextmanager
async def get_connection(
    database: Database = inject(Connectors.database),
) -> Connection:
    """Get async connection to PostgreSQL pool."""
    async with database.get_connection() as conn:
        yield conn
