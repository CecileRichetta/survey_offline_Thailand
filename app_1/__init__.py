from otree.api import *
import csv
from datetime import datetime

doc = """
Consent form for Pilot Study

Elements
- app_1 form -> end of the study if participant does not app_1 

"""


class C(BaseConstants):
    NAME_IN_URL = 'module_1'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    # PAYMENT INFO VARIABLES
    TEMPLATE_CONSENT_FORM_W1 = '_static/texts/consent_form_w1.html'
    DATA_TREATMENT_W1_LOC = '_static/data_internal/for_wave_2/'
    TEMPLATE_CONSENT_FORM_W2 = '_static/texts/consent_form_w2.html'
    # FOR PAYOFF CALCULATION
    TOKEN_ENDOWMENT = 4

class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    enumerator = models.StringField(
        label="ระบุหมายเลขประจำตัวผู้เก็บข้อมูล", # enter your enumerator identifier
        blank=False
    )
    timestamp = models.StringField()
    consent = models.BooleanField(choices=[[True, 'ข้าพเจ้ายินดีที่จะเข้าร่วมในงานวิจัยนี้ '],
                                           [False, 'ข้าพเจ้าไม่ยินดีที่จะเข้าร่วมในงานวิจัยนี้']],
                                  label='ข้าพเจ้ายืนยันว่าเข้าใจข้อมูลข้างต้นดีแล้ว',
                                  widget=widgets.RadioSelect)
    p_label = models.StringField()


# FUNCTIONS
def extract_participant_w1(p):
    participant = p.participant
    with open("_static/data_internal/for_wave_2/participant_wave_1.csv", 'r') as file:
        reader = csv.DictReader(file)
        for row in reader:
            if row['Participant_label'] == participant.label:
                participant.group = int(row['Participant_group'])
                participant.etv = int(row['Participant_etv'])
                participant.treatment_hope = int(row['Participant_treatment_hope'])
                participant.side_ultimatum = int(row['Participant_side_ultimatum'])
                participant.treatment_other = int(row['Participant_treatment_other'])
                break


# PAGES
class Page0(Page):
    pass
    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        if player.session.config['name'] == "session_C4P_THAI_w2":
            participant.military_binary = 997
            extract_participant_w1(player)
        else:
            pass

class Page1(Page):
    form_model = 'player'
    form_fields = ['enumerator']

class Page2(Page):
    form_model = 'player'
    form_fields = ['consent']

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        current_datetime = datetime.now()
        player.timestamp = current_datetime.strftime("%Y-%m-%d %H:%M:%S")
        participant = player.participant
        participant.vars['consent'] = player.consent
        participant.dropout = not player.consent
        player.p_label = participant.label

    def app_after_this_page(player: Player, upcoming_apps):
        if not player.consent:
            participant = player.participant
            participant.dropout = True  # custom field in Player model
            participant.treatment_hope = 999
            participant.participation_fee = 0
            return upcoming_apps[-1]

page_sequence = [
    Page0, # welcome + extract info wave 1
#    Page1, # enumerator identifier
    Page2 # consent form
]
