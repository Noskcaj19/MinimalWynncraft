import re
import json

files = []
mods_lines = open("MODS.md", "r").readlines()
for mod in mods_lines:
    match = re.search(r".*?\)(\*)? (?:.*) PID=(.*) FID=(.*)", mod)
    files.append(
        {
            "projectID": int(match.group(2)),
            "fileID": int(match.group(3)),
            "required": match.group(1) is None,
        },
    )


manifest = {
    "minecraft": {
        "version": "1.12.2",
        "modLoaders": [{"id": "forge-14.23.5.2768", "primary": True}],
    },
    "manifestType": "minecraftModpack",
    "manifestVersion": 1,
    "name": "Minimal Wynncraft Modpack",
    "version": "0.2.0",
    "author": "Noskcaj19",
    "files": files,
    "overrides": "overrides",
}

print(json.dumps(manifest, indent=2))