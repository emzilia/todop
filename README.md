# todop
Very small cli todo application written in Python. Requires Python.

Place in ~/.local/bin so it can be executed within the terminal. When run, a file is created at /var/tmp/todop which is used to save the contents of the todo list.

Usage:
```
todop                 displays the todo list
todop 3               adding a number clears that numbered item from the list
todop brush teeth     add an item to the list with only the command alone
todop add             lets you input a task in a long-form style
todop clear           removes all items from the todo list, deletes file
```

This was created as a test and will be further developed/redesigned.
