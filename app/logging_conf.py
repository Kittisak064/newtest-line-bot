import logging, os

def configure_logging():
    level = logging.DEBUG if os.getenv("APP_ENV","dev")=="dev" else logging.INFO
    logging.basicConfig(
        level=level,
        format="%(asctime)s [%(levelname)s] %(name)s :: %(message)s"
    )
