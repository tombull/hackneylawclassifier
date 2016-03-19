"""Entry point for the API server."""
from app import app
from settings import PORT

app.run(port=PORT)
