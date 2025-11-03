from flask_sqlalchemy import SQLAlchemy

db = SQLAlchemy()

# import models ที่อยู่ในโฟลเดอร์เดียวกัน
from .user import user