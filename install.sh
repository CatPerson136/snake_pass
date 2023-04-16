# This script will install the dependeces for program

if [ -d /etc/apt ]
then
    sudo apt install pip
    pip install customtkinter
    sudo apt install python3-tk
    pip install py4j
fi

# This will install it for Arch and its dirivites
if [ -d /etc/pacman.d ]
then
   sudo pacman -S python3-pip 
   pip install customtkinter
   sudo pacman -S tk  
   pip install py4j
