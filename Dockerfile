# Imagen base de Python
FROM python:3.9-slim

# Directorio de trabajo
WORKDIR /app

# Copiamos el archivo de dependencias y lo instalamos
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt

# Copiamos el resto del código (app.py, Jenkinsfile, etc.)
COPY . .

# Exponemos el puerto 9999 donde la app escuchará
EXPOSE 9999

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]
