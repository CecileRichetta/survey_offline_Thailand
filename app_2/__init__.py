from otree.api import *

doc = """
Demographics questions
"""


class C(BaseConstants):
    NAME_IN_URL = 'app_2'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    VENN_THAILAND = 'imgs/venn_thailand.png'
    # CHOICES IN VARIABLES
    EDUCATION = [
        (0, 'ไม่ได้เข้าโรงเรียน'), # No schooling
        (1, 'ได้รับการศึกษาระดับประถมแต่ไม่จบ'), # Some primary school
        (2, 'จบการศึกษาระดับประถมศึกษา'), # Completed primary school
        (3, "ได้รับการศึกษาระดับมัธยมต้นแต่ไม่จบ"), # Some secondary school
        (4, "จบการศึกษาระดับมัธยมศึกษา"), # Completed secondary school
        (5, 'ได้รับการศึกษาระดับมัธยมปลายแต่ไม่จบ'), # Some high school
        (6, 'จบการศึกษาระดับมัธยมปลาย '), # Completed high school
        (8, 'ได้รับการศึกษาวิชาชีพแต่ไม่จบ'), # Some professional training
        (9, 'สำเร็จการฝึกอบรมวิชาชีพ'), # Completed professional training
        (10, 'ได้รับการศึกษาระดับมหาวิทยาลัยแต่ไม่จบ'), # Some university
        (11, 'จบการศึกษาระดับมหาวิทยาลัย'), # Completed university
        (12, 'อื่น ๆ'), # Other
        (998, "ไม่ทราบ"), # Don't know
        (999, 'ขอไม่ตอบ') # Prefer not to say
    ]
    ECONOMIC_STATUS_1 = [
        (0, "แย่มาก"), # Very bad
        (1, "ค่อนข้างแย่"), # Fairly bad
        (2, "ไม่ถึงกับดีไม่ถึงกับเลว"), # Neither bad nor good
        (3, "ค่อนข้างดี"), # Fairly good
        (4, "ดีมาก"), # Very good
        (998, "ไม่ทราบ"), # Don't know
        (999, 'ขอไม่ตอบ') # Prefer not to say
    ]
    ECONOMIC_STATUS_2 = [
        (0, "น้อยกว่า 10,000 บาท"), # Less than 10'000BHT
        (1, "10,000 - 20,000 บาท"), # 10'000 to 20'000BHT
        (2, "20,000-30,000 บาท"), # 20'000 to 30'000BHT
        (3, "30,000-40,000 บาท"), # 30'000 to 40'000BHT
        (4, "40,000-50,000 บาท"), # 40'000 to 5'000BHT
        (5, "มากกว่า 50,000 บาท"), # more than 50'000BHT
        (998, "ไม่ทราบ"), # Don't know
        (999, 'ขอไม่ตอบ') # Prefer not to say
    ]
    DEPENDENTS_SALARY = [
        (0, "หนึ่งคน"), # one person
        (1, "สองคน"), # two people
        (2, "สามคน"), # three people
        (3, "สี่คน"), # four people
        (4, "ห้าคน"), # five people
        (5, "มากกว่าห้าคน"), # more than give people
        (998, "ไม่ทราบ"),  # Don't know
        (999, 'ขอไม่ตอบ') # Prefer not to say
    ]
    RELIGION = [
        (0, 'อิสลาม'), # Islam
        (1, 'พุทธ'), # Buddhism
        (2, 'คริสต์'), # Christianity
        (3, 'อื่น ๆ'), # Other
        (4, 'ไม่ได้นับถือศาสนาใด'), # None
        (999, 'ขอไม่ตอบ') # Prefer not to say
    ]
    RELIGIOSITY = [
        (0, "ไม่ปฏิบัติตามหลักศาสนาเลย"), # Not religious at all
        (1, "ปฏิบัติตามหลักศาสนาอยู่บ้าง"), # Somewhat religious
        (2, "เคร่งครัดตามหลักศาสนา"), # Religious
        (3, "เคร่งครัดตามหลักศาสนามาก"), # Very religious
        (997, 'ไม่เกี่ยวข้อง'),  # Not applicable
        (999, 'ขอไม่ตอบ') # Prefer not to say
    ]
    INSECURITY = [
        (0, 'ไม่เคยรู้สึกเช่นนั้น'), # Never
        (1, 'แค่ครั้งหรือสองครั้ง'), # Just once or twice
        (2, 'หลายครั้ง'), # Several times
        (3, 'บ่อยครั้ง'), # Many times
        (4, 'ตลอดเวลา'), # Always
        (998, "ไม่ทราบ"),  # Don't know
        (999, 'ขอไม่ตอบ')  # Prefer not to say
    ]
    LANGUAGE_CHOICE_1 = [
        (0, 'ภาษาไทย'), # Thai
        (1, 'ภาษามลายู'), # Malay
        (2, 'ภาษามลายูปนไทย'), # Malay-Thai
        (3, 'ภาษาจีน'), # Chinese
        (4, 'อื่น ๆ'), # Other
        (999, 'ขอไม่ตอบ') # Prefer not to say
    ]
    LANGUAGE_CHOICE_2 = [
        (0, 'ภาษาไทย'), # Thai
        (1, 'ภาษามลายู'), # Malay
        (2, 'ภาษามลายูปนไทย'), # Malay-Thai
        (3, 'ภาษาจีน'), # Chinese
        (4, 'อื่น ๆ'), # Other
        (997, 'ไม่มี'),  # Speak no other language
        (999, 'ขอไม่ตอบ') # Prefer not to say
    ]
    SCALE_AGREEMENT = [
        (0, 'ไม่เห็นด้วยอย่างยิ่ง'), # Completely disagree
        (1, 'ไม่เห็นด้วย'), # Disagree
        (2, 'เฉยๆ'), # Neither disagree or agree
        (3, 'เห็นด้วย'), # Agree
        (4, 'เห็นด้วยอย่างยิ่ง'), # Completely agree
        (998, "ไม่ทราบ"),  # Don't know
        (999, 'ขอไม่ตอบ')  # Prefer not to say
    ]
    BINARY_ANSWER = [
        (1, 'ใช่'),  # Yes
        (0, 'ไม่ใช่'), # No
        (999, 'ขอไม่ตอบ') # Prefer not to say
    ]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # SOCIO-DEM VARIABLES
    age = models.IntegerField(
        label="2.1. โปรดระบุอายุของท่าน (จำนวนปี):", # Please indicate how old you are (in years):
        min=21,
        max=33,
        blank=False
    )
    education = models.IntegerField(
        label="2.2. ระดับการศึกษาสูงสุดสายสามัญ", # What is your highest level of education completed?
        choices=C.EDUCATION,
        blank=False,
        widget=widgets.RadioSelect
    )
    eco_status_1 = models.IntegerField(
        label="2.3. โปรดอธิบายถึงสภาพการดำรงชีวิตในปัจจุบันโดยทั่วไปของท่าน", # In general, how would you describe your own present living conditions?
        widget=widgets.RadioSelect,
        choices=C.ECONOMIC_STATUS_1,
        blank=False
    )
    eco_status_2 = models.IntegerField(
        label="2.4. หากเอารายได้ทั้งหมดมารวมกัน รายได้ต่อเดือนของครัวเรือนท่านอยู่ที่เท่าใด (ก่อนหักภาษี ประกันสังคม และค่าใช้จ่ายอื่น ๆ)",
        # Adding up your sources of income, what is your household's gross monthly income (before deducting taxes, social security contributions and other expenses)?
        choices=C.ECONOMIC_STATUS_2,
        widget=widgets.RadioSelect,
        blank=False
    )
    dependents_salary = models.IntegerField(
        label="2.5. ในครอบครัวของท่านมีสมาชิกกี่คน ",
        # How many people live in your household?
        choices=C.DEPENDENTS_SALARY,
        widget=widgets.RadioSelect,
        blank=False
    )
    religion = models.IntegerField(
        label="2.6. ท่านนับถือศาสนาใด", # what is your religion?
        choices=C.RELIGION,
        widget=widgets.RadioSelect,
        blank=False
    )
    religiosity = models.IntegerField(
        label="2.7. ท่านปฏิบัติตามหลักศาสนามากน้อยเพียงใด", # how religious are you?
        choices=C.RELIGIOSITY,
        widget=widgets.RadioSelect,
        blank=True
    )
    insecurity = models.IntegerField(
        label="2.8. ในช่วงหนึ่งปีที่ผ่านมา ตัวท่านหรือบุคคลใดในครอบครัวรู้สึกไม่ปลอดภัยระหว่างอยู่ในบ้านหรือในละแวกบ้านบ่อยครั้งเพียงใด",
        # Over the past year, how often, if ever, have you or anyone in your family felt unsafe in your home or neighborhood?
        choices=C.INSECURITY,
        widget=widgets.RadioSelect,
        blank=False
    )
    language_1_choice = models.IntegerField(
        label="2.9. ท่านใช้ภาษาใดเป็นหลักในการสื่อสาร",
        # What language do you primarily speak ?
        choices=C.LANGUAGE_CHOICE_1,
        widget=widgets.RadioSelect,
        blank=False
    )
    language_1_situation_homefamily = models.IntegerField(
        label="2.10. ท่านพูดภาษาหลักนี้เมื่ออยู่ในบ้าน",
        # You speak this language when you are at home
        choices=C.BINARY_ANSWER,
        widget=widgets.RadioSelectHorizontal,
        blank=False
    )
    language_1_situation_outside = models.IntegerField(
        label="2.11. ท่านพูดภาษาหลักนี้เมื่ออยู่นอกบ้าน",
        # You speak this language outside of home
        choices=C.BINARY_ANSWER,
        widget=widgets.RadioSelectHorizontal,
        blank=False
    )
    language_2_choice = models.IntegerField(
        label="2.12. นอกจากภาษาหลักแล้ว ท่านพูดภาษาใดอีกบ้าง",
        choices=C.LANGUAGE_CHOICE_2,
        widget=widgets.RadioSelect,
        blank=False
    )
    language_2_situation_homefamily = models.IntegerField(
        label="2.13. จากข้อ 2.12  ท่านพูดภาษานั้นเมื่ออยู่ในบ้าน ",
        # From 2.12 you speak this language at home
        choices=C.BINARY_ANSWER,
        widget=widgets.RadioSelectHorizontal,
        blank=True
    )
    language_2_situation_outside = models.IntegerField(
        label="2.14. จากข้อ 2.12  ท่านพูดภาษานั้นเมื่ออยู่นอกบ้าน ",
        # From 2.12 you speak this language outside of home
        choices=C.BINARY_ANSWER,
        widget=widgets.RadioSelectHorizontal,
        blank=True
    )
    group_attachment_1 = models.IntegerField(
        choices=C.SCALE_AGREEMENT,
        widget=widgets.RadioSelect,
        blank=False
    )
    group_attachment_2 = models.IntegerField(
        choices=C.SCALE_AGREEMENT,
        widget=widgets.RadioSelect,
        blank=False
    )
    venn_1 = models.IntegerField(
        choices=[
            (0, "(1)"),
            (1, "(2)"),
            (2, "(3)"),
            (3, "(4)"),
            (4, "(5)"),
            (998, "ไม่ทราบ"),
            (999, "ขอไม่ตอบ")
        ],
        widget=widgets.RadioSelectHorizontal,
        blank=False
    )

# PAGES
class Page1(Page):
    form_model = 'player'
    form_fields = [
        'age',
        'education',
        'eco_status_1',
        'eco_status_2',
        'dependents_salary',
        'religion',
        'religiosity',
        'insecurity'
    ] # removed gender
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        participant.age = player.age
        print(participant.age)
    def is_displayed(player: Player):
        return player.session.config['name'] == "session_C4P_THAI_w1"
    def error_message(player, values):
        # Only validate religiosity if religion is NOT 7 AND NOT 999
        if values['religion'] != 4 and values['religion'] != 999:
            if values.get('religiosity') is None:
                return 'ข้อผิดพลาด: โปรดตอบคำถามข้อที่ 2.7.'

class Page2(Page):
    form_model = 'player'
    form_fields = [
        'language_1_choice',
        'language_1_situation_homefamily',
        'language_1_situation_outside',
        'language_2_choice',
        'language_2_situation_homefamily',
        'language_2_situation_outside'
    ]
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        if ((player.religion == 0 or player.religion == 4) and
                ((player.language_1_choice == 1 or player.language_1_choice == 2) and
                 (player.language_1_situation_homefamily == 1)) or
                ((player.field_maybe_none('language_2_choice') == 1 or player.field_maybe_none('language_2_choice') == 2) and
                 (player.field_maybe_none('language_2_situation_homefamily') == 1))):
            participant.group = 0
            print(participant.group)
        else:
            participant.group = 1
            print(participant.group)
    def is_displayed(player: Player):
        return player.session.config['name'] == "session_C4P_THAI_w1"
    def error_message(player, values):
        # If they want to donate (ngo_binary == True), they must specify amount and NGO
        if values['language_2_choice'] != 997 and values['language_2_choice'] != 999 :
            if values.get('language_2_situation_homefamily') is None:
                return 'ข้อผิดพลาด: โปรดตอบคำถามข้อที่ 2.13.'
            if values.get('language_2_situation_outside') is None:
                return 'ข้อผิดพลาด: โปรดตอบคำถามข้อที่ 2.14.'


class Page3(Page):
    form_model = 'player'
    form_fields = [
        'group_attachment_1',
        'group_attachment_2',
        'venn_1'
    ]
    @staticmethod
    def is_displayed(player: Player):
        return player.session.config['name'] == "session_C4P_THAI_w1"


page_sequence = [
    Page1, # socio-demographics
    Page2, # language
    Page3 # group attachment with dynamic labels
]
