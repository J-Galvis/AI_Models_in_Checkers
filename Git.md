# Aprendiendo de Git

## Reinizializar un repositorio de git

    - git init
    - git remote add origin (url del repositorio)
    - git fetch

    Ahora, como  quiero conservar los cambios que he hecho en local, inicializo una HEAD

    - git add .
    - git commit -m "HEAD"

    Se hace el reset, lo hago con merge ya que conserva los valores del local

    - git reset --merge origin/master
