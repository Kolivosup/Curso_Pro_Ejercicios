base_de_datos_dinosaurios = [
    ("Tiranosaurio", "Tyrannosaurus Rex", "Carnivoro", "Cretacico", "Sus manos eran tan cortas que no le servian para llevarse la comida al hocico."),
    ("Velociraptor", "Velociraptor Mongoliensis", "Carnivoro", "Cretacico", "Tenia el tamano de un lobo actual y cazaba en grupo usando una garra poderosa en sus patas."),
    ("Triceratops", "Triceratops Horridus", "Herbivoro", "Cretacico", "Su pico curvado como el de un loro le servia para cortar plantas muy duras."),
    ("Braquiosaurio", "Brachiosaurus Brancai", "Herbivoro", "Jurasico", "Era de los pocos dinosaurios con las patas delanteras mas largas que las traseras."),
    ("Estegosaurio", "Stegosaurus Armatus", "Herbivoro", "Jurasico", "Las grandes placas de su lomo le servian para regular la temperatura corporal."),
    ("Arqueopterix", "Archaeopteryx Lithographica", "Carnivoro", "Jurasico", "Se le considera la primera ave y aporta pruebas clave de su evolucion desde los dinosaurios."),
    ("Ornitomimo", "Ornithomimus Velox", "Omnivoro", "Cretacico", "Recibio su nombre por su gran parecido fisico con aves modernas como el avestruz."),
    ("Gallimimo", "Gallimimus Bullatus", "Omnivoro", "Cretacico", "Filtraba el lodo con sus dientes tipo peine para alimentarse y corria muy rapido."),
    ("Alosaurio", "Allosaurus Fragilis", "Carnivoro", "Jurasico", "Se caracteriza por tener protuberancias distintivas justo delante de sus ojos."),
    ("Diplodocus", "Diplodocus Longus", "Herbivoro", "Jurasico", "El extremo de su cola era muy delgado y podia usarlo como un latigo defensivo."),
    ("Amargasaurio", "Amargasaurus Cazaui", "Herbivoro", "Cretacico", "Vivia en manadas y usaba sus llamativas espinas del cuello para defenderse o en el cortejo."),
    ("Mamenquisaurio", "Mamenchisaurus Hochuanensis", "Herbivoro", "Jurasico", "Poseia un cuello enorme y viajaba en grupo cuando escaseaba el alimento."),
    ("Tecodontosaurio", "Thecodontosaurus Antiquus", "Herbivoro", "Triasico", "Es el prosauropodo mas antiguo que se conoce, caracterizado por unas curvas en sus pulgares."),
    ("Deinonicus", "Deinonychus Antirrhopus", "Carnivoro", "Cretacico", "Cazaba en grupo y caminaba apoyando solo dos dedos para mantener libre su gran garra principal."),
    ("Espinosaurio", "Spinosaurus Aegyptiacus", "Carnivoro", "Cretacico", "Su gran cresta dorsal le ayudaba a disipar calor para regular su temperatura corporal."),
    ("Coritosaurio", "Corythosaurus Casuarius", "Herbivoro", "Cretacico", "Se han encontrado esqueletos tan bien conservados que aun mantenian restos de su piel."),
    ("Tuojiangosaurio", "Tuojiangosaurus Multispinus", "Herbivoro", "Jurasico", "Es un pariente asiatico del Estegosaurio con placas y espinas a lo largo del lomo."),
    ("Apatosaurio", "Apatosaurus Ajax", "Herbivoro", "Jurasico", "Durante mucho tiempo se le confundio con el Brontosaurio por un error paleontologico."),
    ("Protoceratops", "Protoceratops Andrewsi", "Herbivoro", "Cretacico", "A diferencia de sus parientes, no tenia cuernos reales sino botones oseos en la nariz."),
    ("Anquilosaurio", "Ankylosaurus", "Herbivoro", "Cretacico", "Estaba completamente blindado con placas oseas y remataba su cola con un pesado mazo de hueso."),
    ("Lambeosaurio", "Lambeosaurus Lambei", "Herbivoro", "Cretacico", "Tenia una bateria de hasta 700 dientes amontonados para triturar plantas duras."),
    ("Paquicefalosaurio", "Pachycephalosaurus Wyomingensis", "Herbivoro", "Cretacico", "Tenia una gruesa boveda osea en el craneo de hasta 25 cm de espesor usada en rituales."),
    ("Parasaurolofus", "Parasaurolophus Walkeri", "Herbivoro", "Cretacico", "Se cree que usaba el tubo de su cresta hueca para emitir sonidos similares a un trombon."),
    ("Iguanodonte", "Iguanodon Bernissartensis", "Herbivoro", "Cretacico", "Tenia un pulgar conico y afilado en forma de pua que utilizaba como arma de defensa."),
    ("Maiasauria", "Maiasauria Peeblesorum", "Herbivoro", "Cretacico", "Su nombre significa Lagarto Buena Madre porque se hallaron nidos con huevos y crias."),
    ("Estiracosaurio", "Styracosaurus Albertensis", "Herbivoro", "Cretacico", "Lucia una vistosa estructura de puas en el craneo usada para impresionar a rivales y parejas.")
]

def mostrar_dinosaurio():
    dino = r"""
              __
             / _)
    _.----._/ /
   /         /
  / (___|___/
 /    |   |
|__/\_|__/\_|
    """
    print(dino)

print("BIENVENIDO A JURASSIC PARK")
print("Encontremos a tu Dinosaurio")
mostrar_dinosaurio()

def menu():
    print("\n1. Buscar por Nombre")
    print("2. Buscar por Especie")
    print("3. Buscar por Dieta")
    print("4. Buscar por Periodo")
    print("5. Mostrar Dinosaurios")
    print("6. Salir")


def mostrar_dinos():
    for Dinosaurio in base_de_datos_dinosaurios:
        print(Dinosaurio)


def buscar_por_columna(indice, texto_busqueda):
    encontrados = False
    for dino in base_de_datos_dinosaurios:

        if texto_busqueda.lower() in dino[indice].lower():
            print(f"-> Nombre: {dino[0]} | Especie: {dino[1]} | Dieta: {dino[2]} | Periodo: {dino[3]} | \nDato_Curioso: {dino[4]}")
            encontrados = True
    if not encontrados:
        print("No se encontraron resultados.")


def mostrar_carita():
    carita = r'''
      .-""""""-.
     /  ~    ~  \
    |  (o)  (o)  |
    |     __     |
    \    \__/    /
     '._      _.'
        `""""`
    '''
    print(carita)

while True:
    menu()
    Dato = int(input("Selecciona (1:6): "))

    if Dato == 1: 
        Nombre = input("ingrese el nombre del dinosaurio:")
        buscar_por_columna(0,Nombre)
    elif Dato == 2: 
            Especie = input("Ingrese la Especie:")
            buscar_por_columna(1,Especie)
    elif Dato == 3: 
        Dieta = input("Ingrese la dieta:")
        buscar_por_columna(2,Dieta)
    elif Dato == 4: 
        Periodo = input("Ingrese la Periodo:")
        buscar_por_columna(3,Periodo)
    elif Dato == 5: 
        mostrar_dinos()
    elif Dato == 6: 
        print("¡Adiós, vuelve pronto!")
        mostrar_carita()
        break
    else :
        print("Opcion no valida")

    
