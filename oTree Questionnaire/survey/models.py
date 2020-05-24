from otree.api import (
    models,
    widgets,
    BaseConstants,
    BaseSubsession,
    BaseGroup,
    BasePlayer,
    Currency as c,
    currency_range,
)

from django.forms import widgets as django_widgets


class Constants(BaseConstants):
    name_in_url = 'survey'
    players_per_group = None
    num_rounds = 1

# Treatment: 1. Consumption coupon, 2. Tax refund, 3. helicopter money

class Subsession(BaseSubsession):
    
    def creating_session(self):
        import itertools
        treatments = itertools.cycle(['1','2','3'])
        for player in self.get_players():
            player.treatment =  next(treatments)


class Group(BaseGroup):
    pass


class Player(BasePlayer):

    treatment = models.StringField()

    age = models.StringField(
        choices = [['a','18岁及以下'],['b','19-22岁'],['c','23-25岁'],['d','26-29岁'],['e','30-39岁'],['f','40岁以上']],
        label='2. 您的年龄区间',
        widget=widgets.RadioSelect,
    )

    gender = models.StringField(
        choices=[['Male','男'], ['Female', '女']],
        label='1. 您的性别',
        widget=widgets.RadioSelect
    )
    
    occupation = models.StringField(
        choices=[['Student','学生'], ['No', '其他']],
        label='3. 您的身份',
        widget=widgets.RadioSelect
    )

    education = models.StringField(
        choices=[['1','高中及以下'], ['2', '大专'],['3','本科'],['4','研究生'],['5','博士及以上']],
        label='4. 您的最高学历',
        widget=widgets.RadioSelect
    )

    income = models.StringField(
        choices=[['1','少于1000元'], ['2', '1000-1999元'],['3','2000-2999元'],['4','3000-4999元'],['5','5000-9999元'],['6','1万元及以上']],
        label='5. 您每月可支配收入区间',
        widget=widgets.RadioSelect
    )

    inc = models.IntegerField(label='6. 请估算您每月可支配收入平均值',min=0,max=10001,widget=widgets.Slider)

    hometown = models.StringField(
        choices=[['1','一线城市（北上广深）'], ['2', '新一线城市（可参考本页底部小贴士）'],['3','新二线城市（可参考本页底部小贴士）'],['4','三线及以下']],
        label='7. 您家乡所在城市梯次',
        widget=widgets.RadioSelect
    )

    location = models.StringField(
        choices=[['1','一线城市（北上广深）'], ['2', '新一线城市（可参考本页底部小贴士）'],['3','新二线城市（可参考本页底部小贴士）'],['4','三线及以下']],
        label='8. 您常住地所在城市梯次',
        widget=widgets.RadioSelect
    )

    necessity = models.StringField( 
        label = "1. 请选择您最常购买的三件商品",
        widget = django_widgets.CheckboxSelectMultiple(
            choices = [
                ['1.png', "洗护用品（洗发水/沐浴露/身体乳等）"], 
                ['2.png', "肉类（猪/牛/羊/鱼/禽等）"], 
                ['3.png', "蛋类（鸡/鸭/鹅等）"],
                ['4.png', "粮食类（米/面/粉/红薯/玉米等）"], 
                ['5.png', "奶制品（一箱牛奶/酸奶等）"], 
                ['6.png', "贴身衣物（内衣/内裤/袜子等）"], 
                ['7.png', "T恤（长袖/短袖等）"], 
                ['8.png', "水果（苹果/梨/香蕉等）"],
                ['9.png', "蔬菜（白菜/生菜/西红柿等）"], 
                ['10.png', "零食（薯片/饼干/坚果等）"]
            ]
        )
    )
    '''
    def necessity_error_message(self,value):
        if len(value.split(',')) != 3:
            return "请务必选择三件"
    '''
    
    comfort = models.StringField(
        label = "2. 请选择你最常购买的三件商品",
        widget = django_widgets.CheckboxSelectMultiple(
            choices = [
                ['11.png', "3C配件（耳机/硬盘/数位板等）"], 
                ['12.png', "鞋子（运动鞋/休闲鞋/高跟鞋等）"], 
                ['13.png', "包包（书包/挎包/手提包等）"],
                ['14.png', "高端护肤品（眼霜/水乳套装/面膜等）"], 
                ['15.png', "高端化妆品（口红/粉底/遮瑕等）"], 
                ['16.png', "衣服（卫衣/卫裤/西装等）"], 
                ['17.png', "游戏装备（数字游戏/游戏装备等）"], 
                ['18.png', "小型家电（烤箱/咖啡机/音响等）"],
                ['19.png', "组装小型家具（组装式书架/晾衣架等）"], 
                ['20.png', "高端文具（钢笔/墨水/画板等）"],       
            ]
        )
    )

    '''
    def comfort_error_message(self,value):
        if len(value.split(',')) != 3:
            return "请务必选择三件"
    '''

    n1 = models.IntegerField(widget=django_widgets.HiddenInput())
    n2 = models.IntegerField(widget=django_widgets.HiddenInput())
    n3 = models.IntegerField(widget=django_widgets.HiddenInput())

    c1 = models.IntegerField(widget=django_widgets.HiddenInput())
    c2 = models.IntegerField(widget=django_widgets.HiddenInput())
    c3 = models.IntegerField(widget=django_widgets.HiddenInput())

    valid = models.IntegerField(widget=django_widgets.HiddenInput())

    attention = models.StringField(
        choices=[['A','A. Stephen'], ['B', 'B. Cindy'],['C','C. Jesse'], ['D','D. Judy']],
        label='请在下列选项中选择S开头的单词',
        widget=widgets.RadioSelect
    )

    valida = models.IntegerField(widget=django_widgets.HiddenInput())

    na1 = models.IntegerField()
    na2 = models.IntegerField()
    na3 = models.IntegerField()

    ca1 = models.IntegerField()
    ca2 = models.IntegerField()
    ca3 = models.IntegerField()

    

