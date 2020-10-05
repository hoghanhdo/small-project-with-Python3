from blog_terminal.terminal import Terminal
from blog_terminal.database import Database

Database.initialize()
terminal = Terminal()
terminal.run_terminal()
