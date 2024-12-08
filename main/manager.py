from flask.cli import FlaskGroup
from main import app, db

# Create a custom Flask CLI manager
manager = FlaskGroup(app)

# Initialize the database with a custom CLI command
@manager.command
def db_init():
    """Initialize the database."""
    db.create_all()

if __name__ == "__main__":
    manager()
