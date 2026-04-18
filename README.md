# Lab04: Visualización de Datos en Raspberry Pi con Node-RED 

## Integrantes

DILAN JESUS MENDOZA GUARIYU 84670

EINER JULIAN AGUDELO ACOSTA 105352

HASBLEIDY JOHANNA SILVA ESCARRAGA 110002


#  Proyecto: Procesamiento de Colores RGB con Node-RED y Python

## Descripción del Proyecto
Este proyecto implementa un sistema que permite seleccionar un color desde una interfaz gráfica en Node-RED, visualizar sus valores RGB y almacenarlos en un archivo de texto. Posteriormente, un script en Python lee este archivo y procesa los valores para mostrar información adicional como su representación hexadecimal y su normalización.

El sistema combina programación visual (Node-RED) con procesamiento de datos en Python, demostrando la integración entre diferentes tecnologías mediante archivos compartidos.

---

## Características
- Interfaz gráfica para selección de color
- Visualización de valores RGB en tiempo real
- Almacenamiento de datos en archivo `.txt`
- Procesamiento de datos con Python
- Conversión a formato hexadecimal
- Normalización de valores RGB (0–1)
- Manejo de errores básicos

---

##  Arquitectura
El sistema sigue una arquitectura tipo **productor-consumidor**:

- **Node-RED (Productor)**
  - Selector de color
  - Conversión a RGB
  - Escritura en archivo

- **Archivo de texto (`rgb_values.txt`)**
  - Medio de almacenamiento e intercambio

- **Python (Consumidor)**
  - Lectura del archivo
  - Procesamiento de datos
  - Visualización de resultados

---

##  Requisitos de Hardware
- Raspberry Pi (opcional pero recomendado)
- Computador con acceso SSH
- Red local compartida
- Almacenamiento para archivos

---

## Estructura de Clases
El proyecto en Python utiliza programación estructurada:

- `leer_colores(archivo)`
  - Lee el archivo
  - Procesa los valores RGB
  - Muestra resultados

- Bloque principal:
```python
if __name__ == "__main__":


```

##  API de Referencia

No se utilizan APIs externas.

Se emplean:

- Node-RED Dashboard (selector de color)
- Librerías estándar de Python:
  - open()
  - readlines()

---

##  Funcionalidades Implementadas

- Selección de color desde interfaz web
- Conversión automática a RGB
- Almacenamiento de registros
- Lectura de datos desde Python
- Conversión a hexadecimal (#RRGGBB)
- Normalización de valores
- Manejo de errores

---

## 🛠️ Tecnologías Utilizadas

- Node-RED
- Node.js
- npm
- Python 3
- Raspberry Pi OS
- SSH

---

## Desafíos Técnicos

- Integración Node-RED ↔ Python
- Formato correcto de datos
- Manejo de rutas en Raspberry Pi
- Sincronización lectura/escritura
- Validación de datos

---

##  Mejoras Futuras

- Uso de base de datos (SQLite/MongoDB)
- Implementación de API REST
- Comunicación directa Node-RED ↔ Python
- Visualización gráfica de colores
- Automatización en tiempo real


##  Conclusiones

- Se logró integrar exitosamente Node-RED y Python mediante un mecanismo sencillo de intercambio de datos usando archivos de texto, demostrando una solución práctica y funcional.

- El uso de Node-RED facilitó la creación de una interfaz gráfica intuitiva, permitiendo la interacción del usuario sin necesidad de programación compleja.

- Python permitió procesar eficientemente los datos RGB, agregando valor mediante conversiones a formato hexadecimal y normalización.

- Se evidenció la importancia de mantener un formato de datos consistente para evitar errores durante el procesamiento.

- La arquitectura productor-consumidor resultó adecuada para este tipo de aplicación, aunque presenta limitaciones en tiempo real.

- El proyecto demuestra cómo tecnologías simples pueden integrarse para crear soluciones útiles en sistemas embebidos y aplicaciones IoT.

- Se identificaron oportunidades de mejora, como el uso de bases de datos y comunicación directa entre sistemas para aumentar la eficiencia y escalabilidad.