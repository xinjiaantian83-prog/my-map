import json

coords = []

with open("raw_coords.txt", "r", encoding="utf-8") as f:
    for line in f:
        line = line.strip()
        if not line:
            continue

        parts = line.split(",")

        if len(parts) >= 2:
            lat = float(parts[0])
            lng = float(parts[1])
            coords.append([lat, lng])

with open("spots.json", "w", encoding="utf-8") as f:
    json.dump(coords, f, ensure_ascii=False, indent=2)

print(f"{len(coords)}件を書き出しました")
