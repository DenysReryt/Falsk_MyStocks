from pathlib import Path
from dotenv import load_dotenv

env_file = Path('./.env')
load_dotenv(dotenv_path=env_file)
