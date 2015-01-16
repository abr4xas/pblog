#!/bin/bash
#
# Ejecutar para actualizar los submodulos que contenga el repo
#

	git submodule foreach git pull origin master
exit 0
