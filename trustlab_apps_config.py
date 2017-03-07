"""Config stem for TRUSTLAB's experiments."""

quota_redirects = {
    'complete': (
        'http://globaltestmarket.com/20/survey/finished.phtml'
    ),
    'screen': (
        'http://globaltestmarket.com/20/survey/finished.phtml?sco=s'
    ),
    'quota_full': (
        'http://globaltestmarket.com/20/survey/finished.phtml?sco=o'
    ),
    'speedster': (
        'http://globaltestmarket.com/20/survey/finished.phtml?sco=tf'
    ),
}

quota_redirects_ko = {
    'complete': (
        'http://activities.mysurvey.com/Waypoint/waypoint/outbound.wp?status=C'
    ),
    'screen': (
        'http://globaltestmarket.com/20/survey/finished.phtml?sco=s'
    ),
    'quota_full': (
        'http://activities.mysurvey.com/Waypoint/waypoint/outbound.wp?status=Q'
    ),
    'speedster': (
        'http://activities.mysurvey.com/Waypoint/waypoint/outbound.wp?status=Q1'
    ),
}

quota_redirects_sl = {
    'complete': (
        'http://globaltestmarket.com/20/survey/finished.phtml?lang=SLV'
    ),
    'speedster': (
        'http://globaltestmarket.com/20/survey/finished.phtml?lang=SLV&sco=tf'
    ),
}

ROOMS_DEFAULTS = {}
ROOMS = [
    {
        'name': 'test',
        'display_name': 'Test Room (for developement and test purposes)'
    },
    {
        'name': 'slovenia_1',
        'display_name': 'Slovenian Room 1'
    },
    {
        'name': 'slovenia_2',
        'display_name': 'Slovenian Room 2'
    },
    {
        'name': 'slovenia_3',
        'display_name': 'Slovenian Room 3'
    },
    {
        'name': 'slovenia_4',
        'display_name': 'Slovenian Room 4'
    },
    {
        'name': 'demo_1',
        'display_name': 'Demo Room 1'
    },
    {
        'name': 'demo_2',
        'display_name': 'Demo Room 2'
    }
]

SESSION_CONFIGS = [
    {
        'name': 'demo_trustlab_2016_A1',
        'display_name': 'TRUSTLAB | DEMO | path 1',
        'num_demo_participants': 126,
        'app_sequence': [
            'timer_start', 'introduction', 'trust',
            'public_goods', 'dictator', 'iat', 'survey_i18n', 'timer_stop',
            'redirect_speedsters', 'earnings', 'redirect_completes'
        ],
        'speedsters_threshold': 1,
        'treatment': 'A1',
        'payoff_group': 1,
        'quota_redirects': quota_redirects_sl,
    },
    {
        'name': 'demo_trustlab_2016_A2',
        'display_name': 'TRUSTLAB | DEMO | path 2',
        'num_demo_participants': 126,
        'app_sequence': [
            'timer_start', 'introduction', 'trust',
            'public_goods', 'dictator', 'iat', 'survey_i18n', 'timer_stop',
            'redirect_speedsters', 'earnings', 'redirect_completes'
        ],
        'speedsters_threshold': 1,
        'treatment': 'A2',
        'payoff_group': 1,
        'quota_redirects': quota_redirects_sl,
    },

    {
        'name': 'trustlab_2016_A1_sl_prod',
        'display_name': 'TRUSTLAB | February 2017 | Slovenia | path 1 | Payoff Group 2 (production)',
        'num_demo_participants': 126,
        'app_sequence': [
            'mandatory_participant_label', 'timer_start', 'introduction', 'trust',
            'public_goods', 'dictator', 'iat', 'survey_i18n', 'timer_stop',
            'redirect_speedsters', 'earnings', 'redirect_completes'
        ],
        'speedsters_threshold': 1,
        'treatment': 'A1',
        'payoff_group': 2,
        'quota_redirects': quota_redirects_sl,
    },
    {
        'name': 'trustlab_2016_A2_sl_prod',
        'display_name': 'TRUSTLAB | February 2017 | Slovenia | path 2 | Payoff Group 2 (production)',
        'num_demo_participants': 126,
        'app_sequence': [
            'mandatory_participant_label', 'timer_start', 'introduction', 'trust',
            'public_goods', 'dictator', 'iat', 'survey_i18n', 'timer_stop',
            'redirect_speedsters', 'earnings', 'redirect_completes'
        ],
        'speedsters_threshold': 1,
        'treatment': 'A2',
        'payoff_group': 2,
        'quota_redirects': quota_redirects_sl,
    },

    {
        'name': 'trustlab_2016_A1_sl',
        'display_name': 'TRUSTLAB | February 2017 | Slovenia | path 1',
        'num_demo_participants': 126,
        'app_sequence': [
            'mandatory_participant_label', 'timer_start', 'introduction', 'trust',
            'public_goods', 'dictator', 'iat', 'survey_i18n', 'timer_stop',
            'redirect_speedsters', 'earnings', 'redirect_completes'
        ],
        'speedsters_threshold': 1,
        'treatment': 'A1',
        'payoff_group': 1,
        'quota_redirects': quota_redirects_sl,
    },
    {
        'name': 'trustlab_2016_A2_sl',
        'display_name': 'TRUSTLAB | February 2017 | Slovenia | path 2',
        'num_demo_participants': 126,
        'app_sequence': [
            'mandatory_participant_label', 'timer_start', 'introduction', 'trust',
            'public_goods', 'dictator', 'iat', 'survey_i18n', 'timer_stop',
            'redirect_speedsters', 'earnings', 'redirect_completes'
        ],
        'speedsters_threshold': 1,
        'treatment': 'A2',
        'payoff_group': 1,
        'quota_redirects': quota_redirects_sl,
    },

    {
        'name': 'test_earnings',
        'display_name': 'Test Earnings',
        'num_demo_participants': 100,
        'app_sequence': [
            'trust', 'public_goods', 'dictator', 'earnings'
        ],
        'treatment': 'A1',
        'payoff_group': 0,
        'speedsters_threshold': 1,
        'quota_redirects': quota_redirects_sl,
    },

    {
        'name': 'test_intro',
        'display_name': 'INTRODUCTION',
        'num_demo_participants': 100,
        'app_sequence': [
            'introduction'
        ],
        'treatment': 'A1',
        'payoff_group': 0,
        'speedsters_threshold': 1,
        'quota_redirects': quota_redirects_sl,
    },
    {
        'name': 'test_trust',
        'display_name': 'TRUST',
        'num_demo_participants': 100,
        'app_sequence': [
            'trust'
        ],
        'treatment': 'A1',
        'payoff_group': 0,
        'speedsters_threshold': 1,
        'quota_redirects': quota_redirects_sl,
    },
    {
        'name': 'test_pg',
        'display_name': 'PUBLIC GOODS',
        'num_demo_participants': 100,
        'app_sequence': [
            'public_goods'
        ],
        'treatment': 'A1',
        'payoff_group': 0,
        'speedsters_threshold': 1,
        'quota_redirects': quota_redirects_sl,
    },
    {
        'name': 'test_dictator',
        'display_name': 'DICTATOR',
        'num_demo_participants': 100,
        'app_sequence': [
            'dictator'
        ],
        'treatment': 'A1',
        'payoff_group': 0,
        'speedsters_threshold': 1,
        'quota_redirects': quota_redirects_sl,
    },
    {
        'name': 'test_iat',
        'display_name': 'IAT',
        'num_demo_participants': 100,
        'app_sequence': [
            'iat'
        ],
        'treatment': 'A1',
        'payoff_group': 0,
        'speedsters_threshold': 1,
        'quota_redirects': quota_redirects_sl,
    },
    {
        'name': 'test_survey',
        'display_name': 'SURVEY',
        'num_demo_participants': 100,
        'app_sequence': [
            'survey_i18n'
        ],
        'treatment': 'A1',
        'payoff_group': 0,
        'speedsters_threshold': 1,
        'quota_redirects': quota_redirects_sl,
    },
]
