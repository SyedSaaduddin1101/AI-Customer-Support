from database import Base, engine

# This will drop all tables and recreate them
print("Dropping all tables...")
Base.metadata.drop_all(bind=engine)

print("Creating all tables...")
Base.metadata.create_all(bind=engine)

print("Database reset complete!")
