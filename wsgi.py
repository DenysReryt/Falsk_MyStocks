from pathlib import Path
from dotenv import load_dotenv

env_file = Path('.env')
load_dotenv(dotenv_path=env_file)

from stocks.main import app

if __name__ == '__main__':
    app.run()

# gunicorn -w 4 wsgi:app -b localhost:5000
