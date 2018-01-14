
import os
import platform
import urllib
import urllib.request
import zipfile
import shutil
import glob
import argparse

from utils import general_utils
from utils import text_utils

from utils.text_utils import FontColours


def fix_ownership(path):
    """Change the owner of the file to SUDO_UID"""

    uid = os.environ.get('SUDO_UID')
    gid = os.environ.get('SUDO_GID')
    if uid is not None:
        os.chown(path, int(uid), int(gid))

    return
        
def download_file(get_file,put_file):

    get_file = urllib.parse.quote(get_file)
    get_file = str.replace(get_file,"https%3A","https:")
    get_file = str.replace(get_file,"http%3A","http:")
    get_file = str.replace(get_file,"%3F","?")
    get_file = str.replace(get_file,"%3D","=")
    get_file = str.replace(get_file,"%26","&")

    if os.path.isfile(put_file) == True:
        print("File: " + FontColours.OKBLUE + put_file + FontColours.ENDC + " already exists.")
        return
    
    try:
        urllib.request.urlretrieve(get_file, put_file)
        print("File downloaded: " + FontColours.OKGREEN + get_file + FontColours.ENDC + ".")
        fix_ownership(put_file)
        print()
        return
    
    except:
        print("File download failed: " + FontColours.FAIL + get_file + FontColours.ENDC + ". (URL not found)")

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
    "RetroPie Amiga Setup Script" + FontColours.ENDC + FontColours.OKGREEN + " (v0.6)" + FontColours.ENDC + " | " + "" +
    FontColours.FAIL + "www.ultimateamiga.co.uk" + FontColours.ENDC)
print()

# Initialisations
# Setup Commandline Argument Parsing

parser = argparse.ArgumentParser(description='Auto-Install Amiga files for RetroPie.')
parser.add_argument('--retropie-path',          # command line argument
                    default=os.path.expanduser('~/RetroPie/'),# Default directory if none supplied                    
                    help="Optional RetroPie path"
                    )

# Parse all command line arguments
args = parser.parse_args()

# original folders (for RetroPie)
base_folder = args.retropie_path
bios_folder = base_folder + "BIOS/"
roms_folder = base_folder + "roms/"
retropie_folder = base_folder + "retropiemenu/"


# Dom's special directory override :P
if platform.system() == "Darwin":
    roms_folder = "/Volumes/roms/"
    bios_folder = "/Volumes/bios/"
    retropie_folder = ""
else:
    base_folder = general_utils.check_inputdirs([base_folder])
    

#check for BIOS sub folder

if os.path.isdir(bios_folder) == True and bios_folder !="":
    print ("Installing Amiga Kickstart (BIOS) files...")
    print()

    #create folder
    os.makedirs(bios_folder + "Amiga/", exist_ok=True)

    # lets download these kickstarts... 
        
    if os.path.isdir(bios_folder + "Amiga/") == True:
            
        rom_source = "http://amigas.ru/amiftp/index.php?dir=AmiFTP/Amiga Kickstart Roms - Complete - TOSEC v0.04/KS-ROMs/&file="

        if os.path.isfile(bios_folder + "Amiga/kick12.rom") == False:
            rom_file = "Kickstart v1.2 rev 33.166 (1986)(Commodore)(A1000).rom"
            download_file(rom_source + rom_file,bios_folder + "Amiga/kick12.rom")

        if os.path.isfile(bios_folder + "Amiga/kick13.rom") == False:
            rom_file = "Kickstart v1.3 rev 34.5 (1987)(Commodore)(A500-A1000-A2000-CDTV).rom"
            download_file(rom_source + rom_file,bios_folder + "Amiga/kick13.rom")
        
        if os.path.isfile(bios_folder + "Amiga/kick31.rom") == False:
            rom_file = "Kickstart v3.1 rev 40.68 (1993)(Commodore)(A1200).rom"
            download_file(rom_source + rom_file,bios_folder + "Amiga/kick31.rom")
            
        if os.path.isfile(bios_folder + "Amiga/a600kick31.rom") == False:
            rom_file = "Kickstart v3.1 rev 40.63 (1993)(Commodore)(A500-A600-A2000).rom"
            download_file(rom_source + rom_file,bios_folder + "Amiga/a600kick31.rom")

        if os.path.isfile(bios_folder + "Amiga/kick25.rom") == False:
            rom_file = "Kickstart v2.05 rev 37.300 (1991)(Commodore)(A600HD).rom"
            download_file(rom_source + rom_file,bios_folder + "Amiga/kick25.rom")

        if os.path.isfile(bios_folder + "Amiga/cd32kick31.rom") == False:
            rom_file = "Kickstart v3.1 rev 40.60 (1993)(Commodore)(CD32).rom"
            download_file(rom_source + rom_file,bios_folder + "Amiga/cd32kick31.rom")

        if os.path.isfile(bios_folder + "Amiga/cd32ext.rom") == False:
            rom_file = "CD32 Extended-ROM rev 40.60 (1993)(Commodore)(CD32).rom"
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
            
    # create sub-folders
            print ("Creating WHDLoad data sub-folders...")
            print()
            os.makedirs(roms_folder + "amiga-data/Games_WHDLoad", exist_ok=True)
            os.makedirs(roms_folder + "amiga-data/Games_WHDLoad_AGA", exist_ok=True)
            os.makedirs(roms_folder + "amiga-data/Games_WHDLoad_CDTV", exist_ok=True)
            os.makedirs(roms_folder + "amiga-data/Games_WHDLoad_CD32", exist_ok=True)
            os.makedirs(roms_folder + "amiga-data/Games_WHDLoad_DemoVersions", exist_ok=True)
            os.makedirs(roms_folder + "amiga-data/Games_WHDLoad_Unofficial", exist_ok=True)

            os.makedirs(roms_folder + "amiga-data/Games_WHDLoad_HDF", exist_ok=True)
            os.makedirs(roms_folder + "amiga-data/Games_WHDLoad_HDF_AGA", exist_ok=True)
            os.makedirs(roms_folder + "amiga-data/Games_WHDLoad_HDF_CDTV", exist_ok=True)
            os.makedirs(roms_folder + "amiga-data/Games_WHDLoad_HDF_DemoVersions", exist_ok=True)
            os.makedirs(roms_folder + "amiga-data/Games_WHDLoad_HDF_AltLanguage", exist_ok=True)
            
            os.makedirs(roms_folder + "amiga-data/Games_CD32", exist_ok=True)
            
    # get some example games
            data_file = "RType.zip"
            game_name = "R-Type"

            if os.path.isfile(roms_folder + "amiga/" + game_name + ".uae") == False:
                download_install_game(data_source+data_file,roms_folder + "amiga-data/Games_WHDLoad/",game_name)
                download_file(data_source + game_name + ".uae",roms_folder + "amiga/" + game_name + ".uae")
            
            data_file = "PuttySquadAGA.zip"
            game_name = "Putty Squad [AGA]"
            
            if os.path.isfile(roms_folder + "amiga/" + game_name + ".uae") == False:          
                download_install_game(data_source+data_file,roms_folder + "amiga-data/Games_WHDLoad_AGA/",game_name)
                download_file(data_source + game_name + ".uae",roms_folder + "amiga/" + game_name + ".uae")

            data_file = "RickDangerous25.zip"
            game_name = "Rick Dangerous 2.5"

            if os.path.isfile(roms_folder + "amiga/" + game_name + ".uae") == False:          
                download_install_game(data_source+data_file,roms_folder + "amiga-data/Games_WHDLoad_DemoVersions/",game_name)
                download_file(data_source + game_name + ".uae",roms_folder + "amiga/" + game_name + ".uae")

            data_file = "AlienBreedTowerAssault_v1.2_AGA_0279.zip"
            game_name = "Alien Breed - Tower Assault [AGA]"

            if os.path.isfile(roms_folder + "amiga/" + game_name + ".uae") == False:                      
                download_install_game(data_source+data_file,roms_folder + "amiga-data/Games_WHDLoad_AGA/",game_name)
                download_file(data_source + game_name + ".uae",roms_folder + "amiga/" + game_name + ".uae")

            data_file = "FlightOfTheAmazonQueen.zip"
            game_name = "Flight of the Amazon Queen"

            if os.path.isfile(roms_folder + "amiga/" + game_name + ".uae") == False:          
                download_install_game(data_source+data_file,roms_folder + "amiga-data/Games_WHDLoad/",game_name)
                download_file(data_source + game_name + ".uae",roms_folder + "amiga/" + game_name + ".uae")


        print("")

else:
        print ("Could not install Amiga Game data or WHD Booter files... (no ROMS folder)")
        print("")



# check for scripting

if os.path.isdir(retropie_folder) == True and retropie_folder !="":
        print ("Installing UAE Config Maker script...")
        print("")

        data_source = "https://raw.githubusercontent.com/HoraceAndTheSpider/UAEConfigMaker/master/"
        data_file = "UAE Config Maker.sh"
            
        download_file(data_source + data_file,retropie_folder + data_file)
        print ("Installed.")
        print("")

else:
        print ("Could not install UAE Config Maker script... (no RetroPie Menu folder)")
        print("")
