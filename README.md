# todop
Very small cli todo application written in Python. Requires Python.

### installation
First, read the ```install.sh``` file to see what it's doing to your system.   
Then, run the file with ```bash install.sh```    
The install.sh can be run a second time to remove the file from your .local/bin

### usage 
When run, a file is created at ```/var/tmp/todop``` which is used to save the contents of the todo list.

commands:
```
tdp                 display the todo list
tdp 3               remove a numbered item from the list
tdp brush teeth     add an item to the list
tdp add             add to the list in a long-form style
tdp clear           clears all items from the list, deletes file
```

