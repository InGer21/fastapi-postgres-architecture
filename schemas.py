from pydantic import BaseModel

class EmpresaResponse(BaseModel):
    id: int
    nombre: str
    presupuesto_usd: float

    class Config:
        from_attributes = True 

class EmpleadoBase(BaseModel):
    nombre: str
    sueldo_usd: float
    empresa_id: int | None = None  
    
    class Config:
        from_attributes = True

class EmpleadoResponse(EmpleadoBase):
    empresa: EmpresaResponse | None = None

class EmpresaConEmpleados(EmpresaResponse):
    empleados: list[EmpleadoBase]