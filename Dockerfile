# Usar una imagen base de Python
FROM python:3.9-slim

# Establecer el directorio de trabajo
WORKDIR /usr/src/app

# Copiar los archivos de requisitos y instalar dependencias
COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

# Copiar el resto de los archivos del proyecto
COPY . .

# Exponer el puerto
EXPOSE 4000

# Comando para ejecutar la aplicación
CMD ["python", "app.py"]
