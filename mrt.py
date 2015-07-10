#! -*-coding:utf-8 -*-
import requests
try:
    import xml.etree.cElementTree as ET
except ImportError:
    import xml.etree.ElementTree as ET

class MRTStation():
	def __init__(self):
		self.station = [{"id":"007","line":["文湖線"],"name":"松山機場"},
			{"id":"008" , "line":["文湖線"] , "name":"中山國中"},
			{"id":"009" , "line":["文湖線"] , "name":"南京東路"},
			{"id":"010" , "line":["文湖線"] , "name":"忠孝復興"},
			{"id":"011" , "line":["文湖線"] , "name":"大安"},
			{"id":"012" , "line":["文湖線"] , "name":"科技大樓"},
			{"id":"013" , "line":["文湖線"] , "name":"六張犁"},
			{"id":"014" , "line":["文湖線"] , "name":"麟光"},
			{"id":"015" , "line":["文湖線"] , "name":"辛亥"},
			{"id":"016" , "line":["文湖線"] , "name":"萬芳醫院"},
			{"id":"017" , "line":["文湖線"] , "name":"萬芳社區"},
			{"id":"018" , "line":["文湖線"] , "name":"木柵"},
			{"id":"019" , "line":["文湖線"] , "name":"動物園"},
			{"id":"021" , "line":["文湖線"] , "name":"大直"},
			{"id":"022" , "line":["文湖線"] , "name":"劍南路"},
			{"id":"023" , "line":["文湖線"] , "name":"西湖"},
			{"id":"024" , "line":["文湖線"] , "name":"港墘"},
			{"id":"025" , "line":["文湖線"] , "name":"文德"},
			{"id":"026" , "line":["文湖線"] , "name":"內湖"},
			{"id":"027" , "line":["文湖線"] , "name":"大湖公園"},
			{"id":"028" , "line":["文湖線"] , "name":"葫洲"},
			{"id":"029" , "line":["文湖線"] , "name":"東湖"},
			{"id":"030" , "line":["文湖線"] , "name":"南港軟體園區"},
			{"id":"031" , "line":["文湖線"] , "name":"南港展覽館"},
			{"id":"032" , "line":["松山新店線"] , "name":"小碧潭"},
			{"id":"033" , "line":["松山新店線"] , "name":"新店"},
			{"id":"034" , "line":["松山新店線"] , "name":"新店區公所"},
			{"id":"035" , "line":["松山新店線"] , "name":"七張"},
			{"id":"036" , "line":["松山新店線"] , "name":"大坪林"},
			{"id":"037" , "line":["松山新店線"] , "name":"景美"},
			{"id":"038" , "line":["松山新店線"] , "name":"萬隆"},
			{"id":"039" , "line":["松山新店線"] , "name":"公館"},
			{"id":"040" , "line":["松山新店線"] , "name":"台電大樓"},
			{"id":"041" , "line":["松山新店線" , "中和新蘆線"] , "name":"古亭"},
			{"id":"042" , "line":["松山新店線" , "淡水信義線"] , "name":"中正紀念堂"},
			{"id":"043" , "line":["松山新店線"] , "name":"小南門"},
			{"id":"045" , "line":["中和新蘆線"] , "name":"頂溪"},
			{"id":"046" , "line":["中和新蘆線"] , "name":"永安市場"},
			{"id":"047" , "line":["中和新蘆線"] , "name":"景安"},
			{"id":"048" , "line":["中和新蘆線"] , "name":"南勢角"},
			{"id":"050" , "line":["淡水信義線"] , "name":"台大醫院"},
			{"id":"051" , "line":["文湖線" , "淡水信義線"] , "name":"台北車站"},
			{"id":"053" , "line":["淡水信義線"] , "name":"中山"},
			{"id":"054" , "line":["淡水信義線"] , "name":"雙連"},
			{"id":"055" , "line":["淡水信義線" , "中和新蘆線"] , "name":"民權西路"},
			{"id":"056" , "line":["淡水信義線"] , "name":"圓山"},
			{"id":"057" , "line":["淡水信義線"] , "name":"劍潭"},
			{"id":"058" , "line":["淡水信義線"] , "name":"士林"},
			{"id":"059" , "line":["淡水信義線"] , "name":"芝山"},
			{"id":"060" , "line":["淡水信義線"] , "name":"明德"},
			{"id":"061" , "line":["淡水信義線"] , "name":"石牌"},
			{"id":"062" , "line":["淡水信義線"] , "name":"唭哩岸"},
			{"id":"063" , "line":["淡水信義線"] , "name":"奇岩"},
			{"id":"064" , "line":["淡水信義線"] , "name":"北投"},
			{"id":"065" , "line":["淡水信義線"] , "name":"新北投"},
			{"id":"066" , "line":["淡水信義線"] , "name":"復興崗"},
			{"id":"067" , "line":["淡水信義線"] , "name":"忠義"},
			{"id":"068" , "line":["淡水信義線"] , "name":"關渡"},
			{"id":"069" , "line":["淡水信義線"] , "name":"竹圍"},
			{"id":"070" , "line":["淡水信義線"] , "name":"紅樹林"},
			{"id":"071" , "line":["淡水信義線"] , "name":"淡水"},
			{"id":"077" , "line":["文湖線"] , "name":"永寧"},
			{"id":"078" , "line":["文湖線"] , "name":"土城"},
			{"id":"079" , "line":["文湖線"] , "name":"海山"},
			{"id":"080" , "line":["文湖線"] , "name":"亞東醫院"},
			{"id":"081" , "line":["文湖線"] , "name":"府中"},
			{"id":"082" , "line":["文湖線"] , "name":"板橋"},
			{"id":"083" , "line":["文湖線"] , "name":"新埔"},
			{"id":"084" , "line":["文湖線"] , "name":"江子翠"},
			{"id":"085" , "line":["文湖線"] , "name":"龍山寺"},
			{"id":"086" , "line":["文湖線" , "松山新店線"] , "name":"西門"},
			{"id":"088" , "line":["文湖線"] , "name":"善導寺"},
			{"id":"089" , "line":["文湖線" , "中和新蘆線"] , "name":"忠孝新生"},
			{"id":"091" , "line":["文湖線"] , "name":"忠孝敦化"},
			{"id":"092" , "line":["文湖線"] , "name":"國父紀念館"},
			{"id":"093" , "line":["文湖線"] , "name":"市政府"},
			{"id":"094" , "line":["文湖線"] , "name":"永春"},
			{"id":"095" , "line":["文湖線"] , "name":"後山埤"},
			{"id":"096" , "line":["文湖線"] , "name":"昆陽"},
			{"id":"097" , "line":["文湖線"] , "name":"南港"},
			{"id":"121" , "line":["中和新蘆線"] , "name":"輔大"},
			{"id":"122" , "line":["中和新蘆線"] , "name":"新莊"},
			{"id":"123" , "line":["中和新蘆線"] , "name":"頭前庄"},
			{"id":"124" , "line":["中和新蘆線"] , "name":"先嗇宮"},
			{"id":"125" , "line":["中和新蘆線"] , "name":"三重"},
			{"id":"126" , "line":["中和新蘆線"] , "name":"菜寮"},
			{"id":"127" , "line":["中和新蘆線"] , "name":"台北橋"},
			{"id":"128" , "line":["中和新蘆線"] , "name":"大橋頭"},
			{"id":"130" , "line":["中和新蘆線"] , "name":"中山國小"},
			{"id":"131" , "line":["中和新蘆線"] , "name":"行天宮"},
			{"id":"132" , "line":["中和新蘆線"] , "name":"松江南京"},
			{"id":"134" , "line":["中和新蘆線"] , "name":"東門"},
			{"id":"174" , "line":["中和新蘆線"] , "name":"蘆洲"},
			{"id":"175" , "line":["中和新蘆線"] , "name":"三民高中"},
			{"id":"176" , "line":["中和新蘆線"] , "name":"徐匯中學"},
			{"id":"177" , "line":["中和新蘆線"] , "name":"三和國中"},
			{"id":"178" , "line":["中和新蘆線"] , "name":"三重國小"},
			{"id":"179" , "line":["中和新蘆線"] , "name":"迴龍"},
			{"id":"180" , "line":["中和新蘆線"] , "name":"丹鳳"}]
	def getTrainTime(self,name="",Id=""):
		if name==Id:
			return
		if name != "":
			for i in self.station:
				if i["name"] == name :
					Id = i["id"]
					break
		s = requests.Session()
		headers = {'content-type':'text/xml','SOAPAcrion':'http://tempuri.org/GetNextTrain2'}
		content = """<?xml version='1.0' encoding='UTF-8'?>
<soap:Envelope xmlns:soap="http://schemas.xmlsoap.org/soap/envelope/" xmlns:xsi="http://www.w3.org/2001/XMLSchema-instance"
xmlns:xsd="http://www.w3.org/2001/SMLSchema">
    <soap:Body>
        <GetNextTrain2 xmlns="http://tempuri.org/">
            <stnid>"""+Id+"""</stnid>
        </GetNextTrain2>
    </soap:Body>
</soap:Envelope>"""
		r = s.post("http://ws.metro.taipei/trtcappweb/Traintime.asmx",data=content,headers=headers)
		xml = r.content
		xmltree = ET.ElementTree()
		xmltree = ET.fromstring(xml)
		result = []
		for elem in xmltree.iter('Detail'):
			result.append({'destination':elem.get('destination'),"countdown":elem.get("countdown").replace(" ",'')})
		return result
