from otree.api import *


doc = """
Questions about trust.
"""


class C(BaseConstants):
    NAME_IN_URL = 'app_8'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    WVS_SCALE = [
        (0, "เราจำเป็นต้องระมัดระวังอย่างยิ่ง"), # You have to be very cautious
        (1, "คนส่วนใหญ่เป็นคนที่เราไว้วางใจได้"), # Most people can be trusted
        (998, "ไม่ทราบ"), # Don't know
        (999, "ขอไม่ตอบ") # Prefer not to say
    ]
    WALLET_SCALE = [
        (0, "เป็นไปไม่ได้เลย"), # Not at all likely
        (1, "ไม่น่าจะเป็นไปได้"), # Not very likely
        (2, "อาจจะเป็นไปได้หรือเป็นไปไม่ได้ "), # Neither likely nor unlikely
        (3, "น่าจะเป็นไปได้"), # Quite likely
        (4, "เป็นไปได้แน่นอน"), # Very likely
        (998, "ไม่ทราบ"), # Don't know
        (999, "ขอไม่ตอบ") # Prefer not to say
        ]
    TRUST_SCALE = [
        (0, "ไม่ไว้วางใจเลย"), # Not at all
        (1, "ไว้วางใจเล็กน้อย"), # A little
        (2, "ไว้วางใจพอสมควร"), # Somewhat
        (3, "ไว้วางใจมาก"), # A lot
        (4, 'ไว้วางใจมากที่สุด'), # Completely
        (998, "ไม่ทราบ"), # Don't know
        (999, "ขอไม่ตอบ") # Prefer not to say
    ]
    IG_OG_TRUST_SCALE = [
        (0, "ไม่เห็นด้วยอย่างยิ่ง"), # Completely disagree
        (1, "ไม่เห็นด้วย"), # Disagree
        (2, "เฉยๆ"), # Neither disagree nor agree
        (3, "เห็นด้วย"), # Agree
        (4, "เห็นด้วยอย่างยิ่ง"), # Completely agree
        (998, "ไม่ทราบ"), # Don't know
        (999, "ขอไม่ตอบ") # Prefer not to say
    ]

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # Social trust
    social_trust_wvs = models.IntegerField(
        label="8.1. โดยทั่วไปแล้ว ท่านคิดว่าคนส่วนใหญ่เป็นคนที่ไว้วางใจได้หรือเห็นว่าเราจำเป็นต้องระมัดระวังอย่างยิ่ง เวลาที่ต้องปฎิสัมพันธ์กับคนอื่นๆ โดยส่วนใหญ่",
        # Generally speaking, would you say that most people can be trusted or would you say it’s necessary to be "
        #               "very cautious when dealing with most people?
        choices=C.WVS_SCALE,
        widget=widgets.RadioSelect,
        blank=False
    )
    social_trust_wallet = models.IntegerField(
        label="8.2. สมมติว่าท่านทำกระเป๋าสตางค์ตกหาย และต่อมาคนที่อาศัยอยู่ในละแวกบ้านเดียวกับท่านเป็นผู้พบกระเป๋าสตางค์บนถนน  "
              "มีความเป็นไปได้มากน้อยเพียงใดที่เขาจะนำกระเป๋าสตางค์มาคืนท่าน โดยไม่มีอะไรสูญหาย",
        # Suppose you lost your purse/wallet containing your address details, and it was found in the street by "
        #               "someone living in the neighborhood you last lived in, in your home country. How likely is it that it would "
        #               "be returned to you with nothing missing?
        choices= C.WALLET_SCALE,
        widget=widgets.RadioSelect,
        blank=False
    )
    social_trust_2 = models.IntegerField(
        label="8.3. ท่านมีความไว้วางใจต่อครอบครัวของท่านมากน้อยเพียงใด",
        # Please tell me how much you trust: Your family.
        choices=C.TRUST_SCALE,
        widget=widgets.RadioSelect,
        blank=False
    )
    social_trust_3 = models.IntegerField(
        label="8.4. ท่านมีความไว้วางใจต่อเพื่อนบ้านของท่านมากน้อยเพียงใด",
        # Please tell me how much you trust: Your neighbors.
        choices=C.TRUST_SCALE,
        widget=widgets.RadioSelect,
        blank=False
    )
    # Intergroup trust
    intergroup_trust_3 = models.IntegerField(
        # dynamic label on webpage
        choices=C.IG_OG_TRUST_SCALE,
        widget=widgets.RadioSelect,
        blank=False
    )
    intergroup_trust_4 = models.IntegerField(
        # dynamic label on webpage
        choices=C.IG_OG_TRUST_SCALE,
        widget=widgets.RadioSelect,
        blank=False
    )
    intergroup_trust_7 = models.IntegerField(
        # dynamic label on webpage
        choices=C.IG_OG_TRUST_SCALE,
        widget=widgets.RadioSelect,
        blank=False
    )
    # Outgroup trust
    outgroup_trust_3 = models.IntegerField(
        # dynamic label on webpage
        choices=C.IG_OG_TRUST_SCALE,
        widget=widgets.RadioSelect,
        blank=False
    )
    outgroup_trust_4 = models.IntegerField(
        # dynamic label on webpage
        choices=C.IG_OG_TRUST_SCALE,
        widget=widgets.RadioSelect,
        blank=False
    )
    outgroup_trust_7 = models.IntegerField(
        # dynamic label on webpage
        choices=C.IG_OG_TRUST_SCALE,
        widget=widgets.RadioSelect,
        blank=False
    )
    # institutional trust
    institutional_trust_1 = models.IntegerField(
        label="8.11. ท่านไว้วางใจสถาบันต่อไปนี้มากน้อยเพียงใด: ตำแหน่งนายกรัฐมนตรี ",
        # The prime minister
        choices=C.TRUST_SCALE,
        widget=widgets.RadioSelect,
        blank=False
    )
    institutional_trust_2 = models.IntegerField(
        label="8.12. ท่านไว้วางใจสถาบันต่อไปนี้มากน้อยเพียงใด: รัฐสภา",
        # The parliament
        choices=C.TRUST_SCALE,
        widget=widgets.RadioSelect,
        blank=False
    )
    institutional_trust_7 = models.IntegerField(
        label="8.13. ท่านไว้วางใจสถาบันต่อไปนี้มากน้อยเพียงใด: สำนักงานตำรวจแห่งชาติ",
        # The Royal Thai Police
        choices=C.TRUST_SCALE,
        widget=widgets.RadioSelect,
        blank=False
    )
    institutional_trust_8 = models.IntegerField(
        label="8.14. ท่านไว้วางใจสถาบันต่อไปนี้มากน้อยเพียงใด: กองทัพ",
        # The army
        choices=C.TRUST_SCALE,
        widget=widgets.RadioSelect,
        blank=False
    )
    institutional_trust_9 = models.IntegerField(
        label="8.15. ท่านไว้วางใจสถาบันต่อไปนี้มากน้อยเพียงใด: ศาลยุติธรรม",
        # The courts of law
        choices=C.TRUST_SCALE,
        widget=widgets.RadioSelect,
        blank=False
    )
    institutional_trust_10 = models.IntegerField(
        label="8.16. ท่านไว้วางใจสถาบันต่อไปนี้มากน้อยเพียงใด: ผู้นำตามธรรมชาติ",
        # The traditional leaders
        choices=C.TRUST_SCALE,
        widget=widgets.RadioSelect,
        blank=False
    )



# PAGES

class Page1(Page):
    form_model = 'player'
    form_fields = [
        'social_trust_wvs',
        'social_trust_wallet',
        'social_trust_2',
        'social_trust_3',
    ]


class Page2(Page):
    form_model = 'player'
    form_fields = [
        'intergroup_trust_3',
        'intergroup_trust_4',
        'intergroup_trust_7'
    ]


class Page3(Page):
    form_model = 'player'
    form_fields = [
        'outgroup_trust_3',
        'outgroup_trust_4',
        'outgroup_trust_7'
    ]


class Page4(Page):
    form_model = 'player'
    form_fields = [
        'institutional_trust_1',
        'institutional_trust_2',
        'institutional_trust_7',
        'institutional_trust_8',
        'institutional_trust_9',
        'institutional_trust_10'
    ]

page_sequence = [
    Page1, # social trust
    Page2, # ingroup trust
    Page3, # outgroup trust
    Page4 # institutional trust
]
