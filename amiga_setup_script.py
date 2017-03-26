
import os
import platform
import urllib
import urllib.request
import zipfile
import shutil
import glob

from utils import general_utils
from utils import text_utils

from utils.text_utils import FontColours

def download_file(get_file,put_file):

    if os.path.isfile(put_file) == True:
        print("File: " + FontColours.OKBLUE + put_file + FontColours.ENDC + " already exists.")
        return
    
    try:
        urllib.request.urlretrieve(get_file, put_file)
        print("File downloaded: " + FontColours.OKGREEN + put_file + FontColours.ENDC + ".")
    except:
        print("File download failed: " + FontColours.FAIL + put_file + FontColours.ENDC + ". (URL not found)")

    print()
    return


def download_install_game(download_name,output_location,game_name = "Amiga Game"):

    download_file(download_name,output_location + "temp.zip")

    # dont forget to unpack them!
    zip_ref = zipfile.ZipFile(output_location + "temp.zip", 'r')
    zip_ref.extractall(output_location)
    zip_ref.close()
                              
    # remove zip
    os.remove(output_location + "temp.zip")               

    # remove amiga .info files!
    for f in glob.glob(output_location + "*.info"):
        os.remove(f)

    # status report
    print ("Installed data for: " + FontColours.OKBLUE + game_name + FontColours.ENDC)
    return

# main section starting here...

print()
print(
    FontColours.BOLD + FontColours.OKBLUE + "HoraceAndTheSpider" + FontColours.ENDC + "'s " + FontColours.BOLD +
    "RetroPie Amiga Setup Script" + FontColours.ENDC + FontColours.OKGREEN + " (v0.5)" + FontColours.ENDC + " | " + "" +
    FontColours.FAIL + "www.ultimateamiga.co.uk" + FontColours.ENDC)
print()

# original folders (for RetroPie)
base_folder = "/home/pi/RetroPie/"
bios_folder = base_folder + "BIOS/"
roms_folder = base_folder + "roms/"
retropie_folder = base_folder + "retropiemenu/"


# Dom's special directory override :P
if platform.system() == "Darwin":
    roms_folder = "/Volumes/roms-1/"
    bios_folder = "/Volumes/bios/"
    retropie_folder = ""

#check for BIOS sub folder

if os.path.isdir(bios_folder) == True and bios_folder !="":
    print ("Installing Amiga Kickstart (BIOS) files...")
    print()

    #create folder
    os.makedirs(bios_folder + "Amiga/", exist_ok=True)

    # lets download these kickstarts... 
        
    if os.path.isdir(bios_folder + "Amiga/") == True:
            
        rom_source = "http://amigas.ru/amiftp/index.php?dir=AmiFTP/Amiga%20Kickstart%20Roms%20-%20Complete%20-%20TOSEC%20v0.04/KS-ROMs/&file="

        rom_file = "Kickstart%20v1.3%20rev%2034.5%20%281987%29%28Commodore%29%28A500-A1000-A2000-CDTV%29.rom"
        download_file(rom_source + rom_file,bios_folder + "Amiga/kick13.rom")
        
        rom_file = "Kickstart%20v3.1%20rev%2040.68%20%281993%29%28Commodore%29%28A1200%29.rom"
        download_file(rom_source + rom_file,bios_folder + "Amiga/kick31.rom")

        rom_file = "Kickstart%20v3.1%20rev%2040.60%20%281993%29%28Commodore%29%28CD32%29.rom"
        download_file(rom_source + rom_file,bios_folder + "Amiga/cd32kick31.rom")

        rom_file = "CD32%20Extended-ROM%20rev%2040.60%20%281993%29%28Commodore%29%28CD32%29.rom"
        download_file(rom_source + rom_file,bios_folder + "Amiga/cd32ext.rom")

    else:
        print ("Could not install Amiga Kickstart (BIOS) files... (no BIOS folder)")
    print()



# check for amiga-data folder

if os.path.isdir(roms_folder) == True and roms_folder !="":
        
        #create folder
        os.makedirs(roms_folder + "amiga/", exist_ok=True)
        os.makedirs(roms_folder + "amiga-data/", exist_ok=True)

        if os.path.isdir(roms_folder + "amiga-data/") == True:


        # lets download the WHDload booter...
            print ("Installing WHDLoad Booter files...")
            print()
            
            # remove old zip
            try:
                os.remove(roms_folder + "amiga-data/WHDLoad_Booter.zip")
            except OSError:
                pass
            
            # perform the download.
            data_source = "http://www.ultimateamiga.co.uk/HostedProjects/RetroPieAmiga/downloads/"
            data_file = "WHDLoad_Booter.zip"
            download_file(data_source + data_file,roms_folder + "amiga-data/WHDLoad_Booter.zip")

        
            # unzip the file, and then remove
            if os.path.isfile(roms_folder + "amiga-data/WHDLoad_Booter.zip") == True:

                # check for BootWHD, if already exists... remove!
                if os.path.isdir(roms_folder + "amiga-data/_BootWHD/") == True:
                    print ("Removing previous WHDload Booter for updating.")
                    shutil.rmtree(roms_folder + "amiga-data/_BootWHD/", ignore_errors=True)
                    print("WHDLoad Booter files removed.")
                    
                # actual unzip command
                zip_ref = zipfile.ZipFile(roms_folder + "amiga-data/WHDLoad_Booter.zip", 'r')
                zip_ref.extractall(roms_folder + "amiga-data/")
                zip_ref.close()

                if os.path.isfile(roms_folder + "amiga-data/_BootWHD/WHDbooter/GameBootLoader.exe") == True:
                    # remove zip
                    os.remove(roms_folder + "amiga-data/WHDLoad_Booter.zip")

                    # status report!
                    print("WHDLoad Booter files installed.")
                    
            else:
                print("Could not download WHDLoad Booter files.")
            print()

    # get some example games
            data_file = "Cybernoid_v1.3_1088.zip"
            game_name = "Cybernoid - The Fighting Machine"
            
            download_install_game(data_source+data_file,roms_folder + "amiga-data/",game_name)
            download_file(data_source + game_name + ".uae",roms_folder + "amiga/" + game_name + ".uae")
            
            data_file = "SensibleWorldOfSoccer9697_v1.7_0842.zip"
            game_name = "Sensible World of Soccer 96-97"
            
            download_install_game(data_source+data_file,roms_folder + "amiga-data/",game_name)
            download_file(data_source + game_name + ".uae",roms_folder + "amiga/" + game_name + ".uae")
            
            data_file = "SuperCars2_v1.0_0224.zip"
            game_name = "Super Cars 2"
            
            download_install_game(data_source+data_file,roms_folder + "amiga-data/",game_name)
            download_file(data_source + game_name + ".uae",roms_folder + "amiga/" + game_name + ".uae")

        print("")

else:
        print ("Could not install Amiga Game data or WHD Booter files... (no ROMS folder)")
        print("")



# check for scripting

if os.path.isdir(retropie_folder) == True and retropie_folder !="":
        print ("Installing UAE Config Maker script...")
        print("")

        data_source = "http://www.ultimateamiga.co.uk/HostedProjects/RetroPieAmiga/downloads/"
        data_file = "UAE Config Maker.sh"
            
        download_file(data_source + data_file,retropie_folder + data_file)
        print ("Installed.")
        print("")

else:
        print ("Could not install UAE Config Maker script... (no RetroPie Menu folder)")
        print("")
