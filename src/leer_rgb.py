# leer_rgb.py

def leer_colores(archivo):
    try:
        with open(archivo, 'r') as f:
            lineas = f.readlines()
        
        print(f"Se encontraron {len(lineas)} registros:\n")
        
        for i, linea in enumerate(lineas):
            linea = linea.strip()
            if linea:
                # Parsear "R:255 G:128 B:0"
                partes = linea.split()
                r = int(partes[0].split(':')[1])
                g = int(partes[1].split(':')[1])
                b = int(partes[2].split(':')[1])
                
                print(f"Registro {i+1}: R={r}, G={g}, B={b}")
                print(f"  → Hex: #{r:02X}{g:02X}{b:02X}")
                print(f"  → Normalizado (0-1): R={r/255:.2f}, G={g/255:.2f}, B={b/255:.2f}")
    
    except FileNotFoundError:
        print("Archivo no encontrado. Selecciona un color primero en Node-RED.")

if __name__ == "__main__":
    leer_colores('/home/dilan/rgb_values.txt')