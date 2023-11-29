from pathlib import Path
filename = "ejemplo.txt"
def writefile():
    try:
        content = "JOSUE RODRIGO FIERRO MORFIN"
        f = open(filename,'w')
        f.write(content)
        f.close()
    except:
        print("An exception occurred")
def readfile():
    try:
        f = open(filename,'r')
        leer = f.read()
        f.close()
        print(leer)
    except:
        print("An exception occurred")
def automatizacion():
    try:
        # Directorio y archivo originales
        original_directory = Path('C:\\Users\\Lenovo\\Desktop\\ibm\\msl\\ibm')
        original_filepath = original_directory / filename

        # Crear el directorio y el archivo original
        original_directory.mkdir(parents=True, exist_ok=True)
        with open(original_filepath, 'w') as f:
            f.write("International Business Machines")

        # Nuevos nombres para el directorio y el archivo
        new_file_path = Path('C:\\Users\\Lenovo\\Desktop\\ibm\\msl\\ibm\\new_prueba.txt')
        new_directory_path = Path('C:\\Users\\Lenovo\\Desktop\\ibm\\msl\\MSL_Test')

        # Renombrar el archivo y el directorio
        original_filepath.rename(new_file_path)
        original_directory.rename(new_directory_path)

    except Exception as e:
        print(f"An exception occurred: {e}")
if __name__ == '__main__':
    #writefile()
    #readfile()
    automatizacion()