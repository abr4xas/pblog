#!/bin/bash
#
# Ejecutar para actualizar los submodulos que contenga el repo
#

git submodule foreach git pull origin master && git pull origin master && git log > CHANGELOG && git add . && git commit -m "Actualizando repo" && git push origin master

exit 0
