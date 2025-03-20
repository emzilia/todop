#!/bin/sh

SCRIPT='todop.py'
SCRIPTPATH="${HOME}/.local/bin/tdp"

# If file exists, remove it, if it doesn't, copy it over.
if [ -f "${SCRIPTPATH}" ]; then
	printf "Uninstalling todop script\n"
	rm "${SCRIPTPATH}"
	if [ ! -f "${SCRIPTPATH}" ]; then
		printf "Script successfully uninstalled!\n"
	else
		printf "Error: Uninstallation failed\n"
	fi
elif [ ! -f "${SCRIPTPATH}" ]; then
	printf "Installing todop script\n"
	cp "${SCRIPT}" "${SCRIPTPATH}"
	if [ -f "${SCRIPTPATH}" ]; then
		printf "Script successfully installed!\n"
	else
		printf "Error: installation failed\n"
	fi
fi
