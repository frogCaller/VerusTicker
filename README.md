# Verus Ticker
<img src="images/verusTicker.jpeg" alt="tinySetup1" width="300">
This project uses a 2.23-inch OLED HAT with a Raspberry Pi to display Verus mining statistics using luckpool's API to get the data.

# Materials
* [Raspberry Pi Zero WH](https://amzn.to/49mZVxC) or [Zero 2 WH](https://amzn.to/3Ov69Dm)<br />
* [Micro SD Cards](https://amzn.to/4erXgWD)<br />
* [2.23inch OLED HAT](https://amzn.to/3V2gCKb)<br />
* [90-degree GPIO extenders](https://amzn.to/3Uooea9)<br />

<br />
(Amazon affiliate links)<br />


## **Installations**

1. **OS install:**
   - ___Raspberry Pi Zero:___ Raspberry Pi OS Lite (64-bit) <br />
   - ___Raspberry Pi 5:___ Raspberry Pi OS Lite (64-bit) <br />
   
2. **Enable SPI & I2C: ( Pi Zero )**
   - Open a terminal on your Raspberry Pi.
   - Run sudo raspi-config.
   - Navigate to Interfacing Options -> SPI -> Enable.
   - Navigate to Interfacing Options -> I2C -> Enable.

3. **Python libraries: ( Pi Zero )**
   - sudo apt-get update
   - sudo apt-get install python3-pip
   - sudo apt-get install python3-pil
   - sudo apt-get install python3-numpy
   - sudo pip3 install spidev
   <br />

# Wiring and Setup
1. **Connect 2.23inch OLED HAT to Raspberry Pi Zero:**
   - Connect the 2.23inch OLED HAT to your Raspberry Pi. <br />
   - Connect the UPS Hat for continuous power supply. This will allow you to move the project anywhere without worrying about power interruptions.

2. Clone the repository:
   ```bash
   sudo apt install git -y
   git clone https://github.com/frogCaller/verus-stats-2.23inch.git
   cd VerusTicker

# Usage Instructions
1. Edit `myVerus.py` and add your Verus Wallet Address:
  - Open myVerus.py in a text editor.
    ```
    nano myVerus.py.py
    ```
  - Locate the line where the wallet address is defined and replace the placeholder with your own Verus wallet address.
    ```
    wallet_address = "VERUS_WALLET_ADDRESS"
    ```
    
2. Display Verus miner stats  ( Pi Zero ):
   - Run the script: `python3 myVerus.py`

3. Display fortune messages (Optional):
   - Utilize the fortune command to display random quotes.
   - Make sure you have fortune installed. `sudo apt install fortune -y`
   - Run `fortune.py`

# Troubleshooting
Common Issues:
   - Ensure SPI & I2C are enabled in the Raspberry Pi configuration.
   - Check all connections if the screen does not display anything.
   - Verify all required packages are installed correctly.
   - [More Info](https://www.waveshare.com/wiki/2.23inch_OLED_HAT)
