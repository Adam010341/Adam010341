#!/usr/bin/env python3
"""Refresh the live GitHub rows of the terminal card in README.md.

The card is the ```text block between <!-- CARD:START --> and <!-- CARD:END -->.
Every row stays exactly as written except the rows this script owns (Repos,
Commits, Followers); those are rewritten in place from the GitHub GraphQL API,
or appended under a separator the first time. Columns are taken from the card
itself, so the ASCII art and the label column stay aligned.

Standard library only. Reads GITHUB_TOKEN; the Actions token is enough, since
only public data is used.

    GITHUB_TOKEN=... python3 scripts/update_card.py            # rewrite README.md
    GITHUB_TOKEN=... python3 scripts/update_card.py --dry-run  # print the card only
"""

import argparse
import json
import os
import re
import sys
import urllib.request
from pathlib import Path

START, END = "<!-- CARD:START -->", "<!-- CARD:END -->"
FENCE_OPEN, FENCE_CLOSE = "```text", "```"
LIVE_LABELS = ("Repos", "Commits", "Followers")
SEPARATOR = "-----------"

QUERY = """
query($login: String!, $cursor: String) {
  user(login: $login) {
    followers { totalCount }
    contributionsCollection { totalCommitContributions }
    repositories(ownerAffiliations: OWNER, privacy: PUBLIC, first: 100, after: $cursor) {
      totalCount
      nodes { stargazerCount isFork }
      pageInfo { hasNextPage endCursor }
    }
  }
}
"""


def graphql(token, variables):
    req = urllib.request.Request(
        "https://api.github.com/graphql",
        data=json.dumps({"query": QUERY, "variables": variables}).encode(),
        headers={
            "Authorization": f"bearer {token}",
            "Content-Type": "application/json",
            "User-Agent": "profile-card-updater",
        },
    )
    with urllib.request.urlopen(req, timeout=30) as resp:
        body = json.load(resp)
    if body.get("errors") or not (body.get("data") or {}).get("user"):
        raise RuntimeError(f"GraphQL error: {body.get('errors') or body}")
    return body["data"]["user"]


def fetch_stats(token, login):
    cursor, stars = None, 0
    while True:
        user = graphql(token, {"login": login, "cursor": cursor})
        repos = user["repositories"]
        stars += sum(r["stargazerCount"] for r in repos["nodes"] if not r["isFork"])
        if not repos["pageInfo"]["hasNextPage"]:
            break
        cursor = repos["pageInfo"]["endCursor"]
    return {
        "repos": repos["totalCount"],
        "stars": stars,
        "commits": user["contributionsCollection"]["totalCommitContributions"],
        "followers": user["followers"]["totalCount"],
    }


def plural(n, word):
    return f"{n:,} {word}{'' if n == 1 else 's'}"


def live_values(stats):
    return {
        "Repos": f"{stats['repos']:,} public · {plural(stats['stars'], 'star')}",
        "Commits": f"{stats['commits']:,} in the past year",
        "Followers": f"{stats['followers']:,}",
    }


def card_columns(rows):
    """(art_width, value_column) as used by the existing card rows."""
    header = re.search(r"\S\s{2,}(\S)", rows[0])  # ASCII art, gap, "user@host"
    if not header:
        raise ValueError("cannot find where the ASCII art ends on the card's first row")
    art = header.start(1)
    for row in rows[1:]:
        m = re.match(r"(\S+ {2,})\S", row[art:])
        if m and not set(m.group(1)) <= {"-", " "}:
            return art, art + len(m.group(1))
    raise ValueError("cannot find a 'Label   value' row on the card")


def render(rows, values):
    art, value_col = card_columns(rows)
    width = value_col - art

    def row_for(prefix, label):
        return (prefix.ljust(art) + label.ljust(width) + values[label]).rstrip()

    out, seen = [], set()
    for row in rows:
        words = row[art:].split(maxsplit=1)
        label = words[0] if words else ""
        if label in values and label not in seen:
            out.append(row_for(row[:art], label))
            seen.add(label)
        else:
            out.append(row)
    missing = [label for label in LIVE_LABELS if label not in seen]
    if missing:
        out.append(" " * art + SEPARATOR)
        out.extend(row_for("", label) for label in missing)
    return out


def update(text, values):
    try:
        head, rest = text.split(START, 1)
        block, tail = rest.split(END, 1)
    except ValueError:
        raise SystemExit(f"README must contain {START} ... {END}")
    lines = block.strip("\n").split("\n")
    if lines[0].strip() != FENCE_OPEN or lines[-1].strip() != FENCE_CLOSE:
        raise SystemExit(f"the card must be a {FENCE_OPEN} code block between the markers")
    card = render(lines[1:-1], values)
    new_block = "\n".join([FENCE_OPEN, *card, FENCE_CLOSE])
    return f"{head}{START}\n{new_block}\n{END}{tail}", card


def main():
    parser = argparse.ArgumentParser(description=__doc__.split("\n")[0])
    parser.add_argument("--readme", default=Path(__file__).resolve().parent.parent / "README.md", type=Path)
    parser.add_argument("--login", default=os.environ.get("GITHUB_REPOSITORY_OWNER", "Adam010341"))
    parser.add_argument("--dry-run", action="store_true", help="print the card, do not write")
    args = parser.parse_args()

    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        raise SystemExit("GITHUB_TOKEN is not set")

    stats = fetch_stats(token, args.login)
    print(f"stats for {args.login}: {json.dumps(stats)}", file=sys.stderr)
    text = args.readme.read_text(encoding="utf-8")
    new_text, card = update(text, live_values(stats))
    print("\n".join(card))
    if args.dry_run:
        return
    if new_text != text:
        args.readme.write_text(new_text, encoding="utf-8")
        print("README.md updated", file=sys.stderr)
    else:
        print("README.md already up to date", file=sys.stderr)


if __name__ == "__main__":
    main()
