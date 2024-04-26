from database import Base, engine

def create_database():
    print("Creating database tables...")
    # Creating all tables defined in Base metadata
    Base.metadata.create_all(bind=engine)
    print("Database tables created successfully!")