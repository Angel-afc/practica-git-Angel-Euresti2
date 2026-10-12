# Commandos basicos de PowerShell

### Resumen de comandos PowerShell


| comando   |  Descripcion                           | Ejemplo   |
| --------- |:--------------------------------------:|:--------: |
|  cd       | abrir carpeta o cambiar                |user\alumno:> cd movies|
|  ls       | muestra archivos de una carpeta        |user\alumno:> ls       |
|  mkdir    | crear archivo o carpeta                |user\amuno\desktop:> mkdir nombre de la carpeta           |
|  clear    | muestra de la ruta de la carpeta       |user\name:> clear-host  |
|  pwd      | muestra la ruta de la carpeta          |user\name:> pwd       |
|  cat      | muestra el contenido de un archivo     |user\name:>           |
|  cp       | copiar un archivo                      |user\name:> cp archivo carpeta     |
|  mv       | mueve un archivo o carpeta a otra ruta |user\name:> mv archivo .txt   C:\destino\nuevo      |

## comandos básicos de git
|comando     | Descripció  | Ejemplo|
|:----------:|:-----------:|:-------:|
| init    |crea un repositorio local en la carpeta| user\name:> git init|
| clone   |clonar archivo|user\name:> git clone https://github.com|
| diff    |Muesra las diferencias exactas en el codigo entre los cambios que as hecho|user\name:> git diff|
| status  |muestra el estado actual de tu espacio de trabajo|user\name:> git status|
| config  |configura las opciones de Git|user\name:> git config --global user.name "tu nombre" git config --global user.email "tu email"|
| merge|une los cambios de otra rama a en la que esta|user\name:> git merge nueva-rama|
| add|prepara los archivos modificados y los añade al staging area|user\name:> git add archivo.txt git add .|
|log|muestra el historial cronológico de todos los cambios guardados{commits}|user\name:> git log|
|commit|guarda permanentemente los cambios preparados en el historial con un mensaje descriptivo|user\name:> git commit -m "explicacion clara del cambio realizado"|
| checkout|cambia de una rama a otra o restaura archivos a una versión anterior|user\name:> git checkout nueva rama|
| branch|lista, crea o elimina ramas, las cuales sirven para trabajar en funciones nuevas sin alterar el código principal|user\name:> git branch(lista ramas) git brench nueva-rama (crear nueva rama)|
| pull|descarga e integra los cambios más recientes del repositor remoto a tu computadora de forma automática|user\name:> git pull origin main|
| push|sube tus cambios locales guardados(commits) al repositorio remoto para compatirlos con otros|user\name:> git push origin main|
| fetch|descarga la información más reciente del servidor remoto pero sin combinarla ni alterar tu código actual|user\name:> git fetch origin|
 
 ##Crear un repositorio de git en PowerShell

- Paso 1 instalar git de la pagina oficial solo si no lo tienes instalado cuando ya se hayga descargado te vas a administrador de arcchivos y le das doble click y le picas que si a todo

- Paso 2;abrir powershell Inicia la aplicacion desde tu computadora

- Paso 3;ir a la carpeta Usa el comando cd seguido de la ruta de tu carpeta user\alumno:> cd desktop

- Paso 4;crear una carpeta Si no existe, puedes crarlo escribiendo user\alumno:> mkdir micarpeta

- Paso 4;Inicializar Git Escribiendo el comando en powershell  (git init)

- Paso 5;verifica el estado comprueba que todo salió bien escribiendo (git status)

- Paso 7;Configurar git con los comandos (git config --global user.name "nombre del usuario)(git config --global user.email "tu correo")

- Paso 8;despues verificas que este la carpeta con el comando (git status)te debe de aparecer el archibo anteriormente creado 

- Paso 8;despues agrega el archivo con git add nombre de archivo

- Paso 9;crea un commit que guarda de forma oficial esos archivos utilisando git commit "nombre del commit"



