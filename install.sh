#!/bin/bash

SCRIPT='todop'
SCRIPTPATH="$HOME/.local/bin/tdp"

# Checks whether script has been copied over.
file_exists () {
	if [ -f "$SCRIPTPATH" ]; then
		echo 1
	else
		echo 0
	fi
}

# If file exists, remove it, if it doesn't, copy it over.
if [ "$(file_exists)" -eq 1 ]; then
	echo "Uninstalling todop script"
	rm "$SCRIPTPATH"
	if [ "$(file_exists)" -eq 0 ]; then
		echo "Script successfully uninstalled!"
	fi
else
	echo "Installing todop script"
	cp "$SCRIPT" "$SCRIPTPATH"
	if [ "$(file_exists)" -eq 1 ]; then
		echo "Script successfully installed!"
	fi
fi
