import json
import re

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


def main():
    spots = []

    with open(RAW_FILE, "r", encoding="utf-8") as f:
        for i, line in enumerate(f):
            item = parse_line(line)
            if item:
                item["id"] = "WNWN-" + str(i + 1).zfill(4)
                spots.append(item)

    with open(OUT_FILE, "w", encoding="utf-8") as f:
        json.dump(spots, f, ensure_ascii=False, indent=2)

    print(f"Wrote {len(spots)} spots to {OUT_FILE}")


if __name__ == "__main__":
    main()
