set mods=mods/@Namalsk Island;^
mods/@Namalsk Survival;^
mods/@CF;^
mods/@Dabs Framework;^
mods/@AICFireplaceIndoor;^
mods/@BuildEverywhere;^
mods/@dbo_creatures;^
mods/@GoreZ;^
mods/@GRW ER7 Gauss Rifle;^
mods/@PvZmoD_CustomisableZombies;^
mods/@SnowOverhaul;^
mods/@Wolf Packs;^
mods/@CreepyZombies;^
mods/@ZomBerry Admin Tools;^
mods/@Kck Mutant Monsters;^
mods/@Radio Toggle and Push-to-Talk;^
mods/@BG_Better9VPlus;^
mods/@No Force Weapon Raise;^
mods/@PseudoGiant;^
mods/@Mystery Box;^
mods/@Ear-Plugs;^
mods/@NoTransmitterNoise;^
mods/@ReducedFireWeaponDamage;^
mods/@DoubleGunHP;^
mods/@CJ187-LootChest;^
mods/@FastFuel;^
mods/@In-Vehicle-Inventory;^
mods/@Vehicle_Battery_Realism;^
mods/@Disable Fuel Pumps;^
mods/@StaminaSettings;^
mods/@TruckFixV2;

set servermods=mods/@SpawnerBubaku

start DayZServer_x64.exe ^
 -config=serverDZ.cfg ^
 -port=2302 ^
 -dologs ^
 -adminlog ^
 -netlog ^
 -freezecheck ^
 -limitFPS=200 ^
 -profiles=C:\Users\Admin\Desktop\Servers\DayZ\config ^
 "-mod=%mods%" ^
 "-servermod=%servermods%"