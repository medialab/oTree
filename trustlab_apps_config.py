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

ROOMS_DEFAULTS = {}
ROOMS = [
    {
        'name': 'test',
        'display_name': 'Test Room (for developement and test purposes)'
    }
]

SESSION_CONFIGS = [
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
        'quota_redirects': quota_redirects_ko,
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
        'quota_redirects': quota_redirects_ko,
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
        'quota_redirects': quota_redirects_ko,
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
        'quota_redirects': quota_redirects_ko,
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
        'quota_redirects': quota_redirects_ko,
    },

    {
        'name': 'trustlab_2016_A1_ko_prod',
        'display_name': 'TRUSTLAB | Sept 2016 | KO | path A1 | Payoff Group 2 (production)',
        'num_demo_participants': 126,
        'app_sequence': [
            'mandatory_participant_label', 'timer_start', 'introduction', 'trust',
            'public_goods', 'dictator', 'iat', 'survey_i18n', 'timer_stop',
            'redirect_speedsters', 'earnings', 'redirect_completes'
        ],
        'speedsters_threshold': 10 * 60,
        'treatment': 'A1',
        'payoff_group': 2,
        'quota_redirects': quota_redirects_ko,
    },
    {
        'name': 'trustlab_2016_A2_ko_prod',
        'display_name': 'TRUSTLAB | Sept 2016 | KO | path A2 | Payoff Group 2 (production)',
        'num_demo_participants': 126,
        'app_sequence': [
            'mandatory_participant_label', 'timer_start', 'introduction', 'trust',
            'public_goods', 'dictator', 'iat', 'survey_i18n', 'timer_stop',
            'redirect_speedsters', 'earnings', 'redirect_completes'
        ],
        'speedsters_threshold': 10 * 60,
        'treatment': 'A2',
        'payoff_group': 2,
        'quota_redirects': quota_redirects_ko,
    },
    {
        'name': 'trustlab_2016_B1_ko_prod',
        'display_name': 'TRUSTLAB | Sept 2016 | KO | path B1 | Payoff Group 2 (production)',
        'num_demo_participants': 126,
        'app_sequence': [
            'mandatory_participant_label', 'timer_start', 'introduction', 'trust',
            'public_goods', 'dictator', 'iat', 'survey_i18n', 'timer_stop',
            'redirect_speedsters', 'earnings', 'redirect_completes'
        ],
        'speedsters_threshold': 10 * 60,
        'treatment': 'B1',
        'payoff_group': 2,
        'quota_redirects': quota_redirects_ko,
    },
    {
        'name': 'trustlab_2016_B2_ko_prod',
        'display_name': 'TRUSTLAB | Sept 2016 | KO | path B2 | Payoff Group 2 (production)',
        'num_demo_participants': 126,
        'app_sequence': [
            'mandatory_participant_label', 'timer_start', 'introduction', 'trust',
            'public_goods', 'dictator', 'iat', 'survey_i18n', 'timer_stop',
            'redirect_speedsters', 'earnings', 'redirect_completes'
        ],
        'speedsters_threshold': 10 * 60,
        'treatment': 'B2',
        'payoff_group': 2,
        'quota_redirects': quota_redirects_ko,
    },

    {
        'name': 'trustlab_2016_A1_ko',
        'display_name': 'TRUSTLAB | Sept 2016 | KO | path A1',
        'num_demo_participants': 126,
        'app_sequence': [
            'mandatory_participant_label', 'timer_start', 'introduction', 'trust',
            'public_goods', 'dictator', 'iat', 'survey_i18n', 'timer_stop',
            'redirect_speedsters', 'earnings', 'redirect_completes'
        ],
        'speedsters_threshold': 1,
        'treatment': 'A1',
        'payoff_group': 1,
        'quota_redirects': quota_redirects_ko,
    },
    {
        'name': 'trustlab_2016_A2_ko',
        'display_name': 'TRUSTLAB | Sept 2016 | KO | path A2',
        'num_demo_participants': 126,
        'app_sequence': [
            'mandatory_participant_label', 'timer_start', 'introduction', 'trust',
            'public_goods', 'dictator', 'iat', 'survey_i18n', 'timer_stop',
            'redirect_speedsters', 'earnings', 'redirect_completes'
        ],
        'speedsters_threshold': 1,
        'treatment': 'A2',
        'payoff_group': 1,
        'quota_redirects': quota_redirects_ko,
    },
    {
        'name': 'trustlab_2016_B1_ko',
        'display_name': 'TRUSTLAB | Sept 2016 | KO | path B1',
        'num_demo_participants': 126,
        'app_sequence': [
            'mandatory_participant_label', 'timer_start', 'introduction', 'trust',
            'public_goods', 'dictator', 'iat', 'survey_i18n', 'timer_stop',
            'redirect_speedsters', 'earnings', 'redirect_completes'
        ],
        'speedsters_threshold': 1,
        'treatment': 'B1',
        'payoff_group': 1,
        'quota_redirects': quota_redirects_ko,
    },
    {
        'name': 'trustlab_2016_B2_ko',
        'display_name': 'TRUSTLAB | Sept 2016 | KO | path B2',
        'num_demo_participants': 126,
        'app_sequence': [
            'mandatory_participant_label', 'timer_start', 'introduction', 'trust',
            'public_goods', 'dictator', 'iat', 'survey_i18n', 'timer_stop',
            'redirect_speedsters', 'earnings', 'redirect_completes'
        ],
        'speedsters_threshold': 1,
        'treatment': 'B2',
        'payoff_group': 1,
        'quota_redirects': quota_redirects_ko,
    }
]
