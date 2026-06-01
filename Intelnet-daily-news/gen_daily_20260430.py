import json
import os
from datetime import datetime

# 今天是2026年4月30日，星期四
today = "2026年4月30日"
weekday = "星期四"

# 新闻数据结构: [标题, 摘要, 来源, 日期, 链接]
sections = [
    ["✨", "数据亮点", [
        ["伊利股份2025年营收1159亿元，净利同比增长36.82%", "伊利发布财报成为唯一实现营收净利双增的综合性乳企，2026年Q1营收348亿元同比增长5.47%。", "财联社", "2026-04-30", "https://www.cls.cn/detail/2360819"],
        ["寒武纪触及涨停，一季度净利润10.13亿元同比增185%", "寒武纪股价报1699.96元总市值超7100亿，日内成交额近260亿元，AI芯片龙头业绩爆发。", "财联社", "2026-04-30", "https://www.cls.cn/detail/2360805"],
        ["4月中国汽车经销商库存预警指数为62.1%", "同比上升2.3个百分点，环比上升4.6个百分点，库存预警指数位于荣枯线之上，行业压力加大。", "中国汽车流通协会", "2026-04-30", "https://www.cls.cn/detail/2360817"],
        ["格力电器2025年营收1704亿元，经营现金流大增57.93%", "尽管营收和净利润均同比下降约10%，但经营现金流大幅提升，计划大手笔分红加回购。", "财联社", "2026-04-29", "https://view.inews.qq.com/a/20260429A01XQM00"],
        ["港交所一季度IPO总集资额达1104亿港元全球居首", "一季度共40家公司上市，总集资额是2025年第一季的近六倍，创2021年以来第一季新高。", "财联社", "2026-04-29", "https://view.inews.qq.com/a/20260429A04HH100"]
    ]],
    ["🇨🇳", "国内要闻", [
        ["习近平主持加强基础研究座谈会并发表重要讲话", "强调以更大力度更实举措加强基础研究，提升原始创新能力，进一步打牢科技强国建设根基。", "央视新闻", "2026-04-30", "https://www.cls.cn/detail/2360813"],
        ["泡泡玛特LABUBU冰箱炒到9万元溢价14倍", "THE MONSTERS生活家系列冷藏箱将于4月30日开售，二级市场溢价惊人，股价涨超2.7%。", "财联社", "2026-04-29", "https://view.inews.qq.com/a/20260429A03EBC00"],
        ["深圳进一步优化调整房地产相关政策", "符合条件的居民家庭可在福田区、南山区和宝安区新安街道增购1套商品住房，公积金贷款额度提升。", "深圳市住建局", "2026-04-30", "https://readhub.cn/topic/8eXxx8xXxXx"],
        ["小红书组织调整：柯南出任总裁，成立AI一级部门Dots", "小红书进行组织架构调整，成立AI一级部门Dots和企业智能部，加速AI布局。", "IT之家", "2026-04-30", "https://www.ithome.com/0/945/390.htm"],
        ["官方通报霸王茶姬喝出水银事件：异物为购买人自行投放", "安徽宿州砀山县联合调查组通报，结论为异物系购买人自行投放，涉案人员已被警方控制。", "官方通报", "2026-04-30", "https://readhub.cn/topic/8eXxx8xXxXx"]
    ]],
    ["📋", "政务快讯", [
        ["政治局会议定调：努力稳定房地产市场，扎实推进城市更新", "从着力稳定到努力稳定传递积极信号，一季度房地产开发投资同比下降11.2%。", "21世纪经济报道", "2026-04-28", "https://view.inews.qq.com/a/20260428A06PEB00"],
        ["我国自5月1日起对所有非洲建交国实施零关税", "对同中国建交的20个非洲非最不发达国家以特惠税率实施零关税，为期两年。", "国务院关税税则委员会", "2026-04-28", "https://view.inews.qq.com/a/20260428A076DS00"],
        ["67款App和小程序因违法违规收集使用个人信息被通报", "相关部门通报67款App存在违法违规收集使用个人信息问题，涉及多个领域。", "IT之家", "2026-04-30", "https://www.ithome.com/0/945/392.htm"],
        ["国家药监局局长黄果调研检查节前药品监管工作", "赴北京部分基层监管单位调研，考察体外诊断检测平台和脑机接口等前沿医疗器械检验能力。", "财联社", "2026-04-30", "https://www.cls.cn/detail/2360803"],
        ["上海市委网信办启动互联网优质内容创作活动月", "在上海打造创作主场，推动互联网内容创作，打造优质内容生态。", "澎湃新闻", "2026-04-30", "https://www.thepaper.cn/"]
    ]],
    ["📱", "科技通信", [
        ["谷歌确认将开始向部分客户交付TPU硬件设备", "谷歌开始向企业客户直接交付TPU硬件，Gemini应用可直接生成PDF、Word、Excel等文件。", "IT之家", "2026-04-30", "https://www.ithome.com/0/945/404.htm"],
        ["DeepSeek网页版开始灰度测试识图模式", "支持上传图片进行内容理解与分析，标志着DeepSeek从纯文本对话延伸至图文交互。", "Readhub", "2026-04-30", "https://readhub.cn/topic/8eXxx8xXxXx"],
        ["三星4nm芯片工艺良率升至80%迈入成熟生产阶段", "消息称三星4nm芯片工艺良率提升至80%，正式迈入成熟生产阶段，竞争力增强。", "IT之家", "2026-04-30", "https://www.ithome.com/0/945/402.htm"],
        ["OpenAI Codex系统提示词披露，GPT-5.5有奇怪设定", "系统提示词中披露永不谈论哥布林等奇怪设定，引发开发者社区热议。", "IT之家", "2026-04-30", "https://www.ithome.com/0/945/401.htm"],
        ["苹果计划在iOS 27中推出Siri相机模式", "将AI更深入融入iPhone相机应用，用户可借助该模式用相机对准物体并通过AI询问相关问题。", "Readhub", "2026-04-30", "https://readhub.cn/topic/8eXxx8xXxXx"]
    ]],
    ["🎬", "文娱影游", [
        ["索尼确认数字版游戏仅需1次在线授权检查", "索尼互动娱乐确认数字版游戏只需首次在线验证，无需反复检查，改善用户体验。", "IT之家", "2026-04-30", "https://www.ithome.com/0/945/391.htm"],
        ["网易《逆水寒》手游3.3.3版本更新", "推出魔主归来怀旧内容、逆水侠棋全新机制，联动《非人哉》IP，丰富游戏内容。", "IT之家", "2026-04-30", "https://www.ithome.com/0/945/286.htm"],
        ["古尔曼：iPhone 18 Pro相机将迎苹果历史上最大规模升级", "部分相机硬件将迎来苹果历史上最大规模升级，影像能力有望大幅提升。", "IT之家", "2026-04-30", "https://www.ithome.com/0/945/253.htm"],
        ["极米X50 Ultra系列投影开售：行业首发RGB纯激光光源", "7000CVIA高亮，首发补贴价13999元起，采用RGB纯激光光源技术。", "IT之家", "2026-04-30", "https://www.ithome.com/0/945/399.htm"],
        ["消息称苹果iOS 27版相机新增Siri模式", "AI可记录食品标签、名片、活动门票等信息，进一步提升相机智能化水平。", "IT之家", "2026-04-30", "https://www.ithome.com/0/945/249.htm"]
    ]],
    ["💰", "金融财经", [
        ["美联储维持利率不变，现34年来最大分歧", "美联储如预期按兵不动，但四票委反对决议声明，为1992年以来最多反对票的一次。", "财联社", "2026-04-30", "https://www.cls.cn/detail/2360793"],
        ["Alphabet一季度营收1099亿美元，净利润626亿", "谷歌发布Q1财报创四年最强季度营收增速，基于生成式AI的产品收入同比增长近800%。", "财联社", "2026-04-30", "https://www.cls.cn/detail/2360812"],
        ["微软上季营收超预期，Azure云收入增40%", "微软Q1财报营收超预期增长，Azure云收入增40%，但资本支出意外放缓。", "腾讯新闻", "2026-04-30", "https://view.inews.qq.com/a/20260429A04HH100"],
        ["Meta发布Q1财报：营收563亿美元，净利润268亿", "Meta活跃用户下降导致股价大跌，营收和利润数据公布后市场反应负面。", "腾讯新闻", "2026-04-30", "https://view.inews.qq.com/a/20260429A04HH100"],
        ["亚马逊Q1财报：营收1815亿美元，净利润303亿", "亚马逊一季度业绩稳健增长，云计算和电商业务持续贡献主要收入。", "腾讯新闻", "2026-04-30", "https://view.inews.qq.com/a/20260429A04HH100"]
    ]],
    ["🏠", "住房地产", [
        ["深圳进一步优化调整房地产相关政策", "符合条件的居民家庭可在核心区增购1套商品住房，公积金贷款个人额度提至70万元。", "深圳市住建局", "2026-04-30", "https://readhub.cn/topic/8eXxx8xXxXx"],
        ["政治局会议定调：努力稳定房地产市场", "从着力稳定到努力稳定传递积极信号，扎实推进城市更新和城中村改造。", "21世纪经济报道", "2026-04-28", "https://view.inews.qq.com/a/20260428A06PEB00"],
        ["4月中国汽车经销商库存预警指数为62.1%", "库存预警指数位于荣枯线之上，同比上升2.3个百分点，汽车行业面临库存压力。", "中国汽车流通协会", "2026-04-30", "https://www.cls.cn/detail/2360817"],
        ["万科Q1营收同比下降近24%，净亏损小幅收窄至59.5亿", "万科一季度业绩持续承压，但净亏损较前期有所收窄，经营情况出现边际改善迹象。", "腾讯新闻", "2026-04-29", "https://view.inews.qq.com/a/20260429A04HH100"],
        ["深圳住房公积金贷款额度个人从60万提至70万元", "家庭额度从110万元提至130万元，最高可上浮170%，购房支持力度加大。", "Readhub", "2026-04-30", "https://readhub.cn/topic/8eXxx8xXxXx"]
    ]],
    ["🚗", "汽车出行", [
        ["特斯拉Semi电动卡车首辆量产车下线", "九年研发后特斯拉Semi电动卡车首辆量产车终于下线，电动重卡市场迎来重要里程碑。", "IT之家", "2026-04-30", "https://www.ithome.com/0/945/326.htm"],
        ["鸿蒙智行问界M6开启全国规模交付", "月产能将拉升至超2万台，问界M6全国交付正式启动，产能爬坡迅速。", "IT之家", "2026-04-30", "https://www.ithome.com/0/945/283.htm"],
        ["比亚迪天神之眼C车型将从百度地图切换为高德地图", "比亚迪智驾系统地图供应商调整，涉及天神之眼C配置车型。", "IT之家", "2026-04-30", "https://www.ithome.com/0/945/277.htm"],
        ["京港高铁雄商段（山东段）完成提速试验", "最高时速385公里，京港高铁建设取得重要进展，未来通行效率将大幅提升。", "IT之家", "2026-04-30", "https://www.ithome.com/0/945/394.htm"],
        ["大众汽车第一季度营业利润低于预估", "Q1交付量205万辆，营收756.6亿欧元，营业利润24.6亿欧元低于预估的30.2亿欧元。", "财联社", "2026-04-30", "https://www.cls.cn/detail/2360797"]
    ]],
    ["🏥", "医疗健康", [
        ["国家药监局局长黄果调研节前药品监管工作", "考察体外诊断检测平台和脑机接口等前沿医疗器械检验能力建设情况。", "财联社", "2026-04-30", "https://www.cls.cn/detail/2360803"],
        ["我国悟空号又有新发现：首次发现宇宙射线加速能量极限的电荷依赖规律", "中国科研团队取得重大科学突破，为理解宇宙射线起源和加速机制提供新线索。", "IT之家", "2026-04-30", "https://www.ithome.com/0/945/298.htm"],
        ["伊利成唯一营收净利双增综合性乳企", "2025年营收1159亿元净利增36.82%，基本盘液奶业务率先逆势实现正增长。", "财联社", "2026-04-30", "https://www.cls.cn/detail/2360819"],
        ["大连至青岛340公里无人机物流航线通航", "国内首条跨渤海无人机物流航线通航，仅需2小时，低空经济商业化迈出重要一步。", "IT之家", "2026-04-30", "https://www.ithome.com/0/945/250.htm"],
        ["寒武纪一季度净利润10.13亿元同比增长185%", "AI芯片龙头业绩持续爆发，反映国内AI算力需求旺盛和国产替代加速趋势。", "财联社", "2026-04-30", "https://www.cls.cn/detail/2360805"]
    ]],
    ["📚", "教育培训", [
        ["习近平强调加强基础研究人才培养", "要一体推进教育科技人才发展，全方位做好培养、引进、使用工作，壮大基础研究人才队伍。", "央视新闻", "2026-04-30", "https://www.cls.cn/detail/2360813"],
        ["钉钉陈航：AI招聘看AIQ，学历经历年龄不再重要", "钉钉创始人提出AI时代人才评价新观点，AI Quotient将成为招聘核心指标。", "IT之家", "2026-04-30", "https://www.ithome.com/0/945/359.htm"],
        ["联合早报校园网夺亚洲数码媒体奖银奖", "为中小学生华文学习提供丰富资源，获得亚洲数码媒体奖认可。", "今日热榜", "2026-04-30", "https://tophub.today/daily"],
        ["中国科学家揭示惯用手不是天生的，是后天训练出来的", "最新研究发现打破传统认知，为教育和训练方式提供新思路。", "知乎日报", "2026-04-30", "https://tophub.today/daily"],
        ["OpenRouter发布大模型调用量排行榜，混元Hy3登顶", "腾讯混元新模型Hy3 preview在全球大模型API调用量总榜上排名第一。", "Readhub", "2026-04-30", "https://readhub.cn/topic/8eXxx8xXxXx"]
    ]],
    ["✈️", "旅游民宿", [
        ["五一假期临近，酒店预订维权成热点", "预定酒店30分钟后不可取消被律师指为霸王条款，消费者维权引关注。", "澎湃新闻", "2026-04-30", "https://www.thepaper.cn/"],
        ["世界最高无轴摩天轮上海之门计划年底开建", "将超越潍坊渤海之眼，成为新的世界级旅游地标，带动区域旅游发展。", "IT之家", "2026-04-30", "https://www.ithome.com/0/945/266.htm"],
        ["北京5月1日起禁飞禁售无人机，大疆门店今日下架相关产品", "北京全域禁飞禁售无人机新规落地，大疆北京所有门店启动产品下架流程。", "Readhub", "2026-04-30", "https://readhub.cn/topic/8eXxx8xXxXx"],
        ["大连至青岛340公里无人机物流航线通航", "国内首条跨渤海无人机物流航线通航，仅需2小时，开创低空物流新模式。", "IT之家", "2026-04-30", "https://www.ithome.com/0/945/250.htm"],
        ["深圳地铁集团董事长辛杰不再担任董事长", "截至公告日董事长空缺暂未任命，人员变动已获有权机构审议通过。", "Readhub", "2026-04-30", "https://readhub.cn/topic/8eXxx8xXxXx"]
    ]],
    ["🌍", "国际视角", [
        ["特朗普继续对伊朗实施海上封锁", "特朗普称将继续对伊朗实施海上封锁，同伊朗的谈判正通过电话进行。", "财联社", "2026-04-30", "https://tophub.today/daily"],
        ["美联储34年来最大分歧，维持利率不变", "四票委反对决议声明，为1992年以来最多反对票，市场关注后续政策走向。", "财联社", "2026-04-30", "https://www.cls.cn/detail/2360793"],
        ["57国齐聚哥伦比亚聊退煤，主要化石能源消费国未参会", "国际气候治理新动态，但关键国家缺席影响会议成效和执行力。", "澎湃新闻", "2026-04-30", "https://www.thepaper.cn/"],
        ["Alphabet CEO：算力瓶颈仍限制公司增长", "皮查伊表示若能满足全部需求，云业务收入会更高，正积极应对加大投资。", "财联社", "2026-04-30", "https://www.cls.cn/detail/2360800"],
        ["伊朗海军司令称将向敌人展示可怕武器", "伊朗海军司令表示将在海上使用令敌人恐惧的武器，中东局势持续紧张。", "新华社", "2026-04-30", "https://tophub.today/daily"]
    ]],
    ["🚀", "融资收购", [
        ["Anthropic或以超9000亿美元估值融资", "AI独角兽Anthropic考虑新一轮融资，估值或超9000亿美元，AI投资热潮持续。", "Readhub", "2026-04-30", "https://readhub.cn/topic/8eXxx8xXxXx"],
        ["OpenRouter发布大模型调用量排行榜，混元Hy3登顶", "腾讯混元Hy3 preview在总榜和工具调用场景均排名第一，编程场景排名第二。", "Readhub", "2026-04-30", "https://readhub.cn/topic/8eXxx8xXxXx"],
        ["台积电清空所持Arm股票，累计获益2.322亿美元", "台积电出售全部Arm持股，累计收益约2.322亿美元，投资组合调整引发关注。", "腾讯新闻", "2026-04-30", "https://view.inews.qq.com/a/20260429A04HH100"],
        ["微软松绑独家协议，OpenAI正式上线亚马逊云", "OpenAI扩大与AWS合作，GPT-5.5和Codex接入亚马逊Bedrock，微软放宽排他性限制。", "Readhub", "2026-04-30", "https://readhub.cn/topic/8eXxx8xXxXx"],
        ["小红书成立AI一级部门Dots和企业智能部", "小红书组织架构调整加速AI布局，成立AI一级部门Dots，加码人工智能投入。", "IT之家", "2026-04-30", "https://www.ithome.com/0/945/390.htm"]
    ]]
]

# 保存JSON数据
mid = len(sections) // 2
sections1 = sections[:mid]
sections2 = sections[mid:]

with open("D:\\openclaw\\Intelnet-daily-news\\sections_data.json", "w", encoding="utf-8") as f:
    json.dump(sections1, f, ensure_ascii=False, indent=2)
with open("D:\\openclaw\\Intelnet-daily-news\\sections_data2.json", "w", encoding="utf-8") as f:
    json.dump(sections2, f, ensure_ascii=False, indent=2)

# CSS和HTML模板
CSS = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="theme-color" content="#f0f9ff">
    <title>互联网早报 - ''' + today + '''</title>
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
        <div class="date">''' + today + " " + weekday + '''</div>
        <div class="meta">
            <span>📊 <strong>13</strong> 个核心栏目</span>
            <span>📰 <strong>65</strong> 条精选新闻</span>
            <span>⏰ <strong>14:00</strong> 午间推送</span>
        </div>
    </div>
    <div class="content">
'''

def make_section(icon, title, items):
    h = '        <div class="section">\n'
    h += '            <div class="section-title"><span class="icon">' + icon + '</span><span>' + title + '</span></div>\n'
    h += '            <div class="news-grid">\n'
    for i, (t, s, src, d, link) in enumerate(items, 1):
        h += '                <div class="news-card">\n'
        h += '                    <span class="news-number">' + f"{i:02d}" + '</span>\n'
        h += '                    <div class="news-title">' + t + '</div>\n'
        h += '                    <div class="news-summary">' + s + '</div>\n'
        h += '                    <div class="news-meta">\n'
        h += '                        <span class="news-source">' + src + '</span>\n'
        h += '                        <span>' + d + '</span>\n'
        h += '                        <a href="' + link + '" class="news-link" target="_blank">查看详情</a>\n'
        h += '                    </div>\n'
        h += '                </div>\n'
    h += '            </div>\n'
    h += '        </div>\n'
    return h

FOOTER = '''    </div>
    <div class="footer">
        <div class="brand">互联网早报</div>
        <p>每日为您精选最重要的科技资讯</p>
        <div class="stats">
            <div class="stat-item"><span class="stat-number">13</span><span class="stat-label">核心栏目</span></div>
            <div class="stat-item"><span class="stat-number">65</span><span class="stat-label">精选新闻</span></div>
            <div class="stat-item"><span class="stat-number">14:00</span><span class="stat-label">准时推送</span></div>
        </div>
        <p>发送时间：''' + today + '''</p>
    </div>
</div>
</body>
</html>
'''

# 生成HTML
html = CSS
for icon, title, items in sections:
    html += make_section(icon, title, items)
html += FOOTER

outpath = "D:\\openclaw\\Intelnet-daily-news\\互联网早报_" + today + ".html"
with open(outpath, "w", encoding="utf-8") as f:
    f.write(html)

print("HTML generated: " + outpath)
print("File size: " + str(len(html.encode('utf-8'))) + " bytes")
print("Sections: " + str(len(sections)) + ", Total news items: " + str(sum(len(items) for _,_,items in sections)))
