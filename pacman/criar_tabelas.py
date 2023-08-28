from config import *
from classes import *
if os.path.exists(arquivobd):
    os.remove(arquivobd)
    
db.create_all()

print("Tabelas criadas")
