#!/usr/bin/env python3
from pathlib import Path
import sys
ROOT = Path(__file__).resolve().parents[1]
required = [
    'demo/EXAMPLE_CITY_CHAPTER.md',
    'demo/CARE_TEAM_ONE_PAGER.md',
    'demo/LESSON_RECEIPT.md',
    'demo/FORK_REPLICATION_CHECKLIST.md',
    'demo/SOURCE_CORRECTION_EXAMPLE.md',
    'demo/CITY_RESOURCE_DIRECTORY_TEMPLATE.md',
    'demo/FORK_PROOF_INDEX.md',
    'README.md',
]
missing = [p for p in required if not (ROOT / p).exists()]
if missing:
    print('MISSING:', *missing, sep='\n- ')
    sys.exit(1)
text = '\n'.join((ROOT / p).read_text(errors='replace') for p in required)
for needle in ['fictional','closed until human approval','SAMHSA','Do not diagnose','source-backed wording correction','closed_until_human_yes','City Resource Directory Template','official public URL','no private event location','Demo Fork Proof Index','Human approval questions','Blocked without explicit human approval']:
    if needle.lower() not in text.lower():
        print('MISSING DEMO NEEDLE:', needle)
        sys.exit(1)
print('DEMO FORK VERIFY OK')
print('demo files:', len(required))
