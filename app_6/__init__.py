from otree.api import *
from functools import wraps
import csv
import os
import math
from pathlib import Path

doc = """
Public Goods Game
"""


class C(BaseConstants):
    NAME_IN_URL = 'app_6'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    # GAME ELEMENTS
    TOKEN_VALUE = 10
    TOKEN_ENDOWMENT = 4
    CHOICES_PG = [
        (0, 'ฉันต้องการเก็บไว้ทั้งหมด 4 เหรียญ'), # I want to keep all my 4 tokens.
        (1, 'ฉันต้องการเก็บไว้ 3 เหรียญและหยอดกระปุกกลาง 1 เหรียญ'), # I want to keep 3 tokens and contribute 1 token to the group bag.
        (2, 'ฉันต้องการเก็บไว้ 2 เหรียญและหยอดกระปุกกลาง 2 เหรียญ'), # I want to keep 2 tokens and contribute 2 tokens to the group bag.
        (3, 'ฉันต้องการเก็บไว้ 1 เหรียญและหยอดกระปุกกลาง 3 เหรียญ'), # I want to keep 1 token and contribute 3 tokens to the group bag.
        (4, 'ฉันไม่ต้องการเก็บเหรียญไว้เลย และต้องการหยอดทั้ง 4 เหรียญในกระปุกกลาง') # I want to keep nothing and contribute all 4 tokens to the group bag.
    ]
    # FILE PATH TREATMENT BALANCE TABLE
    FILE_PATH_TREATMENT = '_static/data_external/treatment_balance.csv'
    # INSTRUCTIONS TEMPLATES
    TEMPLATE_INSTRUCTIONS_ULTIMATUM_PROPOSER = '_static/texts/instr_ultimatum_proposer.html'
    TEMPLATE_INSTRUCTIONS_ULTIMATUM_RESPONDER = '_static/texts/instr_ultimatum_receiver.html'
    TEMPLATE_INSTRUCTIONS_PG = '_static/texts/instr_pg.html'
    # IMAGES TEMPLATES
    IMAGE_PG_INSTR = 'imgs/diagram_PG.png'
    IMAGE_PG_EXAMPLE1 = 'imgs/diagram_PG_example1.png'
    IMAGE_PG_EXAMPLE2 = 'imgs/diagram_PG_example2.png'
    # RISK AVERSION
    RISK_AVERSION = [
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
    # COMPREHENSION CHECKS + VERIFICATION
    pg_cc1 = models.IntegerField(
        label="6.1. โปรดระบุว่าข้อความต่อไปนี้เป็นเรื่องจริงหรือเท็จ: ฉันสามารถตัดสินใจไม่ใส่เหรียญในกระปุกกลางแม้แต่เหรียญเดียว",
        # Please indicate whether the following statements are true or false: I can decide to put zero token in the common bag.
        choices=[
            (1, 'จริง'), # True
            (0, 'เท็จ') # False
        ],
        blank=False,
        widget=widgets.RadioSelectHorizontal
    )
    pg_cc2 = models.IntegerField(
        label="6.2. โปรดระบุว่าข้อความต่อไปนี้เป็นเรื่องจริงหรือเท็จ: คู่ของท่านรู้ว่าท่านใส่เหรียญเข้าไปในกระปุกกลางเท่าใด ก่อนที่เขาจะตัดสินใจ",
        # Please indicate whether the following statements are true or false: The other person knows how much I put in the common bag before making their decision.
        choices=[
            (0, 'จริง'), # True
            (1, 'เท็จ') # False
        ],
        blank=False,
        widget=widgets.RadioSelectHorizontal
    )
    pg_cc3 = models.IntegerField(
        label="6.3. โปรดระบุว่าข้อความต่อไปนี้เป็นเรื่องจริงหรือเท็จ: คู่ของท่านไม่มีตัวตนจริง",
        # Please indicate whether the following statements are true or false: The other person is fake.
        choices=[
            (0, 'จริง'), # True
            (1, 'เท็จ') # False
        ],
        blank=False,
        widget=widgets.RadioSelectHorizontal
    )
    pg_correct_answers = models.IntegerField()
    pg_redo_questions = models.BooleanField(
        label="6.4. คำตอบบางส่วนของท่านต่อคำถามก่อนหน้านี้ไม่ถูกต้อง เราอยากให้ท่านมีโอกาสรับฟังวิธีการทำกิจกรรมอย่างครบถ้วนและมีโอกาสตอบคำถามอีกครั้ง ท่านประสงค์ที่จะรับฟังวิธีการทำกิจกรรมและตอบคำถามอีกครั้งหรือไม่",
        # Some of your answers in the previous questions were not correct. I want to give you the opportunity to listen once more to the full instructions, and answer the questions. Do you want me to listen the instructions and answer once again the questions?
        choices=[
            (True, "ใช่"),
            (False, "ไม่ใช่")
        ],
        widget=widgets.RadioSelectHorizontal)
    # CHOICES IN PG
    decision_pg = models.IntegerField(
        label="",
        choices=C.CHOICES_PG,
        blank=False,
        widget=widgets.RadioSelect
    )
    # RISK AVERSION CHECK
    risk_aversion = models.IntegerField(
        label="6.6. คุณเห็นด้วยกับข้อความต่อไปนี้มากน้อยเพียงใด: โดยทั่วไปแล้ว ฉันพร้อมที่จะรับความเสี่ยงอย่างเต็มที่",
        # How much do you agree with the following statement: Generally speaking, I am person fully prepared to take risks.
        choices=C.RISK_AVERSION,
        widget=widgets.RadioSelect,
        blank=False
    )
    time_preference_6m = models.IntegerField(
        label="6.7. สมมติว่าท่านสามารถเลือกระหว่างการรับเงิน 10,000 บาททันทีหรือเลือกที่จะรับเงินเพิ่มขึ้นแต่ต้องรออีก 6 เดือน  เงินในอนาคตที่จะได้รับควรมีจำนวนเท่าใดจึงจะน่าสนใจมากกว่าการตัดสินใจรับเงิน 10,000 บาทในตอนนี้",
        # Imagine you could choose between receiving 10'00'BAHT immediately, or another amount 6 months from now. How much would the future amount need to be to make it as attractive as receiving $300 immediately?
        blank=False
    )
    time_preference_1y = models.IntegerField(
        label="6.8. สมมติว่าท่านสามารถเลือกระหว่างการรับเงิน 10,000 บาททันทีหรือเลือกที่จะรับเงินเพิ่มขึ้นแต่ต้องรออีก 1 ปี เงินในอนาคตที่จะได้รับควรมีจำนวนเท่าใดจึงจะน่าสนใจมากกว่าการตัดสินใจรับเงิน 10,000 บาทในตอนนี้",
        # Imagine you could choose between receiving $300 immediately, or another amount 1 year from now. How much would the future amount need to be to make it as attractive as receiving $300 immediately?
        blank=False
    )
    time_preference_10y = models.IntegerField(
        label="6.9. สมมติว่าท่านสามารถเลือกระหว่างการรับเงิน 10,000 บาททันทีหรือเลือกที่จะรับเงินเพิ่มขึ้นแต่ต้องรออีก 10 ปี  เงินในอนาคตที่จะได้รับควรมีจำนวนเท่าใดจึงจะน่าสนใจมากกว่าการตัดสินใจรับเงิน 10,000 บาทในตอนนี้",
        # Imagine you could choose between receiving $300 immediately, or another amount 10 years from now. How much would the future amount need to be to make it as attractive as receiving $300 immediately?
        blank=False
    )
    #
    def tokens_kept(self):
        contribution = self.participant.vars.get('decision_PG', 0)
        return C.TOKEN_ENDOWMENT - contribution


# FUNCTIONS
# VERSION SIMPLE ET ROBUSTE pour tes fonctions
def simple_safe_operation(func):
    """
    Version simple qui protège juste contre les crashes
    """

    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Erreur dans {func.__name__}: {e}")
            # Log l'erreur mais ne crash pas le participant
            return None

    return wrapper


def export_participant_data_append_only(player):
    participant = player.participant
    data_folder = Path("_static/data_internal/for_wave_2")

    if player.session.config['name'] == "session_C4P_THAI_w1":
        csv_file_path = data_folder / "participant_wave_1.csv"
        data_folder.mkdir(parents=True, exist_ok=True)

        fieldnames = [
            'Participant_label', 'Participant_group', 'Participant_etv',
            'Participant_treatment_hope', 'Participant_side_ultimatum',
            'Participant_treatment_other'
        ]
        new_row = {
            'Participant_label': participant.label,
            'Participant_group': participant.group,
            'Participant_etv': participant.etv,
            'Participant_treatment_hope': participant.treatment_hope,
            'Participant_side_ultimatum': participant.side_ultimatum,
            'Participant_treatment_other': participant.treatment_other
        }

        temp_file = csv_file_path.with_suffix('.tmp')
        try:
            if csv_file_path.exists():
                # Write new row to temp file first
                with open(temp_file, 'w', newline='') as f:
                    writer = csv.DictWriter(f, fieldnames=fieldnames)
                    writer.writerow(new_row)
                # Append temp content to main file
                with open(temp_file, 'r') as temp:
                    with open(csv_file_path, 'a') as main:
                        main.write(temp.read())
                os.remove(temp_file)
            else:
                # Create new file with header
                with open(csv_file_path, 'w', newline='') as f:
                    writer = csv.DictWriter(f, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerow(new_row)
        except Exception as e:
            if temp_file.exists():
                os.remove(temp_file)
            raise e


def export_games_data_append_only(player):
    participant = player.participant
    data_folder = Path("_static/data_internal/for_wave_2")

    if player.session.config['name'] == "session_C4P_THAI_w1":
        csv_file_path = data_folder / "games_wave_1.csv"
        data_folder.mkdir(parents=True, exist_ok=True)

        fieldnames = ['group', 'etv', 'side_ultimatum', 'decision_UG', 'decision_PG']
        new_row = {
            'group': participant.group,
            'etv': participant.etv,
            'side_ultimatum': participant.side_ultimatum,
            'decision_UG': participant.decision_UG,
            'decision_PG': participant.decision_PG
        }

        temp_file = csv_file_path.with_suffix('.tmp')
        try:
            if csv_file_path.exists():
                with open(temp_file, 'w', newline='') as f:
                    writer = csv.DictWriter(f, fieldnames=fieldnames)
                    writer.writerow(new_row)
                with open(temp_file, 'r') as temp:
                    with open(csv_file_path, 'a') as main:
                        main.write(temp.read())
                os.remove(temp_file)
            else:
                with open(csv_file_path, 'w', newline='') as f:
                    writer = csv.DictWriter(f, fieldnames=fieldnames)
                    writer.writeheader()
                    writer.writerow(new_row)
        except Exception as e:
            if temp_file.exists():
                os.remove(temp_file)
            raise e


def increment_participant_count(csv_file_path, participant):
    try:
        with open(csv_file_path, 'r') as f:
            lines = f.readlines()
    except FileNotFoundError:
        lines = ["group_participant;etv;treatment_hope;side_UG;treatment_other;nb_participant\n"]

    search_line = f"{participant.group};{participant.etv};{participant.treatment_hope};{participant.side_ultimatum};{participant.treatment_other};"

    found = False
    for i, line in enumerate(lines):
        if line.startswith(search_line):
            parts = line.strip().split(';')
            parts[-1] = str(int(parts[-1]) + 1)
            lines[i] = ';'.join(parts) + '\n'
            found = True
            break

    if not found:
        lines.append(f"{search_line}1\n")

    with open(csv_file_path, 'w') as f:
        f.writelines(lines)


def correct_answers_pg(player):
    cc1 = player.field_maybe_none('pg_cc1')
    cc2 = player.field_maybe_none('pg_cc2')
    cc3 = player.field_maybe_none('pg_cc3')
    if None in (cc1, cc2, cc3):
        player.pg_correct_answers = 0
    else:
        player.pg_correct_answers = cc1 + cc2 + cc3


def payoff_PG(participant):
    common_bag = participant.decision_PG + participant.other_PG_decision
    participant.payoff_PG = (C.TOKEN_ENDOWMENT - participant.decision_PG) + (
            (common_bag + (common_bag / 2)) / 2)


def total_payoff(participant):
    participant.total_payoff_token = participant.payoff_UG + participant.payoff_PG
    participant.payoff_games = math.ceil(C.TOKEN_VALUE * participant.total_payoff_token)

# PAGES
class Page1(Page):  # instructions PG
    form_model = 'player'
    form_fields = [
        'pg_cc1',
        'pg_cc2',
        'pg_cc3'
    ]

    @staticmethod
    def before_next_page(player, timeout_happened):
        correct_answers_pg(player)


class Page2(Page):  # comprehension checks PG
    form_model = 'player'
    form_fields = ['pg_redo_questions']

    @staticmethod
    def is_displayed(player):
        return player.pg_correct_answers < 3


class Page3(Page):  # re-read instructions PG
    form_model = 'player'
    form_fields = [
        'pg_cc1',
        'pg_cc2',
        'pg_cc3'
    ]

    @staticmethod
    def before_next_page(player, timeout_happened):
        correct_answers_pg(player)

    def is_displayed(player):
        return player.pg_correct_answers < 3 and player.pg_redo_questions


class Page4(Page):  # decision PG
    form_model = 'player'
    form_fields = [
        'decision_pg'
    ]

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        participant.decision_PG = player.decision_pg
        payoff_PG(participant)
        total_payoff(participant)
        if player.session.config['name'] == "session_C4P_THAI_w1":
            increment_participant_count(C.FILE_PATH_TREATMENT, participant)
        export_games_data_append_only(player)
        export_participant_data_append_only(player)


class Page5(Page):
    pass


class Page6(Page):  # risk aversion
    form_model = 'player'
    form_fields = [
        'risk_aversion',
        'time_preference_6m',
        'time_preference_1y',
        'time_preference_10y'
    ]


page_sequence = [
    Page1, # instructions
    Page2, # re-do instructions ?
    Page3, # instructions round 2
    Page4, # public goods game decision
#    Page5, # payoff
    Page6 # risk aversion
]
