# Roblox FPS Cap Remover

This Python script allows you to remove the FPS cap in Roblox without the need for injecting into the game. It's a simple solution that you can run manually after each Roblox update or automate by creating a task in the Task Scheduler.

## Usage

1. Ensure you have Python installed on your Windows system. If not, download and install Python from [python.org](https://www.python.org/downloads/).
2. Download the script from `/win/main.py`.
3. Run the script manually with `py <path>/main.py` after each Roblox update or set up a task in the Task Scheduler for automatic execution.

## File Location

The script is currently designed for Windows and can be found at `/win/main.py`.

## How It Works

The script locates the Roblox installation on your system and modifies the `ClientAppSettings.json` file to remove the FPS cap. It achieves this by updating the `"DFIntTaskSchedulerTargetFps"` parameter to a high value (e.g., 1000).

**Note:** Support for other operating systems will be implemented in future updates.

Feel free to contribute and improve upon this script! If you encounter any issues or have suggestions, please open an issue in the repository. Happy gaming!
