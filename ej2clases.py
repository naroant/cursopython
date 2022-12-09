class Alumno():
    nombre = ""
    nota = 0
    def inicializar(self,nombreAlumno,notaAlumno):
        self.nombre = nombreAlumno
        self.nota = notaAlumno

    def mostrarAtributos(self):
        print("Nombre del alumno/a:",self.nombre)
        print("Nota:",self.nota)
    def mostrarAprobado(self):
        if self.nota>=5:
            aprobado = True
            print("Su nota es",self.nota,", por lo que ha aprobado.")
        else:
            aprobado = False
            print("Su nota es",self.nota,", por lo que ha suspendido.")

alumno1 = Alumno()
alumno1.inicializar("Maria",6.7)
alumno1.mostrarAtributos()
alumno1.mostrarAprobado()
