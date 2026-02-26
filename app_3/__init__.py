from otree.api import *
import random
import csv

doc = """
Questions military service and exposure to violence"""


class C(BaseConstants):
    NAME_IN_URL = 'app_3'
    PLAYERS_PER_GROUP = None
    NUM_ROUNDS = 1
    # EXTERNAL DATA
    DATA_TREATMENT_LOC = '_static/data_external/treatment_balance.csv'
    # CHOICES IN VARIABLES
    BINARY_ANSWER = [
        (1, 'เคย'),  # Yes
        (0, 'ไม่เคย'), # No
        (999, 'ขอไม่ตอบ') # Prefer not to say
    ]
    BINARY_ANSWER_NA = [
        (1, 'เคย'),  # Yes
        (0, 'ไม่เคย'), # No
        (997, 'ไม่เกี่ยวข้อง'), # Not applicable
        (999, 'ขอไม่ตอบ') # Prefer not to say
    ]
    MILITARY_CONSCRIPTION = [
        (0, 'สมัครใจไปเอง'), # I volunteered
        (1, 'ใบแดง/ผ่านการจับฉลากเกณฑ์ทหาร'), # Through the national draft lottery
        (999, 'ขอไม่ตอบ')  # Prefer not to say
    ]
    MILITARY_DUTY = [
        (0, 'หน้าที่ด้านความมั่นคงของชาติ (จุดตรวจและด่านตรวจ; หน่วยลาดตระเวน; ปฏิบัติการปิดล้อมและตรวจค้น; รักษาความปลอดภัยครูและพระสงฆ์; การบังคับใช้กฎอัยการศึกและพระราชกำหนดการบริหารราชการในสถานการณ์ฉุกเฉิน)'),
        # National security duties (checkpoints and roadblocks; patrol units; surround-and-search operations; security for teachers and monks; enforcing Martial Law and the Emergency Decree)
        (1, 'หน้าที่ด้านกิจการพลเรือน (บรรเทาสาธารณภัย ซ่อมแซมบ้าน โครงการอาสาสมัครพระราชทาน)'),
        # Civic affairs duties (disaster relief; home repairs; royal volunteer projects)
        (2, 'หน้าที่บริการภายในหน่วยทหาร (ทำความสะอาด ทำสวน ทำอาหาร บำรุงรักษารถยนต์ ขับรถ งานธุรการและเอกสาร หน้าที่รักษาการณ์ภายในค่าย ผู้ช่วยเจ้าหน้าที่ทหาร)'),
        # Internal services in military units duties (cleaning; gardening; cooking; vehicule maintenance; driving; clerical work and paperwork; guard duties within compounds; military officers' aides)
        (999, 'ขอไม่ตอบ')  # Prefer not to say
    ]
    PROVINCE_THAILAND = [
        (1, 'กรุงเทพมหานคร'),  # Bangkok
        (2, 'กระบี่'),  # Krabi
        (3, 'กาญจนบุรี'),  # Kanchanaburi
        (4, 'กาฬสินธุ์'),  # Kalasin
        (5, 'กำแพงเพชร'),  # Kamphaeng Phet
        (6, 'ขอนแก่น'),  # Khon Kaen
        (7, 'จันทบุรี'),  # Chanthaburi
        (8, 'ฉะเชิงเทรา'),  # Chachoengsao
        (9, 'ชลบุรี'),  # Chonburi
        (10, 'ชัยนาท'),  # Chainat
        (11, 'ชัยภูมิ'),  # Chaiyaphum
        (12, 'ชุมพร'),  # Chumphon
        (13, 'เชียงราย'),  # Chiang Rai
        (14, 'เชียงใหม่'),  # Chiang Mai
        (15, 'ตรัง'),  # Trang
        (16, 'ตราด'),  # Trat
        (17, 'ตาก'),  # Tak
        (18, 'นครนายก'),  # Nakhon Nayok
        (19, 'นครปฐม'),  # Nakhon Pathom
        (20, 'นครพนม'),  # Nakhon Phanom
        (21, 'นครราชสีมา'),  # Nakhon Ratchasima
        (22, 'นครศรีธรรมราช'),  # Nakhon Si Thammarat
        (23, 'นครสวรรค์'),  # Nakhon Sawan
        (24, 'นนทบุรี'),  # Nonthaburi
        (25, 'นราธิวาส'),  # Narathiwat
        (26, 'น่าน'),  # Nan
        (27, 'บึงกาฬ'),  # Bueng Kan
        (28, 'บุรีรัมย์'),  # Buriram
        (29, 'ปทุมธานี'),  # Pathum Thani
        (30, 'ประจวบคีรีขันธ์'),  # Prachuap Khiri Khan
        (31, 'ปราจีนบุรี'),  # Prachinburi
        (32, 'ปัตตานี'),  # Pattani
        (33, 'พะเยา'),  # Phayao
        (34, 'อยุธยา'),  # Ayutthaya (พระนครศรีอยุธยา)
        (35, 'พังงา'),  # Phang Nga
        (36, 'พัทลุง'),  # Phattalung
        (37, 'พิจิตร'),  # Phichit
        (38, 'พิษณุโลก'),  # Phitsanulok
        (39, 'เพชรบุรี'),  # Phetchaburi
        (40, 'เพชรบูรณ์'),  # Phetchabun
        (41, 'แพร่'),  # Phrae
        (42, 'ภูเก็ต'),  # Phuket
        (43, 'มหาสารคาม'),  # Maha Sarakham
        (44, 'มุกดาหาร'),  # Mukdahan
        (45, 'แม่ฮ่องสอน'),  # Mae Hong Son
        (46, 'ยโสธร'),  # Yasothon
        (47, 'ยะลา'),  # Yala
        (48, 'ร้อยเอ็ด'),  # Roi Et
        (49, 'ระนอง'),  # Ranong
        (50, 'ระยอง'),  # Rayong
        (51, 'ราชบุรี'),  # Ratchaburi
        (52, 'ลพบุรี'),  # Lopburi
        (53, 'ลำปาง'),  # Lampang
        (54, 'ลำพูน'),  # Lamphun
        (55, 'เลย'),  # Loei
        (56, 'ศรีสะเกษ'),  # Si Saket
        (57, 'สกลนคร'),  # Sakhon Nakhon
        (58, 'สงขลา'),  # Songkhla
        (59, 'สตูล'),  # Satun
        (60, 'สมุทรปราการ'),  # Samut Prakan
        (61, 'สมุทรสงคราม'),  # Samut Songkhram
        (62, 'สมุทรสาคร'),  # Samut Sakhon
        (63, 'สระแก้ว'),  # Sa Kaeo
        (64, 'สระบุรี'),  # Saraburi
        (65, 'สิงห์บุรี'),  # Singburi
        (66, 'สุโขทัย'),  # Sukhothaï
        (67, 'สุพรรณบุรี'),  # Suphanburi
        (68, 'สุราษฎร์ธานี'),  # Surat Thani
        (69, 'สุรินทร์'),  # Surin
        (70, 'หนองคาย'),  # Nong Khai
        (71, 'หนองบัวลำภู'),  # Nong Bua Lamphu
        (72, 'อ่างทอง'),  # Ang Thong
        (73, 'อำนาจเจริญ'),  # Amnat Charoen
        (74, 'อุดรธานี'),  # Udon Thani
        (75, 'อุตรดิตถ์'),  # Uttaradit
        (76, 'อุทัยธานี'),  # Uthai Thani
        (77, 'อุบลราชธานี'),  # Ubon Ratchathani
        (997, 'ต่างประเทศ '), # Not applicable: abroad
        (999, 'ขอไม่ตอบ')  # Prefer not to say
    ]
    MONTH = [
        (1, "มกราคม"),
        (2, "กุมภาพันธ์"),
        (3, "มีนาคม"),
        (4, "เมษายน"),
        (5, "พฤษภาคม"),
        (6, "มิถุนายน"),
        (7, "กรกฎาคม"),
        (8, "สิงหาคม"),
        (9, "กันยายน"),
        (10, "ตุลาคม"),
        (11, "พฤศจิกายน"),
        (12, "ธันวาคม"),
        (998, "ไม่ทราบ"),  # Don't know
        (999, 'ขอไม่ตอบ')  # Prefer not to say
    ]
    SCALE_EMPHASIS = [
        (0, 'ไม่มี'), # None
        (1, 'มีบ้าง'), # Some
        (2, 'มีมาก'), # A lot
        (998, "ไม่ทราบ"),  # Don't know
        (999, 'ขอไม่ตอบ')  # Prefer not to say
    ]
    SCALE_SUPPORT = [
        (0, 'ไม่ได้เลย'),  # Not at all
        (1, 'ได้บ้าง'),  # Somewhat
        (2, 'ได้ทุกเมื่อ'),  # Completely
        (998, "ไม่ทราบ"),  # Don't know
        (999, 'ขอไม่ตอบ')  # Prefer not to say
    ]
    SCALE_ETV = [
        (0, 'นานๆ ครั้ง'), # Rarely
        (1, 'บ่อย '), # Often
        (999, 'ขอไม่ตอบ')  # Prefer not to say
    ]


class Subsession(BaseSubsession):
    pass


class Group(BaseGroup):
    pass


class Player(BasePlayer):
    # MILITARY SERVICE
    military_binary = models.IntegerField(
        label="3.1  ท่านเคยเป็นทหารเกณฑ์หรือไม่ ",
        # Did you do your military service?
        choices=C.BINARY_ANSWER,
        widget=widgets.RadioSelect,
        blank=False
    )
    # QUESTIONS MILITARY
    conscription_binary = models.IntegerField(
        label="3.1.2. ถ้าใช่ ท่านเข้าไปเป็นทหารเกณฑ์ได้อย่างไร?",
        # If yes, how did you join the military?
        choices=C.MILITARY_CONSCRIPTION,
        widget=widgets.RadioSelect,
        blank=False
    )
    military_tasks = models.IntegerField(
        label="3.1.3  หน้าที่หลักของท่านในช่วงที่เป็นทหารเกณฑ์คืออะไร ",
        # What was your main duty during your military service?
        choices=C.MILITARY_DUTY,
        widget=widgets.RadioSelect,
        blank=False
    )
    military_province_main = models.IntegerField(
        label="3.1.4. ท่านเคยถูกส่งไปประจำที่จังหวัดใดเป็นหลัก",
        # in which province were you primarily deployed
        choices=C.PROVINCE_THAILAND,
        blank=False
    )
    maindeployment_start_year = models.IntegerField(
        label="3.1.5. ท่านถูกส่งไปประจำที่จังหวัดนั้นในปีไหน",
        choices=[
            [999, "ขอไม่ตอบ"],
            *[[y, str(y)] for y in range(2543, 2568)]
        ],
        blank=True
    )
    maindeployment_start_month = models.IntegerField(
        label="3.1.6. เดือนเริ่มต้น",
        choices=C.MONTH,
        blank=False

    )
    maindeployment_length = models.IntegerField(
        label="3.1.7. ท่านประจำการอยู่ที่จังหวัดนั้นนานเท่าได (จำนวนเดือน)",
        # For how long? (in months):
        min=0,
        max=99,
        blank=True
    )
    deployment_second = models.IntegerField(
        label="3.1.8. ท่านเคยถูกส่งไปประจำที่จังหวัดอื่นหรือไม่",
        # Were you deployed in any other province?
        choices=C.BINARY_ANSWER,
        widget=widgets.RadioSelect,
        blank=False
    )
    military_province_second = models.IntegerField(
        label="3.1.9. ถ้าใช่  ท่านเคยถูกส่งไปประจำที่จังหวัดใดบ้าง?",
        # If yes, in which province were you deployed?
        choices=C.PROVINCE_THAILAND,
        blank=True
    )
    seconddeployment_start_year = models.IntegerField(
        label="3.1.10. ท่านถูกส่งไปประจำที่จังหวัดนี้ตั้งแต่ปีไหน",
        # In which period were you deployed in this province? Buddhist era start year:
        choices=[
            [999, "ขอไม่ตอบ"],
            *[[y, str(y)] for y in range(2543, 2568)]
        ],
        blank=True
    )
    seconddeployment_start_month = models.IntegerField(
        label="3.1.11. เดือนเริ่มต้น",
        choices=C.MONTH,
        blank=True
    )
    seconddeployment_length = models.IntegerField(
        label="3.1.12. ท่านประจำการอยู่ที่จังหวัดนั้นนานเท่าได (จำนวนเดือน)",
        # For how long were you stationed in that province (number of months)?:
        min=0,
        max=99,
        blank=True
    )
    military_socialization_1 = models.IntegerField(
        label="3.1.13. ในช่วงของการเข้าเป็นทหารกองประจำการ มีการเน้นในเรื่องความเคารพต่อผู้มีอำนาจมากน้อยเพียงใด  ",
        # During your service, how much emphasis was placed on respect for authority?
        choices=C.SCALE_EMPHASIS,
        widget = widgets.RadioSelect,
        blank=False
    )
    military_socialization_2 = models.IntegerField(
        label="3.1.14. ในระหว่างที่ท่านเข้าเป็นทหารกองประจำการ มีการให้ความสำคัญกับการเข้าใจภัยคุกคามภายในประเทศในขณะนั้นมากน้อยเพียงใด เช่น ปัญหาความไม่สงบในจังหวัดชายแดนภาคใต้",
        # During your service, how much emphasis was placed on understand the domestic security threats of the time?
        choices=C.SCALE_EMPHASIS,
        widget = widgets.RadioSelect,
        blank=False
    )
    military_socialization_3 = models.IntegerField(
        label="3.1.15. ระหว่างการเป็นทหารกองประจำการ ท่านสามารถพึ่งพาความช่วยเหลือจากเพื่อนทหารเกณฑ์ได้มากน้อยเพียงใด ",
        # During your service, how much could you count on your peers for support?
        choices=C.SCALE_SUPPORT,
        widget = widgets.RadioSelect,
        blank=False
    )
    # QUESTIONS NON-MILITARY
    noncombatant_geography_main = models.IntegerField(
        label="3.2.1. ระหว่างช่วงอายุ 21 ปี ถึงปัจจุบัน ท่านพำนักอาศัยในจังหวัดใดเป็นหลัก",
        #
        choices= C.PROVINCE_THAILAND,
        blank=False
    )
    noncombatant_geography_main_start_year = models.IntegerField(
        label="3.2.2. ท่านอาศัยอยู่ในจังหวัดนั้นในปีไหน",
        # In which period did you reside in this province? Buddhist era start year:
        choices=[
            [999, "ขอไม่ตอบ"],
            *[[y, str(y)] for y in range(2536, 2568)]
        ],
        blank=True
    )
    noncombatant_geography_main_start_month = models.IntegerField(
        label="3.2.3. เริ่มในเดือน", # start month
        choices=C.MONTH,
        blank=False
    )
    noncombatant_geography_main_end_year = models.IntegerField(
        label="3.2.4. ถึงปีไหน",
        # 3.2.3. Until what year?:
        choices=[
            [999, "ขอไม่ตอบ"],
            *[[y, str(y)] for y in range(2543, 2569)]
        ],
        blank=True
    )
    noncombatant_geography_main_end_month = models.IntegerField(
        label="3.2.5. สิ้นสุดในเดือน ", # end month
        choices=C.MONTH,
        blank=False
    )
    noncombatant_geography_second_b = models.IntegerField(
        label="3.2.6. ระหว่างช่วงอายุ 21 ปี ถึงปัจจุบัน  ท่านได้อาศัยอยู่ในจังหวัดอื่นอีกหรือไม่?",
        # During that period, did you also live in another province?
        choices= C.BINARY_ANSWER,
        widget=widgets.RadioSelect,
        blank=False
    )
    noncombatant_geography_second = models.IntegerField(
        label="3.2.7. ถ้าใช่  ท่านไปอาศัยอยู่ที่จังหวัดใด",
        # If yes, in which province did you also reside?
        choices= C.PROVINCE_THAILAND,
        blank=True
    )
    noncombatant_geography_second_start_year = models.IntegerField(
        label="3.2.8. ท่านอาศัยอยู่ในจังหวัดนั้นในปีไหน",
        # In which period did you reside in this province? Buddhist era start year:
        choices=[
            [999, "ขอไม่ตอบ"],
            *[[y, str(y)] for y in range(2536, 2569)]
        ],
        blank=True
    )
    noncombatant_geography_second_start_month = models.IntegerField(
        label="3.2.9. เริ่มในเดือน",
        choices=C.MONTH,
        blank=True
    )
    noncombatant_geography_second_end_year = models.IntegerField(
        label="3.2.10. ถึงปีไหน",
        # Buddhist era end year:
        choices=[
            [999, "ขอไม่ตอบ"],
            *[[y, str(y)] for y in range(2543, 2569)]
        ],
        blank=True
    )
    noncombatant_geography_second_end_month = models.IntegerField(
        label="3.2.11. สิ้นสุดในเดือน",
        choices=C.MONTH,
        blank=True
    )
    # QUESTIONS EXPOSURE TO VIOLENCE
    etv_bi_1 = models.IntegerField(
        label="3.3. ท่านเคยถูกโจมตีหรือซุ่มโจมตีโดยกลุ่มติดอาวุธในความขัดแย้งหรือไม่",
        # … were you ever ambushed by combatants of the conflict or forced to hide during the confrontation?
        choices=C.BINARY_ANSWER,
        widget=widgets.RadioSelectHorizontal,
        blank=False
    )
    etv_sc_1 = models.IntegerField(
        label="3.4. ถ้าใช่  บ่อยเพียงใด",
        # If yes, how often?
        choices=C.SCALE_ETV,
        widget=widgets.RadioSelectHorizontal,
        blank=True
    )
    etv_bi_2 = models.IntegerField(
        label="3.5. ท่านเคยถูกคุกคามจากกลุ่มติดอาวุธในความขัดแย้งหรือไม่",
        # … were you ever threatened by combatants of the conflict?
        choices=C.BINARY_ANSWER,
        widget=widgets.RadioSelectHorizontal,
        blank=False
    )
    etv_sc_2 = models.IntegerField(
        label="3.6. ถ้าใช่  บ่อยเพียงใด",
        # If yes, how often?
        choices=C.SCALE_ETV,
        widget=widgets.RadioSelectHorizontal,
        blank=True
    )
    etv_bi_3 = models.IntegerField(
        label="3.7. ท่านเคยถูกปล่อยทิ้งไม่ให้มีทั้งอาหารและที่พักอาศัยหรือไม่",
        # … were you left without food or shelter?
        choices=C.BINARY_ANSWER,
        widget=widgets.RadioSelectHorizontal,
        blank=False
    )
    etv_sc_3 = models.IntegerField(
        label="3.8. ถ้าใช่  บ่อยเพียงใด",
        # If yes, how often?
        choices=C.SCALE_ETV,
        widget=widgets.RadioSelectHorizontal,
        blank=True
    )
    etv_bi_5_1 = models.IntegerField(
        label="3.9. ท่านเคยได้รับบาดเจ็บทางกาย ถูกทุบตีที่ร่างกาย หรือถูกทรมานโดยกลุ่มติดอาวุธในความขัดแย้งหรือไม่",
        # … were you ever physically injured, subject to beating(s) to the body, or tortured by combatants of the conflict?
        choices=C.BINARY_ANSWER,
        widget=widgets.RadioSelectHorizontal,
        blank=False
    )
    etv_sc_5_1 = models.IntegerField(
        label="3.10. ถ้าใช่  บ่อยเพียงใด",
        # If yes, how often?
        choices=C.SCALE_ETV,
        widget=widgets.RadioSelectHorizontal,
        blank=True
    )
    etv_bi_5_2 = models.IntegerField(
        label="3.11. ท่านเคยได้รับบาดเจ็บทางกาย ถูกทุบตีหรือถูกทรมานโดยผู้บังคับบัญชาหรือเพื่อนทหารเกณฑ์ในความขัดแย้งหรือไม่",
        # … were you ever physically injured, subject to beating(s) to the body, or tortured by your superiors or other conscripts?
        choices=C.BINARY_ANSWER,
        widget=widgets.RadioSelectHorizontal,
        blank=True
    )
    etv_sc_5_2 = models.IntegerField(
        label="3.12. ถ้าใช่  บ่อยเพียงใด",
        # If yes, how often?
        choices=C.SCALE_ETV,
        widget=widgets.RadioSelectHorizontal,
        blank=True
    )
    etv_bi_6 = models.IntegerField(
        label="3.13. ท่านเคยได้พบเห็นหรือประสบกับเหตุระเบิดหรือไม่",
        # …have you ever witnessed or experienced a bombing?
        choices=C.BINARY_ANSWER,
        widget=widgets.RadioSelectHorizontal,
        blank=False
    )
    etv_sc_6 = models.IntegerField(
        label="3.14. ถ้าใช่  บ่อยเพียงใด",
        # If yes, how often?
        choices=C.SCALE_ETV,
        widget=widgets.RadioSelectHorizontal,
        blank=True
    )
    etv_bi_7 = models.IntegerField(
        label="3.15. ท่านเคยพบเห็นการก่อจลาจลหรือไม่ ",
        # … have you ever witnessed or experienced a riot?
        choices=C.BINARY_ANSWER,
        widget=widgets.RadioSelectHorizontal,
        blank=False
    )
    etv_sc_7 = models.IntegerField(
        label="3.16. ถ้าใช่  บ่อยเพียงใด",
        # If yes, how often?
        choices=C.SCALE_ETV,
        widget=widgets.RadioSelectHorizontal,
        blank=True
    )
    etv_bi_8 = models.IntegerField(
        label="3.17. ท่านเคยพบเห็นการลอบยิงหรือการยิงกันหรือไม่",
        # … have you ever witnessed or experienced a shooting?
        choices=C.BINARY_ANSWER,
        widget=widgets.RadioSelectHorizontal,
        blank=False
    )
    etv_sc_8 = models.IntegerField(
        label="3.18. ถ้าใช่  บ่อยเพียงใด",
        # If yes, how often?
        choices=C.SCALE_ETV,
        widget=widgets.RadioSelectHorizontal,
        blank=True
    )


# FUNCTIONS
def assign_treatments(p, csv_file):
    participant = p.participant

    # Read all data from CSV
    all_data = []
    with open(csv_file, 'r') as file:
        reader = csv.DictReader(file, delimiter=';')
        for row in reader:
            all_data.append(row)

    # Filter by group_participant and etv
    group_player = [
        row for row in all_data
        if int(row['group_participant']) == participant.group
           and int(row['etv']) == participant.etv
    ]

    # Find minimum nb_participant value
    if group_player:
        min_value = min(int(row['nb_participant']) for row in group_player)

        # Filter rows with minimum value
        min_rows = [
            row for row in group_player
            if int(row['nb_participant']) == min_value
        ]

        # Select row (random if multiple, otherwise take the first)
        if len(min_rows) > 1:
            selected_row = random.choice(min_rows)
        else:
            selected_row = min_rows[0]

        # Assign treatments
        participant.treatment_hope = int(selected_row['treatment_hope'])
        participant.side_ultimatum = int(selected_row['side_UG'])
        participant.treatment_other = int(selected_row['treatment_other'])
    else:
        # Handle case where no matching rows found
        # You may want to set defaults or raise an error
        pass


# PAGES
class Page1(Page):
    form_model = 'player'
    form_fields = [
        'military_binary'
    ]

    @staticmethod
    def before_next_page(player: Player, timeout_happened):
        participant = player.participant
        participant.military_binary = player.military_binary
        if participant.military_binary !=1:
            participant.etv=0
            assign_treatments(player, C.DATA_TREATMENT_LOC)
            print(participant.treatment_other)
        else:
            pass
    def is_displayed(player: Player):
        return player.session.config['name'] == "session_C4P_THAI_w1"



class Page2_1(Page):
    form_model = 'player'
    @staticmethod
    def get_form_fields(player: Player):
        """Only return form fields if the page is displayed"""
        participant = player.participant
        if participant.military_binary == 1 and player.session.config['name'] == "session_C4P_THAI_w1":
            return [
                'conscription_binary',
                'military_tasks',
                'military_province_main',
                'maindeployment_start_year',
                'maindeployment_start_month',
                'maindeployment_length',
                'deployment_second',
                'military_province_second',
                'seconddeployment_start_year',
                'seconddeployment_start_month',
                'seconddeployment_length'
            ]
        else:
            return []
    def is_displayed(player: Player):
        participant = player.participant
        return participant.military_binary == 1 and player.session.config['name'] == "session_C4P_THAI_w1"
    def error_message(player, values):
        if values['deployment_second'] == 1:
            if values.get('military_province_second') is None:
                return 'ข้อผิดพลาด: โปรดตอบคำถามข้อที่ 3.1.9.'
            if values.get('seconddeployment_start_year') is None:
                return 'ข้อผิดพลาด: โปรดตอบคำถามข้อที่ 3.1.10.'
            if values.get('seconddeployment_start_month') is None:
                return 'ข้อผิดพลาด: โปรดตอบคำถามข้อที่ 3.1.11.'
            if values.get('seconddeployment_length') is None:
                return 'ข้อผิดพลาด: โปรดตอบคำถามข้อที่ 3.1.12.'
    def before_next_page(player, timeout_happened):
        participant = player.participant
        if participant.military_binary==1 & player.conscription_binary==1 :
            participant.etv = 1
        else:
            participant.etv = 0
        assign_treatments(player, C.DATA_TREATMENT_LOC)
        print(participant.treatment_other)


class Page2_2(Page):
    form_model = 'player'
    @staticmethod
    def get_form_fields(player: Player):
        """Only return form fields if the page is displayed"""
        participant = player.participant
        if participant.military_binary != 1 and player.session.config['name'] == "session_C4P_THAI_w1":
            return [
                'noncombatant_geography_main',
                'noncombatant_geography_main_start_year',
                'noncombatant_geography_main_start_month',
                'noncombatant_geography_main_end_year',
                'noncombatant_geography_main_end_month',
                'noncombatant_geography_second_b',
                'noncombatant_geography_second',
                'noncombatant_geography_second_start_year',
                'noncombatant_geography_second_start_month',
                'noncombatant_geography_second_end_year',
                'noncombatant_geography_second_end_month'
            ]
        else:
            return []
    def is_displayed(player: Player):
        participant = player.participant
        return participant.military_binary != 1 and player.session.config['name'] == "session_C4P_THAI_w1"
    def error_message(player, values):
        if values['noncombatant_geography_second_b'] == 1:
            if values.get('noncombatant_geography_second') is None:
                return 'ข้อผิดพลาด: โปรดตอบคำถามข้อที่ 3.2.7.'
            if values.get('noncombatant_geography_second_start_year') is None:
                return 'ข้อผิดพลาด: โปรดตอบคำถามข้อที่ 3.2.8.'
            if values.get('noncombatant_geography_second_start_month') is None:
                return 'ข้อผิดพลาด: โปรดตอบคำถามข้อที่ 3.2.9.'
            if values.get('noncombatant_geography_second_end_year') is None:
                return 'ข้อผิดพลาด: โปรดตอบคำถามข้อที่ 3.2.10.'
            if values.get('noncombatant_geography_second_end_month') is None:
                return 'ข้อผิดพลาด: โปรดตอบคำถามข้อที่ 3.2.11.'


class Page3(Page):
    form_model = 'player'
    @staticmethod
    def get_form_fields(player: Player):
        """Only return form fields if the page is displayed"""
        participant = player.participant
        if participant.military_binary == 1 and player.session.config['name'] == "session_C4P_THAI_w1":
            return [
                'military_socialization_1',
                'military_socialization_2',
                'military_socialization_3'
            ]
        else:
            return []
    def is_displayed(player: Player):
        participant = player.participant
        return participant.military_binary == 1 and player.session.config['name'] == "session_C4P_THAI_w1"


class Page4(Page):
    # Different text on webpage displayed depending on age and military service status
    form_model = 'player'
    @staticmethod
    def get_form_fields(player):
        participant = player.participant
        if participant.etv == 1:
            return [
                'etv_bi_1',
                'etv_sc_1',
                'etv_bi_2',
                'etv_sc_2',
                'etv_bi_3',
                'etv_sc_3',
                'etv_bi_5_1',
                'etv_sc_5_1',
                'etv_bi_5_2',
                'etv_sc_5_2',
                'etv_bi_6',
                'etv_sc_6',
                'etv_bi_7',
                'etv_sc_7',
                'etv_bi_8',
                'etv_sc_8'
    ]
        else:
            return [
                'etv_bi_1',
                'etv_sc_1',
                'etv_bi_2',
                'etv_sc_2',
                'etv_bi_3',
                'etv_sc_3',
                'etv_bi_5_1',
                'etv_sc_5_1',
                'etv_bi_6',
                'etv_sc_6',
                'etv_bi_7',
                'etv_sc_7',
                'etv_bi_8',
                'etv_sc_8'
    ]
    def is_displayed(player: Player):
        return player.session.config['name'] == "session_C4P_THAI_w1"
    def error_message(player, values):
        pairs = [
            ('etv_bi_1', 'etv_sc_1'),
            ('etv_bi_2', 'etv_sc_2'),
            ('etv_bi_3', 'etv_sc_3'),
            ('etv_bi_5_1', 'etv_sc_5_1'),
            ('etv_bi_5_2', 'etv_sc_5_2'),
            ('etv_bi_6', 'etv_sc_6'),
            ('etv_bi_7', 'etv_sc_7'),
            ('etv_bi_8', 'etv_sc_8')
        ]
        for bi_field, sc_field in pairs:
            if bi_field in values and values[bi_field] == 1:
                if sc_field not in values or values[sc_field] is None:
                    return f'ข้อผิดพลาด: โปรดตอบคำถามเกี่ยวกับความถี่'

page_sequence = [
    Page1, # military service filter + treatment assignment
    Page2_1, # questions military service
    Page2_2, # question non-military service
    Page3, # military socialization
    Page4 # exposure to violence
]