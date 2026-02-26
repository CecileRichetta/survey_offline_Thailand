from otree.api import *


doc = """
Evaluation of the questionnaire. 
"""


class C(BaseConstants):
    NAME_IN_URL = ('app_10')
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    # CHOICES
    CHOICES_EVAL = [
        (0, "ไม่เห็นด้วยอย่างยิ่ง"), # Completely disagree
        (1, "ไม่เห็นด้วย"), # Disagree
        (2, "เฉยๆ "), # Neither agree nor disagree
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
    evaluation_1 = models.IntegerField(
        label="10.1. ท่านเห็นด้วยกับประโยคต่อไปนี้มากน้อยเพียงใด: ความยาวของแบบสอบถามมีความเหมาะสม",
        # The length of the questionnaire is appropriate.
        choices=C.CHOICES_EVAL,
        widget=widgets.RadioSelect,
        blank=False
    )
    evaluation_1_long = models.LongStringField(
        label="10.2. โปรดระบุคำถามที่ท่านคิดว่ายาวเกินไป:",
        # Please specify which questions were too long:
        blank=True
    )
    evaluation_2 = models.IntegerField(
        label="10.3. ท่านเห็นด้วยกับประโยคต่อไปนี้มากน้อยเพียงใด: คำถามเข้าใจได้ง่าย",
        # The questions are easy to understand.
        choices=C.CHOICES_EVAL,
        widget=widgets.RadioSelect,
        blank=False
    )
    evaluation_2_long = models.LongStringField(
        label="10.4. โปรดระบุเนื้อหาส่วนที่ท่านคิดว่าเข้าใจยาก",
        #Please specify which elements you found were hard to understand:
        blank=True
    )
    evaluation_3 = models.IntegerField(
        label="10.5. ท่านเห็นด้วยกับประโยคต่อไปนี้มากน้อยเพียงใด: วิธีการทำและตัวอย่างสำหรับกิจกรรมเกี่ยวกับเหรียญทั้งสองกิจกรรมเข้าใจได้ง่าย",
        # The instructions and examples for the two tasks with the tokens are easy to understand.
        choices=C.CHOICES_EVAL,
        widget=widgets.RadioSelect,
        blank=False
    )
    evaluation_3_long = models.LongStringField(
        label="10.6. โปรดระบุเนื้อหาเกี่ยวกับกิจกรรมที่ท่านไม่เข้าใจ:",
        # Please specify what you did not understand about the tasks:
        blank=True
    )
    evaluation_4 = models.IntegerField(
        label="10.7. ท่านเห็นด้วยกับประโยคต่อไปนี้มากน้อยเพียงใด: คำถามเกี่ยวกับประสบการณ์ต่อความรุนแรงทำให้ท่านรู้สึกไม่สบายใจ  ",
        # The questions about the experience of violence in my home country made me uncomfortable.
        choices=C.CHOICES_EVAL,
        widget=widgets.RadioSelect,
        blank=False
    )
    evaluation_4_long = models.LongStringField(
        label="10.8. คำถามใดทำให้ท่านรู้สึกไม่สบายใจมากที่สุด",
        # Which questions made you most uncomfortable:
        blank=True
    )
    evaluation_5 = models.IntegerField(
        label="10.9. ท่านเห็นด้วยกับประโยคต่อไปนี้มากน้อยเพียงใด: สิทธิของท่านในฐานะผู้เข้าร่วมมีความชัดเจนตั้งแต่ต้น ",
        # My rights as a participant were clear from the start.
        choices=C.CHOICES_EVAL,
        widget=widgets.RadioSelect,
        blank=False
    )
    evaluation_5_long = models.LongStringField(
        label="10.10. เนื้อหาเกี่ยวกับสิทธิของท่านในฐานะผู้เข้าร่วมส่วนใดที่ขาดความชัดเจน",
        # What parts about your rights as a participant were not clear:
        blank=True
    )
    evaluation_6 = models.IntegerField(
        label="10.11. ท่านเห็นด้วยกับประโยคต่อไปนี้มากน้อยเพียงใด: แบบสอบถามมีความน่าสนใจ",
        # The questionnaire was interesting.
        choices=C.CHOICES_EVAL,
        widget=widgets.RadioSelect,
        blank=False
    )
    evaluation_6_long = models.LongStringField(
        label="10.12. เนื้อหาส่วนใดของแบบสอบถามที่ไม่น่าสนใจ",
        # Which parts of the questionnaire were not interesting:
        blank=True
    )
    evaluation_other = models.LongStringField(
        label="10.13. ท่านมีความเห็นหรือข้อสังเกตเพิ่มเติมเกี่ยวกับแบบสอบถามหรือไม่",
        # Do you have any additional remarks or comments on the questionnaire?
        blank=True
    )
# PAGES
class Page1(Page):
    form_model = 'player'
    form_fields = [
        'evaluation_1',
        'evaluation_1_long',
        'evaluation_2',
        'evaluation_2_long',
        'evaluation_3',
        'evaluation_3_long',
        'evaluation_4',
        'evaluation_4_long',
        'evaluation_5',
        'evaluation_5_long',
        'evaluation_6',
        'evaluation_6_long',
        'evaluation_other'
    ]

page_sequence = [
    Page1
]
