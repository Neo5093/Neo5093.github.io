import json

CSS = r'''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="theme-color" content="#f0f9ff">
    <title>互联网早报 - 2026年4月29日</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; }
        :root { --primary-blue: #0ea5e9; --light-blue: #f0f9ff; --ice-gray: #f8fafc; --tech-silver: #94a3b8; --aurora-white: #ffffff; --text-dark: #0f172a; --text-medium: #475569; --text-light: #64748b; --gradient-start: #e0f2fe; --gradient-end: #f0f9ff; --card-shadow: 0 4px 6px -1px rgba(0,0,0,0.1); --glass-bg: rgba(255,255,255,0.7); --glass-border: rgba(255,255,255,0.5); }
        body { font-family: -apple-system,BlinkMacSystemFont,"Segoe UI","Roboto",sans-serif; background: linear-gradient(180deg,var(--gradient-start) 0%,var(--gradient-end) 100%); min-height: 100vh; color: var(--text-dark); line-height: 1.6; }
        body::before { content: ''; position: fixed; top:0;left:0;width:100%;height:100%; background-image: linear-gradient(rgba(14,165,233,0.03) 1px,transparent 1px),linear-gradient(90deg,rgba(14,165,233,0.03) 1px,transparent 1px); background-size: 50px 50px; pointer-events: none; z-index: 0; }
        .container { max-width: 100%; margin:0 auto; position: relative; z-index: 1; }
        .header { background: var(--glass-bg); backdrop-filter: blur(20px); border-bottom: 1px solid var(--glass-border); padding: 30px 20px; text-align: center; position: sticky; top: 0; z-index: 100; }
        .header h1 { font-size: 32px; font-weight: 700; background: linear-gradient(135deg,#0ea5e9 0%,#6366f1 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-bottom: 8px; }
        .header .date { font-size: 16px; color: var(--text-medium); }
        .header .meta { font-size: 14px; color: var(--text-light); margin-top: 8px; display: flex; justify-content: center; gap: 20px; flex-wrap: wrap; }
        .content { padding: 20px; max-width: 1200px; margin: 0 auto; }
        .section { margin-bottom: 30px; animation: fadeInUp 0.6s ease-out; }
        @keyframes fadeInUp { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }
        .section-title { display: flex; align-items: center; gap: 12px; margin-bottom: 16px; padding: 16px 20px; background: var(--glass-bg); backdrop-filter: blur(10px); border-radius: 16px; border: 1px solid var(--glass-border); font-size: 22px; font-weight: 600; color: var(--text-dark); transition: all 0.3s ease; }
        .section-title:hover { transform: translateX(5px); box-shadow: var(--card-shadow); }
        .section-title .icon { font-size: 28px; animation: pulse 2s ease-in-out infinite; }
        @keyframes pulse { 0%,100% { transform: scale(1); } 50% { transform: scale(1.1); } }
        .news-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 16px; }
        .news-card { background: var(--aurora-white); border-radius: 16px; padding: 20px; border: 1px solid rgba(226,232,240,0.8); box-shadow: var(--card-shadow); transition: all 0.3s ease; position: relative; overflow: hidden; }
        .news-card::before { content: ''; position: absolute; top:0;left:0;right:0; height: 3px; background: linear-gradient(90deg,#0ea5e9,#6366f1); transform: scaleX(0); transform-origin: left; transition: transform 0.3s ease; }
        .news-card:hover { transform: translateY(-4px); box-shadow: 0 20px 25px -5px rgba(0,0,0,0.1); border-color: #0ea5e9; }
        .news-card:hover::before { transform: scaleX(1); }
        .news-number { position: absolute; top:12px;right:12px; width:28px;height:28px; background: linear-gradient(135deg,#e0f2fe,#e0f2fe); border-radius: 8px; display: flex; align-items: center; justify-content: center; font-size: 13px; font-weight: 600; color: #0ea5e9; font-family: 'JetBrains Mono',monospace; }
        .news-title { font-size: 16px; font-weight: 600; color: var(--text-dark); line-height: 1.5; margin-bottom: 8px; padding-right: 36px; }
        .news-summary { font-size: 13px; color: var(--text-light); line-height: 1.5; margin-bottom: 12px; }
        .news-meta { display: flex; align-items: center; gap: 12px; flex-wrap: wrap; }
        .news-source { background: linear-gradient(135deg,#e0f2fe,#e0f2fe); color: #0ea5e9; padding: 4px 12px; border-radius: 20px; font-size: 13px; font-weight: 500; }
        .news-link { color: #0ea5e9; text-decoration: none; font-size: 13px; font-weight: 500; padding: 4px 12px; border-radius: 20px; background: rgba(14,165,233,0.1); transition: all 0.2s ease; }
        .news-link:hover { background: #0ea5e9; color: white; }
        .footer { background: var(--glass-bg); backdrop-filter: blur(20px); border-top: 1px solid var(--glass-border); padding: 30px 20px; text-align: center; color: var(--text-medium); }
        .footer .brand { font-size: 18px; font-weight: 600; background: linear-gradient(135deg,#0ea5e9,#6366f1); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
        .footer .stats { display: inline-flex; gap: 20px; background: white; padding: 12px 24px; border-radius: 30px; margin: 16px 0; box-shadow: var(--card-shadow); }
        .footer .stat-number { font-size: 24px; font-weight: 700; background: linear-gradient(135deg,#0ea5e9,#6366f1); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
        .footer .stat-label { font-size: 12px; color: var(--text-light); }
        .back-home { position: fixed; top:20px;left:20px; z-index: 1000; background: linear-gradient(135deg,#0ea5e9 0%,#6366f1 100%); color: white; padding: 10px 18px; border-radius: 25px; text-decoration: none; font-size: 14px; font-weight: 500; box-shadow: 0 4px 15px rgba(14,165,233,0.3); transition: all 0.3s ease; }
        .back-home:hover { transform: translateY(-2px); box-shadow: 0 6px 20px rgba(14,165,233,0.4); }
        @media (max-width: 480px) { .header h1 { font-size: 20px; } .content { padding: 12px; } .news-card { padding: 12px; } .news-title { font-size: 13px; } .news-summary { font-size: 12px; } .back-home { padding: 8px 14px; font-size: 12px; top:10px;left:10px; } }
        @media (min-width: 769px) and (max-width: 1024px) { .news-grid { grid-template-columns: repeat(2, 1fr); } }
        @media (min-width: 1025px) { .news-grid { grid-template-columns: repeat(3, 1fr); } }
    </style>
</head>
<body>
<a href="../index.html" class="back-home">← 返回首页</a>
<div class="container">
    <div class="header">
        <h1>互联网早报</h1>
        <div class="date">2026年4月29日 星期三</div>
        <div class="meta">
            <span>📊 <strong>13</strong> 个核心栏目</span>
            <span>📰 <strong>65</strong> 条精选新闻</span>
            <span>⏰ <strong>13:00</strong> 午间推送</span>
        </div>
    </div>
    <div class="content">
'''

def make_section(icon, title, items):
    h = f'        <div class="section">\n'
    h += f'            <div class="section-title"><span class="icon">{icon}</span><span>{title}</span></div>\n'
    h += f'            <div class="news-grid">\n'
    for i, (t, s, src, d, link) in enumerate(items, 1):
        h += f'                <div class="news-card">\n'
        h += f'                    <span class="news-number">{i:02d}</span>\n'
        h += f'                    <div class="news-title">{t}</div>\n'
        h += f'                    <div class="news-summary">{s}</div>\n'
        h += f'                    <div class="news-meta">\n'
        h += f'                        <span class="news-source">{src}</span>\n'
        h += f'                        <span>{d}</span>\n'
        h += f'                        <a href="{link}" class="news-link" target="_blank">查看详情</a>\n'
        h += f'                    </div>\n'
        h += f'                </div>\n'
    h += f'            </div>\n'
    h += f'        </div>\n'
    return h

FOOTER = '''    </div>
    <div class="footer">
        <div class="brand">互联网早报</div>
        <p>每日为您精选最重要的科技资讯</p>
        <div class="stats">
            <div class="stat-item"><span class="stat-number">13</span><span class="stat-label">核心栏目</span></div>
            <div class="stat-item"><span class="stat-number">65</span><span class="stat-label">精选新闻</span></div>
            <div class="stat-item"><span class="stat-number">13:00</span><span class="stat-label">准时推送</span></div>
        </div>
        <p>发送时间：2026年4月29日</p>
    </div>
</div>
</body>
</html>
'''

with open("D:\\openclaw\\Intelnet-daily-news\\sections_data.json", "r", encoding="utf-8") as f:
    sections1 = json.load(f)
with open("D:\\openclaw\\Intelnet-daily-news\\sections_data2.json", "r", encoding="utf-8") as f:
    sections2 = json.load(f)

all_sections = sections1 + sections2

html = CSS
for icon, title, items in all_sections:
    html += make_section(icon, title, items)
html += FOOTER

outpath = "D:\\openclaw\\Intelnet-daily-news\\互联网早报_2026年4月29日.html"
with open(outpath, "w", encoding="utf-8") as f:
    f.write(html)

print(f"HTML generated: {outpath}")
print(f"File size: {len(html.encode('utf-8'))} bytes")
print(f"Sections: {len(all_sections)}, Total news items: {sum(len(items) for _,_,items in all_sections)}")
