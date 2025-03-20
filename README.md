# todop
Very small cli todo application written in Python. Requires Python.

Place in ~/.local/bin so it can be executed within the terminal. When run, a file is created at /var/tmp/todop which is used to save the contents of the todo list.

Usage:
```
todop                 display the todo list
todop 3               remove a numbered item from the list
todop brush teeth     add an item to the list
todop add             add to the list in a long-form style
todop clear           clears all items from the list, deletes file
```

This was created as a practice project and will be further developed/redesigned.
