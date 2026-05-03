#!/usr/bin/env python3
from pathlib import Path
import json, re, sys
ROOT = Path(__file__).resolve().parents[1]
required = [
    'README.md','LICENSE','CONTRIBUTING.md','.env.example','docs/index.html',
    'docs/sources/SOURCES.md','docs/harm-reduction/HARM_REDUCTION_FIELD_GUIDE.md',
    'docs/harm-reduction/RAVE_CARE_TEAM_PLAYBOOK.md','docs/harm-reduction/OVERDOSE_RESPONSE_EDUCATION.md',
    'docs/harm-reduction/SAFE_DANCE_SPACE_CHECKLIST.md','docs/lessons/FORK_THIS_LESSON.md',
    'framework/prompts/harm-reduction-prompts.md','framework/ui/HARM_REDUCTION_UNICODE_UI.md',
    'framework/payloads/harm-reduction-city.payload.example.json','framework/tags/harm-reduction-tags.json',
    '.github/ISSUE_TEMPLATE/source_correction.yml','.github/ISSUE_TEMPLATE/city_chapter.yml','.github/ISSUE_TEMPLATE/care_team.yml',
    '.github/PULL_REQUEST_TEMPLATE.md'
]
missing = [p for p in required if not (ROOT / p).exists()]
if missing:
    print('MISSING:', *missing, sep='\n- ')
    sys.exit(1)
for rel in ['framework/payloads/harm-reduction-city.payload.example.json','framework/tags/harm-reduction-tags.json']:
    json.loads((ROOT / rel).read_text())
text = '\n'.join((ROOT / p).read_text(errors='replace') for p in required if p.endswith(('.md','.html','.example')))
for needle in ['not medical advice','closed_until_human_yes','National Harm Reduction Coalition','SAMHSA','DanceSafe']:
    if needle.lower() not in text.lower():
        print('MISSING NEEDLE:', needle)
        sys.exit(1)
if re.search(r'(ghp_|github_pat_|sk-[A-Za-z0-9]|hf_[A-Za-z0-9]|BEGIN [A-Z ]*PRIVATE KEY)', text):
    print('SECRET-LIKE MARKER FOUND')
    sys.exit(1)
if re.search(r'guarantee[s]? safety|prevents all overdose|medical training certified', text, re.I):
    print('UNSAFE OVERCLAIM FOUND')
    sys.exit(1)
print('HARM REDUCTION KIT VERIFY OK')
print('required files:', len(required))
print('sources:', len((ROOT / 'docs/sources/SOURCES.md').read_text().splitlines()) - 2)
