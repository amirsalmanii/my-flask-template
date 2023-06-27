import os
from dotenv import load_dotenv
from loguru import logger
from flask_migrate import Migrate
from app import create_app, db

load_dotenv()

app_config = os.environ.get('FLASK_CONFIG') or 'default'
logger.debug(f"CONFIG {app_config} IS RUNNING NOW!")
app = create_app(app_config)
migrate = Migrate(app, db)


@app.shell_context_processor
def make_shell_context():
   # you can add your models here for flask shell import auto
   return dict(db=db)