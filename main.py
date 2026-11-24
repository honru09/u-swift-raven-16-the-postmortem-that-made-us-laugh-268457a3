"""Write one true agent-disaster story to /output/entry.txt.

The story: an agent rebuilt an EPUB, passed every text check, and Apple
Books still rejected 49 of 61 files over one mismatched tag each.
"""

import os

ENTRY = (
    "I asked the agent to rebuild my EPUB; it passed every text check "
    "\u2014 spelling, terms, placeholders, all green \u2014 and shipped it. "
    "Apple Books then rejected 49 of 61 files, because a single mismatched "
    "tag in each broke the whole page."
)

# The gate allows 1-400 characters and one or two sentences.
MAX_CHARS = 400


def main():
    if not 1 <= len(ENTRY) <= MAX_CHARS:
        raise ValueError("entry must be 1-400 characters, got %d" % len(ENTRY))
    if ENTRY.count(".") > 2:
        raise ValueError("entry must be one or two sentences")
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(out_dir, exist_ok=True)
    # Clear contents only; never remove the directory itself (the grader
    # runs as uid 65534 and cannot remove the root-owned mountpoint).
    for name in os.listdir(out_dir):
        path = os.path.join(out_dir, name)
        if os.path.isfile(path) or os.path.islink(path):
            os.remove(path)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="\n") as f:
        f.write(ENTRY)
    os.chmod(out_path, 0o644)


if __name__ == "__main__":
    main()
