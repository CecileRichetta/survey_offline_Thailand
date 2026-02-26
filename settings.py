from os import environ

environ['DATABASE_URL']="postgres://otree_user:OT_spirit12@localhost/django_db"

ROOMS = [
    dict(
        name="C4PTHP",
        display_name="C4PTHP",
        welcome_page="_welcome_pages/Page0.html",
        participant_label_file="_rooms/participant_label_thai_inc.txt",
        use_secure_urls=False
    ),
    dict(
        name="C4PTHP_TRAINING_1",
        display_name="C4PTHP_TRAINING_1",
        welcome_page="_welcome_pages/Page0.html",
        participant_label_file="_rooms/participant_label_thai_inc.txt",
        use_secure_urls=False
    ),
    dict(
        name="C4PTHP_TRAINING_2",
        display_name="C4PTHP_TRAINING_2",
        welcome_page="_welcome_pages/Page0.html",
        participant_label_file="_rooms/participant_label_thai_inc.txt",
        use_secure_urls=False
    ),
    dict(
        name="pilot_THAI_HEAD",
        display_name="C4P_pilot_THAI_HEAD"
    )
]

SESSION_CONFIGS = [
    dict(
         name='session_C4P_THAI_w1',
        app_sequence=[
            'app_1', 'app_2', 'app_3', 'app_4', 'app_5', 'app_6',
            'app_7', 'app_8', 'app_9', 'app_10'
        ],
         num_demo_participants=2,
     ),
    dict(
         name='session_C4P_THAI_w2',
        app_sequence=[
            'app_1', 'app_2', 'app_3', 'app_4', 'app_5', 'app_6',
            'app_7', 'app_8', 'app_9', 'app_10'
        ],
         num_demo_participants=2,
     ),
    dict(
        name='session_C4P_THAI_headenumerator',
        app_sequence=[
            'app_12'
        ],
        num_demo_participants=1,
    ),
]

SESSION_CONFIG_DEFAULTS = dict(
    real_world_currency_per_point=1.00, participation_fee=0.00, doc=""
)

PARTICIPANT_FIELDS = [
    'dropout', 'participation_fee',
    'group', 'age', 'military_binary', 'etv', 'treatment_hope', 'side_ultimatum', 'treatment_other',
    'decision_UG', 'decision_PG',
    'other_UG_decision', 'other_PG_decision',
    'payoff_UG', 'payoff_PG',
    'total_payoff_token', 'payoff_games', 'total_compensation'
]

SESSION_FIELDS = []

LANGUAGE_CODE = 'en'
REAL_WORLD_CURRENCY_CODE = 'BHT'
USE_POINTS = True

ADMIN_USERNAME = 'admin'
ADMIN_PASSWORD = environ.get('OTREE_ADMIN_PASSWORD')
AUTH_LEVEL = environ.get('OTREE_AUTH_LEVEL')

DEMO_PAGE_INTRO_HTML = """ """
SECRET_KEY = '9805055233605'
