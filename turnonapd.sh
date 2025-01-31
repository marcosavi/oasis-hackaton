#!/bin/bash

# Path to the file that needs editing
FILE="/etc/network/interfaces"

# Uncomment the required lines
sudo sed -i '/#iface wlan0 inet static/s/^#//g' $FILE
sudo sed -i '/# address 192.168.4.1/s/^#//g' $FILE
sudo sed -i '/# netmask 255.255.255.0/s/^#//g' $FILE
sudo sed -i '/#allow-hotplug wlan0/s/^#//g' $FILE
sudo sed -i '/#up iptables-restore < \/etc\/iptables.ipv4.nat/s/^#//g' $FILE

# Disable NetworkManager and enable hostapd
sudo systemtctl stop hostapd
sudo systemtctl stop hostapd
sudo systemtctl stop hostapd
sudo systemtctl stop hostapd
sudo systemctl stop dnsmasq
sudo systemctl stop dnsmasq
sudo systemctl stop dnsmasq
sudo systemctl stop dnsmasq
sudo systemctl stop NetworkManager
sudo systemctl stop NetworkManager
sudo systemctl stop NetworkManager
sudo systemctl start dnsmasq
sudo systemctl start hostapd

echo "NetworkManager is stopped and disabled. Hostapd is started and enabled."

