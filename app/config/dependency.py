from app.config.database import SessionLocal


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_url_api():
    return "http://localhost:8080/api"
