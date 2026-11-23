"""Wraps src/lived.html (page content) into index.html (full page for GitHub Pages / local server)."""
from pathlib import Path
root = Path(__file__).parent
body = (root / 'src' / 'lived.html').read_text()
head = '''<!doctype html>
<html lang="en">
<head>
<meta charset="utf-8">
<meta http-equiv="Cache-Control" content="no-cache, no-store, must-revalidate">
<meta http-equiv="Pragma" content="no-cache">
<meta http-equiv="Expires" content="0">
<meta name="viewport" content="width=device-width,initial-scale=1,viewport-fit=cover">
<meta name="apple-mobile-web-app-capable" content="yes">
<meta name="mobile-web-app-capable" content="yes">
<meta name="apple-mobile-web-app-status-bar-style" content="default">
<meta name="apple-mobile-web-app-title" content="Lived">
<meta name="theme-color" content="#ffffff">
</head>
<body>
'''
(root / 'index.html').write_text(head + body + '\n</body>\n</html>\n')
print('index.html built')
