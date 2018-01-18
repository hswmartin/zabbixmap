# -*- coding: utf-8 -*

import os
basedir = os.path.abspath(os.path.dirname(__file__))
basedir2 = os.path.abspath(os.path.dirname(__file__))

class Config:
    url = "http://10.0.11.246/zabbix/api_jsonrpc.php"                   #The IP address is the server of zabbix.
    header = {"Content-Type": "application/json"}
    hash_password = 'c24919836dbbaa02d566c805b7f0ff7e'
    groupid = ['9']                                            #groupid
    listofhost = [
[       "Hlj-heb-3560",
        "BJ-3560",
        "SX-TY-3560",
        "SXI-XA-3560",
        "HN-CD-3560",
        "HN-HH-3560",
        "HB-WC-3560",
        "HN-HY-3560",
        "JS-NJ-3560",
        "HN-ZZ-3560",
        "GZ-GY-3560",
        "10.112.0.2",
        "qiqihaerDBserver",
        "benxiDBserver",
        "huludaoDBserver",
        "yingkoudashiqiaoDBserver", 
],
[     "dalianDBserver",
         "JL-CC-3560",
        "TJ-3560",
        "Heb-SJZ-3560",
        "GS-LZ-3560",
        "WC-HY-3560",
        "WC-CSW-3560",
        "WC-HS-3560",
        "HN-YY-3560",
        "HN-SY-3560",
        "HN-CZ-3560",
        "AH_HF_3560V2",
        "changshaxiangjiangDBserver",
        "foshanDBserver",
        "jingmenDBserver",   
        "zhijiangDBserver",
],
[      "zhangjiajieDBserver",
        "HN_CS_3560X",
        "HK-3560",
        "WC-XY-3560",
        "CQ-3560",
        "GD-SZ-3560",
        "GX-NN-3560",
        "JX-NC-3560",
        "LN-SY-3560",
        "SC-CD-3560",
        "SD-JN-3560",
        "SH-3560",
        "YN-KN-3560",
        "liubanshuiDBserver",
        "handanDBserver",
        "tianmenDBserver",
]
    ]
    site_info = [
[       [126.600653,45.767043, "哈尔滨交换机<br>当前出口流量:"],
        [116.457124,39.87734, "北京交换机<br>当前出口流量:"],
        [112.592144,37.845793, "太原交换机<br>当前出口流量:"],
        [108.950763,34.286793, "西安交换机<br>当前出口流量:"],
        [111.694245,29.043279, "常德交换机<br>当前出口流量:"],
        [109.971028,27.543224, "怀化交换机<br>当前出口流量:"],
        [114.325687,30.545254, "武昌交换机<br>当前出口流量:"],
        [112.571877,26.91886, "衡阳交换机<br>当前出口流量:"],
        [118.781954,32.03062, "南京交换机<br>当前出口流量:"],
        [113.190263,27.799612, "株洲交换机<br>当前出口流量:"],
        [106.736804,26.567174, "贵阳交换机<br>当前出口流量:"],
        [87.628031,43.790236,"新疆乌鲁木齐阿迪娅VPN<br>当前出口流量:"],
        [123.962577,47.361397,"齐齐哈尔爱尔眼科医院VPN<br>当前出口流量:"],
        [123.766931,41.28548,"本溪爱尔眼科医院VPN<br>当前出口流量:"],
        [120.873532,40.761746,"葫芦岛爱尔眼科医院VPN<br>当前出口流量:"],
],
[       [121.588861,38.98761, "大连爱尔眼科VPN<br>当前出口流量:"],
        [125.350592,43.88681, "长春交换机<br>当前出口流量:"],
        [117.147149,39.105408, "天津交换机<br>当前出口流量:"],
        [114.483294,38.032093, "石家庄交换机<br>当前出口流量:"],
        [103.849135,36.04918, "兰州交换机<br>当前出口流量:"],
        [114.234672,30.56671, "汉阳交换机<br>当前出口流量:"],
        [114.325687,30.545254, "武昌交换机<br>当前出口流量:"],
        [115.074693,30.244633, "黄石交换机<br>当前出口流量:"],
        [112.349878,28.563622, "益阳交换机<br>当前出口流量:"],
        [111.496602,27.239076, "邵阳交换机<br>当前出口流量:"],
        [113.036234,25.786211, "郴州交换机<br>当前出口流量:"],
        [117.240425,31.837894, "合肥交换机<br>当前出口流量:"],
        [112.93187,28.225846,"长沙湘江VPN<br>当前出口流量:"],
        [113.139648,23.042401,"佛山爱尔眼科VPN<br>当前出口流量:"],
        [112.210311,31.049414,"荆门爱尔眼科VPN<br>当前出口流量:"],
],
[       [110.497716,29.12986,"张家界爱尔眼科VPN<br>当前出口流量:"],
        [112.991898,28.166898, "长沙交换机<br>当前出口流量:"],
        [114.264686,30.619264, "汉口交换机<br>当前出口流量:"],
        [112.139993,32.040407, "襄阳交换机<br>当前出口流量:"],
        [106.541329,29.577745, "重庆交换机<br>当前出口流量:"],
        [114.094036,22.541222, "深圳交换机<br>当前出口流量:"],
        [108.304659,22.860322, "南宁交换机<br>当前出口流量:"],
        [115.922167,28.661901, "南昌交换机<br>当前出口流量:"],
        [123.361713,41.787147, "沈阳交换机<br>当前出口流量:"],
        [104.048302,30.657112, "成都交换机<br>当前出口流量:"],
        [117.0768,36.696247, "济南交换机<br>当前出口流量:"],
        [121.418984,31.201762, "上海交换机<br>当前出口流量:"],
        [102.731503,25.030228, "昆明交换机<br>当前出口流量:"],
        [104.879846,26.58529,"贵阳六盘水VPN<br>当前出口流量:"],
        [114.492099,36.624003,"邯郸爱尔眼科VPN<br>当前出口流量:"],
        [113.180169,30.667433,"天门爱尔眼科VPN<br>当前出口流量:"],
]

    ]

    @staticmethod
    def init_app(app):
        pass

config = {

    'default': Config
}

