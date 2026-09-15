Angel Gabriel Euresti Conde
2630228
crear un repositorio local utilizando Git, sincronizarlo con un repositorio remoto en GitHub y comprobar el flujo de trabajo en ambos sentidos
Repositorio local --GitHub
GitHub --Repositorio local

se utulizaron los siguientes comandos de git:
git init . se usa para iniciar un repositorio de git en la ubicacion actual
git branch -m "main" . se usa para asignarle un nombre a la rama principal
git status . se usa para ver el estatus de los archivos en el repositorio
git add . se usa para añadir los archivos del repositorio a la zona de staging
git commit -m "nombre" se usa para commitear los archivos que estan en la zona de staging y le da un nombre al commit y una id unica
git remote add origin url . se usa para vincular el repositorio local con el repositorio de github
git remote -v , se usa para ver si el repositorio local esta conectado con el repositorio de git
git push -u origin main . se usa para pasar los archivos del repositorio local al repositorio en git por primera vez
git pull origin main se usa para descargar los cambios del repositorio de git al repositorio local

tube que sincronizar mi cuenta de github con la yave ya que no me dejaba acceder a mi cuenta

el repositorio local se creo primero con un mkdir "nombre" y luego ya dentro de la carpeta se uso un git init, despues configure git y se configuro el nombre de la rama principal con git branch -M main

primero se creo el repositorio en github y se copio su url, luego en el repositorio local se uso git remote add origin "url" y se verifico que estuvieran vinculados con git remote -v

se modifico el archivo datos.txt y se uso el comando git status para despues usar el git add . para pasarlo a la zona de staging y se creo un nuevo commit con git commit -m "commit" para por ultimo usar un git push

se modifico el archivo datos.txt y se realiza un commt desde github para despues descargarlo en el repositorio local con git pull

en el repositorio tenemos tanto el archivo datos.txt el cual es al que modificamos desde github para descargarlo local y modificamos local para volver a subirlo a gihub y el README.md el caul es este mismo archivo el cuak tiene toda esta informacion que el profesor nos pidio en classroom que es parte de la practica de git y github