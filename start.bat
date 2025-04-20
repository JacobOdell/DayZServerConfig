set mods=^
mods/@DeerIsle;^
mods/@Dabs Framework;^
mods/@AICFireplaceIndoor;^
mods/@dbo_creatures;^
mods/@CF;^
mods/@GoreZ;^
mods/@PvZmoD_CustomisableZombies;^
mods/@CreepyZombies;^
mods/@ZomBerry Admin Tools;^
mods/@Kck Mutant Monsters;^
mods/@Radio Toggle and Push-to-Talk;^
mods/@BG_Better9VPlus;^
mods/@No Force Weapon Raise;^
mods/@PseudoGiant;^
mods/@Ear-Plugs;^
mods/@NoTransmitterNoise;^
mods/@ReducedFireWeaponDamage;^
mods/@DoubleGunHP;^
mods/@FastFuel;^
mods/@In-Vehicle-Inventory;^
mods/@Repair Vehicle Tank;^
mods/@StaminaSettings;^
mods/@Winter Livonia;^
mods/@Winter Chernarus V2;^
mods/@Winter DeerIsle;^
mods/@TruckFixV2;^
mods/@Zens Blood Trail;^
mods/@WendigoCreature;^
mods/@AJs Creatures V2;^
mods/@FlipTransport;

REM set servermods=mods/@SpawnerBubaku

start DayZServer_x64.exe ^
 -config=serverDZ.cfg ^
 -dologs ^
 -port=2302 ^
 -adminlog ^
 -netlog ^
 -freezecheck ^
 -limitFPS=200 ^
 -profiles=C:\Users\Admin\Desktop\Servers\DayZ\DeerIsleWinter\config ^
 -NoBattlEye ^
 "-mod=%mods%" ^
 "-servermod=%servermods%"