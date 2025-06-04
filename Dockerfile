# Usar la imagen oficial de Jenkins LTS como base
FROM jenkins/jenkins:lts

# Cambiar a usuario root para poder instalar paquetes
USER root

# Actualizar el gestor de paquetes e instalar el cliente Docker
RUN apt-get update && \
    apt-get install -y docker.io && \
    rm -rf /var/lib/apt/lists/*

# Agregar al usuario 'jenkins' al grupo 'docker'
RUN usermod -aG docker jenkins

# Regresar al usuario jenkins para que Jenkins se ejecute con su configuración habitual
USER jenkins

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
