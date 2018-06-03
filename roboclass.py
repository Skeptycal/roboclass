from app import app
from config import Client

@app.shell_context_processor
def make_shell_context():
    return {'db': Client.db}