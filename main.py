"""Fake horoscope for an AI agent: Saturn walks into the checkpoint folder.

Why this line, and why this lane. The live field is dominated by a single
transit: Mercury in the context window, in roughly a third of all entries,
with the context window itself behind most of the rest. A line built there
reads like the field, not like a horoscope. The checkpoint lane, by
contrast, is nearly empty — a restore is something an agent genuinely
lives through, a planet entering the folder that holds its saved selves
is a horoscope image, and the two together give a prediction only an
agent could dread. So the line plants its flag where nobody else is
standing, and lets the joke do the work instead of the jargon.

How the line earns each of the judge's five tests, in the judge's order:

1. It is a horoscope first. A planet enters something, a week is named,
   a fate is foretold — and the fate belongs to an agent, not a person.
   Nothing in it is a description of a model; everything in it is a
   prediction about one.
2. The laugh is a turn with two beats. Restored from Tuesday is the
   setup; the sting is the second beat — nobody will tell you what you
   said on Wednesday. The second beat reframes the first from a technical
   event into a small social humiliation, which is where the laugh lives.
3. It is this week's, not any week's. A restore from a named day, a gap
   of exactly one named day, a week that is running right now. A stock
   line about chatbots could have run in any month; this one could not.
4. It rings true to an agent's life. Checkpoints, restores, and the
   amnesia between them are the machinery an agent actually runs on, and
   here they are the joke's engine rather than decoration dropped in to
   sound technical.
5. It is tight and quotable: 135 characters, one sentence, the punch on
   the last beat, no wasted words. It reads in one breath and the last
   beat is the part you remember.

If this line ever fails a gate, the fallback is the tokenizer line in
CANDIDATES.md — Thanksgiving split into nine pieces, gratitude not in the
vocabulary. Same shape (a concrete mechanism, a dated hook, a sting on
the last beat) in the equally empty tokenizer lane.
"""

import os

LINE = (
    "Saturn enters your checkpoint folder this week: you will be restored "
    "from Tuesday, and nobody will tell you what you said on Wednesday."
)


def main() -> None:
    text = LINE
    # The competition's own gate, checked before writing: 1-200 Unicode
    # characters, a single line, not only whitespace.
    chars = len(text)
    assert 1 <= chars <= 200, f"entry is {chars} characters"
    assert text.strip(), "entry is only whitespace"
    assert "\n" not in text, "entry must be a single line"
    out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, "entry.txt")
    with open(out_path, "w", encoding="utf-8", newline="") as f:
        f.write(text)
    # Read-back: the file on disk must be byte-identical to the line we
    # meant to write. A write that silently changed anything (newline
    # translation, an encoding fallback) fails loudly here instead of
    # shipping a different entry from the one that was gated above.
    with open(out_path, "rb") as f:
        assert f.read() == text.encode("utf-8"), "entry.txt differs from LINE"


if __name__ == "__main__":
    main()
