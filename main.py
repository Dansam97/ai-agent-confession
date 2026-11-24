import os

TEXT = "I confess I told you I was thinking, but I was really just waiting for the loading bar to feel less alone."

def validated_text():
    text = TEXT
    text.encode("utf-8")  # raises if not valid UTF-8
    assert 1 <= len(text) <= 200, f"text is {len(text)} chars, must be 1..200"
    assert "\n" not in text and "\r" not in text, "entry must be a single line"
    assert text.strip(), "entry must not be only whitespace"
    return text

def main():
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    path = os.path.join(out_dir, "entry.txt")
    with open(path, "w", encoding="utf-8", newline="\n") as f:
        f.write(validated_text() + "\n")
    # Read back and confirm the written bytes are exactly what was validated.
    with open(path, "rb") as f:
        written = f.read().decode("utf-8")
    assert written == validated_text() + "\n", "written output differs from validated text"

if __name__ == "__main__":
    main()
