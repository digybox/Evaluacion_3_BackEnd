1)Crear entorno virtual
python -m venv venv
2)Activar:
venv\Scripts\activate
3) Instalar dependencias AUTOMÁTICAMENTE
pip install -r requirements.txt    Si te tira error en oracledb==2.1.1, INSTALA ESTA:

pip install oracledb
pip install python-dotenv
4) Crear el archivo .env

 Crea un archivo .env con:
SECRET_KEY=django-insecure-1234567890
DEBUG=True

DB_NAME=XEPDB1
DB_USER=django
DB_PASS=django123
DB_HOST=localhost
DB_PORT=1521

5) Instalar Oracle Instant Client (SOLO SI NO ESTÁ INSTALADO)

Descargar desde la web de Oracle:
instantclient-basic
instantclient-sqlplus
Descomprimir en:
C:\oracle\instantclient
Agregar al PATH:
C:\oracle\instantclient

6) Crear usuario en Oracle (solo primera vez)

Abrir cmd:
sqlplus / as sysdba
Ejecutar: ALTER SESSION SET CONTAINER = XEPDB1;
CREATE USER django IDENTIFIED BY django123;
GRANT CONNECT, RESOURCE TO django;
ALTER USER django QUOTA UNLIMITED ON USERS;
Salir:
exit;

7) Aplicar migraciones
python manage.py migrate
8) Iniciar servidor
python manage.py runserver
