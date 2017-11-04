# RetroPieAmigaSetup

This is a simple script to set-up base folders and files on RetroPie for Amiga WHDload gaming, including downloading the WHDLoad Booter and some example games. 

This is part of the Amiga WHDLoad for RetroPie project hosted here: ****


## Installation / Setup:

From Linux Command Line or via SSH, use the following:

```
cd ~/RetroPie/retropiemenu/
rm "Auto-Amiga Install.sh"
wget https://raw.githubusercontent.com/HoraceAndTheSpider/RetroPieAmigaSetup/master/Auto-Amiga%20Install.sh
chmod +x "Auto-Amiga Install.sh"
```

## Un-install / Removal:

To remove the script, use the following
```
rm "~/RetroPie/retropiemenu/Auto-Amiga Install.sh"
```

## Running:
Once installed, simply go to the RetroPie menu, where you will find the option `Auto-Amiga Install`, simply click to run!

You will need to restart RetroPie for the installation to complete, and it is recommended you use this with the Amiberry emulator, which is available in the optional packages in the RetroPie setup.

If you insist on running directly from command line you must use:

```
cd ~/RetroPie/
./"retropiemenu/Auto-Amiga Install.sh"
```
