from otree.api import *
from functools import wraps
from pathlib import Path
from datetime import datetime
import csv
import os

doc = """
Support for peace agreement provisions. 
"""

def treatment_other_check_g0_choices(player):
    import random
    shuffled = [
        (0, 'บุคคลผู้นี้เป็นคนเชื้อสายมลายูที่เคยอาศัยอยู่ในภาคใต้ตอนล่าง'),
        (1, 'บุคคลนั้นเป็นคนเชื้อสายไทย'),
    ]
    fixed = [(998, 'ไม่ทราบ'), (999, 'ขอไม่ตอบ')]
    random.shuffle(shuffled)
    return shuffled + fixed

def treatment_other_check_g3_choices(player):
    import random
    shuffled = [(0, 'ฝ่ายขบวนการ'), (1, 'กองทัพ')]
    fixed = [(998, 'ไม่ทราบ'), (999, 'ขอไม่ตอบ')]
    random.shuffle(shuffled)
    return shuffled + fixed

def treatment_other_check_g4_choices(player):
    import random
    shuffled = [(0, 'ฝ่ายขบวนการ'), (1, 'กองทัพ')]
    fixed = [(998, 'ไม่ทราบ'), (999, 'ขอไม่ตอบ')]
    random.shuffle(shuffled)
    return shuffled + fixed

class C(BaseConstants):
    NAME_IN_URL = 'app_9'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    PARTICIPATION_FEE = 30
    # CHOICES
    CHOICE_PEACE_SUPPORT = [
        (0, "ไม่สนับสนุนเลย"), # Not at all
        (1, "สนับสนุนเล็กน้อย"), # Just a little
        (2, "สนับสนุนพอสมควร"), # Somewhat
        (3, "สนับสนุนมาก"), # A lot
        (4, "สนับสนุนมากที่สุด"), # Completely
        (998, "ไม่ทราบ"), # Don't know
        (999, "ขอไม่ตอบ") # Prefer not to say
    ]
    CHOICE_NGO_NAME = [
        (0, "1. สภาประชาสังคมชายแดนใต้ เครือข่ายองค์กรประชาสังคม 45 กลุ่มที่มีความหลากหลายทางชาติพันธุ์และศาสนาซึ่งทำงานเพื่อส่งเสริมการแก้ปัญหาความขัดแย้งในชายแดนใต้ด้วยสันติวิธี"),
        (1, "2. สมาคมด้วยใจเพื่อการช่วยเหลือด้านมนุษยธรรม กลุ่มประชาสังคมที่ขับเคลื่อนโดยผู้หญิงชาวมุสลิมซึ่งทำงานด้านมนุษยธรรมและสิทธิมนุษยชน โดยเน้นหนักไปที่พื้นที่จังหวัดชายแดนภาคใต้"),
        (2, "3. เครือข่ายชาวพุทธเพื่อสันติภาพ กลุ่มประชาสังคมที่ทำงานกับชุมชนชาวพุทธในจังหวัดชายแดนภาคใต้เพื่อหนุนเสริมกระบวนการสันติภาพและส่งเสริมการอยู่ร่วมกันในสังคมที่มีความแตกต่างหลากหลาย")
    ]
    HOPE_SCALE = [
        (0, "สิ้นหวังมาก"), # Very hopeless
        (1, "สิ้นหวัง"), # Hopeless
        (2, "ไม่เชิงสิ้นหวังหรือมีความหวัง "), # Neither hopeless nor hopeful
        (3, "มีความหวัง"), # Hopeful
        (4, "มีความหวังมาก"), # Very hopeful
        (998, "ไม่ทราบ"), # Don't know
        (999, "ขอไม่ตอบ") # Prefer not to say
    ]



class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    justice_provision_1 = models.IntegerField(
        label="9.1. ในด้านที่เกี่ยวกับความขัดแย้ง ท่านสนับสนุนมาตรการต่อไปนี้มากน้อยเพียงใด: นิรโทษกรรมให้อดีตสมาชิกขบวนการติดอาวุธที่ต่อสู้กับรัฐทุกคน",
        # Regarding the conflict, please tell me how much do you support the following initiative: Amnesty of all previous fighters.
        choices=C.CHOICE_PEACE_SUPPORT,
        widget=widgets.RadioSelect,
        blank=False
    )
    military_provision_2 = models.IntegerField(
        label="9.2. ในด้านที่เกี่ยวกับความขัดแย้ง ท่านสนับสนุนมาตรการต่อไปนี้มากน้อยเพียงใด: การหยุดยิง",
        # Regarding the conflict, please tell me how much do you support the following initiative: A ceasefire.
        choices=C.CHOICE_PEACE_SUPPORT,
        widget=widgets.RadioSelect,
        blank=False
    )
    military_provision_3 = models.IntegerField(
        label="9.3. ในด้านที่เกี่ยวกับความขัดแย้ง ท่านสนับสนุนมาตรการต่อไปนี้มากน้อยเพียงใด: การปลดอาวุธและเปิดโอกาสให้อดีตสมาชิกขบวนการติดอาวุธที่ต่อสู้กับรัฐได้กลับคืนสู่สังคมในฐานะพลเรือน",
        # Regarding the conflict, please tell me how much do you support the following initiative: Disarmament and reintegration of previous fighters in civilian life.
        choices=C.CHOICE_PEACE_SUPPORT,
        widget=widgets.RadioSelect,
        blank=False
    )
    military_provision_4 = models.IntegerField(
        label="9.4. ในด้านที่เกี่ยวกับความขัดแย้ง ท่านสนับสนุนมาตรการต่อไปนี้มากน้อยเพียงใด: การถอนกำลังทหารออกจากภาคใต้ตอนล่าง",
        # Regarding the conflict, please tell me how much do you support the following initiative: Troops withdrawals from the Deep South.
        choices=C.CHOICE_PEACE_SUPPORT,
        widget=widgets.RadioSelect,
        blank=False
    )
    political_provision_3 = models.IntegerField(
        label="9.5. ในด้านที่เกี่ยวกับความขัดแย้ง ท่านสนับสนุนมาตรการต่อไปนี้มากน้อยเพียงใด: การพูดคุยสันติภาพ",
        # Regarding the conflict, please tell me how much do you support the following initiative: Peace talks.
        choices=C.CHOICE_PEACE_SUPPORT,
        widget=widgets.RadioSelect,
        blank=False
    )
    territorial_provision_2 = models.IntegerField(
        label="9.6. ในด้านที่เกี่ยวกับความขัดแย้ง ท่านสนับสนุนมาตรการต่อไปนี้มากน้อยเพียงใด: เสรีภาพทางด้านวัฒนธรรม",
        #  Regarding the conflict, please tell me how much do you support the following initiative: Cultural freedom.
        choices=C.CHOICE_PEACE_SUPPORT,
        widget=widgets.RadioSelect,
        blank=False
    )
    territorial_provision_6 = models.IntegerField(
        label="9.7. ในด้านที่เกี่ยวกับความขัดแย้ง ท่านสนับสนุนมาตรการต่อไปนี้มากน้อยเพียงใด: สิทธิในการปกครองตนเองระดับภูมิภาค/ท้องถิ่น",
        # Regarding the conflict, please tell me how much do you support the following initiative: Local regional autonomy.
        choices=C.CHOICE_PEACE_SUPPORT,
        widget=widgets.RadioSelect,
        blank=False
    )
    territorial_provision_7 = models.IntegerField(
        label="9.8. ในด้านที่เกี่ยวกับความขัดแย้ง ท่านสนับสนุนมาตรการต่อไปนี้มากน้อยเพียงใด: การแบ่งสรรปันอำนาจระดับภูมิภาค/ท้องถิ่น เช่น คนเชื้อสายมลายู ไทย จีนมีส่วนร่วมในการปกครองระดับท้องถิ่น",
        # Regarding the conflict, please tell me how much do you support the following initiative: Local regional power-sharing.
        choices=C.CHOICE_PEACE_SUPPORT,
        widget=widgets.RadioSelect,
        blank=False
    )
    territorial_provision_9 = models.IntegerField(
        label="9.9. ในด้านที่เกี่ยวกับความขัดแย้ง ท่านสนับสนุนมาตรการต่อไปนี้มากน้อยเพียงใด: การพัฒนาทางเศรษฐกิจและสังคมระดับภูมิภาค",
        # Regarding the conflict, please tell me how much do you support the following initiative: Regional economic and social development.
        choices=C.CHOICE_PEACE_SUPPORT,
        widget=widgets.RadioSelect,
        blank=False
    )
    ngo_binary = models.BooleanField(
        label="9.10. ท่านต้องการบริจาคส่วนหนึ่งของค่าตอบแทนการตอบแบบสอบถามหรือไม่",
        # 9.10. Do you want to give part of your participation fee?
        choices=[
            (False, "ไม่ต้องการ"),
            (True, "ต้องการ")
        ],
        blank=False
    )
    ngo_amount = models.IntegerField(
        label="9.11. ถ้าใช่ บริจาคเป็นจำนวนเท่าใด",
        max=200,
        blank=True
    )
    ngo_name = models.IntegerField(
        label="9.12. ให้กับองค์กรพัฒนาเอกชนใด",
        choices=C.CHOICE_NGO_NAME,
        widget=widgets.RadioSelect,
        blank=True
    )
    hope_check = models.IntegerField(
        label="9.13. ท่านมีความหวังมากน้อยเพียงใดว่ารัฐบาลไทยกับกลุ่มติดอาวุธในภาคใต้จะสามารถแสวงหาข้อตกลงร่วมกันโดยผ่านการเจรจาสันติภาพได้ ",
        # How hopeful do you feel right now about the possibility of a peace process bewteen the central Thai government and armed groups in the Deep South?
        choices= C.HOPE_SCALE,
        blank=False,
        widget=widgets.RadioSelect
    )
    treatment_other_check_g0 = models.IntegerField(
        label="9.14.3. ระหว่างการทำกิจกรรมในแบบสำรวจรอบนี้และรอบที่แล้ว ท่านได้มีปฏิสัมพันธ์กับคู่สนทนาท่านหนึ่ง  ท่านคิดว่าคู่สนทนาของท่านเป็นใคร:",
        blank=False,
        widget=widgets.RadioSelect
    )
    treatment_other_check_g3 = models.IntegerField(
        label="9.14.1. ในระหว่างกิจกรรม ท่านได้จับคู่กับบุคคลเชื้อสายมลายูที่เคยอาศัยอยู่ในภาคใต้ตอนล่างและเป็นอดีตทหาร  ท่านคาดเดาได้หรือไม่ว่าคู่ของท่านสังกัดฝ่ายใด?",
        blank=False,
        widget=widgets.RadioSelect
    )
    treatment_other_check_g4 = models.IntegerField(
        label="9.14.2. ในระหว่างกิจกรรม  ท่านได้เล่นกับคู่ของท่านที่เป็นคนเชื้อสายไทยและเป็นอดีตทหาร ท่านคาดเดาได้หรือไม่ว่าคู่ของท่านคุณอยู่ฝ่ายใด?",
        blank=False,
        widget=widgets.RadioSelect
    )

# DECORATEUR
def simple_safe_operation(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except Exception as e:
            print(f"Erreur dans {func.__name__}: {e}")
            return None
    return wrapper

# FUNCTIONS
@simple_safe_operation
def export_payoffs_headenumerator(player):
    participant = player.participant
    data_folder = Path("_static/data_internal/payoffs")
    timestamp = datetime.now().strftime("%Y_%m_%d_%H:%M")
    csv_file_path = data_folder / "payoffs.csv"
    temp_file = csv_file_path.with_suffix('.tmp')

    data_folder.mkdir(parents=True, exist_ok=True)

    fieldnames = [
        'participant_label', 'date_interview', 'participation_fee',
        'payoff_games', 'total_compensation'
    ]
    new_row = {
        'participant_label': participant.label,
        'date_interview': timestamp,
        'participation_fee': participant.participation_fee,
        'payoff_games': participant.payoff_games,
        'total_compensation': participant.total_compensation
    }

    try:
        if csv_file_path.exists():
            # Copy original to temp, then append new row
            with open(csv_file_path, 'r', newline='') as original:
                with open(temp_file, 'w', newline='') as temp:
                    temp.write(original.read())
            with open(temp_file, 'a', newline='') as temp:
                writer = csv.DictWriter(temp, fieldnames=fieldnames)
                writer.writerow(new_row)
        else:
            # Create new file with header
            with open(temp_file, 'w', newline='') as temp:
                writer = csv.DictWriter(temp, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerow(new_row)

        # Replace original with temp
        os.replace(temp_file, csv_file_path)

    except Exception as e:
        if temp_file.exists():
            os.remove(temp_file)
        print(f"Erreur dans export_payoffs_headenumerator: {e}")
        raise e


# PAGES
class Page1(Page):
    form_model = 'player'
    form_fields = [
            'justice_provision_1',
            'military_provision_2',
            'military_provision_3',
            'military_provision_4',
            'political_provision_3',
            'territorial_provision_2',
            'territorial_provision_6',
            'territorial_provision_7',
            'territorial_provision_9'
        ]

class Page2(Page):
    form_model = 'player'
    form_fields = [
        'ngo_binary',
        'ngo_amount',
        'ngo_name'
    ]

    @staticmethod
    def before_next_page(player, timeout_happened):
        participant = player.participant
        if player.ngo_binary==True and player.ngo_amount !=997:
            participant.participation_fee = 200 - player.ngo_amount
        else:
            participant.participation_fee=200
        participant.total_compensation = participant.participation_fee + participant.payoff_games
        export_payoffs_headenumerator(player)
    def error_message(player, values):
        # If they want to donate (ngo_binary == True), they must specify amount and NGO
        if values['ngo_binary'] == True:
            if values.get('ngo_amount') is None:
                return 'โปรดระบุจำนวนเงินที่ต้องการบริจาค'
            if values.get('ngo_name') is None:
                return 'โปรดเลือกองค์กรพัฒนาเอกชน (NGO)'



class Page3(Page):
    form_model = 'player'
    @staticmethod
    def get_form_fields(player: Player):
        """Only return form fields if the page is displayed"""
        participant = player.participant
        if player.session.config['name'] == "session_C4P_THAI_w1":
            return ['hope_check']
        elif player.session.config['name'] == "session_C4P_THAI_w2":
            if participant.treatment_other == 0:
                return [
                    'hope_check',
                    'treatment_other_check_g0'
                ]
            elif participant.treatment_other == 3:
                return [
                    'hope_check',
                    'treatment_other_check_g3'
                ]
            elif participant.treatment_other == 4:
                return [
                    'hope_check',
                    'treatment_other_check_g4'
                ]
            else:
                return ['hope_check']



page_sequence = [
    Page1,
    Page2,
    Page3
]
