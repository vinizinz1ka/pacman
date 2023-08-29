from config import *
from backend.rotas import *

with app.app_context():
    db.create_all()
    CORS(app)
    app.run(debug=True, host="0.0.0.0")