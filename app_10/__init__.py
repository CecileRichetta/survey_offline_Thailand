from otree.api import *


doc = """
Final app 
- recall -> if no, debrief
- final thank you
"""


class C(BaseConstants):
    NAME_IN_URL = 'app_11'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    TEMPLATE_DEBRIEF_FORM = '_static/texts/debrief_form.html'


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    recall_firstwave = models.BooleanField(
        label="11.1. ดังที่กล่าวในช่วงต้นของแบบสอบถาม งานวิจัยนี้มีสองรอบ ท่านต้องการเข้าร่วมในการสำรวจความคิดเห็นในรอบที่ 2 หรือไม่",
        # As mentionned at the beginning of the questionnaire, this is a two-parts study. Would you like to participate in the second wave of this survey?
        choices=[
            (True, "ใช่"),
            (False, "ไม่ใช่")
        ],
        widget=widgets.RadioSelect,
        blank=False
    )



# FUNCTIONS

# PAGES
class Page1_1(Page):
    form_model = 'player'
    @staticmethod
    def get_form_fields(player):
        participant = player.participant
        if participant.dropout is False and player.session.config['name'] == "session_C4P_THAI_w1":
            return [
                'recall_firstwave'
            ]
        else:
            pass
    def is_displayed(player):
        participant = player.participant
        return not participant.dropout and player.session.config['name'] == "session_C4P_THAI_w1"


class Page1_2(Page):
    @staticmethod
    def is_displayed(player):
        participant = player.participant
        return not participant.dropout

class Page2(Page):
    pass
    @staticmethod
    def is_displayed(player):
        participant = player.participant
        return (not participant.dropout) and (
                (player.field_maybe_none('recall_firstwave') is False and participant.treatment_hope == 1) or
                (player.session.config['name'] == "session_C4P_THAI_w2" and participant.treatment_hope == 1)
        )


class Page3(Page):
    pass


page_sequence = [
    Page1_1,
    Page1_2,
    Page2,
    Page3
]
