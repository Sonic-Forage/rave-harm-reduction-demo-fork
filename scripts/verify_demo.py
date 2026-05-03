#!/usr/bin/env python3
from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[1]
required = ['demo/EXAMPLE_CITY_CHAPTER.md','demo/CARE_TEAM_ONE_PAGER.md','demo/LESSON_RECEIPT.md','README.md']
missing = [p for p in required if not (ROOT / p).exists()]
if missing:
    print('MISSING:', *missing, sep='\n- ')
    sys.exit(1)
text = '\n'.join((ROOT / p).read_text(errors='replace') for p in required)
for needle in ['fictional','closed until human approval','SAMHSA','Do not diagnose']:
    if needle.lower() not in text.lower():
        print('MISSING DEMO NEEDLE:', needle)
        sys.exit(1)
print('DEMO FORK VERIFY OK')
print('demo files:', len(required))
