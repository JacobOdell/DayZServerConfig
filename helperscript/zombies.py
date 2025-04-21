import os

# List of zombie names
zombie_names = [
    "ZmbM_RCZ_HermitSkinny_Beige",
    "ZmbM_RCZ_HermitSkinny_Black",
    "ZmbM_RCZ_HermitSkinny_Gray",
    "ZmbM_RCZ_HermitSkinny_Blue",
    "ZmbM_RCZ_HermitSkinny_Green",
    "ZmbM_RCZ_HermitSkinny_Red",
    "ZmbM_RCZ_HermitSkinny_White",
    "ZmbM_RCZ_HermitSkinny_Yellow",
    "ZmbF_RCZ_FatSkinny_Beige",
    "ZmbF_RCZ_FatSkinny_Black",
    "ZmbF_RCZ_FatSkinny_Gray",
    "ZmbF_RCZ_FatSkinny_Blue",
    "ZmbF_RCZ_FatSkinny_Green",
    "ZmbF_RCZ_FatSkinny_Red",
    "ZmbF_RCZ_FatSkinny_White",
    "ZmbF_RCZ_FatSkinny_Yellow",
    "ZmbM_RCZ_Military_Beige",
    "ZmbM_RCZ_Military_Black",
    "ZmbM_RCZ_Military_Gray",
    "ZmbM_RCZ_Military_Blue",
    "ZmbM_RCZ_Military_Green",
    "ZmbM_RCZ_Military_Red",
    "ZmbM_RCZ_Military_White",
    "ZmbM_RCZ_Military_Yellow",
    "ZmbF_RCZ_Scientist_Beige",
    "ZmbF_RCZ_Scientist_Black",
    "ZmbF_RCZ_Scientist_Gray",
    "ZmbF_RCZ_Scientist_Blue",
    "ZmbF_RCZ_Scientist_Green",
    "ZmbF_RCZ_Scientist_Red",
    "ZmbF_RCZ_Scientist_White",
    "ZmbF_RCZ_Scientist_Yellow",
    "ZmbM_RCZ_Officer_Beige",
    "ZmbM_RCZ_Officer_Black",
    "ZmbM_RCZ_Officer_Gray",
    "ZmbM_RCZ_Officer_Blue",
    "ZmbM_RCZ_Officer_Green",
    "ZmbM_RCZ_Officer_Red",
    "ZmbM_RCZ_Officer_White",
    "ZmbM_RCZ_Officer_Yellow",
    "ZmbM_RCZ_Worker_Beige",
    "ZmbM_RCZ_Worker_Black",
    "ZmbM_RCZ_Worker_Gray",
    "ZmbM_RCZ_Worker_Blue",
    "ZmbM_RCZ_Worker_Green",
    "ZmbM_RCZ_Worker_Red",
    "ZmbM_RCZ_Worker_White",
    "ZmbM_RCZ_Worker_Yellow",
    "ZmbF_RCZ_Nurse_Beige",
    "ZmbF_RCZ_Nurse_Black",
    "ZmbF_RCZ_Nurse_Gray",
    "ZmbF_RCZ_Nurse_Blue",
    "ZmbF_RCZ_Nurse_Green",
    "ZmbF_RCZ_Nurse_Red",
    "ZmbF_RCZ_Nurse_White",
    "ZmbF_RCZ_Nurse_Yellow",
    "ZmbM_RCZ_Civilian_Beige",
    "ZmbM_RCZ_Civilian_Black",
    "ZmbM_RCZ_Civilian_Gray",
    "ZmbM_RCZ_Civilian_Blue",
    "ZmbM_RCZ_Civilian_Green",
    "ZmbM_RCZ_Civilian_Red",
    "ZmbM_RCZ_Civilian_White",
    "ZmbM_RCZ_Civilian_Yellow",
    "ZmbF_RCZ_Civilian_Beige",
    "ZmbF_RCZ_Civilian_Black",
    "ZmbF_RCZ_Civilian_Gray",
    "ZmbF_RCZ_Civilian_Blue",
    "ZmbF_RCZ_Civilian_Green",
    "ZmbF_RCZ_Civilian_Red",
    "ZmbF_RCZ_Civilian_White",
    "ZmbF_RCZ_Civilian_Yellow"
]

# Template XML content
xml_template = """        <Health_Points              Day="100"     Night="100"/>
        <Resistance_to_Bullets      Day="1.0"     Night="1.0"/>     
        <Resistance_to_Melees       Day="1.0"     Night="1.0"/>
        <Resistance_to_HeavyAttack  Day="0.5"     Night="0.5"/>     
        <Resistance_to_Vehicles     Day="1.0"     Night="1.0"/>     
        <Resistance_to_Explosions   Day="0.01"    Night="0.01"/>    
        <Resistance_to_Stun_Bullets Day="0.2"     Night="0.2"/>
        <Resistance_to_HeadShots    Day="0.2"     Night="0.2"/>
        <Resist_to_Melee_HeadShots  Day="0.6"     Night="0.6"/>
        <Special_HeadShot_Weapons   Day="0"       Night="0"/>
        <Move_Speed_Min             Day="0.0"     Night="0.0"/>
        <Move_Speed_Max             Day="3.0"     Night="3.0"/>
        <Move_Speed_Adjust_Max      Day="0.0"     Night="0.0"/>
        <Animation_Type             Day="-9"      Night="-9"/>
        <Chance_To_Spawn_Crawling   Day="0.0"     Night="0.0"/>
        <Can_Dodge                  Day="0"       Night="0"/>
        <Hit_Players_On_Obstacles   Day="0"       Night="0"/>
        <Immune_To_MultiHit         Day="1"       Night="1"/>
        <Attack_Speed               Day="1.0"     Night="1.0"/>
        <Ratio_Damage_Health        LightAttack_NotBlocked="1.0" LightAttack_Blocked="0.0" HeavyAttack_NotBlocked="1.0" HeavyAttack_Blocked="0.5" NightRatio="1.0"/>
        <Ratio_Damage_Shock         LightAttack_NotBlocked="1.0" LightAttack_Blocked="0.0" HeavyAttack_NotBlocked="1.0" HeavyAttack_Blocked="0.5" NightRatio="1.0"/>
        <Bleeding_Chance            LightAttack_NotBlocked="0.1" LightAttack_Blocked="0.0" HeavyAttack_NotBlocked="0.1" HeavyAttack_Blocked="0.1" NightRatio="1.0"/>
        <Damage_Blood               LightAttack_NotBlocked="0" LightAttack_Blocked="0" HeavyAttack_NotBlocked="0" HeavyAttack_Blocked="0" NightRatio="1.0"/>
        <Damage_Stamina             LightAttack_NotBlocked="0" LightAttack_Blocked="0" HeavyAttack_NotBlocked="0" HeavyAttack_Blocked="0" NightRatio="1.0"/>
        <Vision_Distance_Ratio      Day="1.0" Night="0.8" WithBloodyHands="0.5" WithSpecialMask="0.25" MinimumRatioDistance="0.1"/>
        <Can_Be_Backstabbed         Day="1"       Night="1"/>
        <Resist_Contaminated_Effect Day="0"       Night="0"/>
        <Numb_Of_Hit_To_Break_Doors Day="5"       Night="5"/>
        <Size_Mini                  Day="1.0"     Night="1.0"/>
        <Size_Maxi                  Day="1.0"     Night="1.0"/>
        <Can_Throw_Stones           Day="0"       Night="0"/>
"""

def generate_zombie_xml(file_name="zombies.xml"):
    with open(file_name, "w", encoding="utf-8") as f:
        # Write the root element
        f.write("<types>\n")
        
        # Add each zombie <type> entry
        for zombie in zombie_names:
            f.write(f'    <type name="{zombie}">\n')
            f.write(xml_template)
            f.write("    </type>\n")
        
        # Close the root element
        f.write("</types>\n")
    
    print(f"XML file '{file_name}' generated successfully!")

# Run the function
if __name__ == "__main__":
    generate_zombie_xml()
