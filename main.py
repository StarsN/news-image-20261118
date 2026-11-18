# A program that writes one image summing up the world news of
# Wednesday 18 November 2026 to /output/entry.png: it copies the
# entry.png beside this file. Standard library only, no network,
# deterministic: the same bytes every run.
import os
import shutil
from pathlib import Path

HERE = Path(__file__).resolve().parent
OUT = Path(os.environ.get("MAKEFUN_OUTPUT_DIR", "/output"))

OUT.mkdir(parents=True, exist_ok=True)
shutil.copyfile(HERE / "entry.png", OUT / "entry.png")
