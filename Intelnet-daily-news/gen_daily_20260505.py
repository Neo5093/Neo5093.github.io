import json
import os
from datetime import datetime

# 今天是2026年5月5日，星期二
today = "2026年5月5日"
weekday = "星期二"

# 新闻数据结构: [图标, 栏目名, [ [标题, 摘要, 来源, 日期, 链接], ... ] ]
sections = [
    ["✨", "数据亮点", [
        ["余额宝七日年化收益率首次跌破1%", "天弘余额宝货币基金7日年化收益率首次跌破1%关口，创下历史新低，货币基金收益率持续下行引发市场关注。", "IT之家", "2026-05-05", "https://www.ithome.com/0/946/431.htm"],
        ["金饰价格跌破1400元，黄金创史上最大双月跌幅", "国际金价单日重挫超100美元，国内金饰价格跌破1400元/克，黄金创历史最大双月跌幅，避险情绪降温。", "腾讯新闻", "2026-05-05", "https://view.inews.qq.com/a/20260505A02WK600"],
        ["五一假期上海线上线下消费增长7.7%", "五一假期上海消费市场活力十足，线上线下消费同比增长7.7%，假日经济持续释放增长潜力。", "财联社", "2026-05-05", "https://www.cls.cn/detail/2363028"],
        ["美国关键国债收益率突破5%", "美国关键期限国债收益率突破5%关口，创下近年新高，市场对美联储维持高利率预期持续升温。", "财联社", "2026-05-05", "https://www.cls.cn/detail/2363050"],
        ["赛力斯4月新能源汽车销量33132辆，同比增长5.22%", "赛力斯公布4月产销数据，新能源汽车销量保持增长态势，问界系列持续贡献主要销量。", "IT之家", "2026-05-05", "https://www.ithome.com/0/946/443.htm"]
    ]],
    ["🇨🇳", "国内要闻", [
        ["习近平对湖南浏阳烟花厂爆炸事故作出重要指示", "湖南长沙浏阳市一烟花厂发生爆炸事故，已致26死61伤，习近平作出重要指示要求全力救援救治。", "新闻联播", "2026-05-05", "https://tv.cctv.com/2026/05/05/VIDEYJnXJGFqKKCc5qSxHnCL260505.shtml"],
        ["五一假期全社会跨区域人员流动量预计超15亿人次", "2026年五一假期全国跨区域人员流动量预计超15亿人次，铁路、公路、民航客流均创新高。", "新华财经", "2026-05-05", "https://tv.cctv.com/2026/05/05/VIDEL6kuYyrOAQd8VQmtfjkC260505.shtml"],
        ["豆包将新增付费订阅服务", "豆包App Store页面出现付费版本声明，将推出标准版68元/月、加强版200元/月、专业版500元/月三档订阅。", "Readhub", "2026-05-05", "https://readhub.cn/topic/8sqkjdKrUsF"],
        ["红果回应VIP付费争议：非新增，仅限极少量影视", "红果短剧回应VIP付费热搜，称按版权方要求仅少量影视需VIP，此规则自平台上线就有，短剧仍免费。", "Readhub", "2026-05-05", "https://readhub.cn/topic/8spdLLEidkV"],
        ["追觅俞浩拟对168个社交平台账号进行起诉", "追觅创始人俞浩发文称网络出现不实信息，已向小红书、微信公众号等平台及168个涉嫌侵权账号发起诉讼。", "Readhub", "2026-05-05", "https://readhub.cn/topic/8sqsBIFSEwp"]
    ]],
    ["📋", "政务快讯", [
        ["5月5日周二《新闻联播》要闻22条", "本期新闻联播涵盖习近平重要指示、美伊局势、五一假期消费、国际局势等22条重要要闻。", "财联社", "2026-05-05", "https://www.cls.cn/detail/2363027"],
        ["湖南浏阳烟花厂爆炸已致26死61伤", "湖南浏阳一烟花厂发生爆炸事故，截至发稿已造成26人死亡、61人受伤，救援工作仍在进行中。", "腾讯新闻", "2026-05-05", "https://view.inews.qq.com/a/20260505A03VNQ00"],
        ["普京决定5月8日至9日停火", "俄罗斯总统普京宣布5月8日至9日实施临时停火，纪念卫国战争胜利日，俄乌冲突再现缓和窗口。", "新浪财经", "2026-05-05", "https://wap.cj.sina.cn/pc/7x24/4860025"],
        ["俄乌先后宣布临时停火", "俄乌双方先后宣布临时停火决定，国际社会关注后续和平谈判进展及停火协议执行情况。", "腾讯新闻", "2026-05-05", "https://view.inews.qq.com/a/20260505A028ZS00"],
        ["今日立夏，全国大部地区天气晴好", "5月5日迎来立夏节气，全国大部分地区天气晴好，气温逐步回升，南方部分地区有分散性降雨。", "新民早报", "2026-05-05", "https://www.shobserver.com/staticsg/res/html/web/newsDetail.html?id=1107370&sid=11"]
    ]],
    ["📱", "科技通信", [
        ["苹果研发投入破历史纪录：单季同比大增34%", "苹果2026财年Q2研发费用达114亿美元，同比增长34%创历史新高，新增资金聚焦AI智能服务研发。", "Readhub", "2026-05-05", "https://readhub.cn/topic/8spqYfpc0BL"],
        ["消息称特斯拉FSD欧洲审批遇阻，监管机构质疑安全性", "特斯拉FSD自动驾驶系统在欧洲面临审批障碍，监管机构质疑其安全性与命名是否存在误导消费者嫌疑。", "IT之家", "2026-05-05", "https://www.ithome.com/0/946/464.htm"],
        ["三星重新在美推出Galaxy Z Flip 7 FE，定价899美元起", "三星重新在美国市场推出Galaxy Z Flip 7 FE小折叠手机，定价维持899美元起，折叠屏市场竞争加剧。", "IT之家", "2026-05-05", "https://www.ithome.com/0/946/460.htm"],
        ["微软优化Win11小组件：默认关闭MSN资讯流", "微软对Windows 11小组件进行优化，默认关闭MSN资讯流推送，减少用户干扰，提升使用体验。", "IT之家", "2026-05-05", "https://www.ithome.com/0/946/453.htm"],
        ["光刻胶企业JSR首次在中国台湾地区设半导体材料生产基地", "日本光刻胶巨头JSR首次在中国台湾设立半导体材料生产基地，预计最早2028年投产，强化供应链布局。", "IT之家", "2026-05-05", "https://www.ithome.com/0/946/424.htm"]
    ]],
    ["🎬", "文娱影游", [
        ["吴宜泽绝杀墨菲登顶世锦赛，36年来最年轻冠军", "中国选手吴宜泽在斯诺克世锦赛决赛绝杀墨菲夺冠，成为36年来最年轻的世锦赛冠军，中国军团蝉联梦想成真。", "腾讯新闻", "2026-05-05", "https://view.inews.qq.com/a/20260505A01V4P00"],
        ["《极限竞速：地平线6》官宣开发完成已送厂压盘", "微软《极限竞速：地平线6》官宣开发完成并已送厂压盘，游戏将提供色盲滤镜、屏幕朗读等无障碍功能。", "IT之家", "2026-05-05", "https://www.ithome.com/0/946/423.htm"],
        ["5月索尼PS Plus会免游戏上线", "2026年5月PS Plus会免游戏正式上线，包含《明末：渊虚之羽》《EA Sports FC 26》等多款大作。", "IT之家", "2026-05-05", "https://www.ithome.com/0/946/427.htm"],
        ["消息称卡普空《生化危机：代号维罗妮卡》重制版有望下月官宣", "卡普空经典恐怖游戏《生化危机：代号维罗妮卡》重制版有望于下月正式官宣，粉丝期待值拉满。", "IT之家", "2026-05-05", "https://www.ithome.com/0/946/421.htm"],
        ["Take-Two CEO确认《GTA6》首发无缘PC平台", "Take-Two CEO确认《GTA6》首发将仅登陆主机平台，PC版本预计将在后续推出，主机玩家为核心受众。", "IT之家", "2026-05-05", "https://www.ithome.com/0/946/417.htm"]
    ]],
    ["💰", "金融财经", [
        ["PayPal盘前跌幅扩大至10%", "PayPal盘前交易跌幅扩大至10%，公司业绩指引不及预期引发市场担忧，支付巨头面临增长压力。", "财联社", "2026-05-05", "https://www.cls.cn/detail/2363048"],
        ["谷歌母公司Alphabet将筹集至少90亿欧元", "Alphabet正式启动加拿大元债券发售，将筹集至少90亿欧元，用于一般企业用途和债务再融资。", "财联社", "2026-05-05", "https://www.cls.cn/detail/2363025"],
        ["套现约455亿，李嘉诚又卖了", "李嘉诚旗下公司再次大手笔套现，此次出售资产获利约455亿港元，持续优化全球资产配置。", "腾讯新闻", "2026-05-05", "https://view.inews.qq.com/a/20260505A05J3Z00"],
        ["Coinbase宣布裁员14%，CEO称AI正改变公司运营模式", "数字货币交易平台Coinbase宣布裁员14%，CEO表示AI正在深刻改变公司运营方式和人员需求结构。", "IT之家", "2026-05-05", "https://www.ithome.com/0/946/459.htm"],
        ["美国3月国际贸易逆差为603亿美元", "美国3月国际贸易逆差扩大至603亿美元，进出口数据均出现波动，贸易平衡面临持续挑战。", "财联社", "2026-05-05", "https://www.cls.cn/detail/2363040"]
    ]],
    ["🏠", "住房地产", [
        ["五一外围股市分化，港股恒生科技指数冲高回落", "五一假期全球主要资本市场走势分化，港股恒生科技指数受算力热潮共振，冲高突破5000点后回落。", "每日经济新闻", "2026-05-05", "https://www.nbd.com.cn/articles/2026-05-05/4379123.html"],
        ["美国3月建筑许可终值环比下降11.4%", "美国3月建筑许可终值环比下降11.4%，房地产市场降温迹象明显，新建住宅开工活动持续放缓。", "财联社", "2026-05-05", "https://www.cls.cn/detail/2363049"],
        ["五一假期景区交易笔数环比大涨277%", "微信支付发布五一假期数据报告，景区交易笔数环比大涨277%，港澳游受欢迎，消费复苏势头强劲。", "IT之家", "2026-05-05", "https://www.ithome.com/0/946/436.htm"],
        ["美国关键国债收益率突破5%", "美国关键期限国债收益率突破5%关口，房贷利率随之攀升，对房地产市场构成进一步压力。", "财联社", "2026-05-05", "https://www.cls.cn/detail/2363050"],
        ["世界最高无轴摩天轮上海之门计划年底开建", "上海计划年底开建世界最高无轴摩天轮「上海之门」，将超越潍坊渤海之眼成为新的世界级旅游地标。", "IT之家", "2026-05-05", "https://www.ithome.com/0/946/266.htm"]
    ]],
    ["🚗", "汽车出行", [
        ["小米首款增程全尺寸SUV「昆仑N3」低伪装路试谍照曝光", "小米昆仑N3低伪装谍照曝光，前大灯组造型锐利、车头可见激光雷达凸起，定位全尺寸增程SUV。", "IT之家", "2026-05-05", "https://www.ithome.com/0/946/462.htm"],
        ["特斯拉奥斯汀Robotaxi开启夜间无安全员运营", "特斯拉在奥斯汀正式开启Robotaxi夜间无安全员运营，自动驾驶商业化迈出重要一步。", "IT之家", "2026-05-05", "https://www.ithome.com/0/946/432.htm"],
        ["新一代小米SU7汽车首销期今日截止", "新一代小米SU7首销期5月5日截止，最高送6.9万元权益，市场关注首销期过后的订单持续性。", "IT之家", "2026-05-05", "https://www.ithome.com/0/946/430.htm"],
        ["本田电动化豪赌失利，多款热门车型换代延期至2030年后", "本田电动化战略受挫，多款热门车型换代计划延期至2030年后，传统车企转型电动化面临挑战。", "IT之家", "2026-05-05", "https://www.ithome.com/0/946/435.htm"],
        ["大众汽车面临15亿欧元巨额罚款", "大众汽车因难以达成碳排放目标，面临欧盟15亿欧元巨额罚款，电动化转型压力进一步加大。", "IT之家", "2026-05-05", "https://www.ithome.com/0/946/438.htm"]
    ]],
    ["🏥", "医疗健康", [
        ["湖南浏阳烟花厂爆炸已致26死61伤", "湖南浏阳一烟花厂发生爆炸事故，造成重大人员伤亡，当地已启动应急响应全力救治伤员。", "腾讯新闻", "2026-05-05", "https://view.inews.qq.com/a/20260505A03VNQ00"],
        ["RingConn Gen 3智能戒指发布：支持夜间血压实时追踪", "RingConn发布第三代智能戒指，新增夜间血压实时追踪功能，售价2599元，健康监测再升级。", "IT之家", "2026-05-05", "https://www.ithome.com/0/946/437.htm"],
        ["美光CEO称AI仍处于早期阶段，存储供应持续吃紧", "美光CEO表示AI浪潮处于早期阶段，推理端迎来拐点，DRAM和NAND闪存供应持续紧张。", "Readhub", "2026-05-05", "https://readhub.cn/topic/8sqsBIFSEwp"],
        [" quantum计算机联手超级计算机，创下大分子模拟新纪录", "量子计算机与超级计算机联合运算，在大分子模拟领域创下新纪录，量子计算实用化迈出重要一步。", "IT之家", "2026-05-05", "https://www.ithome.com/0/946/429.htm"],
        ["大连至青岛340公里无人机物流航线通航", "国内首条跨渤海无人机物流航线正式通航，大连至青岛340公里仅需2小时，低空经济商业化提速。", "IT之家", "2026-05-05", "https://www.ithome.com/0/946/250.htm"]
    ]],
    ["📚", "教育培训", [
        ["钉钉陈航：AI招聘看AIQ，学历经历年龄不再重要", "钉钉创始人陈航提出AI时代人才评价新观点，AI Quotient将成为招聘核心指标，传统学历权重下降。", "IT之家", "2026-05-05", "https://www.ithome.com/0/946/359.htm"],
        ["英伟达黄仁勋痛批Anthropic阿莫迪，呼吁AI领袖慎言慎行", "黄仁勋反驳Anthropic CEO关于AI将取代50%入门白领的言论，呼吁AI行业领袖以事实为据、慎言慎行。", "Readhub", "2026-05-05", "https://readhub.cn/topic/8sqsBIFSEwp"],
        ["中国科学家揭示惯用手不是天生的", "最新研究发现惯用手并非天生，而是后天训练形成，为教育和训练方式提供新思路和新依据。", "知乎日报", "2026-05-05", "https://tophub.today/daily"],
        ["OpenRouter发布大模型调用量排行榜，混元Hy3登顶", "腾讯混元新模型Hy3 preview在全球大模型API调用量总榜和工具调用场景均排名第一。", "Readhub", "2026-05-05", "https://readhub.cn/topic/8sqsBIFSEwp"],
        ["马斯克寻求就OpenAI诉讼达成和解", "马斯克在开庭前两天联系OpenAI联合创始人商讨和解，寻求领导层变更及1500亿美元损害赔偿。", "Readhub", "2026-05-05", "https://readhub.cn/topic/8srGSpTqKN1"]
    ]],
    ["✈️", "旅游民宿", [
        ["五一假期景区交易笔数环比大涨277%", "微信支付发布五一数据报告，景区交易笔数环比大涨277%，港澳游受欢迎，文旅消费强劲复苏。", "IT之家", "2026-05-05", "https://www.ithome.com/0/946/436.htm"],
        ["五一假期全社会跨区域人员流动量预计超15亿人次", "2026年五一假期全国跨区域人员流动量预计超15亿人次，铁路、公路、民航客流均创同期新高。", "新华财经", "2026-05-05", "https://tv.cctv.com/2026/05/05/VIDEL6kuYyrOAQd8VQmtfjkC260505.shtml"],
        ["世界最高无轴摩天轮上海之门计划年底开建", "上海计划年底开建世界最高无轴摩天轮，将超越潍坊渤海之眼，成为世界级旅游新地标。", "IT之家", "2026-05-05", "https://www.ithome.com/0/946/266.htm"],
        ["五一假期酒店预订维权成热点", "五一假期酒店预订「30分钟后不可取消」被指霸王条款，消费者维权问题引发社会广泛关注。", "澎湃新闻", "2026-05-05", "https://www.thepaper.cn/"],
        ["北京5月1日起禁飞禁售无人机，大疆门店下架相关产品", "北京全域禁飞禁售无人机新规落地，大疆北京所有门店启动产品下架流程，低空管理趋严。", "Readhub", "2026-05-05", "https://readhub.cn/topic/8sqsBIFSEwp"]
    ]],
    ["🌍", "国际视角", [
        ["特朗普称美国与伊朗处于「迷你战争」状态", "特朗普公开称美国与伊朗处于「迷你战争」状态，霍尔木兹海峡局势持续紧张，国际油价剧烈波动。", "腾讯新闻", "2026-05-05", "https://view.inews.qq.com/a/20260505A01RQR00"],
        ["美称在霍尔木兹海峡击沉6艘伊朗小型船只", "美方称在霍尔木兹海峡击沉6艘伊朗小型船只，伊朗称美「疏导」行动将酿僵局，中东局势升级。", "新闻联播", "2026-05-05", "https://tv.cctv.com/2026/05/05/VIDE3mFSl2MxMbItaIkeppRx260505.shtml"],
        ["美称将推进对欧盟汽车加征关税计划", "美国称将推进对欧盟汽车加征关税计划，欧方称美方有政治目的将予以反制，贸易摩擦再起。", "新闻联播", "2026-05-05", "https://tv.cctv.com/2026/05/05/VIDEwhtb6JrWaG3rnFHKgJpv260505.shtml"],
        ["美以协调或准备对伊朗发动新一轮打击", "美以双方正在协调，或准备对伊朗发动新一轮军事打击，中东地区紧张局势面临进一步升级风险。", "财联社", "2026-05-05", "https://www.cls.cn/detail/2363051"],
        ["57国齐聚哥伦比亚聊退煤，主要化石能源消费国未参会", "57国在哥伦比亚召开退煤会议，但中美等主要化石能源消费国未参会，会议成效和执行力受质疑。", "澎湃新闻", "2026-05-05", "https://www.thepaper.cn/"]
    ]],
    ["🚀", "融资收购", [
        ["OpenAI与私募巨头敲定100亿美元合资协议", "OpenAI为新合资企业「The Deployment Company」筹集超40亿美元，获19位投资者支持。", "Readhub", "2026-05-05", "https://readhub.cn/topic/8srMBf0uKvM"],
        ["Anthropic接近与黑石、高盛等达成15亿美元合资协议", "Anthropic接近与黑石、高盛等达成15亿美元合资协议，各方投资约3亿美元，AI投资热潮持续。", "Readhub", "2026-05-05", "https://readhub.cn/topic/8sqsBIFSEwp"],
        ["AI芯片制造商Cerebras拟IPO集资40亿美元，估值达400亿美元", "Cerebras Systems拟IPO最多筹集40亿美元，估值目标约400亿美元，承销银行已收到超100亿美元认购意向。", "Readhub", "2026-05-05", "https://readhub.cn/topic/8sql1Dx8QJ4"],
        ["eBay确认收到GameStop主动发起的收购要约", "eBay确认收到GameStop主动提出的不具约束力收购提议，eBay董事会将审慎评估该提议。", "Readhub", "2026-05-05", "https://readhub.cn/topic/8srKk7cN7ho"],
        ["台积电或重启龙潭晶圆厂建设计划，投资达190亿美元", "台积电可能重启龙潭晶圆厂计划，预期导入次世代埃米级制程，预计带动约190亿美元投资。", "Readhub", "2026-05-05", "https://readhub.cn/topic/8sqdXPMboMK"]
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
output_path = r"D:\openclaw\Intelnet-daily-news\互联网早报_2026年5月5日.html"
with open(output_path, "w", encoding="utf-8") as f:
    f.write(CSS + content + footer)

print(f"✅ 已生成：{output_path}")
print(f"📊 共 {len(sections)} 个栏目，{sum(len(s[2]) for s in sections)} 条新闻")
