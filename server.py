"""Entry point for the API server."""
from app import app
from settings import PORT

app.run(host='0.0.0.0',port=PORT)
