from sqlalchemy import create_engine, Column, Integer, String
from sqlalchemy.orm import declarative_base, sessionmaker

# Crear el motor de la base de datos
engine = create_engine('mysql+pymysql://root:admin@localhost:3306/academia2', echo=True) # Base de datos en disco

# Definiar la clase base
Base = declarative_base()

# Definir la clase que representa la tabla
class Usuarios(Base):
    __tablename__ = 'usuarios'
    id = Column(Integer, primary_key=True, autoincrement=True)
    nombre = Column(String(50))
    edad = Column(Integer)

    def __repr__(self):
        return f"<Usuario(nombre='{self.nombre}', edad={self.edad})>"
    
# Crear las tablas en la base de datos
Base.metadata.create_all(engine)

# Crear una sesión para interactuar con la base de datos
Session = sessionmaker(bind=engine)
session = Session()

# Crear un nuevo usuario en la base de datos manera 1
'''
print("Menu")
print("Ingresar nuevo usuario")
inputNombre = input("Nombre: ")
inputEdad = input("Edad: ")

nuevo_usuario = Usuarios(nombre=inputNombre, edad=inputEdad)

# Agregar el nuevo usuario a la sesión
session.add(nuevo_usuario)
session.commit()
'''
# Crear un nuevo usuario en la base de datos manera 2
usuario1 = Usuarios(nombre="Juan", edad=30)
usuario2 = Usuarios(nombre="Maria", edad=25)

session.add_all([usuario1, usuario2])
session.commit()

# Consultar todos los usuarios
usuarios = session.query(Usuarios).all()
for usuario in usuarios:
    print(usuario)