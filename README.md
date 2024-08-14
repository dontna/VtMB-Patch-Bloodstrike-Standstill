# VtMB-Patch-Bloodstrike-Standstill
A Python script to allow Blood Strike and Blood Salvo skills to regain blood even while moving.

# Why?
I was playing [Vampire: The Masquerade - Bloodlines](https://store.steampowered.com/app/2600/Vampire_The_Masquerade__Bloodlines/) recently and, for the first time, played as an initiate of the Tremere clan. I was enjoying my time with the unique Thaumaturgy spells, however whenever you use *Blood Strike* or *Blood Salvo* you are required to stand still for 5 seconds to gain any blood back from the spells, which is very silly since filling up your blood metre is the entire point of these spells exsistence. 

So I decided enough was enough, and reverse engineered parts of the game to create this patch.

# How does it work?
The game code for Vampire: The Masquerade - Bloodlines is mostly stored in a dll file named *'vampire.dll'*. Inside of this file there is a function that determines if the blood projectile from our spell should return, or if it should just disappear.

All this patch is doing is finding the unique bytes for that function, then patching it to instantly return. I wouldn't recommend this method by default, but I did a lot of testing and determined that the function wasn't used for anything else in the game.

# How to use?
*Note: This was created to be used ***with the base version of the [Unofficial Patch](https://www.moddb.com/mods/vtmb-unofficial-patch)***. It may not patch the game correctly if you are using the base game or the Unofficial Patch Plus.*

1. Get the path to your base game directory. If you are using Steam, you can do the following steps.
   * Find your game in your Steam library
   * **Right click** --> **Properties**
   * go to **Installed Files** --> **Browse**
   * This will then open a window to your game directory, just copy the path from the bar.
  
2. Run the script. You can paste the directory in as an argument now or you can just run the script and it will ask for the directory later.

   *If you do it as a command line arg, please make sure to wrap it in quotes (" "); otherwise the script can get confused*
   
   `python patch.py "/mnt/games/SteamLibrary/steamapps/common/VtMB/"`

   You can also do `python patch.py` and you can paste in the path later, without having to worry about wrapping it in quotes; which I personally find easier.

4. If you are using the **base unofficial patch** (not unofficial patch plus) and the path is correct, you should see the message `Sucessfully patched game!`

If you see this message, you're ready to start playing!

# How to uninstall patch?
When the script created the patch, it automatically created a backup named 'vampire.dll.bak'. To remove the script all you need to do is the following:

1. Go to the game directory path, you found earlier.
2. From here go to **Vampire** --> **dlls**
3. **Delete 'vampire.dll'**
4. rename **'vampire.dll.bak'** --> **'vampire.dll'**

The patch is now removed, and your game will be restored to how it was before the patch!
