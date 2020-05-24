from otree.api import Currency as c, currency_range

from ._builtin import Page, WaitPage
from .models import Constants


class Demographics(Page):
    form_model = 'player'
    form_fields = [ 'gender','age','occupation','education','income','inc','hometown','location']


class GoodsSelection(Page):
    form_model = 'player'
    form_fields = ['necessity','comfort']
    def error_message(self,values):
        if len(values['necessity'].split(',')) != 3:
            if len(values['comfort'].split(',')) != 3:
                return "每题只限选择三件商品"
            else:
                return "第一题请只选择三件商品"
        if len(values['comfort'].split(',')) != 3:
            return "第二题请只选择三件商品"


class Consumption1(Page):
    live_method = 'live_auction'
    form_model = 'player'
    form_fields = ['n1','n2','n3','c1','c2','c3','valid']
    def vars_for_template(self):
        nChoice = self.player.necessity.lstrip('[').rstrip(']').split(',')
        cChoice = self.player.comfort.lstrip('[').rstrip(']').split(',')
        label = {'1.png':"洗护用品",
        '2.png':"肉类",
        '3.png':"蛋类",
        '4.png':"粮食类",
        '5.png':"奶制品",
        '6.png': "贴身衣物", 
        '7.png': "T恤", 
        '8.png': "水果",
        '9.png': "蔬菜", 
        '10.png': "零食",
        '11.png':"3C配件",
        '12.png':"鞋子",
        '13.png':"包包",
        '14.png':"高端护肤品",
        '15.png':"高端化妆品",
        '16.png':"衣服",
        '17.png':"游戏装备",
        '18.png':"小型家电",
        '19.png':"组装小型家具",
        '20.png':"高端文具"
        }
        detail = {
        '1.png':"洗发水/沐浴露等",
        '2.png':"猪/牛/羊/鱼/禽等",
        '3.png':"鸡/鸭/鹅等",
        '4.png':"米/面粉/玉米等",
        '5.png':"一箱牛奶/酸奶等",
        '6.png': "内衣/裤袜等", 
        '7.png': "长袖/T恤等", 
        '8.png': "苹果/梨/香蕉等",
        '9.png': "白菜/生菜/番茄等", 
        '10.png': "薯片/饼干/坚果等",
        '11.png':"耳机/硬盘/数位板等",
        '12.png':"运动鞋/高跟鞋等",
        '13.png':"书包/挎包/手提包等",
        '14.png':"眼霜/水乳套装等",
        '15.png':"口红/粉底/遮瑕等",
        '16.png':"卫衣/西装等",
        '17.png':"数字游戏/装备等",
        '18.png':"烤箱/咖啡机等",
        '19.png':"组装书架/晾衣架等",
        '20.png':"钢笔/墨水/画板等"
        }
        n1 = nChoice[0].strip(' ').strip("'")
        n2 = nChoice[1].strip(' ').strip("'")
        n3 = nChoice[2].strip(' ').strip("'")
        c1 = cChoice[0].strip(' ').strip("'")
        c2 = cChoice[1].strip(' ').strip("'")
        c3 = cChoice[2].strip(' ').strip("'")
        return dict(
            nImg1 = '{}'.format(n1),
            nImg2 = '{}'.format(n2),
            nImg3 = '{}'.format(n3),
            cImg1 = '{}'.format(c1),
            cImg2 = '{}'.format(c2),
            cImg3 = '{}'.format(c3),
            nLab1 = label[n1],
            nLab2 = label[n2],
            nLab3 = label[n3],
            cLab1 = label[c1],
            cLab2 = label[c2],
            cLab3 = label[c3],
            ndet1 = detail[n1],
            ndet2 = detail[n2],
            ndet3 = detail[n3],
            cdet1 = detail[c1],
            cdet2 = detail[c2],
            cdet3 = detail[c3]
        )
    def error_message(self,values):
        if values['valid'] == -1:
            return "账户余额不足，请重新填写"
        elif values['valid'] == -2:
            return "请重新填写"


class SpecialOffer(Page):
    form_model = 'player'

    def vars_for_template(self):
        if self.player.treatment == '1':
            offer = 'consumption coupon'
        elif self.player.treatment == '2':
            offer = 'tax refund'
        else:
            offer = 'helicopter money'
        return dict(
            offer = offer
        )



class Consumption2(Page):
    form_model = 'player'
    form_fields = ['na1','na2','na3','ca1','ca2','ca3','valida']
    def vars_for_template(self):
        nChoice = self.player.necessity.lstrip('[').rstrip(']').split(',')
        cChoice = self.player.comfort.lstrip('[').rstrip(']').split(',')
        label = {'1.png':"洗护用品",
        '2.png':"肉类",
        '3.png':"蛋类",
        '4.png':"粮食类",
        '5.png':"奶制品",
        '6.png': "贴身衣物", 
        '7.png': "T恤", 
        '8.png': "水果",
        '9.png': "蔬菜", 
        '10.png': "零食",
        '11.png':"3C配件",
        '12.png':"鞋子",
        '13.png':"包包",
        '14.png':"高端护肤品",
        '15.png':"高端化妆品",
        '16.png':"衣服",
        '17.png':"游戏装备",
        '18.png':"小型家电",
        '19.png':"组装小型家具",
        '20.png':"高端文具"
        }
        detail = {
        '1.png':"洗发水/沐浴露等",
        '2.png':"猪/牛/羊/鱼/禽等",
        '3.png':"鸡/鸭/鹅等",
        '4.png':"米/面粉/玉米等",
        '5.png':"一箱牛奶/酸奶等",
        '6.png': "内衣/裤袜等", 
        '7.png': "长袖/T恤等", 
        '8.png': "苹果/梨/香蕉等",
        '9.png': "白菜/生菜/番茄等", 
        '10.png': "薯片/饼干/坚果等",
        '11.png':"耳机/硬盘/数位板等",
        '12.png':"运动鞋/高跟鞋等",
        '13.png':"书包/挎包等",
        '14.png':"眼霜/水乳套装等",
        '15.png':"口红/粉底/遮瑕等",
        '16.png':"卫衣/西装等",
        '17.png':"数字游戏/装备等",
        '18.png':"烤箱/咖啡机等",
        '19.png':"组装书架/晾衣架等",
        '20.png':"钢笔/墨水/画板等"
        }
        n1 = nChoice[0].strip(' ').strip("'")
        n2 = nChoice[1].strip(' ').strip("'")
        n3 = nChoice[2].strip(' ').strip("'")
        c1 = cChoice[0].strip(' ').strip("'")
        c2 = cChoice[1].strip(' ').strip("'")
        c3 = cChoice[2].strip(' ').strip("'")
        if self.player.treatment == '1':
            offer = 'consumption coupon'
        elif self.player.treatment == '2':
            offer = 'tax refund'
        else:
            offer = 'helicopter money'
        return dict(
            offer = offer,
            nImg1 = '{}'.format(n1),
            nImg2 = '{}'.format(n2),
            nImg3 = '{}'.format(n3),
            cImg1 = '{}'.format(c1),
            cImg2 = '{}'.format(c2),
            cImg3 = '{}'.format(c3),
            nLab1 = label[n1],
            nLab2 = label[n2],
            nLab3 = label[n3],
            cLab1 = label[c1],
            cLab2 = label[c2],
            cLab3 = label[c3],
            ndet1 = detail[n1],
            ndet2 = detail[n2],
            ndet3 = detail[n3],
            cdet1 = detail[c1],
            cdet2 = detail[c2],
            cdet3 = detail[c3]
        )
    def error_message(self,values):
        if values['valida'] == -2:
            return "账户余额不足，请重新填写"
        elif values['valida'] == -1:
            return "请重新填写"

class Attention(Page):
    form_model = 'player'
    form_fields = ['attention']

page_sequence =[Demographics, GoodsSelection, Consumption1, SpecialOffer, Consumption2, Attention]
