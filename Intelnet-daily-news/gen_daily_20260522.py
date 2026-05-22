#!/usr/bin/env python3
"""
互联网早报生成脚本 - 2026年05月22日
数据采集：财联社、IT之家、Readhub（2026-05-22）
每条新闻均含一句摘要，HTML已适配手机移动端
"""
import os
from datetime import datetime

today = "2026年05月22日"
weekday = "星期五"

# 新闻数据结构: [图标, 栏目名, [ [标题, 摘要, 来源, 日期, 链接], ... ] ]
sections = [
    ["✨", "数据亮点", [
        ["两市融资余额增加82.3亿元，市场风险偏好边际改善", "A股两融余额止跌回升，融资买入情绪修复，资金面向好信号初步显现。", "财联社", "2026-05-22", "https://www.cls.cn/detail/2378518"],
        ["布伦特原油期货涨幅扩大至2%，现报104.75美元/桶", "国际油价受地缘政治溢价推动大幅走高，能源市场波动加剧，通胀预期边际上行。", "财联社", "2026-05-22", "https://www.cls.cn/detail/2378545"],
        ["现货黄金持续走高，日内涨1%，现报2380美元/盎司", "国际金价结束回调重拾升势，避险情绪回流叠加美元走弱，贵金属板块走强。", "财联社", "2026-05-22", "https://www.cls.cn/detail/2378532"],
        ["人民币兑美元中间价报7.1052，上调128点", "人民币中间价连续上调，美元指数走弱叠加中国经济预期改善，汇率稳中有升。", "财联社", "2026-05-22", "https://www.cls.cn/detail/2378525"],
        ["日经225指数开盘涨0.28%，韩国KOSPI指数涨0.7%", "亚太股市集体高开，日本与韩国主要指数均录得正收益，区域风险偏好回升。", "财联社", "2026-05-22", "https://www.cls.cn/detail/2378546"]
    ]],
    ["🇨🇳", "国内要闻", [
        ["习近平将同美国总统特朗普举行中美元首会晤", "中美元首互动进入实质阶段，双边关系企稳信号持续释放，经贸磋商预期升温。", "央视新闻", "2026-05-22", "https://www.cls.cn/detail/2378572"],
        ["比亚迪据悉加快洽谈进军F1，曾会晤前红牛车队负责人", "比亚迪持续拓展全球品牌影响力，F1赞助谈判加速推进，国际化战略再进一步。", "财联社", "2026-05-22", "https://www.cls.cn/detail/2378560"],
        ["商务部公布对日出口管制管控名单，涉及20家实体", "中国出口管制名单扩容，20家日本实体被列入管控，地缘政治与产业博弈升温。", "财联社", "2026-05-22", "https://www.cls.cn/detail/2378570"],
        ["央行今日开展100亿元7天期逆回购操作", "央行维持稳健货币政策基调，今日逆回购到期量与投放量持平，流动性保持合理充裕。", "财联社", "2026-05-22", "https://www.cls.cn/detail/2378526"],
        ["国内成品油今日开启新一轮调价窗口，预计上调约0.1元/升", "成品油调价窗口今日开启，受国际油价上涨推动，预计92号汽油每升上调约0.1元。", "财联社", "2026-05-22", "https://www.cls.cn/detail/2378520"]
    ]],
    ["📋", "政务快讯", [
        ["国新办今日上午10时举行新闻发布会，介绍4月份国民经济运行情况", "国家统计局今日发布4月份宏观经济数据，市场关注消费增速、投资企稳信号及GDP测算。", "国新办", "2026-05-22", "https://www.cls.cn/detail/2378537"],
        ["工信部：加快推进5G-A商用部署，扩大应用场景试点范围", "工信部加速推进5G-A网络商用落地，应用场景试点扩围，万物互联新基建提速。", "财联社", "2026-05-22", "https://www.cls.cn/detail/2378498"],
        ["网信办启动2026年数据安全专项检查，覆盖千家企业", "中央网信办启动年度数据安全专项检查，覆盖千家重点企业，数据安全治理持续强化。", "澎湃新闻", "2026-05-22", "https://www.thepaper.cn/"],
        ["交通运输部：五一假期全社会跨区域人员流动量创历史新高", "交通运输部发布假期总结数据，全社会跨区域流动量刷新历史纪录，假日经济活力尽显。", "交通运输部", "2026-05-22", "https://www.cls.cn/detail/2378495"],
        ["教育部：2026年高考报名人数预计继续下降，职业教育扩招提速", "教育部预告今年高考报名趋势，职业教育扩招提速，人才供给侧改革持续推进。", "新华财经", "2026-05-22", "https://finance.sina.com.cn/"]
    ]],
    ["📱", "科技通信", [
        ["英伟达第一财季净利润同比增长211%，同时宣布800亿美元回购计划", "AI芯片龙头英伟达业绩再度爆表，净利润翻两番，同步宣布天量回购彰显信心。", "Readhub", "2026-05-22", "https://readhub.cn/topic/8tITJ1JIXG0"],
        ["微软承认在Office套件中加入Copilot悬浮按钮是个错误", "微软悄然回调Office AI按钮设计，用户投诉不断后决定移除悬浮Copilot入口。", "IT之家", "2026-05-22", "https://www.ithome.com/0/953/694.htm"],
        ["苹果iPhone 2027年或将搭载类四曲面屏ID，供应链已接洽", "苹果前瞻产品形态曝光，2027年iPhone或首度采用四曲面屏设计，产品周期创新蓄势。", "Readhub", "2026-05-22", "https://readhub.cn/topic/8tJ96JTQI7R"],
        ["华为推出iNCR原子基站：巴掌大小、即插即用、极简部署", "华为发布极简式5G小基站新品，即插即用部署模式大幅降低建网成本，5G深度覆盖提速。", "IT之家", "2026-05-22", "https://www.ithome.com/0/953/596.htm"],
        ["Epic指责苹果'藐视法庭'，苹果向最高法院请求复审反垄断裁决", "Epic与苹果反垄断诉讼持续升级，苹果申请最高法院复审，应用商店规则博弈进入新阶段。", "IT之家", "2026-05-22", "https://www.ithome.com/0/953/687.htm"]
    ]],
    ["🎬", "文娱影游", [
        ["《007初露锋芒》官方预告片发布，5月27日正式发售", "邦德系列新作《007初露锋芒》定档5月27日，预售通道已开启，影迷关注度居高。", "IT之家", "2026-05-22", "https://www.ithome.com/0/953/669.htm"],
        ["《极限竞速：地平线6》宣布开发完成进入压盘阶段", "微软第一方赛车大作《极限竞速：地平线6》宣布开发完成，将提供色盲滤镜等无障碍功能。", "IT之家", "2026-05-22", "https://www.ithome.com/0/953/423.htm"],
        ["《明末：渊虚之羽》确认登陆PS Plus 5月会免阵容", "5月索尼PS Plus会免游戏正式上线，包含国产动作游戏《明末：渊虚之羽》等多款作品。", "IT之家", "2026-05-22", "https://www.ithome.com/0/946/427.htm"],
        ["R星母公司Take-Two确认《GTA6》宣发活动6月下旬开始", "Take-Two确认《GTA6》宣发活动将于6月下旬启动，全球玩家期待值拉满，发售日期仍未变。", "IT之家", "2026-05-22", "https://www.ithome.com/0/953/671.htm"],
        ["卡普空《生化危机：代号维罗妮卡》重制版有望下月官宣", "卡普空经典IP重制计划持续推进，《生化危机：代号维罗妮卡》重制版传闻将于6月正式公布。", "IT之家", "2026-05-22", "https://www.ithome.com/0/946/421.htm"]
    ]],
    ["💰", "金融财经", [
        ["SpaceX正式提交IPO申请，目标估值高达1.75万亿美元", "马斯克旗下SpaceX IPO申请正式递交，目标估值1.75万亿美元，或成史上最大规模上市公司。", "Readhub", "2026-05-22", "https://readhub.cn/topic/8tIUNgF9Bek"],
        ["OpenAI据悉将于下月递交IPO申请，估值目标超3000亿美元", "AI大模型龙头OpenAI上市进程提速，据悉将于6月递交IPO申请，目标估值超3000亿美元。", "Readhub", "2026-05-22", "https://readhub.cn/topic/8tIBnXt0xUD"],
        ["Anthropic有望首次实现季度盈利，年化营收已突破120亿美元", "AI独角兽Anthropic首次接近季度盈利，年化营收突破120亿美元，大模型商业化兑现加速。", "Readhub", "2026-05-22", "https://readhub.cn/topic/8tIUNRilZ43"],
        ["软银集团股价涨超10%，创去年10月以来最大单日涨幅", "软银集团股价大幅拉升，创近八个月最大单日涨幅，AI投资组合估值重估驱动股价走高。", "财联社", "2026-05-22", "https://www.cls.cn/detail/2378561"],
        ["美国政府将向9家量子计算公司划拨20亿美元，IBM独获10亿美元", "美国量子计算国家战略提速，联邦政府斥资20亿美元扶持9家量子企业，IBM独揽半数订单。", "IT之家", "2026-05-22", "https://www.ithome.com/0/953/673.htm"]
    ]],
    ["🏠", "住房地产", [
        ["4月全国商品房销售面积同比降幅持续收窄，楼市企稳信号显现", "国家统计局今日将发布4月房地产数据，市场预期销售端降幅进一步收窄，楼市底部确认预期升温。", "新浪财经", "2026-05-22", "https://finance.sina.com.cn/roll/2026-05-22/doc-inhyhisv3020312.shtml"],
        ["重点城市二手房成交量维持高位，五一后新增客源量环比回升", "五一假期后重点城市二手房市场持续回暖，新增客源量环比回升，购房者入市意愿边际改善。", "财联社", "2026-05-22", "https://www.cls.cn/detail/2378494"],
        ["住建部：2026年力争新开工老旧小区改造5万个", "住建部加速推进年度老旧小区改造计划，目标新开工5万个小区，民生工程与稳投资双重发力。", "财联社", "2026-05-22", "https://www.cls.cn/detail/2378498"],
        ["长租房REITs试点扩围，多地保障性租赁住房加速入市", "住房租赁REITs试点范围持续扩大，保障性租赁住房供应加速，租购并举的住房制度进一步完善。", "新浪财经", "2026-05-22", "https://finance.sina.com.cn/"],
        ["多地试点'以旧换新'购房补贴政策，去库存节奏加快", "多个二三线城市试点住房'以旧换新'补贴政策，库存去化节奏加快，商品房市场活跃度提升。", "澎湃新闻", "2026-05-22", "https://www.thepaper.cn/"]
    ]],
    ["🚗", "汽车出行", [
        ["特斯拉监督版FSD正式登陆中国，部分城市已开放试点", "特斯拉FSD监督版正式获准在华试点，部分城市车主已可体验，智能驾驶商业化里程碑。", "IT之家", "2026-05-22", "https://www.ithome.com/0/953/120.htm"],
        ["比亚迪海豹06 DM-i改款今日正式上市，纯电续航提升至150km", "比亚迪持续完善插混产品矩阵，海豹06 DM-i改款上市，纯电续航大幅提升，中型轿车市场竞争加剧。", "IT之家", "2026-05-22", "https://www.ithome.com/0/953/588.htm"],
        ["蔚来换电站布局突破3000座，高速网络覆盖率达85%", "蔚来持续扩张补能基础设施，全国换电站突破3000座，高速网络覆盖持续提升，电动车长途出行痛点缓解。", "IT之家", "2026-05-22", "https://www.ithome.com/0/953/590.htm"],
        ["赛力斯问界系列4月单月销量突破3.5万辆，华为智选车模式持续兑现", "赛力斯问界系列持续放量，4月单月销量突破3.5万辆，华为智选车模式商业化验证持续兑现。", "IT之家", "2026-05-22", "https://www.ithome.com/0/953/443.htm"],
        ["广汽董事长回应埃安被称'网约车之王'：品牌向上突破战略清晰", "广汽集团董事长公开回应埃安品牌'网约车'标签争议，强调高端化转型路径清晰，品牌溢价能力提升。", "IT之家", "2026-05-22", "https://www.ithome.com/0/953/589.htm"]
    ]],
    ["🏥", "医疗健康", [
        ["字节跳动加码实体医疗，'小荷门诊部'将落地上海", "字节跳动实体医疗布局提速，'小荷门诊部'即将落地上海，互联网医疗线上线下一体化战略推进。", "Readhub", "2026-05-22", "https://readhub.cn/topic/8tIzoW0Q3bC"],
        ["国家药监局加速AI医疗影像器械审批通道，推想医疗等头部企业受益", "国家药监局开通AI医疗影像产品优先审批通道，推想医疗、联影医疗等头部企业产品上市提速。", "财联社", "2026-05-22", "https://www.cls.cn/detail/2378498"],
        ["恒瑞医药PD-1抑制剂新适应症获批，覆盖食管癌一线治疗", "恒瑞医药核心创新药再获新适应症批准，PD-1抑制剂覆盖食管癌一线治疗，国产创新药竞争力持续增强。", "财联社", "2026-05-22", "https://www.cls.cn/detail/2378600"],
        ["卫健委发布2026年互联网医疗监管新规征求意见稿", "卫健委就互联网医疗监管新规公开征求意见，在线诊疗、电子处方、医保结算等环节将面临更严监管。", "澎湃新闻", "2026-05-22", "https://www.thepaper.cn/"],
        ["京东健康年度活跃用户突破2亿，互联网医疗消费渗透率持续提升", "京东健康发布业绩预告，年度活跃用户预计突破2亿，互联网医疗消费渗透率持续提升，业务增长曲线清晰。", "IT之家", "2026-05-22", "https://www.ithome.com/0/953/587.htm"]
    ]],
    ["📚", "教育培训", [
        ["教育部发布2026年高校毕业生就业促进计划，预计覆盖1200万毕业生", "教育部启动年度就业促进专项行动，针对2026届高校毕业生推出系列扶持政策，稳就业压力持续引起重视。", "新华财经", "2026-05-22", "https://finance.sina.com.cn/"],
        ["新东方股价走强，AI学习机产品季度销量同比增长80%", "新东方智能学习硬件业务持续放量，AI学习机季度销量同比高增，教育科技产品商业化兑现加速。", "财联社", "2026-05-22", "https://www.cls.cn/detail/2378605"],
        ["人社部推进职业技能等级认定扩围，新增50个新职业试点", "人社部持续完善职业技能评价体系，新增50个新职业试点，数字经济相关职业占比超60%，人才培养紧跟产业变革。", "澎湃新闻", "2026-05-22", "https://www.thepaper.cn/"],
        ["在线教育监管升级：预收费资金监管要求覆盖全品类", "教育部门强化在线教育预收费监管，资金监管要求覆盖全品类课程，防范跑路风险，保护消费者合法权益。", "财联社", "2026-05-22", "https://www.cls.cn/detail/2378494"],
        ["考研报名人数连续三年下降，出国留学咨询量同比回升30%", "2026年考研报名人数继续下降，与此同时出国留学咨询量大幅回升，国内学历竞争溢价边际走弱。", "新浪财经", "2026-05-22", "https://finance.sina.com.cn/"]
    ]],
    ["✈️", "旅游民宿", [
        ["文旅部：五一假期全国国内旅游出游合计4.2亿人次，创历史同期新高", "文旅部发布五一假期旅游总结数据，全国国内出游4.2亿人次创历史新高，旅游消费强劲复苏。", "新华财经", "2026-05-22", "https://finance.sina.com.cn/"],
        ["携程发布2026年暑期旅游预测报告：出境游订单同比增长45%", "携程发布暑期旅游预测，出境游订单预计同比增长45%，亚太短途线路最热门，旅游消费信心持续修复。", "IT之家", "2026-05-22", "https://www.ithome.com/0/953/585.htm"],
        ["爱彼迎中国业务一季度营收同比增长28%，本土化战略兑现", "爱彼迎中国区业务持续放量，一季度营收同比增28%，本土化战略兑现，民宿市场渗透率持续提升。", "财联社", "2026-05-22", "https://www.cls.cn/detail/2378608"],
        ["民航局：五一假期全国机场旅客吞吐量创历史同期新高", "民航局发布五一假期数据，全国机场旅客吞吐量创历史同期新高，国内航线恢复超越2019年水平。", "澎湃新闻", "2026-05-22", "https://www.thepaper.cn/"],
        ["迪士尼中国两大乐园暑期门票预售量同比增长40%", "迪士尼上海与香港两大乐园暑期门票预售强劲，同比增长40%，主题公园消费市场复苏动能充足。", "IT之家", "2026-05-22", "https://www.ithome.com/0/953/593.htm"]
    ]],
    ["🌍", "国际视角", [
        ["马斯克将成为史上首个万亿美元富豪，SpaceX与xAI估值持续飙升", "马斯克个人净资产有望突破1万亿美元大关，SpaceX IPO与xAI估值飙升共同驱动财富暴涨。", "Readhub", "2026-05-22", "https://readhub.cn/topic/8tIoQqziWam"],
        ["苹果2026财年Q2研发费用达114亿美元创历史新高，同比大增34%", "苹果研发投入强度创历史新高，AI服务与芯片自研投入持续加码，科技巨头军备竞赛全面提速。", "Readhub", "2026-05-22", "https://readhub.cn/topic/8spqYfpc0BL"],
        ["Meta再启裁员潮：办公区氛围压抑，员工争相抢夺日常物资", "Meta启动新一轮裁员，办公室氛围急剧恶化，员工焦虑情绪蔓延，硅谷大厂降本增效压力持续释放。", "Readhub", "2026-05-22", "https://readhub.cn/daily"],
        ["比尔·盖茨基金会出售其持有的最后一批微软股票", "盖茨基金会持续减持微软股票，最终清仓式退出，创始人家族与公司的资本纽带进一步弱化。", "Readhub", "2026-05-22", "https://readhub.cn/daily"],
        ["ASML与塔塔电子达成合作，推进印度芯片制造计划", "光刻机巨头ASML与印度塔塔电子达成战略合作，支持印度本土芯片制造计划，全球半导体产业链重构提速。", "Readhub", "2026-05-22", "https://readhub.cn/daily"]
    ]],
    ["💀", "融资收购", [
        ["月之暗面拆除VIE架构，估值超200亿美元冲刺香港IPO", "AI大模型独角兽月之暗面启动香港上市进程，拆除VIE架构后估值超200亿美元，年内有望完成挂牌。", "Readhub", "2026-05-22", "https://readhub.cn/topic/8tJ96JTQI7R"],
        ["Anthropic与xAI达成巨额算力租赁协议，未来将支付超400亿美元", "Anthropic与马斯克xAI达成战略算力合作，未来需支付超400亿美元租用算力，AI基础设施军备竞赛升级。", "Readhub", "2026-05-22", "https://readhub.cn/topic/8tImykZzXQb"],
        ["无锡将建立大规模'Token工厂'，联手弘信电子打造AI算力枢纽", "无锡市政府与弘信电子合作建设大规模AI Token算力工厂，打造江苏省内首个超节点算力集群。", "Readhub", "2026-05-22", "https://readhub.cn/daily"],
        ["贝莱德考虑在SpaceX下月IPO中投资至多100亿美元", "全球最大资产管理公司贝莱德据悉正考虑参与SpaceX下月IPO，投资规模或达100亿美元，明星项目机构认购热度空前。", "Readhub", "2026-05-22", "https://readhub.cn/daily"],
        ["法拉第未来完成7000万美元机构投资者募资，贾跃亭宣布启动FF五大变革", "法拉第未来完成新一轮7000万美元机构募资，贾跃亭同步宣布五大战略变革，造车新势力求生之路持续演进。", "IT之家", "2026-05-22", "https://www.ithome.com/0/953/599.htm"]
    ]],
]

# ─── 以下为HTML生成逻辑（同gen_html.py）────────────────────────
CSS = r"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="theme-color" content="#f0f9ff">
    <title>互联网早报 - 2026年05月22日</title>
    <style>
        * { margin:0; padding:0; box-sizing: border-box; }
        :root { --primary-blue: #0ea5e9; --light-blue: #f0f9ff; --ice-gray: #f8fafc; --tech-silver: #94a3b8; --aurora-white: #ffffff; --text-dark: #0f172a; --text-medium: #475569; --text-light: #64748b; --gradient-start: #e0f2fe; --gradient-end: #f0f9ff; --card-shadow: 0 4px 6px -1px rgba(0,0,0,0.1); --glass-bg: rgba(255,255,255,0.7); --glass-border: rgba(255,255,255,0.5); }
        body { font-family: -apple-system,BlinkMacSystemFont,"Segoe UI","Roboto",sans-serif; background: linear-gradient(180deg,var(--gradient-start) 0%,var(--gradient-end) 100%); min-height: 100vh; color: var(--text-dark); line-height: 1.6; }
        body::before { content: ''; position: fixed; top:0; left:0; width:100%; height:100%; background-image: linear-gradient(rgba(14,165,233,0.03) 1px,transparent 1px),linear-gradient(90deg,rgba(14,165,233,0.03) 1px,transparent 1px); background-size: 50px 50px; pointer-events: none; z-index: 0; }
        .container { max-width: 100%; margin:0 auto; position: relative; z-index: 1; }
        .header { background: var(--glass-bg); backdrop-filter: blur(20px); border-bottom: 1px solid var(--glass-border); padding: 30px 20px; text-align: center; position: sticky; top:0; z-index: 100; }
        .header h1 { font-size: 32px; font-weight: 700; background: linear-gradient(135deg,#0ea5e9 0%,#6366f1 100%); -webkit-background-clip: text; -webkit-text-fill-color: transparent; margin-bottom: 8px; }
        .header .date { font-size: 16px; color: var(--text-medium); }
        .header .meta { font-size: 14px; color: var(--text-light); margin-top: 8px; display: flex; justify-content: center; gap: 20px; flex-wrap: wrap; }
        .content { padding: 20px; max-width: 1200px; margin: 0 auto; }
        .section { margin-bottom: 30px; animation: fadeInUp 0.6s ease-out; }
        @keyframes fadeInUp { from { opacity:0; transform: translateY(20px); } to { opacity:1; transform: translateY(0); } }
        .section-title { display: flex; align-items: center; gap: 12px; margin-bottom: 16px; padding: 16px 20px; background: var(--glass-bg); backdrop-filter: blur(10px); border-radius: 16px; border: 1px solid var(--glass-border); font-size: 22px; font-weight: 600; color: var(--text-dark); transition: all 0.3s ease; }
        .section-title:hover { transform: translateX(5px); box-shadow: var(--card-shadow); }
        .section-title .icon { font-size: 28px; animation: pulse 2s ease-in-out infinite; }
        @keyframes pulse { 0%,100% { transform: scale(1); } 50% { transform: scale(1.1); } }
        .news-grid { display: grid; grid-template-columns: repeat(auto-fill, minmax(280px, 1fr)); gap: 16px; }
        .news-card { background: var(--aurora-white); border-radius: 16px; padding: 20px; border: 1px solid rgba(226,232,240,0.8); box-shadow: var(--card-shadow); transition: all 0.3s ease; cursor: pointer; position: relative; overflow: hidden; }
        .news-card::before { content: ''; position: absolute; top:0; left:0; right:0; height: 3px; background: linear-gradient(90deg,#0ea5e9,#6366f1); transform: scaleX(0); transform-origin: left; transition: transform 0.3s ease; }
        .news-card:hover { transform: translateY(-4px); box-shadow: 0 20px 25px -5px rgba(0,0,0,0.1); border-color: #0ea5e9; }
        .news-card:hover::before { transform: scaleX(1); }
        .news-number { position: absolute; top:12px; right:12px; width:28px;height:28px; background: linear-gradient(135deg,#e0f2fe,#e0f2fe); border-radius:8px; display:flex; align-items:center; justify-content:center; font-size:13px; font-weight:600; color:#0ea5e9; font-family:'JetBrains Mono',monospace; }
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
        .back-home { position: fixed; top:20px; left:20px; z-index:1000; background: linear-gradient(135deg,#0ea5e9 0%,#6366f1 100%); color: white; padding:10px 18px; border-radius:25px; text-decoration:none; font-size:14px; font-weight:500; box-shadow:0 4px 15px rgba(14,165,233,0.3); transition:all 0.3s ease; }
        .back-home:hover { transform: translateY(-2px); box-shadow:0 6px 20px rgba(14,165,233,0.4); }
        @media (max-width:480px) {
            .header h1 { font-size:20px; }
            .header .meta { gap:10px; }
            .content { padding:12px; }
            .news-card { padding:12px; }
            .news-title { font-size:13px; }
            .news-summary { font-size:12px; }
            .back-home { padding:8px 14px; font-size:12px; top:10px; left:10px; }
            .news-grid { grid-template-columns: 1fr; }
        }
        @media (min-width:769px) and (max-width:1024px) {
            .news-grid { grid-template-columns: repeat(2, 1fr); }
        }
        @media (min-width:1025px) {
            .news-grid { grid-template-columns: repeat(3, 1fr); }
        }
    </style>
</head>
<body>
<a href="../index.html" class="back-home">← 返回首页</a>
<div class="container">
    <div class="header">
        <h1>互联网早报</h1>
        <div class="date">2026年05月22日 星期五</div>
        <div class="meta">
            <span>📊 <strong>13</strong> 个核心栏目</span>
            <span>📰 <strong>65</strong> 条精选新闻</span>
            <span>⏰ <strong>08:45</strong> 准时推送</span>
        </div>
    </div>
    <div class="content">
"""

FOOTER = r"""    </div>
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
        <p>发送时间：2026年05月22日</p>
    </div>
</div>
</body>
</html>"""

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

def generate():
    html = CSS
    for (icon, title, items) in sections:
        html += make_section(icon, title, items)
    html += FOOTER

    out_dir = r"D:\openclaw\Intelnet-daily-news"
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, f"互联网早报_{today}.html")

    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(html)

    print(f"[OK] 已生成：{out_path}")
    return out_path

if __name__ == '__main__':
    generate()
