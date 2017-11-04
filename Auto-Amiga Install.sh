#!/bin/bash

pushd ~/RetroPie/../
wget https://github.com/HoraceAndTheSpider/RetroPieAmigaSetup/archive/master.zip 
unzip master.zip
rm master.zip
mv RetroPieAmigaSetup-master .retropie_amiga_setup
cd .retropie_amiga_setup
python3 amiga_setup_script.py
cd ..
rm -r .retropie_amiga_setup

cp ~/RetroPie/BIOS/Amiga/kick13.rom ~/RetroPie/roms/amiga-data/_BootWHD/Devs/Kickstarts/kick34005.A500
cp ~/RetroPie/BIOS/Amiga/kick31.rom ~/RetroPie/roms/amiga-data/_BootWHD/Devs/Kickstarts/kick40068.A1200
cp ~/RetroPie/BIOS/Amiga/kick12.rom ~/RetroPie/roms/amiga-data/_BootWHD/Devs/Kickstarts/kick33180.A500

popd


