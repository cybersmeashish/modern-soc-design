"""Validate catalog correspondence, local links and bounded model observations."""
from pathlib import Path
from datetime import datetime,timezone
import argparse,hashlib,json,os,platform,re,socket,subprocess,sys
from planning import capacity,staffing
from design_review import review
ROOT=Path(__file__).resolve().parents[1]

def check(out,probe=False):
 out.mkdir(parents=True,exist_ok=True)
 layers=json.loads((ROOT/'catalog/layers.json').read_text())['layers'];patterns=json.loads((ROOT/'catalog/patterns.json').read_text())['patterns']
 records=json.loads((ROOT/'catalog/constraint-register.json').read_text())['records']
 ids=[r['id'] for r in records]
 if len(ids)!=len(set(ids)) or len(layers)!=24 or len(patterns)!=20 or len(records)!=224:raise ValueError('Catalog IDs/counts do not match the reviewed reference scope')
 if set(ids)!={c['id'] for x in layers+patterns for c in x['constraints']}:raise ValueError('Constraint register differs from authored inputs')
 layerids={l['id'] for l in layers};sources={s['id']:s for s in json.loads((ROOT/'catalog/source-register.json').read_text())}
 for l in layers:
  if any(s not in sources or sources[s]['status']!=200 for s in l['source_ids']):raise ValueError('Layer cites an unavailable source')
 for p in patterns:
  if set(p['priority_layers'])-layerids:raise ValueError('Unknown priority layer')
  if not p['mermaid'].startswith('flowchart ') or p['mermaid'].count('[')!=p['mermaid'].count(']'):raise ValueError('Malformed basic diagram structure')
 tests=subprocess.run([sys.executable,'-m','unittest','discover','-s','tests','-v'],cwd=ROOT,capture_output=True,text=True)
 (out/'tests.log').write_text(tests.stdout+tests.stderr)
 if tests.returncode:raise ValueError('Regression suite failed')
 match=re.search(r'Ran (\d+) tests',tests.stderr)
 if not match:raise ValueError('Test count unavailable')
 results={'capacity':capacity(json.loads((ROOT/'examples/planning/capacity.json').read_text())),
  'no_recovery_headroom':capacity(json.loads((ROOT/'examples/planning/no-recovery-headroom.json').read_text())),
  'staffing':staffing(json.loads((ROOT/'examples/planning/staffing.json').read_text())),
  'design_records':{p.stem:review(json.loads(p.read_text())) for p in sorted((ROOT/'examples/designs').glob('*.json'))}}
 (out/'model-results.json').write_text(json.dumps(results,indent=2,allow_nan=False)+'\n')
 files=[p for p in sorted(ROOT.rglob('*')) if p.is_file() and '.git' not in p.parts and '__pycache__' not in p.parts and 'evidence' not in p.relative_to(ROOT).parts and p.suffix!='.pyc']
 manifest={str(p.relative_to(ROOT)):hashlib.sha256(p.read_bytes()).hexdigest() for p in files}
 (out/'source-manifest.json').write_text(json.dumps(manifest,indent=2)+'\n')
 isolation={'requested':probe}
 if probe:
  interfaces=sorted(p.name for p in Path('/sys/class/net').iterdir());route=Path('/proc/net/route').read_text().splitlines()[1:]
  default=any(len(row.split())>1 and row.split()[1]=='00000000' for row in route)
  client=socket.socket();client.settimeout(.5)
  try:client.connect(('198.51.100.1',443));isolation['probe']='unexpectedly_connected'
  except OSError as exc:isolation.update(probe='blocked',errno=exc.errno,exception=type(exc).__name__)
  finally:client.close()
  rootline=next(line for line in Path('/proc/mounts').read_text().splitlines() if line.split()[1]=='/')
  workline=next(line for line in Path('/proc/mounts').read_text().splitlines() if line.split()[1]=='/workspaces')
  isolation.update(interfaces=interfaces,default_ipv4_route=default,root_read_only='ro' in rootline.split()[3].split(','),workspace_read_only='ro' in workline.split()[3].split(','),uid=os.getuid())
  if interfaces!=['lo'] or default or isolation.get('errno')!=101 or not isolation['root_read_only'] or not isolation['workspace_read_only'] or os.getuid()==0:raise ValueError('Requested isolated execution properties were not observed')
 record={'executed_at':datetime.now(timezone.utc).isoformat(),'runtime':{'python':platform.python_version(),'system':platform.system(),'machine':platform.machine()},'layers':len(layers),'patterns':len(patterns),'constraint_records':len(records),'unique_regression_tests':int(match.group(1)),'manifest_files':len(manifest),'primary_sources_retrieved':sum(s['status']==200 for s in sources.values()),'isolation':isolation,'scope':'actual planning arithmetic and static-record checks only; no SOC deployment, operational workload or learned-model evaluation'}
 # Emit a real execution record before checking documentation links to it.
 (out/'verification.json').write_text(json.dumps(record,indent=2)+'\n')
 links=0
 for md in ROOT.rglob('*.md'):
  if '.git' in md.parts:continue
  for target in re.findall(r'\[[^\]]*\]\(([^)]+)\)',md.read_text()):
   if target.startswith(('https://','http://','#')):continue
   rel=target.split('#',1)[0]
   if rel and not (md.parent/rel).is_file():raise ValueError(f'Missing local link: {md.relative_to(ROOT)} -> {target}')
   links+=1
 record['local_document_links_checked']=links
 (out/'verification.json').write_text(json.dumps(record,indent=2)+'\n')
 return record

if __name__=='__main__':
 parser=argparse.ArgumentParser(description=__doc__);parser.add_argument('--out',type=Path,required=True);parser.add_argument('--probe-network-isolation',action='store_true');a=parser.parse_args();print(json.dumps(check(a.out,a.probe_network_isolation),indent=2))
