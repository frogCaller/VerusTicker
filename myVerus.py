## PLEASE ADD YOUR VERUS WALLET ON LINE 39:
## my_Verus_Wallet = "YOUR_VERUS_WALLET"

import time
import random
import sys
import os
import requests
import logging
from datetime import datetime
import json
import subprocess
from bs4 import BeautifulSoup
import spidev
from drive import SSD1305
from PIL import Image,ImageDraw,ImageFont
import re
###################################################################

disp = SSD1305.SSD1305()
disp.Init()
logging.info("clear display")
disp.clear()
width = disp.width
height = disp.height
image = Image.new('1', (width, height))
draw = ImageDraw.Draw(image)
draw.rectangle((0,0,width,height), outline=0, fill=0)
padding = 0
top = padding
bottom = height-padding
x = 0
timeframe = 0.01
font = ImageFont.truetype('04B_08__.TTF',8)

###############################
# ADD YOUR VERUS WALLET BELOW #
###############################
my_Verus_Wallet = "YOUR_VERUS_WALLET"

def convert_to_th(input_hashrate):
    units = {
        "H/s": 1e-12,
        "KH/s": 1e-9,
        "MH/s": 1e-6,
        "GH/s": 1e-3,
        "G H/s": 1e-3,
        "TH/s": 1,
        "PH/s": 1e3,
        "EH/s": 1e6
    }
    try:
        value, unit = input_hashrate.split()
        return float(value) * units[unit]
    except ValueError:
        return float(0.00)*units["H/s"]

def get_coin_price(coin_id, coin_name):
    url = f"https://api.coingecko.com/api/v3/simple/price?ids={coin_id}&vs_currencies=usd"
    try:
        response = requests.get(url)
        response.raise_for_status()
        data = response.json()
        return data.get(coin_name, {}).get("usd")
    except requests.RequestException as e:
        print(f"Error fetching {coin_name} price: {e}")
        return None

def format_hash_rate(hash_rate):
    units = ['H/s', 'KH/s', 'MH/s', 'GH/s', 'TH/s', 'PH/s', 'EH/s', 'ZH/s']
    unit_index = 0
    while hash_rate >= 1000 and unit_index < len(units) - 1:
        hash_rate /= 1000
        unit_index += 1
    return f"{hash_rate:.2f} {units[unit_index]}"

def convert_to_output_units(hash_rate_th):
    units = [
        (1e9, "ZH/s"),
        (1e6, "EH/s"),
        (1e3, "PH/s"),
        (1, "TH/s"),
        (1e-3, "GH/s"),
        (1e-6, "MH/s"),
        (1e-9, "KH/s"),
        (1e-12, "H/s")
    ]
    for factor, unit in units:
        if hash_rate_th >= factor:
            return hash_rate_th / factor, unit
    return hash_rate_th, "H/s"


def get_verus_data(verus_url):
    try:
        response = requests.get(verus_url)
        response.raise_for_status()
        data = response.json()
        return {
            "hashrate": data.get("hashrateString", "N/A"),
            "balance": data.get("balance", "N/A"),
            "paid": data.get("paid", "N/A")
        }
    except requests.RequestException as e:
        print(f"Error fetching Verus data: {e}")
        return None

def buffer(sec):
    disp.getbuffer(image)
    disp.ShowImage()
    time.sleep(sec)
    draw.rectangle((0, 0, width, height), outline=0, fill=0)

def linetext(line, content):
    draw.text((x, top+line), content, font=font, fill=255)

def main():
    verus_url = "https://luckpool.net/verus/miner/" + my_Verus_Wallet

    current_date = datetime.now()
    draw.rectangle((0, 0, width, height), outline=0, fill=0)

    # Get the width of the date and time strings using getbbox
    date_text = current_date.strftime("%B %d %Y")
    time_text = current_date.strftime("%-I:%M %p")
    date_bbox = font.getbbox(date_text)
    time_bbox = font.getbbox(time_text)
    date_width = date_bbox[2] - date_bbox[0]
    time_width = time_bbox[2] - time_bbox[0]

    # Calculate the X position to center the text
    date_x = (width - date_width) // 2
    time_x = (width - time_width) // 2

    # Draw the centered text
    draw.text((date_x, 8), date_text, font=font, fill=255)
    draw.text((time_x, 16), time_text, font=font, fill=255)

    buffer(3)

    verus_data = get_verus_data(verus_url)
    match = re.match(r"^\d+(\.\d+)?", verus_data['hashrate'])
    hash_rate_num = float(match.group(0))
    adjusted_hash_rate = hash_rate_num

    if verus_data:
        verus_price = get_coin_price("verus-coin", "verus-coin")
        current_amount = verus_price * verus_data['balance']
        total_amount = verus_price * verus_data['paid']
        
        linetext(0, f"VRSC: ${verus_price:.2f}")
        linetext(8, f"Amount: {verus_data['paid']:.3f}" + f" (${total_amount:,.2f})")
        linetext(16, f"Now: {verus_data['balance']:.4f}" + f" (${current_amount:,.2f})")
        linetext(24, f"RATE: {verus_data['hashrate']}/s")
        buffer(20)

        myVerus = convert_to_th(f"{verus_data['hashrate']}/s")

if __name__ == "__main__":
    while True:
        main()
