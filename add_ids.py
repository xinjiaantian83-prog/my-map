import json
from pathlib import Path

SPOTS_FILE = Path("spots.json")
PREFIX = "WNWN-"

def main():
    data = json.loads(SPOTS_FILE.read_text(encoding="utf-8"))

    used_ids = set()
    max_num = 0

    for item in data:
        spot_id = item.get("id")
        if isinstance(spot_id, str) and spot_id.startswith(PREFIX):
            used_ids.add(spot_id)
            try:
                n = int(spot_id.replace(PREFIX, ""))
                if n > max_num:
                    max_num = n
            except ValueError:
                pass

    next_num = max_num + 1

    for item in data:
        if "id" not in item or not item["id"]:
            while f"{PREFIX}{next_num:04d}" in used_ids:
                next_num += 1

            new_id = f"{PREFIX}{next_num:04d}"
            item["id"] = new_id
            used_ids.add(new_id)
            next_num += 1

    SPOTS_FILE.write_text(
        json.dumps(data, ensure_ascii=False, indent=2),
        encoding="utf-8"
    )

    print("spots.json に固定IDを付与しました。")

if __name__ == "__main__":
    main()
