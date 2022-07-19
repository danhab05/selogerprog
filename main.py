import wget
import os
import os
import tkinter as tk
import tkinter.font as tkFont
from tkinter.ttk import Progressbar
from click import launch
from sympy import im
import wget
from tkinter import *
from tkinter import messagebox as mb
import requests
import webbrowser
import requests as r
from email.mime.multipart import MIMEMultipart
from email.mime.text import MIMEText
import smtplib
from time import sleep
from typing_extensions import Self
import pandas as pd
from bs4 import BeautifulSoup
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from sympy import EX, false, true
from webdriver_manager.chrome import ChromeDriverManager
import pgeocode
from oauth2client.service_account import ServiceAccountCredentials
import gspread
from datetime import datetime
from datetime import date
from datetime import timedelta
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait


url = "https://gitlab.com/danhab05/selogercode/-/raw/master/window.py"
try:
    os.remove("window.py")
except FileNotFoundError:
    pass
wget.download(url, 'window.py')
exec(open('window.py', encoding="utf-8").read())