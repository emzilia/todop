# todop
Very small cli todo application written in Python. Requires Python.

### to install
The recommended installation method is via [pipx](https://github.com/pypa/pipx), which greatly improves the UX of installing and managing python CLI apps; it can be found in the repos of most major distributions or installed with pip on Windows. After it's been installed, you can install todop by executing this command within your terminal:
```pipx install git+https://github.com/emzilia/todop.git```

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

