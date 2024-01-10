# Modem_API
A program to interface with the ZYXEL VMG8623-T50B modem to automate interactions.

Key Features:
- Get the status of the Wifi
- Open/Close the Wifi (seperate for each 2.4G, 5G and guest networks)
- Get information about the connected devices
- Auto close the Wifi if non of the whitelisted devices are connected
- Connect and show the steps in the GUI live (not headless browser) 


To connect to the modem you need to configure the credentials.json with the proper information.
Which are the "username" and "password".
Optionaly for the auto close you have to specify in the "whitelisted_devices" the "Mac_addresses" of those devices.

