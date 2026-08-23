import os
import sqlite3
import datetime
import tkinter as tk
from tkinter import ttk


# optional   pdf export

# Brand theme constants
APP_TITLE = "Billing system"
COMPANY_NAME = "Samad techie"
COMPANY_ADDRESS = "adasrsh vihar colony, chinhut, Lucknow 226028"
COMPANY_PHONE = "+91 9594138854"
COMPANY_WEBSITE =  "www.samadtechie.in"
CURRENCY = "\u20b9"    #rupee sign

NAVY = "#0B2545"
NAVY_DARK = "#081A33"
NAVY_MID = "#13315C"
AMBER = "#F5A623"
AMBER_DARK = "#C97F0B"
LIGHT_BG = "#F4F7FB"
WHITE = "#FFFFFF"
GREY = "#5B6B7B"
RED = "#C0392B"
GREEN = "#1E8449"

BASE_DIR = os.path.dirname(os.path.abspath(__file__))
DB_PATH = os.path.join(BASE_DIR, "billing_system.db")
INVOICE_DIR = os.path.join(BASE_DIR, "invoices")
ASSETS_DIR = os.path.join(BASE_DIR, "assets")
os.makedirs(INVOICE_DIR, exist_ok=True)


#  DATABASE Layer

class Database:
    """thin wraper around sqlite3 for all billing-system persistence"""

    def __init__(self, path=DB_PATH):
        self.conn = sqlite3.connect(path)
        self.conn.row_factory = sqlite3.Row
        self.conn.execute("PRAGMA foreign_key = ON")
        self._create_tables()
        self._seed_if_empty()

    