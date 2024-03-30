## MEMORIA EJERCICIO

Alumno: Sergio Ramírez Domínguez<br>
Fecha: 30-03-2024

Creamos un proyecto conda llamado `nube_wiki` e inicializamos un proyecto git. Llamamos al repositorio `nube_wiki`.

!["Crear proyecto conda e inicializar Git"](imagenes/1-Crear_proyecto_conda_inicializar_git.png)

Instalamos jupyter lab para crear nuestro entorno de código

> conda install jupyterlab

!["Crear entorno código"](imagenes/2-Crear_entorno_codigo.png)

Instalamos las primeras librerías solicitadas

> conda install conda-forge::wikipedia <br>
> conda install conda-forge::stop-words

Hacemos un primer commit para agregar los archivos creados, aunque previamente, creamos el archivo `.gitignore` para no tener en nuestro repositorio archivos innecesarios:

* .gitignore

