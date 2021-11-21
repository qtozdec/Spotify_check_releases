from pathlib import Path
from environs import Env

env = Env()
env.read_env()


BOT_TOKEN = env.str("BOT_TOKEN")
SKIP_UPDATES = env.bool("SKIP_UPDATES", False)
WORK_PATH: Path = Path(__file__).parent.parent

ADMINS_ID = env.list("ADMINS_ID")

SPOTIFY_CLIENT_ID = env.str("SPOTIFY_CLIENT_ID")
SPOTIFY_CLIENT_SECRET = env.str("SPOTIFY_CLIENT_SECRET")
SPOTIFY_REDIRECT_URI = env.str("SPOTIFY_REDIRECT_URI")
SPOTIFY_USER_REFRESH = env.str("SPOTIFY_USER_REFRESH")
