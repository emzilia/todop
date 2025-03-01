#!/usr/bin/env python3

from sys import argv
from pathlib import Path

class NoteList():
    # file contents are all saved to a tmp file, it's only 
    # a daily todo after all.
    def __init__(self):
        self.user_input = ''
        self.pathstr = "/var/tmp/todop"
        self.path = Path(self.pathstr)
        if not self.path.is_file():
            with open(self.path, 'x') as t:
                t.close()

    # ensures there are no extra newlines within the tmp file
    def rm_lines(self, file):
        file = Path(file)
        lines: list[str] = file.read_text().splitlines()
        filtered: list[str] = [
            line
            for line in lines
            if line.strip()
        ]
        file.write_text('\n'.join(filtered))

    # runs blank line function and enumerates file line by line,
    # including line numbers
    def list_tasks(self) -> None:
        print('')
        self.rm_lines(self.path)
        with open(self.path, 'r+') as f:
            lines: list[str] = f.readlines()
        for index, item in enumerate(lines):
            item: str = item.strip('\n')
            print(f' {index + 1}: {item}')
        print('')

    # removes specified line item by rewriting the file back to itself
    def done_task(self, item_number) -> None:
        with open(self.path, 'r') as f:
            lines: list[str] = f.readlines()
        with open(self.path, 'w') as f:
            for index, line in enumerate(lines):
                if index != int(item_number)-1:
                    f.write(line)
        self.list_tasks()

    # adds a task to the list using either the command arguments, or 
    # input given after the add command. 
    # appends user's string to a newline within the temp file.
    def add_task(self) -> None:
        if not self.user_string:
            with open(self.path, 'a') as f:
                self.user_input: str = input()
                f.write(f'\n{self.user_input}')
        else:
            with open(self.path, 'a') as f:
                f.write(f'\n{self.user_string}')
        self.list_tasks()

    # prints a cute little help readout
    def show_help(self) -> None:
        print(
            'Usage: tdp [command/number] (todo items in sentence form)\n\n'
            '    Run by itself to show the todo list.\n' 
            '    Add one number as an argument to remove it from the list.\n'
            "    Items can be added in one line with 'tdp foo bar'\n\n"
            '    Commands:\n'
            '        add        adds a task to the list.\n'
            '        clear      clears all tasks from the list.\n'
        )

    # clears the list, starts fresh with a new file on the next run
    def clear_file(self) -> None:
        tmp: Path = self.path
        if tmp.is_file():
            tmp.unlink()

    def process_args(self):
        # running the command by itself shows the todo list
        if len(argv) == 1:
            self.list_tasks()
            quit()

        # with one argument, add, clear, and help are accepted commands
        # numbers remove the specified item from the list
        # any other string adds the string to the list
        if len(argv) == 2:
            if argv[1] == 'add':
                self.user_string = ''
                self.add_task()
            elif argv[1] == 'clear':
                self.clear_file()
            elif argv[1] in ['--help', '-h', 'help']:
                self.show_help()
            elif argv[1].isnumeric():
                self.done_task(int(argv[1]))
            else:
                self.user_string: str = ''
                for word in argv[1:]:
                    self.user_string += word + ' '
                self.add_task()
        # with more than one argument, all arguments are treated as a single
        # sentence that is added to the list.
        elif len(argv) > 2:
            self.user_string: str = ''
            for word in argv[1:]:
                self.user_string += word + ' '
            self.add_task()

