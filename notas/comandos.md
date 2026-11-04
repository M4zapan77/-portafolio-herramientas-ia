# Mis comandos de terminal y Git

Notas de las prácticas 4 y 5. Los comandos de terminal corresponden a Git Bash en Windows.

## Terminal

| Comando | Para qué sirve |
| --- | --- |
| `pwd` | Mostrar la ruta de la carpeta en la que estoy. |
| `ls` | Listar los archivos y carpetas del directorio actual. |
| `ls -R` | Ver también el contenido de las subcarpetas. |
| `cd carpeta` | Entrar en una carpeta. |
| `cd ..` | Subir a la carpeta anterior. |
| `mkdir notas` | Crear una carpeta llamada notas. |
| `touch archivo.md` | Crear un archivo vacío si no existe. |
| `cp origen.md destino.md` | Copiar un archivo. |
| `cat README.md` | Leer el contenido de un archivo en la terminal. |
| `explorer .` | Abrir la carpeta actual en el Explorador de Windows. |
| `notepad README.md` | Abrir el archivo con el Bloc de notas. |

## Git en local y GitHub

| Comando | Para qué sirve |
| --- | --- |
| `git init` | Iniciar el historial de Git en la carpeta actual. |
| `git config user.name "Diego Isaac Rico Hernández"` | Configurar mi nombre como autor dentro del repositorio. |
| `git status` | Ver la rama actual y los cambios pendientes. |
| `git diff` | Revisar los cambios que todavía no he preparado. |
| `git add README.md` | Preparar los cambios de un archivo para el siguiente commit. |
| `git commit -m "Completa la portada del portafolio"` | Guardar los cambios preparados con un mensaje que explique qué cambió. |
| `git log --oneline` | Ver el historial, con un commit por renglón. |
| `git log -1` | Consultar el autor y el mensaje del último commit. |
| `git restore archivo.md` | Descartar los cambios sin preparar de un archivo; se pierde lo que no se había guardado en un commit. |
| `git branch -M main` | Renombrar la rama actual como main. |
| `git remote -v` | Consultar las direcciones de los repositorios remotos. |
| `git clone URL` | Descargar un repositorio y su historial a una carpeta nueva. |
| `git pull --ff-only` | Descargar cambios y avanzar la rama local si no hay historias divergentes. |
| `git push -u origin main` | Subir la rama main por primera vez y vincularla con origin/main. |
| `git push` | Subir al repositorio remoto los commits locales pendientes. |

## Ciclo de trabajo

1. Antes de editar, descargar los cambios de GitHub con `git pull --ff-only`.
2. Editar los archivos y revisar el resultado con `git status` y `git diff`.
3. Preparar los archivos que sí quiero guardar con `git add`.
4. Crear un commit con un mensaje descriptivo.
5. Subirlo con `git push` y comprobar el resultado en GitHub.

El archivo `.gitignore` indica qué archivos locales no debe guardar Git. En este portafolio se ignora `notas/borrador.txt`.
