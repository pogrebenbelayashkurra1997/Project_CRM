from fastapi import FastAPI
from app.routers import contacts, leads, stats
from app.db import Base, engine

Base.metadata.create_all(bind=engine)

app = FastAPI(title="Mini CRM")

app.include_router(contacts.router)
app.include_router(leads.router)
app.include_router(stats.router)
