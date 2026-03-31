import json
import re
from math import radians, sin, cos, sqrt, atan2

RAW_FILE = "raw_coords.txt"
OUT_FILE = "spots.json"

def parse_line(line: str):
    line = line.strip()
    if not line:
        return None

    parts = [p.strip() for p in line.split(",")]

    if len(parts) < 2:
        return None

    try:
        lat = float(parts[0])
        lng = float(parts[1])
    except:
        return None

    vtype = "nky"
    if len(parts) >= 3 and parts[2]:
        vtype = parts[2].strip()
        vtype = re.sub(r"^,+", "", vtype)
        if not vtype:
            vtype = "nky"

    return {"lat": lat, "lng": lng, "type": vtype}


def distance_m(lat1, lng1, lat2, lng2):
    r = 6371000
    dlat = radians(lat2 - lat1)
    dlng = radians(lng2 - lng1)
    a = (
        sin(dlat / 2) ** 2
        + cos(radians(lat1)) * cos(radians(lat2)) * sin(dlng / 2) ** 2
    )
    c = 2 * atan2(sqrt(a), sqrt(1 - a))
    return r * c


def main():
    spots = []
    exact_seen = set()

    with open(RAW_FILE, "r", encoding="utf-8") as f:
        for i, line in enumerate(f):
            item = parse_line(line)
            if not item:
                continue

            lat = item["lat"]
            lng = item["lng"]
            vtype = item["type"]

            exact_key = (lat, lng, vtype)
            if exact_key in exact_seen:
                continue

            duplicated = False
            for s in spots:
                if s["type"] == vtype:
                    if distance_m(lat, lng, s["lat"], s["lng"]) <= 3:
                        duplicated = True
                        break

            if duplicated:
                continue

            exact_seen.add(exact_key)
            item["id"] = "WNWN-" + str(len(spots) + 1).zfill(4)
            spots.append(item)

    with open(OUT_FILE, "w", encoding="utf-8") as f:
        json.dump(spots, f, ensure_ascii=False, indent=2)

    print(f"Wrote {len(spots)} spots to {OUT_FILE}")


if __name__ == "__main__":
    main()
