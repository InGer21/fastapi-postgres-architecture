from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
import models
import schemas
from database import engine, get_db

# Initialize database metadata
models.Base.metadata.create_all(bind=engine)

app = FastAPI(title="Backend Master API")

@app.get("/")
def home():
    return {"message": "FastAPI server running with PostgreSQL"}

@app.get("/empleados/", response_model=list[schemas.EmpleadoResponse])
def obtener_empleados(db: Session = Depends(get_db)):
    empleados = db.query(models.Empleado).all()
    return empleados

@app.get("/empresas/{empresa_id}", response_model=schemas.EmpresaConEmpleados)
def obtener_empresa(empresa_id: int, db: Session = Depends(get_db)):
    empresa = db.query(models.Empresa).filter(models.Empresa.id == empresa_id).first()
    if empresa is None:
        raise HTTPException(status_code=404, detail="Company not found")
    return empresa