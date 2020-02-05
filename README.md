# osu-obs-script
OBS script that gets osu! player info and displays it. Designed for tourney streaming.

Displays player name, rank, country, and avatar.

## Known Issues
If you keep getting a `no such file or directory` error, make a new folder in the `img` folder called `avatars`

## Installation
Tested only on Windows, but should work across Mac/Linux

### 1. Install Python 3.6.x and prerequisites
**OBS only supports Python 3.6.x for scripts.** [Script tested on Python 3.6.8.](https://www.python.org/downloads/release/python-368/) Adding Python to PATH is recommended.

Once installed, install requests using `pip install requests` in terminal/PowerShell.

### 2. Set up OBS
Open the Scripts window (Tools > Scripts). Click on the Python Settings tab and enter the installation path for Python. On Windows, the default install path for Python 3.6 is `C:/Users/[Username]/AppData/Local/Programs/Python/Python36`.

### 3. Set up plugin
The plugin should be in its own folder (containing `player_info.py` and the `img` folder). In the Scripts tab, add `player_info.py` as a script.

### 4. Configuration
* **osu! API key** - Enter your osu! api key here (https://osu.ppy.sh/p/api/)
* **User** - User to display (can be in user ID or username format)
* **Name Source** - Source to display username to (this must be a text source)
* **Rank Source** - Source to display rank to (this must be a text source)
* **Avatar Source** - Source to display avatar to (this must be an image source)
* **Country Source** - Source to display country flag to (this must be an image source)

The avatar is downloaded and saved to the `img/avatars/` directory. Flags are located in the `img/flags/` directory.

**Once settings are saved, you must refresh the display using the Refresh button.**

### 5. Additional displays
The easiest way to make additional player displays is to make a copy of the `player_info.py` script in the same folder and configuring it separately.

## Acknowledgements
Flags from https://github.com/ppy/osu-resources/

## License
[GNU General Public License v3.0](https://github.com/ceIery/osu-obs-script/blob/master/LICENSE)
