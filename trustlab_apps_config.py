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

SESSION_CONFIGS = [
    {
        'name': 'test',
        'display_name': 'TEST',
        'num_demo_participants': 126,
        'app_sequence': [
            'timer_start', 'trust', 'public_goods',
            'dictator', 'iat', 'timer_stop', 'earnings', 'redirect_completes'
        ],
        'treatment': 'A1a',
        'payoff_group': 0,
        'speedsters_threshold': 1,
        'quota_redirects': quota_redirects_ko,
    },

    {
        'name': 'trustlab_2016_run01_A1a_ko_prod',
        'display_name': 'TRUSTLAB | Sept 2016 | KO | path A1a or A1b | \
Payoff Group 2 (production)',
        'num_demo_participants': 126,
        'app_sequence': [
            'timer_start', 'trust', 'public_goods',
            'dictator', 'iat', 'survey_i18n', 'timer_stop',
            'redirect_speedsters', 'earnings', 'redirect_completes'
        ],
        'speedsters_threshold': 10 * 60,
        'treatment': 'A1a',
        'payoff_group': 2,
        'quota_redirects': quota_redirects_ko,
    },
    {
        'name': 'trustlab_2016_run01_A2a_ko_prod',
        'display_name': 'TRUSTLAB | Sept 2016 | KO | path A2a or A2b | \
Payoff Group 2 (production)',
        'num_demo_participants': 126,
        'app_sequence': [
            'timer_start', 'trust', 'public_goods',
            'dictator', 'iat', 'survey_i18n', 'timer_stop',
            'redirect_speedsters', 'earnings', 'redirect_completes'
        ],
        'speedsters_threshold': 10 * 60,
        'treatment': 'A2a',
        'payoff_group': 2,
        'quota_redirects': quota_redirects_ko,
    },
    {
        'name': 'trustlab_2016_run01_B1a_ko_prod',
        'display_name': 'TRUSTLAB | Sept 2016 | KO | path B1a or B1b | \
Payoff Group 2 (production)',
        'num_demo_participants': 126,
        'app_sequence': [
            'timer_start', 'trust', 'public_goods',
            'dictator', 'iat', 'survey_i18n', 'timer_stop',
            'redirect_speedsters', 'earnings', 'redirect_completes'
        ],
        'speedsters_threshold': 10 * 60,
        'treatment': 'B1a',
        'payoff_group': 2,
        'quota_redirects': quota_redirects_ko,
    },
    {
        'name': 'trustlab_2016_run01_B2a_ko_prod',
        'display_name': 'TRUSTLAB | Sept 2016 | KO | path B2a or B2b | \
Payoff Group 2 (production)',
        'num_demo_participants': 126,
        'app_sequence': [
            'timer_start', 'trust', 'public_goods',
            'dictator', 'iat', 'survey_i18n', 'timer_stop',
            'redirect_speedsters', 'earnings', 'redirect_completes'
        ],
        'speedsters_threshold': 10 * 60,
        'treatment': 'B2a',
        'payoff_group': 2,
        'quota_redirects': quota_redirects_ko,
    },

    {
        'name': 'trustlab_2016_run01_A1a_ko',
        'display_name': 'TRUSTLAB | Sept 2016 | KO | path A1a or A1b',
        'num_demo_participants': 126,
        'app_sequence': [
            'timer_start', 'trust', 'public_goods',
            'dictator', 'iat', 'survey_i18n', 'timer_stop',
            'redirect_speedsters', 'earnings', 'redirect_completes'
        ],
        'speedsters_threshold': 1,
        'treatment': 'A1a',
        'payoff_group': 1,
        'quota_redirects': quota_redirects_ko,
    },
    {
        'name': 'trustlab_2016_run01_A2a_ko',
        'display_name': 'TRUSTLAB | Sept 2016 | KO | path A2a or A2b',
        'num_demo_participants': 126,
        'app_sequence': [
            'timer_start', 'trust', 'public_goods',
            'dictator', 'iat', 'survey_i18n', 'timer_stop',
            'redirect_speedsters', 'earnings', 'redirect_completes'
        ],
        'speedsters_threshold': 1,
        'treatment': 'A2a',
        'payoff_group': 1,
        'quota_redirects': quota_redirects_ko,
    },
    {
        'name': 'trustlab_2016_run01_B1a_ko',
        'display_name': 'TRUSTLAB | Sept 2016 | KO | path B1a or B1b',
        'num_demo_participants': 126,
        'app_sequence': [
            'timer_start', 'trust', 'public_goods',
            'dictator', 'iat', 'survey_i18n', 'timer_stop',
            'redirect_speedsters', 'earnings', 'redirect_completes'
        ],
        'speedsters_threshold': 1,
        'treatment': 'B1a',
        'payoff_group': 1,
        'quota_redirects': quota_redirects_ko,
    },
    {
        'name': 'trustlab_2016_run01_B2a_ko',
        'display_name': 'TRUSTLAB | Sept 2016 | KO | path B2a or B2b',
        'num_demo_participants': 126,
        'app_sequence': [
            'timer_start', 'trust', 'public_goods',
            'dictator', 'iat', 'survey_i18n', 'timer_stop',
            'redirect_speedsters', 'earnings', 'redirect_completes'
        ],
        'speedsters_threshold': 1,
        'treatment': 'B2a',
        'payoff_group': 1,
        'quota_redirects': quota_redirects_ko,
    }
]
