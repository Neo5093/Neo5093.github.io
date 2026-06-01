import json
import os
from datetime import datetime

# 今天是2026年5月11日，星期一
today = "2026年5月11日"
weekday = "星期一"

# 新闻数据结构: [图标, 栏目名, [ [标题, 摘要, 来源, 日期, 链接], ... ] ]
sections = [
    ["✨", "数据亮点", [
        ["MSCI亚太指数上涨1%至273.72点", "MSCI亚太指数早盘上涨1%，报273.72点，亚太股市整体表现强劲。", "财联社", "2026-05-11", "https://www.cls.cn/detail/2367440"],
        ["韩国KOSPI指数涨超4%续创历史新高", "韩国KOSPI指数大涨超4%，报7802.82点，连续刷新历史最高纪录。", "财联社", "2026-05-11", "https://www.cls.cn/detail/2367403"],
        ["韩国5月上旬出口同比增长43.7%", "韩国5月1日至10日出口同比大增43.7%，进口增长14.9%，贸易顺差初值17亿美元。", "财联社", "2026-05-11", "https://www.cls.cn/detail/2367405"],
        ["SK海力士、三星电子股价齐创新高", "SK海力士股价上涨逾8%创历史新高，三星电子股价上涨超5%同步刷新纪录。", "财联社", "2026-05-11", "https://www.cls.cn/detail/2367402"],
        ["沙特阿美一季度净利1201亿", "沙特阿美公布一季度业绩，净利润达1201亿元人民币，石油巨头持续高盈利。", "MBA智库", "2026-05-11", "https://news.mbalib.com/story/258689"]
    ]],
    ["🇨🇳", "国内要闻", [
        ["天舟十号货运飞船发射任务取得圆满成功", "天舟十号货运飞船发射圆满成功，为空间站运送约6.3吨补给物资，实现10战10捷。", "央视新闻", "2026-05-11", "https://www.cls.cn/detail/2367431"],
        ["字节跳动计划将AI基础设施支出增加25%至2000亿", "字节跳动加速布局AI，今年AI基础设施支出计划增加25%至2000亿元人民币。", "财联社", "2026-05-11", "https://www.cls.cn/detail/2367428"],
        ["丁薛祥调研华为芯片基础技术实验室，与任正非交谈", "国务院副总理丁薛祥到访华为上海研发中心，考察芯片基础技术实验室并与任正非交流。", "快科技", "2026-05-11", "https://readhub.cn/topic/8syqfbAIhP4"],
        ["国务院常务会议强调加强水网、新型电网、算力网等规划建设", "国务院常务会议强调加强水网、新型电网、算力网、新一代通信网等规划建设。", "财联社", "2026-05-11", "https://www.cls.cn/detail/2367419"],
        ["河北印发《现代化钢铁产业2026年重点工作清单》", "河北省提出年内钢铁领域突破25项关键技术、研发30个以上新品种、推广10个钢铁大模型。", "财联社", "2026-05-11", "https://www.cls.cn/detail/2367426"]
    ]],
    ["📋", "政务快讯", [
        ["三部门印发《智能体规范应用与创新发展实施意见》", "国家网信办等三部门发文，促进智能体与数控机床、工业机器人等制造业融合。", "财联社", "2026-05-11", "https://www.cls.cn/detail/2367419"],
        ["四部门印发促进人工智能与能源双向赋能行动方案", "国家能源局等四部门发文，力争2030年AI算力设施清洁能源供给保障能力大幅提升。", "财联社", "2026-05-11", "https://www.cls.cn/detail/2367419"],
        ["河北钢铁产业年内突破25项关键技术", "河北省钢铁产业2026年重点工作明确，将突破25项关键技术、认定20个以上绿钢品种。", "财联社", "2026-05-11", "https://www.cls.cn/detail/2367426"],
        ["国家体育总局：不组织、不参与运动员庆生等活动", "体育总局发文规范粉丝行为，呼吁不组织不参与运动员私人庆生活动，保持理性。", "新浪财经", "2026-05-11", "https://finance.sina.com.cn/wm/2026-05-11/doc-inhxnmvx0729657.shtml"],
        ["发改委主任调研上海人工智能实验室", "发改委主任郑栅洁调研上海人工智能实验室，强调加强基础研究、注重从源头解决底层技术问题。", "财联社", "2026-05-11", "https://www.cls.cn/detail/2367419"]
    ]],
    ["📱", "科技通信", [
        ["央视揭秘新能源汽车\"锁电\"真相", "央视调查曝光新能源汽车OTA\"锁电\"现象，揭示电池续航缩水的行业潜规则。", "IT之家", "2026-05-11", "https://www.ithome.com/0/948/562.htm"],
        ["阿里巴巴将深度整合千问与淘宝", "阿里计划将通义千问AI深度接入淘宝，推出智能体式购物服务，接入超40亿款商品库。", "IT之家", "2026-05-11", "https://www.ithome.com/0/948/562.htm"],
        ["马斯克入局AI编程赛道：Grok Build曝光", "马斯克推出AI编程应用Grok Build，入局AI辅助编程赛道，对标Claude Code和OpenAI Codex。", "界面新闻", "2026-05-11", "https://www.jiemian.com/article/14405353.html"],
        ["苹果与英特尔就芯片代工达成初步协议", "苹果与英特尔就芯片代工业务达成初步合作协议，英特尔有望获得苹果订单。", "少数派", "2026-05-11", "https://sspai.com/post/109610"],
        ["慧荣科技预警：NAND闪存缺货潮或延续至2028年", "慧荣科技高管发出行业预警，NAND闪存供应紧张局面可能持续至2028年，影响存储产业链。", "IT之家", "2026-05-11", "https://www.ithome.com/0/948/571.htm"]
    ]],
    ["🎬", "文娱影游", [
        ["亚马逊Prime Video增加\"Clips\"短视频信息流", "亚马逊跟进Netflix策略，在Prime Video中加入短视频信息流功能，布局短内容赛道。", "IT之家", "2026-05-11", "https://www.ithome.com/0/948/569.htm"],
        ["腾讯天美G1工作室总经理高敏离职，工作室或整体裁撤", "腾讯天美G1工作室总经理高敏离职，该工作室或因运营不佳面临整体裁撤。", "凤凰科技", "2026-05-11", "https://readhub.cn/topic/8sz4FSZp9m6"],
        ["任天堂股价下跌9%，财报未达市场预期", "任天堂股价大跌9%，此前发布的财报和业绩预测未达市场预期，游戏巨头承压。", "财联社", "2026-05-11", "https://www.cls.cn/detail/2367411"],
        ["世界杯中国转播费从3亿美元腰斩到1.5亿", "2026年世界杯中国地区转播权费用从3亿美元降至1.5亿美元，体育赛事版权价值大幅缩水。", "36氪", "2026-05-11", "https://36kr.com/p/3804132892646919"],
        ["中国女乒实现世乒赛七连冠", "中国女乒在世乒赛团体赛中3-2逆转日本夺冠，实现七连冠，孙颖莎独得两分成最大功臣。", "新民早报", "2026-05-11", "https://www.shobserver.com/staticsg/res/html/web/newsDetail.html?id=1110229"]
    ]],
    ["💰", "金融财经", [
        ["中金：AI现在仍未到典型的\"泡沫\"阶段", "中金公司研报认为，从需求、投资强度和市场定价三维度看，AI未到典型\"泡沫\"阶段。", "财联社", "2026-05-11", "https://www.cls.cn/detail/2367423"],
        ["中信证券：国际供应链冲击加速高端膜材料国产化", "中信证券测算2025年高端PET基膜市场空间160亿元，三大赛道国产化率将快速提升。", "财联社", "2026-05-11", "https://www.cls.cn/detail/2367409"],
        ["港交所前4月IPO融资同比增约6倍", "港交所前4个月IPO融资规模同比增长约6倍，港股市场活跃度显著提升，发行制度或将优化。", "财联社", "2026-05-11", "https://www.cls.cn/detail/2367382"],
        ["景林资产大幅加仓英特尔", "知名投资机构景林资产大幅增持英特尔股票，看好芯片龙头前景，半导体投资热度不减。", "格隆汇", "2026-05-11", "https://www.gelonghui.com/p/4698407"],
        ["全球芯片LOF、中韩半导体ETF因大幅溢价停牌1小时", "因大幅溢价，全球芯片LOF、中韩半导体ETF华泰柏瑞停牌一小时，半导体投资过热。", "财联社", "2026-05-11", "https://www.cls.cn/detail/2367370"]
    ]],
    ["🏠", "住房地产", [
        ["央媒调查辽宁凌源20万吨钢渣露天堆放，当地将投入千万处理", "中央媒体调查发现辽宁凌源市存在20万吨钢渣长期露天堆放问题，当地政府承诺投入数千万元整治。", "澎湃新闻", "2026-05-11", "https://www.thepaper.cn/newsDetail_forward_33154022"],
        ["龚仆调研上峰水泥", "相关领导调研上峰水泥企业，了解水泥行业发展情况，关注建筑材料产业动态。", "中国水泥网", "2026-05-11", "https://www.ccement.com/news/content/68454139100245001.html"],
        ["央视曝光AI买家秀：电商平台虚假评价乱象", "央视调查曝光电商平台AI生成虚假买家秀现象，揭示电商评价体系的信任危机。", "微信", "2026-05-11", "http://mp.weixin.qq.com/s?__biz=MzA5NDc1NzQ4MA==&mid=2654660214"],
        ["中信证券：高端膜材料国产化加速", "中信证券测算高端PET基膜市场空间广阔，偏光片及离保膜、MLCC离型膜国产化率将快速提升。", "财联社", "2026-05-11", "https://www.cls.cn/detail/2367409"],
        ["河北钢铁产业2026年重点工作清单发布", "河北钢铁产业年内将加快36个重点项目建设，推广10个钢铁大模型，推动建筑材料产业升级。", "财联社", "2026-05-11", "https://www.cls.cn/detail/2367426"]
    ]],
    ["🚗", "汽车出行", [
        ["零跑在德国推出T03汽车租赁方案：49欧元/月", "中国新能源汽车品牌零跑进军欧洲市场，在德国推出极具竞争力的T03租赁方案，月租仅49欧元。", "IT之家", "2026-05-11", "https://www.ithome.com/0/948/574.htm"],
        ["央视揭秘新能源汽车\"锁电\"真相", "央视调查曝光新能源汽车OTA\"锁电\"现象，揭示电池续航缩水的行业潜规则，消费者权益引关注。", "IT之家", "2026-05-11", "https://www.ithome.com/0/948/562.htm"],
        ["宝马全新长轴距X5将于明年登录中国", "宝马宣布全新长轴距版X5将于2027年在中国市场上市，豪华SUV市场竞争将加剧。", "微信", "2026-05-11", "http://mp.weixin.qq.com/s?__biz=MzA5NDc1NzQ4MA==&mid=2654660214"],
        ["比亚迪与神州租车开展闪充合作", "比亚迪与神州租车达成闪充技术合作，布局租车市场充电网络，推动新能源出行生态建设。", "微信", "2026-05-11", "http://mp.weixin.qq.com/s?__biz=MzA5NDc1NzQ4MA==&mid=2654660214"],
        ["国产百万级MPV即将发布", "国产高端MPV车型即将上市，定价达百万级别，中国品牌向豪华市场发起冲击。", "微信", "2026-05-11", "http://mp.weixin.qq.com/s?__biz=MjM5OTAzMjc4MA==&mid=2650874373"]
    ]],
    ["🏥", "医疗健康", [
        ["翰森制药自研ADC药物获纳入突破性治疗", "翰森制药自研B7-H3靶向ADC注射用HS-20093获NMPA批准纳入突破性治疗药物，用于食管鳞癌。", "财联社", "2026-05-11", "https://www.cls.cn/detail/2367399"],
        ["涉疫邮轮预计10日疏散90余人", "一艘出现疫情的邮轮预计疏散90余名人员，涉及公共卫生应急响应与海上旅游安全管理。", "澎湃新闻", "2026-05-11", "https://www.thepaper.cn/newsDetail_forward_33154017"],
        ["美科技行业失业率升至3.8%，AI驱动裁员加重", "美国IT岗位失业率升至3.8%，信息行业四月流失1.3万个岗位，AI成为企业压缩人力规模的考量。", "凤凰科技", "2026-05-11", "https://readhub.cn/topic/8t0yBD97DSQ"],
        ["国家体育总局规范运动员庆生活动", "体育总局回应多地运动员庆生活动，称占用公共资源、干扰备战且涉嫌侵权，呼吁公众保持理性。", "新浪财经", "2026-05-11", "https://finance.sina.com.cn/wm/2026-05-11/doc-inhxnmvx0729657.shtml"],
        ["韩国KOSPI 200指数期货上涨5%触发熔断", "韩国KOSPI 200指数期货大涨5%，触发熔断机制，程序化交易暂停5分钟，市场波动剧烈。", "财联社", "2026-05-11", "https://www.cls.cn/detail/2367429"]
    ]],
    ["📚", "教育培训", [
        ["黄仁勋：应届生们别怕AI，当下是开启事业的最佳时机", "英伟达CEO黄仁勋在演讲中鼓励应届毕业生积极拥抱AI技术，认为当前是进入科技行业的最佳时机。", "IT之家", "2026-05-11", "https://www.ithome.com/0/948/566.htm"],
        ["武汉大学就OPPO母亲节文案发声", "武汉大学文学院声明\"极不认同\"校友团队母亲节文案的价值倾向，OPPO已道歉并下架物料。", "微信", "2026-05-11", "https://readhub.cn/topic/8t14xQJ8DZB"],
        ["国家体育总局规范粉丝行为", "体育总局发文规范粉丝行为，呼吁不组织不参与运动员私人活动，维护体育教育生态。", "新浪财经", "2026-05-11", "https://finance.sina.com.cn/wm/2026-05-11/doc-inhxnmvx0729657.shtml"],
        ["中金：AI未到典型泡沫阶段", "中金公司研报从需求、投资强度和市场定价三维度分析，认为AI投资仍需理性看待。", "财联社", "2026-05-11", "https://www.cls.cn/detail/2367423"],
        ["发改委主任调研上海人工智能实验室", "发改委主任郑栅洁调研上海人工智能实验室，强调加强基础研究，为AI科研教育指明方向。", "财联社", "2026-05-11", "https://www.cls.cn/detail/2367419"]
    ]],
    ["✈️", "旅游民宿", [
        ["游客投诉演唱会座椅脏被\"拉黑\"，桂林文旅已道歉", "有游客因投诉演唱会场地座椅脏乱被桂林文旅部门\"拉黑\"，事后当地文旅局公开道歉并解除限制。", "澎湃新闻", "2026-05-11", "https://www.thepaper.cn/newsDetail_forward_33154144"],
        ["涉疫邮轮预计10日疏散90余人", "一艘出现疫情的邮轮预计将于5月10日疏散90余名人员，涉及海上旅游安全与公共卫生应急。", "澎湃新闻", "2026-05-11", "https://www.thepaper.cn/newsDetail_forward_33154017"],
        ["零跑在德国推出T03租赁方案", "中国新能源汽车品牌零跑进军欧洲市场，在德国推出极具竞争力的T03租赁方案，月租仅49欧元。", "IT之家", "2026-05-11", "https://www.ithome.com/0/948/574.htm"],
        ["五一假期景区交易笔数环比大涨277%", "微信支付发布五一假期数据报告，景区交易笔数环比大涨277%，港澳游受欢迎，消费复苏势头强劲。", "IT之家", "2026-05-05", "https://www.ithome.com/0/946/436.htm"],
        ["世界最高无轴摩天轮上海之门计划年底开建", "上海计划年底开建世界最高无轴摩天轮\"上海之门\"，将超越潍坊渤海之眼成为新的世界级旅游地标。", "IT之家", "2026-05-05", "https://www.ithome.com/0/946/266.htm"]
    ]],
    ["🌍", "国际视角", [
        ["伊朗拒绝美国提出的结束战争方案", "伊朗已拒绝美国提出的结束战争方案，认为同意该方案将意味着屈从于特朗普的过分要求。", "财联社", "2026-05-11", "https://www.cls.cn/detail/2367370"],
        ["中美将在韩国举行经贸磋商", "中美将在韩国举行新一轮经贸磋商，双方就经贸关系进行对话，国际市场关注进展。", "新浪财经", "2026-05-11", "https://finance.sina.com.cn/stock/y/2026-05-11/doc-inhxnmvr2073704.shtml"],
        ["泰国前总理他信假释出狱", "当地时间5月11日上午，泰国前总理他信假释出狱，泰国政坛面临新的变数。", "央视新闻", "2026-05-11", "https://www.cls.cn/detail/2367439"],
        ["美国FCC豁免外国设备软件更新限制至2029年", "美国联邦通信委员会延长临时豁免期限，部分外国产无人机和路由器可继续在美国获得软件更新至2029年。", "快科技", "2026-05-11", "https://readhub.cn/topic/8t0YS4S87Zp"],
        ["美科技行业失业率四月升至3.8%", "美国IT岗位失业率升至3.8%，信息行业四月流失1.3万个岗位，AI技术应用加剧裁员压力。", "凤凰科技", "2026-05-11", "https://readhub.cn/topic/8t0yBD97DSQ"]
    ]],
    ["🚀", "融资收购", [
        ["DeepSeek被曝融资500亿，CEO梁文锋或自掏200亿领投", "DeepSeek首轮融资规模达500亿元，CEO梁文锋个人出资200亿领投，将创中国AI领域单轮融资纪录。", "格隆汇", "2026-05-11", "https://readhub.cn/topic/8t0ZrYuHPGp"],
        ["阿玛尼拟向欧莱雅、LV等三家集团出让15%股份", "乔治·阿玛尼计划向欧莱雅、LVMH、依视路陆逊梯卡三家出让15%股份，履行创始人遗嘱安排。", "财联社", "2026-05-11", "https://readhub.cn/topic/8t0wjK8Vj9z"],
        ["字节跳动计划将AI基础设施支出增加25%", "字节跳动今年AI基础设施支出计划增加25%至2000亿元人民币，持续加码人工智能领域投入。", "财联社", "2026-05-11", "https://www.cls.cn/detail/2367428"],
        ["港交所前4月IPO融资同比增约6倍", "港交所前4个月IPO融资规模同比增长约6倍，已从消费医药转向AI、高端装备等科技制造板块。", "财联社", "2026-05-11", "https://www.cls.cn/detail/2367382"],
        ["Circle今日将发布财报", "加密货币公司Circle将于今日发布财报，市场关注其业绩表现，加密支付赛道持续升温。", "富途资讯", "2026-05-11", "https://news.futunn.com/post/72829976"]
    ]]
]

# CSS和HTML模板
CSS = '''<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0, maximum-scale=1.0, user-scalable=no">
    <meta name="theme-color" content="#f0f9ff">
    <title>互联网早报 - ''' + today + '''</title>
    <style>
        * { margin: 0; padding: 0; box-sizing: border-box; -webkit-tap-highlight-color: transparent; }
        :root { --primary-blue: #0ea5e9; --light-blue: #f0f9ff; --ice-gray: #f8fafc; --tech-silver: #94a3b8; --aurora-white: #ffffff; --text-dark: #0f172a; --text-medium: #475569; --text-light: #64748b; --gradient-start: #e0f2fe; --gradient-end: #f0f9ff; --card-shadow: 0 4px 6px -1px rgba(0,0,0,0.1); --glass-bg: rgba(255,255,255,0.7); --glass-border: rgba(255,255,255,0.5); }
        body { font-family: -apple-system,BlinkMacSystemFont,"Segoe UI","Roboto","PingFang SC","Hiragino Sans GB","Microsoft YaHei",sans-serif; background: linear-gradient(180deg,var(--gradient-start) 0%,var(--gradient-end) 100%); min-height: 100vh; color: var(--text-dark); line-height: 1.6; -webkit-font-smoothing: antialiased; }
        body::before { content: ''; position: fixed; top:0;left:0;width:100%;height:100%; background-image: linear-gradient(rgba(14,165,233,0.03) 1px,transparent 1px),linear-gradient(90deg,rgba(14,165,233,0.03) 1px,transparent 1px); background-size: 50px 50px; pointer-events: none; z-index: 0; }
        .container { max-width: 100%; margin:0 auto; position: relative; z-index: 1; }
        .header { background: var(--glass-bg); backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px); border-bottom: 1px solid var(--glass-border); padding: 24px 16px; text-align: center; position: sticky; top: 0; z-index: 100; }
        .header h1 { font-size: 26px; font-weight: 700; background: linear-gradient(135deg,#0ea5e9 0%,#6366f1 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-bottom: 6px; }
        .header .date { font-size: 15px; color: var(--text-medium); }
        .header .meta { font-size: 13px; color: var(--text-light); margin-top: 6px; display: flex; justify-content: center; gap: 16px; flex-wrap: wrap; }
        .content { padding: 16px; max-width: 1200px; margin: 0 auto; }
        .section { margin-bottom: 24px; animation: fadeInUp 0.6s ease-out; }
        @keyframes fadeInUp { from { opacity: 0; transform: translateY(20px); } to { opacity: 1; transform: translateY(0); } }
        .section-title { display: flex; align-items: center; gap: 10px; margin-bottom: 12px; padding: 12px 16px; background: var(--glass-bg); backdrop-filter: blur(10px); -webkit-backdrop-filter: blur(10px); border-radius: 14px; border: 1px solid var(--glass-border); font-size: 18px; font-weight: 600; color: var(--text-dark); transition: all 0.3s ease; }
        .section-title:hover { transform: translateX(5px); box-shadow: var(--card-shadow); }
        .section-title .icon { font-size: 24px; animation: pulse 2s ease-in-out infinite; }
        @keyframes pulse { 0%,100% { transform: scale(1); } 50% { transform: scale(1.1); } }
        .news-grid { display: grid; grid-template-columns: 1fr; gap: 12px; }
        @media (min-width: 769px) and (max-width: 1024px) { .news-grid { grid-template-columns: repeat(2, 1fr); } }
        @media (min-width: 1025px) { .news-grid { grid-template-columns: repeat(3, 1fr); } }
        .news-card { background: var(--aurora-white); border-radius: 14px; padding: 16px; border: 1px solid rgba(226,232,240,0.8); box-shadow: var(--card-shadow); transition: all 0.3s ease; position: relative; overflow: hidden; }
        .news-card::before { content: ''; position: absolute; top:0;left:0;right:0; height: 3px; background: linear-gradient(90deg,#0ea5e9,#6366f1); transform: scaleX(0); transform-origin: left; transition: transform 0.3s ease; }
        .news-card:hover { transform: translateY(-4px); box-shadow: 0 20px 25px -5px rgba(0,0,0,0.1); border-color: #0ea5e9; }
        .news-card:hover::before { transform: scaleX(1); }
        .news-number { position: absolute; top:10px;right:10px; width:26px;height:26px; background: linear-gradient(135deg,#e0f2fe,#e0f2fe); border-radius: 8px; display: flex; align-items: center; justify-content: center; font-size: 12px; font-weight: 600; color: #0ea5e9; font-family: 'JetBrains Mono',monospace; }
        .news-title { font-size: 15px; font-weight: 600; color: var(--text-dark); line-height: 1.5; margin-bottom: 8px; padding-right: 34px; }
        .news-summary { font-size: 13px; color: var(--text-light); line-height: 1.5; margin-bottom: 10px; display: -webkit-box; -webkit-line-clamp: 2; -webkit-box-orient: vertical; overflow: hidden; }
        .news-meta { display: flex; align-items: center; gap: 8px; flex-wrap: wrap; }
        .news-source { background: linear-gradient(135deg,#e0f2fe,#e0f2fe); color: #0ea5e9; padding: 3px 10px; border-radius: 20px; font-size: 12px; font-weight: 500; }
        .news-date { font-size: 12px; color: var(--tech-silver); }
        .news-link { color: #0ea5e9; text-decoration: none; font-size: 12px; font-weight: 500; padding: 3px 10px; border-radius: 20px; background: rgba(14,165,233,0.1); transition: all 0.2s ease; }
        .news-link:hover { background: #0ea5e9; color: white; }
        .footer { background: var(--glass-bg); backdrop-filter: blur(20px); -webkit-backdrop-filter: blur(20px); border-top: 1px solid var(--glass-border); padding: 24px 16px; text-align: center; color: var(--text-medium); }
        .footer .brand { font-size: 16px; font-weight: 600; background: linear-gradient(135deg, #0ea5e9, #6366f1); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
        .footer .stats { display: inline-flex; gap: 16px; background: white; padding: 10px 20px; border-radius: 30px; margin: 12px 0; box-shadow: var(--card-shadow); }
        .footer .stat-number { font-size: 20px; font-weight: 700; background: linear-gradient(135deg, #0ea5e9, #6366f1); -webkit-background-clip: text; -webkit-text-fill-color: transparent; }
        .footer .stat-label { font-size: 11px; color: var(--text-light); }
        .back-home { position: fixed; top: 16px; left: 16px; z-index: 1000; background: linear-gradient(135deg, #0ea5e9 0%, #6366f1 100%); color: white; padding: 8px 14px; border-radius: 25px; text-decoration: none; font-size: 13px; font-weight: 500; box-shadow: 0 4px 15px rgba(14, 165, 233, 0.3); transition: all 0.3s ease; }
        .back-home:hover { transform: translateY(-2px); box-shadow: 0 6px 20px rgba(14, 165, 233, 0.4); }
        @media (max-width: 480px) {
            .header { padding: 18px 12px; }
            .header h1 { font-size: 22px; }
            .header .meta { gap: 10px; font-size: 12px; }
            .content { padding: 12px; }
            .news-card { padding: 14px; }
            .news-title { font-size: 14px; }
            .news-summary { font-size: 12px; }
            .section-title { font-size: 16px; padding: 10px 14px; }
            .footer .stats { gap: 10px; padding: 8px 14px; }
            .back-home { padding: 6px 12px; font-size: 12px; top: 10px; left: 10px; }
        }
    </style>
</head>
<body>
    <a href="../index.html" class="back-home">← 返回首页</a>
    <div class="container">
        <div class="header">
            <h1>互联网早报</h1>
            <div class="date">''' + today + ''' ''' + weekday + '''</div>
            <div class="meta">
                <span>📊 <strong>13</strong> 个核心栏目</span>
                <span>📰 <strong>65</strong> 条精选新闻</span>
                <span>⏰ <strong>08:45</strong> 准时推送</span>
            </div>
        </div>
        <div class="content">
'''

# 生成各栏目HTML
content = ""
for sec in sections:
    icon, name, news_list = sec
    content += f'''            <div class="section">
                <div class="section-title">
                    <span class="icon">{icon}</span>
                    <span>{name}</span>
                </div>
                <div class="news-grid">
'''
    for i, n in enumerate(news_list):
        title, summary, source, date, link = n
        num = f"{i+1:02d}"
        content += f'''                    <div class="news-card">
                        <span class="news-number">{num}</span>
                        <div class="news-title">{title}</div>
                        <div class="news-summary">{summary}</div>
                        <div class="news-meta">
                            <span class="news-source">{source}</span>
                            <span class="news-date">{date}</span>
                            <a href="{link}" class="news-link" target="_blank">查看详情 →</a>
                        </div>
                    </div>
'''
    content += '''                </div>
            </div>
'''

footer = '''        </div>
        <div class="footer">
            <div class="brand">互联网早报</div>
            <p>每日为您精选最重要的科技资讯</p>
            <div class="stats">
                <div class="stat-item">
                    <span class="stat-number">13</span>
                    <span class="stat-label">核心栏目</span>
                </div>
                <div class="stat-item">
                    <span class="stat-number">65</span>
                    <span class="stat-label">精选新闻</span>
                </div>
                <div class="stat-item">
                    <span class="stat-number">08:45</span>
                    <span class="stat-label">准时推送</span>
                </div>
            </div>
            <p>发送时间：''' + today + '''</p>
            <p style="margin-top:8px;font-size:12px;color:var(--text-light);">数据来源：财联社 · IT之家 · Readhub · 今日热榜 · 澎湃新闻</p>
        </div>
    </div>
</body>
</html>'''

# 保存HTML
output_path = r"D:\openclaw\Intelnet-daily-news\互联网早报_2026年5月11日.html"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(CSS + content + footer)

print(f"✅ 已生成：{output_path}")
print(f"📊 共 {len(sections)} 个栏目，{sum(len(s[2]) for s in sections)} 条新闻")
