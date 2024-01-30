# DiscordTM
  
  * DiscordTM (Discord Terminal Messenger) is a command line script to send a recieve Discord messages without the webapp
  * Haven't found an actual use for this so 🤷‍♂️

  * This was also just something I wrote in class to pass the time so it doesn't work all that well


  ## How to use
  
  Install the latest version of Python and install
  
  ```https://www.python.org/downloads/```
    
  Once Python is installed open a new terminal/Powershell if on Windows (also called command line) and run the command
  
  ```pip install discord```


  Download the entire folder titled DiscordTM and run the ```main.py``` file 
  When the file opens in the terminal you will be prompted with multiple options, pick the setup and follow the directions below to get the channel id/bot token of the bot

### Setup the Discord Application

  Navigate to ```https://discord.com/developers/applications``` and make a new application (the bot name does not matter)

  Under the "General Information" tab find the application id to be used to invite the bot

  Under the "Bot" tab click "Reset Token" and copy the token (this is unique and allows full control over the bot so do not share it)

  Still in the "Bot" tab scroll down to "Privileged Gateway Intents" and enable "Message Content Intent" and under "Bot Permissions" enable "Send Messages"

### Setup Discord Channel

  Create a new (or use an existing) Discord server and invite the bot by using this link but replacing (YOURBOTID) (remove the parenthesis when replacing with your id) with the application id you copied before ```https://discord.com/oauth2/authorize?client_id=(YOURBOTID)&permissions=0&scope=bot%20applications.commands```

  In the discord server, right click the channel you want to be used and copy the channel id and make sure the bot has permission to view the channel

### Setup DiscordTM 

  Run the main file by navigating to the directory in a terminal and running ```python3 main.py``` or ```python main.py``` or right click the main file and open with Python

  Run the setup by entering 3 when prompted and setting the channel id and token id, this is where you can change your username

## Run DiscordTM 

  To run the program, launch the ```main.py``` program and follow the prompts to send and recieve messages. From there, follow the prompts to be able to send + recieve messages
  
  * be aware you will need to load the message viewer and the message sender in different terminals
  * the program will produce an error if you do not have a channel id and token set
