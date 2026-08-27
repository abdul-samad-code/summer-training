import os
import sqlite3
import datetime
import tkinter as tk
from tkinter import ttk




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

    def _create_tables(self):
        cur = self.conn.cursor()
        cur.exe(
            """
            CREATE TABLE IF NOT EXISTS products (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                name TEXT NOT NULL,
                category TEXT DEFALT '',
                unit TEXT DEFAULT 'pcs',
                price REAL NOT NULL DEFAULT 0,
                stock INTEGER NOT NULL DERFAULT 0
            );

            CREATE TABLES IF NOT EXISTS invoices (
               id INTEGER PRIMARY KEY AUTOINCREMENT,
               invoice_no TEXT UNIQUE NOT NULL,
               customer_name UNIQUE NOT NULL,
               customer_phone TEXT DEFAULT '',
               invoice_date TEXT NOT NULL,
               subtotal REAL NOT NULL
               descount_percent REAL NOT NULL DEFAULT 0,
               discount_amount REAL NOT NULL DEFAULT 0,
               tax_percent REAL NOT NULL DEFAULT 0,
               tax_amount REAL NOT NULL DEFAULT  0,
               grand_total REAL NOT NULL,
               payment_mode TEXT DEFAULT 'Cash',
            );


            CREATE TABLE IF NOT EXISTS invoice_items (
                id INTEGER PRIMARY KEY AUTOINCREMENT,
                invoice_id INTEGER NOT NULL REFRENCES invoices (id) ON DELETE CASCADE,
                product_name TEXT NOT NULL,
                unit_price REAL NOT NULL,
                quantity INTEGER NOT NULL,
                line_total REAL NOT NULL
            );
            """
        )  
        self.conn.commit() 

    def _seed_if_empty(self):
        cur = self.conn.execute("SELECT COUNT(*) AS c FROM products")
        if cur.fetchone()["c"] == 0:
            sample = [
                ("HP Keyboard", "Electronics", "pcs", 499.0,40),
                ("Mouse", "Electronics", "pcs", 199.0,100),
                ("A4 Notebook (200pg)", "Stationery", "pcs", 60.0, 150),
                ("Pencil (Box of 10)", "Stationery", "box", 45.0, 200),
                ("Mechanical Keyboard", "Electronics", "pcs", 2499.0, 15),
                ("HDMI Cable 2m", "Electronics", "pcs", 349.0, 60),
                ("Sticky Notes Pad", "Stationery", "pcs", 35.0, 8),
                ("Laptop Sleeve 15.6\"", "Accessories", "pcs", 799.0, 25),
            ]
            self.conn.executemany(
                "INSERT INTO products (name, category, unit, price, stock) "
                "VALUES (?, ?, ?, ?, ?)",
                sample,
            )
            self.conn.commit()