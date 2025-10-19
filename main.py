# main.py
import sys
import os
sys.path.append(os.path.dirname(os.path.abspath(__file__)))

from lib.database import create_tables
from lib.cli import main_menu

if __name__ == "__main__":
    create_tables()     
    main_menu()         
