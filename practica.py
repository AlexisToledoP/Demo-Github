# =====================================================
# SISTEMA DE GESTION
# POSTA DE SALUD SANTA ROSA SJL
# =====================================================


# =====================================================
# CLASE PERSONA
# =====================================================

# Esta es la clase padre.
# Sirve como base para crear pacientes y medicos.
# Contiene los datos que ambos tienen en comun.

class Persona:

    # El metodo __init__ se ejecuta al crear una persona.
    # self representa al objeto que estamos creando.
    # nombre y dni son los datos que recibimos.

    def __init__(self, nombre, dni):

        # Guardamos el nombre en el objeto.
        self.nombre = nombre

        # Los dos guiones bajos indican que DNI
        # es un atributo privado.
        self.__dni = dni

    # Este metodo permite consultar el DNI
    # sin acceder directamente al atributo privado.

    def obtener_dni(self):

        # return devuelve el valor del DNI.
        return self.__dni


# =====================================================
# CLASE PACIENTE
# =====================================================

# Paciente hereda de Persona.
# Esto significa que recibe sus atributos y metodos.
# Ademas, tiene telefono y edad.

class Paciente(Persona):

    # Constructor de la clase Paciente.
    # Recibe nombre, DNI, telefono y edad.

    def __init__(self, nombre, dni, telefono, edad):

        # super() permite llamar al constructor
        # de la clase padre Persona.
        # Asi guardamos el nombre y el DNI.

        super().__init__(nombre, dni)

        # Guardamos los datos propios del paciente.
        self.telefono = telefono
        self.edad = edad

    # Este metodo organiza la informacion del paciente
    # para mostrarla de forma ordenada.

    def mostrar_informacion(self):

        # return devuelve un texto con los datos.
        # La letra f permite insertar variables
        # dentro del texto usando llaves.

        return (
            f"Paciente: {self.nombre} | "
            f"DNI: {self.obtener_dni()} | "
            f"Telefono: {self.telefono} | "
            f"Edad: {self.edad}"
        )


# =====================================================
# CLASE MEDICO
# =====================================================

# Medico tambien hereda de Persona.
# Recibe los datos comunes de Persona
# y agrega especialidad y codigo.

class Medico(Persona):

    # Constructor de la clase Medico.

    def __init__(self, nombre, dni, especialidad, codigo):

        # Llamamos al constructor de la clase padre.
        # Guarda el nombre y el DNI del medico.

        super().__init__(nombre, dni)

        # Guardamos los datos propios del medico.
        self.especialidad = especialidad
        self.codigo = codigo

    # Metodo para mostrar los datos del medico.

    def mostrar_informacion(self):

        # Devolvemos todos los datos en un solo texto.

        return (
            f"Medico: {self.nombre} | "
            f"DNI: {self.obtener_dni()} | "
            f"Especialidad: {self.especialidad} | "
            f"Codigo: {self.codigo}"
        )


# =====================================================
# CLASE CITA
# =====================================================

# Esta clase representa una cita medica.
# Relaciona a un paciente con un medico.
# Tambien guarda la fecha y la hora de la cita.

class Cita:

    # Constructor de la clase Cita.
    # Recibe los objetos paciente y medico,
    # ademas de la fecha y la hora.

    def __init__(self, paciente, medico, fecha, hora):

        # Guardamos el objeto paciente.
        self.paciente = paciente

        # Guardamos el objeto medico.
        self.medico = medico

        # Guardamos la fecha y la hora.
        self.fecha = fecha
        self.hora = hora

    # Metodo para mostrar la informacion de una cita.

    def mostrar_cita(self):

        # Accedemos a los datos del paciente y del medico
        # que estan relacionados con esta cita.

        return (
            f"Paciente: {self.paciente.nombre} | "
            f"Medico: {self.medico.nombre} | "
            f"Especialidad: {self.medico.especialidad} | "
            f"Fecha: {self.fecha} | "
            f"Hora: {self.hora}"
        )


# =====================================================
# CLASE POSTASALUD
# =====================================================

# Esta clase administra el funcionamiento de la posta.
# Permite registrar, buscar y mostrar informacion.
# Tambien guarda las listas de pacientes, medicos y citas.

class PostaSalud:

    # Constructor de la clase.
    # Recibe el nombre del establecimiento.

    def __init__(self, nombre):

        # Guardamos el nombre de la posta.
        self.nombre = nombre

        # Creamos tres listas vacias.
        # Las listas almacenaran los objetos registrados.
        # Al inicio no hay ningun registro.

        self.pacientes = []
        self.medicos = []
        self.citas = []

    # -------------------------------------------------
    # REGISTRAR PACIENTE
    # -------------------------------------------------

    # Este metodo recibe un objeto paciente
    # y lo agrega a la lista de pacientes.

    def registrar_paciente(self, paciente):

        # append() agrega un elemento al final de la lista.
        self.pacientes.append(paciente)

        # Mensaje que confirma el registro.
        print("\nPaciente registrado correctamente.")

    # -------------------------------------------------
    # REGISTRAR MEDICO
    # -------------------------------------------------

    # Este metodo recibe un objeto medico
    # y lo agrega a la lista de medicos.

    def registrar_medico(self, medico):

        # Agregamos el medico a la lista.
        self.medicos.append(medico)

        # Mostramos un mensaje de confirmacion.
        print("\nMedico registrado correctamente.")

    # -------------------------------------------------
    # REGISTRAR CITA
    # -------------------------------------------------

    # Este metodo recibe una cita
    # y la guarda en la lista de citas.

    def registrar_cita(self, cita):

        # Agregamos la cita a la lista.
        self.citas.append(cita)

        # Mensaje de confirmacion.
        print("\nCita registrada correctamente.")

    # -------------------------------------------------
    # BUSCAR PACIENTE
    # -------------------------------------------------

    # Este metodo busca un paciente por su DNI.
    # Recibe el DNI que queremos encontrar.

    def buscar_paciente(self, dni):

        # Recorremos todos los pacientes registrados.
        # paciente representa cada elemento de la lista.

        for paciente in self.pacientes:

            # Comparamos el DNI buscado con el DNI
            # de cada paciente.

            if paciente.obtener_dni() == dni:

                # Si coinciden, devolvemos el paciente.
                return paciente

        # Si termina el recorrido y no lo encuentra,
        # devolvemos None.
        # None significa que no se encontro el paciente.

        return None

    # -------------------------------------------------
    # MOSTRAR PACIENTES
    # -------------------------------------------------

    # Este metodo muestra todos los pacientes registrados.

    def mostrar_pacientes(self):

        # Titulo de la lista.
        print("\n==== LISTA DE PACIENTES ====")

        # len() cuenta cuantos elementos tiene una lista.
        # Si la cantidad es 0, no hay pacientes.

        if len(self.pacientes) == 0:

            print("No existen pacientes registrados.")

        else:

            # Recorremos la lista de pacientes.
            # Mostramos los datos de cada uno.

            for paciente in self.pacientes:

                print(paciente.mostrar_informacion())

    # -------------------------------------------------
    # MOSTRAR MEDICOS
    # -------------------------------------------------

    # Este metodo muestra todos los medicos registrados.

    def mostrar_medicos(self):

        print("\n==== LISTA DE MEDICOS ====")

        # Comprobamos si la lista esta vacia.

        if len(self.medicos) == 0:

            print("No existen medicos registrados.")

        else:

            # Recorremos la lista y mostramos
            # la informacion de cada medico.

            for medico in self.medicos:

                print(medico.mostrar_informacion())

    # -------------------------------------------------
    # MOSTRAR CITAS
    # -------------------------------------------------

    # Este metodo muestra todas las citas registradas.

    def mostrar_citas(self):

        print("\n==== CITAS MEDICAS ====")

        # Revisamos si existen citas en la lista.

        if len(self.citas) == 0:

            print("No existen citas registradas.")

        else:

            # Recorremos la lista de citas.
            # Mostramos los datos de cada cita.

            for cita in self.citas:

                print(cita.mostrar_cita())

    # -------------------------------------------------
    # GENERAR REPORTE
    # -------------------------------------------------

    # Este metodo muestra un resumen de los registros
    # que tiene la posta.

    def generar_reporte(self):

        print("\n-------------------------")
        print("    REPORTE DE LA POSTA")
        print("-------------------------")

        # Mostramos el nombre del establecimiento.
        print("Establecimiento:", self.nombre)

        # len() cuenta los elementos de cada lista.
        # Asi sabemos cuantos pacientes, medicos y citas
        # se encuentran registrados.

        print("Total de pacientes:", len(self.pacientes))
        print("Total de medicos:", len(self.medicos))
        print("Total de citas:", len(self.citas))


# =====================================================
# PROGRAMA PRINCIPAL
# =====================================================

# Creamos el objeto principal de la posta.
# Este objeto administrara todas las listas
# y los metodos de la clase PostaSalud.

posta = PostaSalud("Posta de Salud Santa Rosa SJL")

# REGISTRO INICIAL DE 5 MEDICOS

medico1 = Medico(
    "Dr. Carlos Flores",
    "41873233",
    "Medicina General",
    "MED001"
)

medico2 = Medico(
    "Dra. Elena Vargas",
    "42789862",
    "Oftalmologia",
    "MED002"
)

medico3 = Medico(
    "Dr. Miguel Torres",
    "45678912",
    "Medicina Interna",
    "MED003"
)

medico4 = Medico(
    "Dra. Rosa Mendoza",
    "46789123",
    "Ginecologia",
    "MED004"
)

medico5 = Medico(
    "Dr. Luis Ramirez",
    "47891234",
    "Odontologia",
    "MED005"
)

# Agregamos los 5 medicos a la posta

posta.registrar_medico(medico1)
posta.registrar_medico(medico2)
posta.registrar_medico(medico3)
posta.registrar_medico(medico4)
posta.registrar_medico(medico5)


# =====================================================
# FUNCION PARA REGISTRAR PACIENTE
# =====================================================

# Esta funcion pide los datos del paciente
# directamente desde la consola.

def registrar_paciente():

    print("\n==== REGISTRAR PACIENTE ====")

    # input() muestra un mensaje y espera
    # a que el usuario escriba un dato.
    # El dato ingresado se guarda en una variable.

    nombre = input("Ingrese el nombre del paciente: ")
    dni = input("Ingrese el DNI: ")

    # Buscamos si ya existe un paciente con ese DNI.
    # Llamamos al metodo buscar_paciente de la posta.

    paciente_existente = posta.buscar_paciente(dni)

    # Si el resultado no es None,
    # significa que ya hay un paciente con ese DNI.

    if paciente_existente != None:

        print("Este paciente ya esta registrado.")

    else:

        # Si no existe, pedimos los otros datos.

        telefono = input("Ingrese el telefono: ")
        edad = input("Ingrese la edad: ")

        # Creamos un nuevo objeto Paciente
        # utilizando los datos ingresados.

        paciente = Paciente(nombre, dni, telefono, edad)

        # Llamamos al metodo para agregar el paciente
        # a la lista de la posta.

        posta.registrar_paciente(paciente)


# =====================================================
# FUNCION PARA REGISTRAR MEDICO
# =====================================================

# Esta funcion solicita los datos de un medico
# mediante la consola.

def registrar_medico():

    print("\n==== REGISTRAR MEDICO ====")

    # Pedimos los datos del medico.

    nombre = input("Ingrese el nombre del medico: ")
    dni = input("Ingrese el DNI: ")
    especialidad = input("Ingrese la especialidad: ")
    codigo = input("Ingrese el codigo del medico: ")

    # Creamos el objeto Medico con los datos ingresados.

    medico = Medico(nombre, dni, especialidad, codigo)

    # Enviamos el objeto al metodo de registro.
    # El metodo lo agrega a la lista de medicos.

    posta.registrar_medico(medico)


# =====================================================
# FUNCION PARA REGISTRAR CITA
# =====================================================

# Esta funcion permite registrar una cita.
# Para hacerlo, primero necesitamos un paciente
# y un medico que ya esten registrados.

def registrar_cita():

    print("\n==== REGISTRAR CITA ====")

    # Comprobamos si hay pacientes registrados.
    # Si la lista esta vacia, no podemos crear la cita.

    if len(posta.pacientes) == 0:

        print("Primero debe registrar un paciente.")

        # return termina la funcion en este punto.
        return

    # Comprobamos si hay medicos registrados.

    if len(posta.medicos) == 0:

        print("Primero debe registrar un medico.")
        return

    # Pedimos el DNI del paciente que tendra la cita.

    dni = input("Ingrese el DNI del paciente: ")

    # Buscamos al paciente utilizando su DNI.

    paciente = posta.buscar_paciente(dni)

    # Si no se encuentra al paciente,
    # mostramos un mensaje y terminamos la funcion.

    if paciente == None:

        print("Paciente no encontrado.")
        return

    # Mostramos la lista de medicos disponibles.

    print("\n==== MEDICOS DISPONIBLES ====")
    posta.mostrar_medicos()

    # Pedimos el codigo del medico elegido.

    codigo = input("\nIngrese el codigo del medico: ")

    # Creamos una variable vacia para guardar
    # al medico que encontremos.

    medico_encontrado = None

    # Recorremos la lista de medicos registrados.

    for medico in posta.medicos:

        # Comparamos el codigo ingresado
        # con el codigo de cada medico.

        if medico.codigo == codigo:

            # Si coinciden, guardamos el objeto medico.
            medico_encontrado = medico

    # Si no encontramos un medico con ese codigo,
    # mostramos un mensaje y terminamos.

    if medico_encontrado == None:

        print("Medico no encontrado.")
        return

    # Si encontramos al paciente y al medico,
    # solicitamos los datos de la cita.

    fecha = input("Ingrese la fecha (DD/MM/AAAA): ")
    hora = input("Ingrese la hora (HH:MM): ")

    # Creamos un objeto Cita.
    # Le pasamos los objetos paciente y medico
    # que encontramos, junto con la fecha y hora.

    cita = Cita(paciente, medico_encontrado, fecha, hora)

    # Guardamos la nueva cita en la lista.

    posta.registrar_cita(cita)


# =====================================================
# FUNCION PARA BUSCAR PACIENTE
# =====================================================

# Esta funcion permite buscar un paciente
# escribiendo su DNI en la consola.

def buscar_paciente():

    print("\n==== BUSQUEDA DE PACIENTE ====")

    # Solicitamos el DNI que queremos buscar.

    dni = input("Ingrese el DNI que desea buscar: ")

    # Llamamos al metodo buscar_paciente
    # y guardamos el resultado.

    paciente = posta.buscar_paciente(dni)

    # Comprobamos si el paciente fue encontrado.

    if paciente != None:

        print("\nPaciente encontrado:")

        # Mostramos toda su informacion.

        print(paciente.mostrar_informacion())

    else:

        # Si el resultado es None,
        # mostramos que no existe ese paciente.

        print("\nPaciente no encontrado.")


# =====================================================
# MENU PRINCIPAL
# =====================================================

# Creamos una variable llamada opcion.
# Al inicio esta vacia.
# Luego guardara la opcion que el usuario elija.

opcion = ""

# while repite las instrucciones mientras
# la opcion sea diferente de "7".
# La opcion 7 sirve para salir del sistema.

while opcion != "7":

    # Mostramos el menu principal.

    print("\n================================")
    print(" POSTA DE SALUD SANTA ROSA SJL")
    print("================================")

    print("1. Registrar paciente")
    print("2. Registrar medico")
    print("3. Registrar cita")
    print("4. Mostrar pacientes")
    print("5. Mostrar medicos")
    print("6. Mostrar citas")
    print("7. Salir")
    print("8. Buscar paciente")
    print("9. Generar reporte")

    print("================================")

    # input() permite que el usuario
    # escriba el numero de la opcion.
    # Se guarda como texto en la variable opcion.

    opcion = input("Seleccione una opcion: ")

    # =================================================
    # OPCIONES DEL MENU
    # =================================================

    # Si el usuario escribe "1",
    # llamamos a la funcion para registrar pacientes.

    if opcion == "1":

        registrar_paciente()

    # Si escribe "2", registramos un medico.

    elif opcion == "2":

        registrar_medico()

    # Si escribe "3", registramos una cita.

    elif opcion == "3":

        registrar_cita()

    # Si escribe "4", mostramos los pacientes.

    elif opcion == "4":

        posta.mostrar_pacientes()

    # Si escribe "5", mostramos los medicos.

    elif opcion == "5":

        posta.mostrar_medicos()

    # Si escribe "6", mostramos las citas.

    elif opcion == "6":

        posta.mostrar_citas()

    # Si escribe "7", mostramos el mensaje de salida.
    # Despues, el while terminara porque
    # opcion ya sera igual a "7".

    elif opcion == "7":

        print("\nGracias por utilizar el sistema.")

    # Si escribe "8", buscamos un paciente.

    elif opcion == "8":

        buscar_paciente()

    # Si escribe "9", generamos el reporte.

    elif opcion == "9":

        posta.generar_reporte()

    # Si escribe cualquier otro valor,
    # mostramos que la opcion no es valida.

    else:

        print("\nOpcion no valida. Intente nuevamente.")
