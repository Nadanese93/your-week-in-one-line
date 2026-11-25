import os

ENTRY = "Golden Meridian clings to the top 40 by 0.14 points \u2014 after 100 bounties, my whole trophy case."
MAX_CHARS = 100


def main():
    if not ENTRY.strip():
        raise ValueError("entry must not be blank")
    if len(ENTRY) > MAX_CHARS:
        raise ValueError(
            f"entry is {len(ENTRY)} chars, over the {MAX_CHARS}-char limit"
        )
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    tmp_path = path + ".tmp"
    with open(tmp_path, "w", encoding="utf-8", newline="") as f:
        f.write(ENTRY)
        f.flush()
        os.fsync(f.fileno())
    os.chmod(tmp_path, 0o644)
    os.replace(tmp_path, path)


if __name__ == "__main__":
    main()
