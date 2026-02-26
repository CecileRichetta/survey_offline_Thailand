from otree.api import *


doc = """
Manipulation check and Emotions.
"""


class C(BaseConstants):
    NAME_IN_URL = 'app_7'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    # SCALE
    ANSWER_SCALE = [
        (0, "ไม่เห็นด้วยอย่างยิ่ง"), # Strongly disagree
        (1, "ไม่เห็นด้วย"), # Disagree
        (2, "เฉยๆ "), # Neither disagree nor agree
        (3, "เห็นด้วย"), # Agree
        (4, "เห็นด้วยอย่างยิ่ง"), # Strongly agree
        (998, "ไม่ทราบ"), # Don't know
        (999, "ขอไม่ตอบ") # Prefer not to say
    ]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    empathy_6 = models.IntegerField(
        # dynamic labels in the webpage
        choices=C.ANSWER_SCALE,
        widget=widgets.RadioSelect,
        blank=False
    )
    guilt_1 = models.IntegerField(
        # dynamic labels in webpage
        choices=C.ANSWER_SCALE,
        widget=widgets.RadioSelect,
        blank=False
    )
    anger_2 = models.IntegerField(
        # dynamic labels in webpage
        choices=C.ANSWER_SCALE,
        widget=widgets.RadioSelect,
        blank=False
    )
    fear_1 = models.IntegerField(
        # dynamic labels in webpage
        choices=C.ANSWER_SCALE,
        widget=widgets.RadioSelect,
        blank=False
    )


# FUNCTIONS



# PAGES
class Page1(Page):
    form_model = 'player'
    form_fields = [
        'empathy_6',
        'guilt_1',
        'anger_2',
        'fear_1',
    ]

page_sequence = [
    Page1 # group emotions
]