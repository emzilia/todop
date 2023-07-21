#!/bin/bash

SCRIPT='todop'
SCRIPTPATH="$HOME/.local/bin/tdp"

# If file exists, remove it, if it doesn't, copy it over.
if [ -f "$SCRIPTPATH" ]; then
	echo "Uninstalling todop script"
	rm "$SCRIPTPATH"
	if [ ! -f "$SCRIPTPATH" ]; then
		echo "Script successfully uninstalled!"
	fi
else
	echo "Installing todop script"
	cp "$SCRIPT" "$SCRIPTPATH"
	if [ -f "$SCRIPTPATH" ]; then
		echo "Script successfully installed!"
	fi
fi
