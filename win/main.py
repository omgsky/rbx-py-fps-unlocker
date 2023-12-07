import os
import json

versions = os.path.join(os.environ["LOCALAPPDATA"], "Roblox", "versions")

app_folder = os.path.join(versions, [
    folder for folder in os.listdir(versions)
    if os.path.exists(os.path.join(versions, folder, "RobloxPlayerBeta.exe"))
][0])

client_settings = os.path.join(app_folder, "ClientSettings")
client_app_settings_json = os.path.join(client_settings, "ClientAppSettings.json")

os.makedirs(client_settings, exist_ok=True)

with open(client_settings, "w") as f:
    json.dump({
        "DFIntTaskSchedulerTargetFps": 1000
    }, f)
    f.close()
