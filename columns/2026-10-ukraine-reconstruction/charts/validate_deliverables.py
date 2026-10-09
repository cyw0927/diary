"""Publication integrity checks: math, source coverage, links and datasets."""
import json,re,ast
from pathlib import Path
import pandas as pd
from collect_sources import ROOT,DATA
s=(ROOT/'ukraine_reconstruction_critique.md').read_text(encoding='utf-8');body=s.split('### 출처')[0]
assert s.startswith('# 우크라이나 재건 - 21세기 최악의 사기극\n')
assert len(re.findall(r'^## \d+\.',body,re.M))==12
assert 20000<=len(body)<=40000
refs=json.loads((DATA/'source_registry.json').read_text(encoding='utf-8'));used={n for n in re.findall(r'\[(\d+)\]',body)}
assert used<=set(refs)
assert set(re.findall(r'\*\*\[(\d+)\]\*\*',s.split('### 출처')[1]))==used
assert s.count('### 출처')==1
for p in ROOT.glob('*.md'):
 text=p.read_text(encoding='utf-8')
 for target in re.findall(r'\]\(([^)]+)\)',text):
  if target.startswith(('http:','https:','#')):continue
  assert (p.parent/target.split('#')[0]).exists(),(p.name,target)
 for line in text.splitlines():assert not line.rstrip('\n').endswith(' '),(p.name,line)
audit=json.loads((DATA/'claim_audit.json').read_text(encoding='utf-8'));assert [x['id'] for x in audit]==list(range(1,62));assert all(x['status'] for x in audit)
sect=json.loads((DATA/'rdna5_sectors.json').read_text(encoding='utf-8'));assert len(sect)==18
for r in sect:assert abs((r['needs']-r['damage'])-r['gap'])<.001
assert abs(587.7-195.1-392.6)<.001
stocks=json.loads((DATA/'korean_stocks_comparison.json').read_text(encoding='utf-8'))
for r in stocks:
 assert r['base']['date']=='20230515' and r['end']['date']=='20230717'
 assert abs((r['peak']['close']/r['base']['close']-1)*100-r['peak_return'])<1e-9
 if r['code']=='001140':assert r['base']['volume']==0
assert abs((4740/1458-1)*100-225.1028806584362)<1e-8
wdi=pd.read_csv(DATA/'prewar_wdi.csv');assert len(wdi)==864 and wdi.country.nunique()==9
hold=pd.read_csv(DATA/'ukrn_holdings_20261008.csv');wc=hold.groupby('country').weight.sum()*100
assert abs(wc['United States']-43.88)<.0001 and abs(wc['Ukraine']-.18)<.0001
assert 99.9<wc.sum()<100.1
assert len(list((ROOT/'images').glob('*.png')))==11
from PIL import Image
for p in (ROOT/'images').glob('*.png'):
 with Image.open(p) as im:assert im.width>=1600 and im.height>=1000
for p in DATA.glob('*.json'):json.loads(p.read_text(encoding='utf-8-sig'))
for p in (ROOT/'charts').glob('*.py'):ast.parse(p.read_text(encoding='utf-8'))
print(json.dumps({'body_chars':len(body),'chapters':12,'used_sources':len(used),'original_sources_audited':61,'registry_sources':len(refs),'figures':11,'checks':'passed','KRX_original_price_certification':'not_completed; explicitly disclosed'},ensure_ascii=False))
