from app.pkg.settings import settings
from app.pkg.di import factory

from .database import Database

__all__ = ["Connectors"]


class Connectors:
    #: Database: Connector to database.
    database = factory(
        Database,
        dsn=settings.POSTGRES.DSN,
    )
