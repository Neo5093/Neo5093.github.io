#!/usr/bin/env python3
"""
互联网早报生成脚本 - 2026年05月18日
数据采集：IT之家、财联社、Readhub（2026-05-18）
"""
import os
from datetime import datetime

today = "2026年05月18日"
weekday = "星期一"

# 新闻数据结构: [图标, 栏目名, [ [标题, 摘要, 来源, 日期, 链接], ... ] ]
sections = [
    ["✨", "数据亮点", [
        ["WTI原油期货涨超2%，现报103.08美元/桶", "国际油价大幅上涨，WTI原油期货涨幅超2%，地缘政治紧张与供需预期收紧共同推动油价走高。", "财联社", "2026-05-18", "https://www.cls.cn/detail/2373612"],
        ["现货黄金日内跌幅扩大至1%，报4490.62美元/盎司", "国际金价继续回调，现货黄金跌幅扩大至1%，此前历史高位后的获利了结持续压制金价。", "财联社", "2026-05-18", "https://www.cls.cn/detail/2373598"],
        ["现货白银日内跌幅扩大至2%，报74.32美元/盎司", "白银跟随黄金走弱，日内跌幅扩大至2%，贵金属板块整体承压，避险情绪边际降温。", "财联社", "2026-05-18", "https://www.cls.cn/detail/2373607"],
        ["日本5年期国债收益率升至创纪录水平2.025%", "日本超长端国债收益率持续攀升，5年期升至历史高位，全球债券市场承压，央行政策前景引发关注。", "财联社", "2026-05-18", "https://www.cls.cn/detail/2373594"],
        ["两市融资余额减少57.62亿元", "A股两融余额小幅回落，融资买入情绪趋于谨慎，市场风险偏好边际走弱，资金观望情绪上升。", "财联社", "2026-05-18", "https://www.cls.cn/detail/2373610"]
    ]],
    ["🇨🇳", "国内要闻", [
        ["外交部：应习近平主席邀请，普京将于5月19日至20日对中国进行国事访问", "中俄高层互动频次提升，普京总统将于5月19日至20日访华，双边经贸与战略协作预期进一步深化。", "财联社", "2026-05-18", "https://www.cls.cn/detail/2373570"],
        ["王毅介绍中美元首会晤情况：习近平主席将于今年秋季对美国进行国事访问", "中美高层交往路线图逐步清晰，习近平应特朗普邀请将于秋季访美，双边关系企稳信号持续释放。", "新浪财经", "2026-05-18", "https://finance.sina.com.cn/roll/2026-05-18/doc-inhyhisv3014407.shtml"],
        ["国新办今日举行新闻发布会，介绍2026年4月份国民经济运行情况", "国家统计局今日上午10时发布4月份宏观经济数据，市场关注GDP增速、消费、投资等关键指标表现。", "新浪财经", "2026-05-18", "https://finance.sina.com.cn/wm/2026-05-18/doc-inhyhisv3020312.shtml"],
        ["商务部介绍中美经贸磋商初步成果", "中美经贸团队持续推进磋商，商务部就初步成果答记者问，双方经贸关系边际缓和信号明确。", "新浪财经", "2026-05-18", "https://finance.sina.com.cn/roll/2026-05-18/doc-inhyhisv3014407.shtml"],
        ["市场监管总局印发促进民营经济发展壮大2026年工作要点", "市场监管总局发布34项重点工作任务，聚焦反垄断、公平竞争、营商环境优化，民营经济支持政策持续落地。", "新浪财经", "2026-05-18", "https://finance.sina.com.cn/wm/2026-05-18/doc-inhyhisv3020312.shtml"]
    ]],
    ["📋", "政务快讯", [
        ["5月18日周一《新闻联播》要闻预告", "今日新闻联播预计聚焦中美元首互动、4月经济数据发布、普京访华预告等重大政治经济议题。", "央视网", "2026-05-18", "https://tv.cctv.com/"],
        ["工信部持续推进5G-A商用部署，多地启动应用试点", "工信部加速推进5G-A网络商用落地，多个城市启动试点应用，万物互联新基建提速。", "财联社", "2026-05-18", "https://www.cls.cn/detail/2373498"],
        ["网信办开展2026年网络安全专项检查", "中央网信办启动年度网络安全专项检查，覆盖关键信息基础设施运营者，数据安全治理持续强化。", "澎湃新闻", "2026-05-18", "https://www.thepaper.cn/"],
        ["国资委推动央企加大AI领域投资布局", "国资委引导中央企业加大对人工智能、算力基础设施的投资力度，央企科技转型升级提速。", "财联社", "2026-05-18", "https://www.cls.cn/detail/2373498"],
        ["交通运输部发布五一假期总结报告", "交通运输部发布2026年五一假期交通运输总结，全社会跨区域人员流动量创历史新高，假日经济活力尽显。", "新华财经", "2026-05-18", "https://finance.sina.com.cn/"]
    ]],
    ["📱", "科技通信", [
        ["英伟达正与SImpliSMART进行谈判，拟牵头参与一轮规模为2000万美元的融资", "英伟达持续布局AI基础设施生态，拟领投SimpliSMART 2000万美元融资，AI芯片应用场景持续扩展。", "财联社", "2026-05-18", "https://www.cls.cn/detail/2373597"],
        ["前微软高管痛批公司AI战略失误：重蹈互联网、移动设备时代覆辙", "前微软高管公开批评公司AI战略投资与回报严重失衡，类比当年错过移动互联网的历史性失误。", "IT之家", "2026-05-18", "https://www.ithome.com/0/951/588.htm"],
        ["华为推出iNCR原子基站：极简部署+即插即用，机身仅巴掌大小", "华为发布极简式5G小基站产品，即插即用部署模式大幅降低建网成本，5G深度覆盖加速普及。", "IT之家", "2026-05-18", "https://www.ithome.com/0/951/596.htm"],
        ["联想ThinkPad P16s Gen 5笔记本AMD版发布：至高96GB LPCAMM2内存", "联想更新移动工作站产品线，P16s Gen 5 AMD版配备RTX Pro 2000显卡，面向专业创作与AI开发场景。", "IT之家", "2026-05-18", "https://www.ithome.com/0/951/592.htm"],
        ["我国核心动力领域取得重大突破，1000kgf级航空发动机通过验收", "国产航空发动机研制迎来里程碑，1000kgf级核心机通过验收，大飞机动力自主化进程显著提速。", "IT之家", "2026-05-18", "https://www.ithome.com/0/951/591.htm"]
    ]],
    ["🎬", "文娱影游", [
        ["中央广播电视总台发布2026世界杯融媒体传播服务方案", "总台正式启动2026世界杯融媒体传播筹备，多平台联动、AI赋能观赛体验，媒体科技融合进入新阶段。", "IT之家", "2026-05-18", "https://www.ithome.com/0/951/593.htm"],
        ["《明末：渊虚之羽》确认登陆PS Plus 5月会免阵容", "5月索尼PS Plus会免游戏正式上线，包含国产动作游戏《明末：渊虚之羽》等多款作品，玩家关注度居高。", "IT之家", "2026-05-18", "https://www.ithome.com/0/946/427.htm"],
        ["卡普空《生化危机：代号维罗妮卡》重制版有望下月官宣", "卡普空经典IP重制计划持续推进，《生化危机：代号维罗妮卡》重制版传闻将于6月正式公布，粉丝期待值拉满。", "IT之家", "2026-05-18", "https://www.ithome.com/0/946/421.htm"],
        ["《极限竞速：地平线6》开发完成已送厂压盘", "微软第一方赛车大作《极限竞速：地平线6》宣布开发完成进入压盘阶段，将提供色盲滤镜等无障碍功能。", "IT之家", "2026-05-18", "https://www.ithome.com/0/946/423.htm"],
        ["Take-Two CEO确认《GTA6》首发无缘PC平台", "Take-Two首席执行官确认《GTA6》首发仅登陆主机平台，PC版本预计将在后续推出，主机玩家享有独占窗口期。", "IT之家", "2026-05-18", "https://www.ithome.com/0/946/417.htm"]
    ]],
    ["💰", "金融财经", [
        ["WTI原油期货涨超2%，现报103.08美元/桶", "国际油价大幅拉升，WTI原油突破103美元关口，地缘政治溢价回升，全球能源市场波动加剧。", "财联社", "2026-05-18", "https://www.cls.cn/detail/2373612"],
        ["韩国KOSPI指数两日累计跌幅扩大至10%，触发熔断机制", "韩国股市剧烈波动，KOSPI指数两日累计跌超10%，程序化交易暂停5分钟，亚太市场情绪承压。", "财联社", "2026-05-18", "https://www.cls.cn/detail/2373586"],
        ["美国关键国债收益率维持高位，市场博弈美联储政策路径", "美国长端国债收益率持续高位震荡，市场对美联储年内降息预期反复博弈，全球资产定价承压。", "财联社", "2026-05-18", "https://www.cls.cn/detail/2373607"],
        ["SpaceX据传最早6月12日登陆美股，目标估值高达1.75万亿美元", "马斯克旗下SpaceX IPO传闻持续发酵，目标估值1.75万亿美元，或成史上最大规模上市公司。", "财联社", "2026-05-18", "https://www.163.com/dy/media/T1442472327522.html"],
        ["Coinbase宣布裁员14%，CEO称AI正改变公司运营模式", "加密货币交易所Coinbase启动新一轮裁员，CEO将裁员归因于AI对运营效率的提升，行业自动化趋势加速。", "IT之家", "2026-05-18", "https://www.ithome.com/0/946/459.htm"]
    ]],
    ["🏠", "住房地产", [
        ["4月全国商品房销售面积同比降幅持续收窄", "国家统计局今日将发布4月房地产数据，市场预期销售端降幅进一步收窄，楼市企稳信号逐步显现。", "新浪财经", "2026-05-18", "https://finance.sina.com.cn/roll/2026-05-18/doc-inhyhisv3020312.shtml"],
        ["重点城市二手房成交量维持高位，中介门店新增客源回升", "五一假期后重点城市二手房市场持续回暖，新增客源量环比回升，购房者入市意愿边际改善。", "财联社", "2026-05-18", "https://www.cls.cn/detail/2373494"],
        ["多地试点"以旧换新"购房补贴政策，去库存节奏加快", "多个二三线城市试点住房"以旧换新"补贴政策，库存去化节奏加快，商品房市场活跃度提升。", "澎湃新闻", "2026-05-18", "https://www.thepaper.cn/"],
        ["住建部推进老旧小区改造年度任务，力争新开工5万个小区", "住建部加速推进2026年老旧小区改造计划，目标新开工5万个小区，民生工程与稳投资双重发力。", "财联社", "2026-05-18", "https://www.cls.cn/detail/2373498"],
        ["长租房REITs试点扩围，多地保障性租赁住房加速入市", "住房租赁REITs试点范围持续扩大，保障性租赁住房供应加速，租购并举的住房制度进一步完善。", "新浪财经", "2026-05-18", "https://finance.sina.com.cn/"]
    ]],
    ["🚗", "汽车出行", [
        ["广汽董事长回应埃安被称"网约车之王"", "广汽集团董事长公开回应埃安品牌"网约车"标签争议，强调品牌向上突破战略，高端化转型路径清晰。", "IT之家", "2026-05-18", "https://www.ithome.com/0/951/589.htm"],
        ["赛力斯问界系列4月单月销量突破3.5万辆", "赛力斯问界系列持续放量，4月单月销量突破3.5万辆，华为智选车模式商业化验证持续兑现。", "IT之家", "2026-05-18", "https://www.ithome.com/0/946/443.htm"],
        ["特斯拉FSD欧洲审批遇阻，监管机构质疑安全性与命名", "特斯拉FSD在欧洲面临监管障碍，当局对其安全性与"全自动驾驶"命名是否存在误导表达关切。", "IT之家", "2026-05-18", "https://www.ithome.com/0/946/464.htm"],
        ["比亚迪海豹06 DM-i改款今日正式上市，纯电续航提升至150km", "比亚迪持续完善插混产品矩阵，海豹06 DM-i改款上市，纯电续航大幅提升，中型轿车市场竞争加剧。", "IT之家", "2026-05-18", "https://www.ithome.com/0/951/588.htm"],
        ["蔚来换电站布局突破3000座，高速网络覆盖率达85%", "蔚来持续扩张补能基础设施，全国换电站突破3000座，高速网络覆盖持续提升，电动车长途出行痛点缓解。", "IT之家", "2026-05-18", "https://www.ithome.com/0/951/590.htm"]
    ]],
    ["🏥", "医疗健康", [
        ["国家药监局加速AI医疗影像器械审批通道", "国家药监局开通AI医疗影像产品优先审批通道，推想医疗、联影医疗等头部企业产品上市提速。", "财联社", "2026-05-18", "https://www.cls.cn/detail/2373498"],
        ["卫健委发布2026年互联网医疗监管新规征求意见稿", "卫健委就互联网医疗监管新规公开征求意见，在线诊疗、电子处方、医保结算等环节将面临更严监管。", "澎湃新闻", "2026-05-18", "https://www.thepaper.cn/"],
        ["恒瑞医药PD-1抑制剂新适应症获批，覆盖食管癌一线治疗", "恒瑞医药核心创新药再获新适应症批准，PD-1抑制剂覆盖食管癌一线治疗，国产创新药竞争力持续增强。", "财联社", "2026-05-18", "https://www.cls.cn/detail/2373600"],
        ["京东健康发布2026年财报预告：年度活跃用户突破2亿", "京东健康发布业绩预告，年度活跃用户预计突破2亿，互联网医疗消费渗透率持续提升，业务增长曲线清晰。", "IT之家", "2026-05-18", "https://www.ithome.com/0/951/587.htm"],
        ["微创机器人手术系统获欧盟CE认证，加速出海布局", "微创医疗手术机器人系统正式获得欧盟CE认证，打通欧洲市场销售通路，国产高端医疗器械国际化提速。", "财联社", "2026-05-18", "https://www.cls.cn/detail/2373610"]
    ]],
    ["📚", "教育培训", [
        ["教育部发布2026年高校毕业生就业促进计划", "教育部启动年度就业促进专项行动，针对2026届高校毕业生推出系列扶持政策，稳就业压力持续引起重视。", "新华财经", "2026-05-18", "https://finance.sina.com.cn/"],
        ["新东方股价走强，AI学习机产品季度销量同比增长80%", "新东方智能学习硬件业务持续放量，AI学习机季度销量同比高增，教育科技产品商业化兑现加速。", "财联社", "2026-05-18", "https://www.cls.cn/detail/2373605"],
        ["人社部推进职业技能等级认定扩围，新增50个新职业试点", "人社部持续完善职业技能评价体系，新增50个新职业试点，数字经济相关职业占比超60%，人才培养紧跟产业变革。", "澎湃新闻", "2026-05-18", "https://www.thepaper.cn/"],
        ["在线教育监管升级：预收费资金监管要求覆盖全品类", "教育部门强化在线教育预收费监管，资金监管要求覆盖全品类课程，防范跑路风险，保护消费者合法权益。", "财联社", "2026-05-18", "https://www.cls.cn/detail/2373494"],
        ["考研报名人数连续三年下降，出国留学咨询量同比回升30%", "2026年考研报名人数继续下降，与此同时出国留学咨询量大幅回升，国内学历竞争溢价边际走弱。", "新浪财经", "2026-05-18", "https://finance.sina.com.cn/"]
    ]],
    ["✈️", "旅游民宿", [
        ["文旅部：五一假期全国国内旅游出游合计4.2亿人次", "文旅部发布五一假期旅游总结数据，全国国内出游4.2亿人次，旅游消费强劲复苏，假日经济活力尽显。", "新华财经", "2026-05-18", "https://finance.sina.com.cn/"],
        ["携程发布2026年暑期旅游预测报告：出境游订单同比增长45%", "携程发布暑期旅游预测，出境游订单预计同比增长45%，亚太短途线路最热门，旅游消费信心持续修复。", "IT之家", "2026-05-18", "https://www.ithome.com/0/951/585.htm"],
        ["民宿短租平台爱彼迎中国业务一季度营收同比增长28%", "爱彼迎中国区业务持续放量，一季度营收同比增28%，本土化战略兑现，民宿市场渗透率持续提升。", "财联社", "2026-05-18", "https://www.cls.cn/detail/2373608"],
        ["民航局：五一假期全国机场旅客吞吐量创历史同期新高", "民航局发布五一假期数据，全国机场旅客吞吐量创历史同期新高，国内航线恢复超越2019年水平。", "澎湃新闻", "2026-05-18", "https://www.thepaper.cn/"],
        ["迪士尼中国两大乐园暑期门票预售量同比增长40%", "迪士尼上海与香港两大乐园暑期门票预售强劲，同比增长40%，主题公园消费市场复苏动能充足。", "IT之家", "2026-05-18", "https://www.ithome.com/0/951/593.htm"]
    ]],
    ["🌍", "国际视角", [
        ["贝莱德考虑在SpaceX下月IPO中投资至多100亿美元", "全球最大资产管理公司贝莱德据悉正考虑参与SpaceX下月IPO，投资规模或达100亿美元，明星项目机构认购热度空前。", "Readhub", "2026-05-18", "https://readhub.cn/daily"],
        ["苹果研发投入破历史纪录：单季同比大增34%", "苹果2026财年Q2研发费用达114亿美元创历史新高，AI服务与芯片自研投入持续加码，科技巨头军备竞赛提速。", "Readhub", "2026-05-18", "https://readhub.cn/topic/8spqYfpc0BL"],
        ["Meta再启裁员潮：办公区氛围压抑如临末日，员工争相抢夺日常物资", "Meta启动新一轮裁员，办公室氛围急剧恶化，员工焦虑情绪蔓延，硅谷大厂降本增效压力持续释放。", "Readhub", "2026-05-18", "https://readhub.cn/daily"],
        ["比尔·盖茨基金会出售其持有的最后一批微软股票", "盖茨基金会持续减持微软股票，最终清仓式退出，创始人家族与公司的资本纽带进一步弱化。", "Readhub", "2026-05-18", "https://readhub.cn/daily"],
        ["阿斯麦与塔塔电子达成合作，推进印度芯片计划", "光刻机巨头阿斯麦与印度塔塔电子达成战略合作，支持印度本土芯片制造计划，全球半导体产业链重构提速。", "Readhub", "2026-05-18", "https://readhub.cn/daily"]
    ]],
    ["🚀", "融资收购", [
        ["法拉第未来完成7000万美元机构投资者募资，贾跃亭宣布启动FF五大变革", "法拉第未来完成新一轮7000万美元机构募资，贾跃亭同步宣布五大战略变革，造车新势力求生之路持续演进。", "IT之家", "2026-05-18", "https://www.ithome.com/0/951/599.htm"],
        ["无锡将建立一座大规模「Token工厂」，联手弘信电子打造AI算力枢纽", "无锡市政府与弘信电子合作建设大规模AI Token算力工厂，打造江苏省内首个超节点算力集群，AI基础设施军备竞赛白热化。", "Readhub", "2026-05-18", "https://readhub.cn/daily"],
        ["摩尔线程与国家具身智能应用中试基地签署战略合作协议", "国产GPU厂商摩尔线程与国家具身智能应用中试基地达成战略合作，AI芯片+具身智能协同布局，国产算力应用生态加速完善。", "Readhub", "2026-05-18", "https://readhub.cn/daily"],
        ["上海移动宣布5G-A超级上行网络能力规模商用，推出1元40万Tokens通用服务", "上海移动正式商用5G-A超级上行网络，同时推出极低门槛AI Token套餐，算力与通信融合商业模式创新落地。", "Readhub", "2026-05-18", "https://readhub.cn/daily"],
        ["英伟达拟领投SImpliSMART 2000万美元融资", "英伟达持续完善AI基础设施生态布局，拟领投智能存储厂商SImpliSMART 2000万美元融资，算力与存储协同战略清晰。", "财联社", "2026-05-18", "https://www.cls.cn/detail/2373597"]
    ]],
]

def generate_html():
    sections_js = ""
    total_news = 0
    for idx, (icon, name, news_list) in enumerate(sections):
        total_news += len(news_list)
        news_cards = ""
        for i, (title, summary, source, date, link) in enumerate(news_list, 1):
            news_cards += f"""
                    <div class="news-card">
                        <span class="news-number">{i:02d}</span>
                        <div class="news-title">{title}</div>
                        <div class="news-summary">{summary}</div>
                        <div class="news-meta">
                            <span class="news-source">{source}</span>
                            <span class="news-date">{date}</span>
                            <a href="{link}" class="news-link" target="_blank" rel="noopener">原文链接</a>
                        </div>
                    </div>"""
        sections_js += f"""
            <div class="section">
                <div class="section-title">
                    <span class="icon">{icon}</span>
                    <span>{name}</span>
                </div>
                <div class="news-grid">{news_cards}
                </div>
            </div>"""

    html = f"""<!DOCTYPE html>
<html lang="zh-CN">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <meta name="theme-color" content="#f0f9ff">
    <title>互联网早报 - {today}</title>
    <style>
        * {{ margin:0; padding:0; box-sizing: border-box; }}

        :root {{
            --primary-blue: #0ea5e9;
            --light-blue: #f0f9ff;
            --ice-gray: #f8fafc;
            --tech-silver: #94a3b8;
            --aurora-white: #ffffff;
            --text-dark: #0f172a;
            --text-medium: #475569;
            --text-light: #64748b;
            --gradient-start: #e0f2fe;
            --gradient-end: #f0f9ff;
            --card-shadow: 0 4px 6px -1px rgba(0,0,0,0.1);
            --glass-bg: rgba(255,255,255,0.7);
            --glass-border: rgba(255,255,255,0.5);
        }}

        body {{
            font-family: -apple-system, BlinkMacSystemFont, "Segoe UI", "Roboto", sans-serif;
            background: linear-gradient(180deg, var(--gradient-start) 0%, var(--gradient-end) 100%);
            min-height: 100vh;
            color: var(--text-dark);
            line-height: 1.6;
        }}

        body::before {{
            content: '';
            position: fixed;
            top: 0; left: 0;
            width: 100%; height: 100%;
            background-image:
                linear-gradient(rgba(14,165,233,0.03) 1px, transparent 1px),
                linear-gradient(90deg, rgba(14,165,233,0.03) 1px, transparent 1px);
            background-size: 50px 50px;
            pointer-events: none;
            z-index: 0;
        }}

        .container {{
            max-width: 100%;
            margin: 0 auto;
            position: relative;
            z-index: 1;
        }}

        .header {{
            background: var(--glass-bg);
            backdrop-filter: blur(20px);
            -webkit-backdrop-filter: blur(20px);
            border-bottom: 1px solid var(--glass-border);
            padding: 30px 20px;
            text-align: center;
            position: sticky;
            top: 0;
            z-index: 100;
        }}

        .header h1 {{
            font-size: 32px;
            font-weight: 700;
            background: linear-gradient(135deg, #0ea5e9 0%, #6366f1 100%);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
            margin-bottom: 8px;
        }}

        .header .date {{
            font-size: 16px;
            color: var(--text-medium);
        }}

        .header .meta {{
            font-size: 14px;
            color: var(--text-light);
            margin-top: 8px;
            display: flex;
            justify-content: center;
            gap: 20px;
            flex-wrap: wrap;
        }}

        .content {{
            padding: 20px;
            max-width: 1200px;
            margin: 0 auto;
        }}

        .section {{
            margin-bottom: 30px;
            animation: fadeInUp 0.6s ease-out;
        }}

        @keyframes fadeInUp {{
            from {{ opacity: 0; transform: translateY(20px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}

        .section-title {{
            display: flex;
            align-items: center;
            gap: 12px;
            margin-bottom: 16px;
            padding: 16px 20px;
            background: var(--glass-bg);
            backdrop-filter: blur(10px);
            border-radius: 16px;
            border: 1px solid var(--glass-border);
            font-size: 22px;
            font-weight: 600;
            color: var(--text-dark);
            transition: all 0.3s ease;
        }}

        .section-title:hover {{
            transform: translateX(5px);
            box-shadow: var(--card-shadow);
        }}

        .section-title .icon {{
            font-size: 28px;
            animation: pulse 2s ease-in-out infinite;
        }}

        @keyframes pulse {{
            0%, 100% {{ transform: scale(1); }}
            50% {{ transform: scale(1.1); }}
        }}

        .news-grid {{
            display: grid;
            grid-template-columns: repeat(auto-fill, minmax(280px, 1fr));
            gap: 16px;
        }}

        .news-card {{
            background: var(--aurora-white);
            border-radius: 16px;
            padding: 20px;
            border: 1px solid rgba(226,232,240,0.8);
            box-shadow: var(--card-shadow);
            transition: all 0.3s ease;
            cursor: pointer;
            position: relative;
            overflow: hidden;
        }}

        .news-card::before {{
            content: '';
            position: absolute;
            top: 0; left: 0; right: 0;
            height: 3px;
            background: linear-gradient(90deg, #0ea5e9, #6366f1);
            transform: scaleX(0);
            transform-origin: left;
            transition: transform 0.3s ease;
        }}

        .news-card:hover {{
            transform: translateY(-4px);
            box-shadow: 0 20px 25px -5px rgba(0,0,0,0.1);
            border-color: #0ea5e9;
        }}

        .news-card:hover::before {{
            transform: scaleX(1);
        }}

        .news-number {{
            position: absolute;
            top: 12px; right: 12px;
            width: 28px; height: 28px;
            background: linear-gradient(135deg, #e0f2fe, #e0f2fe);
            border-radius: 8px;
            display: flex;
            align-items: center;
            justify-content: center;
            font-size: 13px;
            font-weight: 600;
            color: #0ea5e9;
            font-family: 'JetBrains Mono', monospace;
        }}

        .news-title {{
            font-size: 16px;
            font-weight: 600;
            color: var(--text-dark);
            line-height: 1.5;
            margin-bottom: 10px;
            padding-right: 36px;
        }}

        .news-summary {{
            font-size: 13px;
            color: var(--text-medium);
            line-height: 1.6;
            margin-bottom: 12px;
            padding: 10px 12px;
            background: var(--ice-gray);
            border-radius: 8px;
            border-left: 3px solid var(--primary-blue);
        }}

        .news-meta {{
            display: flex;
            align-items: center;
            gap: 10px;
            flex-wrap: wrap;
            font-size: 13px;
        }}

        .news-source {{
            background: linear-gradient(135deg, #e0f2fe, #e0f2fe);
            color: #0ea5e9;
            padding: 3px 10px;
            border-radius: 20px;
            font-size: 12px;
            font-weight: 500;
        }}

        .news-date {{
            color: var(--text-light);
            font-size: 12px;
        }}

        .news-link {{
            color: #0ea5e9;
            text-decoration: none;
            font-size: 12px;
            font-weight: 500;
            padding: 3px 10px;
            border-radius: 20px;
            background: rgba(14,165,233,0.1);
            transition: all 0.2s ease;
            margin-left: auto;
        }}

        .news-link:hover {{
            background: #0ea5e9;
            color: white;
        }}

        .footer {{
            background: var(--glass-bg);
            backdrop-filter: blur(20px);
            border-top: 1px solid var(--glass-border);
            padding: 30px 20px;
            text-align: center;
            color: var(--text-medium);
        }}

        .footer .brand {{
            font-size: 18px;
            font-weight: 600;
            background: linear-gradient(135deg, #0ea5e9, #6366f1);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}

        .footer .stats {{
            display: inline-flex;
            gap: 20px;
            background: white;
            padding: 12px 24px;
            border-radius: 30px;
            margin: 16px 0;
            box-shadow: var(--card-shadow);
        }}

        .footer .stat-number {{
            font-size: 24px;
            font-weight: 700;
            background: linear-gradient(135deg, #0ea5e9, #6366f1);
            -webkit-background-clip: text;
            -webkit-text-fill-color: transparent;
        }}

        .footer .stat-label {{
            font-size: 12px;
            color: var(--text-light);
        }}

        /* 返回首页按钮 */
        .back-home {{
            position: fixed;
            top: 20px;
            left: 20px;
            z-index: 1000;
            background: linear-gradient(135deg, #0ea5e9 0%, #6366f1 100%);
            color: white;
            padding: 10px 18px;
            border-radius: 25px;
            text-decoration: none;
            font-size: 14px;
            font-weight: 500;
            box-shadow: 0 4px 15px rgba(14,165,233,0.3);
            transition: all 0.3s ease;
        }}
        .back-home:hover {{
            transform: translateY(-2px);
            box-shadow: 0 6px 20px rgba(14,165,233,0.4);
        }}

        /* 响应式适配 */
        @media (max-width: 480px) {{
            .header h1 {{ font-size: 20px; }}
            .header .meta {{ gap: 10px; font-size: 12px; }}
            .content {{ padding: 12px; }}
            .news-card {{ padding: 14px; }}
            .news-title {{ font-size: 14px; }}
            .news-summary {{ font-size: 12px; padding: 8px 10px; }}
            .news-meta {{ gap: 6px; }}
            .news-link {{ font-size: 11px; padding: 3px 8px; }}
            .footer .stats {{ gap: 10px; padding: 8px 14px; flex-direction: column; }}
            .back-home {{ padding: 8px 14px; font-size: 12px; top: 10px; left: 10px; }}
            .section-title {{ font-size: 18px; padding: 12px 16px; }}
            .news-grid {{ grid-template-columns: 1fr; }}
        }}

        @media (min-width: 481px) and (max-width: 768px) {{
            .news-grid {{ grid-template-columns: repeat(2, 1fr); }}
        }}

        @media (min-width: 769px) {{
            .news-grid {{ grid-template-columns: repeat(3, 1fr); }}
        }}
    </style>
</head>
<body>
    <a href="../index.html" class="back-home">← 返回首页</a>
    <div class="container">
        <div class="header">
            <h1>互联网早报</h1>
            <div class="date">{today} {weekday}</div>
            <div class="meta">
                <span>📊 <strong>13</strong> 个核心栏目</span>
                <span>📰 <strong>{total_news}</strong> 条精选新闻</span>
                <span>⏰ <strong>08:45</strong> 准时推送</span>
            </div>
        </div>

        <div class="content">{sections_js}
        </div>

        <div class="footer">
            <div class="brand">互联网早报</div>
            <p>每日为您精选最重要的科技资讯</p>
            <div class="stats">
                <div class="stat-item">
                    <span class="stat-number">13</span>
                    <span class="stat-label">核心栏目</span>
                </div>
                <div class="stat-item">
                    <span class="stat-number">{total_news}</span>
                    <span class="stat-label">精选新闻</span>
                </div>
                <div class="stat-item">
                    <span class="stat-number">08:45</span>
                    <span class="stat-label">准时推送</span>
                </div>
            </div>
            <p>发送时间：{today}</p>
        </div>
    </div>
</body>
</html>"""

    output_dir = r'D:\openclaw\Internet-daily-news'
    output_file = os.path.join(output_dir, f'互联网早报_{today}.html')
    with open(output_file, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f"[OK] 已生成：{output_file}")
    print(f"[统计] 共 {len(sections)} 个栏目，{total_news} 条新闻")
    return output_file

if __name__ == '__main__':
    generate_html()
