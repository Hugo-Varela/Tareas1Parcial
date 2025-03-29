import sqlite3
conexion=sqlite3.connect("Matricula(CURC).db")
cursor=conexion.cursor()
try:
    #CREACION TABLA ESTUDIANTES
    cursor.execute("""create table Estudiantes
                   (ID_Alumno integer primary key,
                    Nombre text,
                    Apellido text,
                    Telefono integer,
                    Direccion text)""")
    print("Tabla Estudiantes Creada...")
    
    #CREACION TABLA MAESTROS
    cursor.execute("""create table Maestros
                   (ID_Maestro integer primary key,
                    Nombre text,
                    Apellido text,
                    Telefono integer,
                    Direccion text)""")
    print("Tabla Maestros Creada...")
    
    #CREACION DE TABLA SECCIONES
    cursor.execute("""CREATE TABLE Secciones (
            ID_Seccion INTEGER PRIMARY KEY AUTOINCREMENT,
            ID_Docente INTEGER,
            ID_Clase INTEGER,
            Hora_Inicio TEXT,
            Hora_Fin TEXT,
            FOREIGN KEY (ID_Docente) REFERENCES Docentes(ID_Docente) ON DELETE CASCADE,
            FOREIGN KEY (ID_Clase) REFERENCES Clases(ID_Clase) ON DELETE CASCADE);""")
    
    #CREACION DE TABLA MATRICULA
    cursor.execute("""CREATE TABLE Matricula (
            ID_Matricula INTEGER PRIMARY KEY AUTOINCREMENT,
            ID_Alumno INTEGER,
            ID_Seccion INTEGER,
            FOREIGN KEY(ID_Alumno) REFERENCES Alumnos(ID_Alumno) ON DELETE CASCADE,
            FOREIGN KEY(ID_Seccion) REFERENCES Secciones(ID_Seccion) ON DELETE CASCADE);""")

    
    #CREACION DE TABLA CLASES
    cursor.execute("""create table Clases(
            ID_Clase integer primary key autoincrement,
            Nombre_Clase text);""")

    conexion.commit()
    print("Tabla Alumnos creada...")
    print("Tabla Maestros creada...")
    print("Tabla Secciones creada...")
    print("Tabla Matricula creada...")
    print("Tabla Clases creada...")
except sqlite3.OperationalError:
    print("")

