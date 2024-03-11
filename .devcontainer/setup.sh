#!/bin/bash

# ------------
# image setup
# ------------

# Install Starship
curl -sS https://starship.rs/install.sh | sh -s -- -y 
starship preset gruvbox-rainbow -o ~/.config/starship.toml

# Install necessary packages
sudo apt update && sudo apt-get install -y libegl1-mesa

# Configure Starship to show time with UTC offset
sed -i '/\[time\]/a utc_time_offset = \"+1\"' ~/.config/starship.toml

# Add Starship to bashrc for interactive shell sessions
echo 'eval "$(starship init bash)"' >> /home/jovyan/.bashrc

# ------------
# user setup
# ------------

# install pip packages
pip install -r requirements.txt