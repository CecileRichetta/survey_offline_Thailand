from otree.api import *


doc = """
Treatment hope
"""


class C(BaseConstants):
    NAME_IN_URL = 'app_4'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    # CONSTANTS
    BINARY_ANSWER = [
        (0, 'ไม่เคย'), # No
        (1, 'เคย'), # Yes
        (998, 'ไม่ทราบ'), # Don't know
        (999, 'ขอไม่ตอบ') # Prefer not to say
    ]
    HOPE_READ = [
        (0, 'ตั้งใจ'),  # No
        (1, 'ไม่ตั้งใจ '),  # Yes
    ]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    text_check = models.IntegerField(
        label="4.1. จากข้อความข้างต้น นักวิจัยได้ข้อสรุปเกี่ยวกับโอกาสของความสำเร็จในการสร้างความปรองดองในภาคใต้แล้วใช่หรือไม่?",
        # Have the researchers already reached a conclusion about the chances of success of reconciliation in the Deep South?
        choices=C.BINARY_ANSWER,
        widget=widgets.RadioSelect,
        blank=False
    )
    hope_recall = models.IntegerField(
        label="4.2.ท่านเคยรู้สึกมีความหวังบ้างหรือไม่ว่ากระบวนการสันติภาพในจังหวัดชายแดนภาคใต้จะประสบความสำเร็จได้ กรุณาใช้เวลาสักครู่เพื่อทบทวนเรื่องนี้",
        # Can you recall a moment in time that made you feel hopeful that the peace process in southern Thailand is achievable? Please take some time to think about it.
        choices=C.BINARY_ANSWER,
        widget=widgets.RadioSelect,
        blank=False
    )
    hope_reason = models.LongStringField(
        label="4.3. ถ้าเคยมีความรู้สึกเช่นนั้น ช่วยกรุณาเล่าให้เราฟังภายใน 1-2 ประโยค",
        # If yes, could you please share this memory with me, in one or two sentences?
        blank=True
    )

# PAGES
class Page1_1(Page):
    form_model = 'player'
    @staticmethod
    def get_form_fields(player: Player):
        """Only return form fields if the page is displayed"""
        participant = player.participant #
        if participant.treatment_hope == 1 and player.session.config['name'] == "session_C4P_THAI_w1":
            return [
                'text_check',
                'hope_recall',
                'hope_reason'
            ]
        else:
            return []
    def is_displayed(player):
        participant = player.participant
        return participant.treatment_hope == 1 and player.session.config['name'] == "session_C4P_THAI_w1"


class Page1_2(Page):
    form_model = 'player'
    @staticmethod
    def get_form_fields(player: Player):
        """Only return form fields if the page is displayed"""
        participant = player.participant #
        if participant.treatment_hope == 0 and player.session.config['name'] == "session_C4P_THAI_w1":
            return [
                'text_check'
            ]
        else:
            return []
    def is_displayed(player):
        participant = player.participant
        return participant.treatment_hope == 0 and player.session.config['name'] == "session_C4P_THAI_w1"


page_sequence = [
    Page1_1,
    Page1_2
]
