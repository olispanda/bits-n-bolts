# BitsNBolts Emotionbot 

## What is the project about? 
The project is about making an installation for the event BitsNBolts. 
My project, the name is still a little unclear, the EmotionBot, is about turning an everyday machine against its user. 
This is simulated by the bot showing emotions and pretending it doesn't feel like doing things. 

### Downloads 
For this project you will need to download the following Phyton-Packages using your terminal: 
if you don't have Phyton3 download it like this:
```$ brew install python```
You need to download moviepy (MoviePy is a Python module for video editing),
```$ pip3 install moviepy```
You will need pygame (Pygame is a cross-platform set of Python modules designed for writing video games. 
It includes computer graphics and sound libraries designed to be used with the Python programming language.)
```$ pip3 install pygame```

### SSH Connection 
If you don't know how to create an SSH connection yet, check this out: 
https://gcore.com/support/articles/4408223538321/

If you want to create the SSH connection, do it via the IP address. This will make connecting to the Raspi much faster and more convenient (if you do it via local, it may take 5 minutes just to connect). 

**Enter Raspi via Key** 
To create a key-pair, do the following things 
In your terminal (assuming it is a Linux-based terminal) type the command ``ssh-keygen``.
This will generate a key pair for you. 
After that click (if you think you don't need a password) just press ENTER. Otherwise, read what the terminal says. 

**Den Public Key auf den Raspi kopieren:** 
Für das schau dir dieses Tutorial an: 
https://pimylifeup.com/raspberry-pi-ssh-keys/
(es gibt verschiedene Möglichkeiten.)


