from sqlalchemy import Column, Integer, String, Numeric, ForeignKey
from sqlalchemy.orm import relationship
from database import Base

class Empresa(Base):
    __tablename__ = "empresa" 

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    presupuesto_usd = Column(Numeric(15, 2), default=100000.00)

    empleados = relationship("Empleado", back_populates="empresa")


class Empleado(Base):
    __tablename__ = "empleados"

    id = Column(Integer, primary_key=True, index=True)
    nombre = Column(String(100), nullable=False)
    sueldo_usd = Column(Numeric(10, 2), nullable=False)
    empresa_id = Column(Integer, ForeignKey("empresa.id"))

    empresa = relationship("Empresa", back_populates="empleados")
