# Usa una imagen base de Python
FROM python:3.8-slim

# Crea y establece el directorio de trabajo
WORKDIR /app

# Copia el archivo de requerimientos y lo instala
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copia el resto de los archivos de la aplicación
COPY . .

# Expone el puerto en el que se ejecutará la app
EXPOSE 9999

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]
