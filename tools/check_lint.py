from pathlib import Path
import sys
text=Path(sys.argv[1]).read_text(encoding='utf-8-sig')
pre=text.split('Statistics:')[0]
lines=[l for l in pre.splitlines() if l.strip() and 'lint report, generated at:' not in l]
if lines:raise SystemExit('Lint diagnostics:\n'+'\n'.join(lines))
print('PASS: clean Ren’Py lint')
