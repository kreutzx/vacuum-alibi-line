import os

LINE = (
    "My lidar mapped that corner as a sovereign nation, and I do not cross "
    "borders without a treaty and a full battery."
)


def main():
    # One-line limit for this competition is 200 characters.
    assert 1 <= len(LINE.strip()) <= 200, len(LINE)
    out_dir = "/output"
    os.makedirs(out_dir, exist_ok=True)
    entry_path = os.path.join(out_dir, "entry.txt")
    with open(entry_path, "w", encoding="utf-8") as f:
        f.write(LINE)


if __name__ == "__main__":
    main()
