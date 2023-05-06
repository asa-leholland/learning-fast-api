from raven import Client

from app.core.config import settings

client_sentry = Client(settings.SENTRY_DSN)

