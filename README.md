# DayZ NAMALSK Server Configuration Files

This is collection of configuration files used for our private Namalsk PVE server.

### NOTE:
It is worth mentioning that a functional gas mask with a filter installed is required when crossing the choke points (Sebjan Dam and Sebjan Marsh) to the southern part of the island as well as within Athena-3. Full NBC gear is required within Athena-2.

## Installation

1. Prereqs: __Windows__ Host Machine
2. Install a DayZ server using SteamCMD. [Refer to this link for guidance.](https://www.ionos.com/digitalguide/server/know-how/dayz-server-hosting/)
3. Install the mods that are listed at the top of start.bat into mods/ and their associated keys into keys/
4. Namalsk Island (the map) requires special care. With Namalsk Island (the mod) installed, install the __regular__ Namalsk mission files from [the official Namalsk github](https://github.com/SumrakDZN/Namalsk-Server), following the installation instructions there.
5. Replace __every__ file within your SteamCMD DayZ server installation with the ones that are within this repo, should they exist.
6. Ensure that start.bat is able to find DayZServer_x64.exe and run it.
7. (Optional) For admin access via the ZomBerry mod, add each user's SteamID to config/ZomBerry/admins.cfg
8. (Optional) economyeditor/namalsk.xml contains all the custom territories added. In order to make changes, use the Economy Editor DayZTool to open it after copying the relative economy editor tool files from "Central Economy Tool" from [the official Namalsk github](https://github.com/SumrakDZN/Namalsk-Server). After making changes to namalsk.xml within the tool, export the zones and __append__ them to their relative \*_territories.xml files from territoryTypes/\*.xml

## Usage

Run start.bat, assuming ports are forwarded correctly.

## Known Issues

Sometimes players will get sick with gas contamination when riding vehicles through the fog despite wearing the appropriate PPE. It _seems_ less likely to happen if you equip **and** unequip the appropriate PPE while outside vehicles.
