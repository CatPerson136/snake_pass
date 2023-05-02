# This will install it for Ubuntu and its dirivites
if [ -d /etc/apt ]
then
    sudo apt install pip python3-tk
    pip install customtkinter py4j
fi

# This will install it for Arch and its dirivites (untested)
if [ -d /etc/pacman.d ]
then
   sudo pacman -S python3-pip tk 
   pip install customtkinter py4j
fi

# This will install it for Fedora and its dirivites
if [ -d /etc/dnf ]
then
   sudo dnf install python3-pip python3-tkinter 
   pip install customtkinter py4j
fi
