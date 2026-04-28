from pathlib import Path
src = Path('final1.html').read_text(encoding='utf-8')
style_start = src.find('<style>')
style_end = src.find('</style>', style_start)
script_start = src.find('<script>', style_end)
script_end = src.rfind('</script>')
if style_start == -1 or style_end == -1 or script_start == -1 or script_end == -1:
    raise SystemExit('Could not locate style or script sections')
html_start = src[:style_start]
css = src[style_start+len('<style>'):style_end]
html_middle = src[style_end+len('</style>'):script_start]
js = src[script_start+len('<script>'):script_end]
html_end = src[script_end+len('</script>'):]
index = html_start + '  <link rel="stylesheet" href="style.css">\n' + html_middle + '  <script src="app.js"></script>\n' + html_end
Path('public/index.html').write_text(index, encoding='utf-8')
Path('public/style.css').write_text(css.strip() + '\n', encoding='utf-8')
Path('public/app.js').write_text(js.strip() + '\n', encoding='utf-8')
print('Split complete: public/index.html, public/style.css, public/app.js')
