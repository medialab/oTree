"""Config stem for TRUSTLAB's experiments."""
total_fr = 1500
total_ko = 1500
total_gmi = 20

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

quota_gender_age_groups_fr = {
    '1_18_24': {
        'percentage': 7, 'expected': total_fr * (7 / 100), 'currently': 0
    },
    '1_25_34': {
        'percentage': 10, 'expected': total_fr * (10 / 100), 'currently': 0
    },
    '1_35_44': {
        'percentage': 11, 'expected': total_fr * (11 / 100), 'currently': 0
    },
    '1_45_54': {
        'percentage': 11, 'expected': total_fr * (11 / 100), 'currently': 0
    },
    '1_55_64': {
        'percentage': 10, 'expected': total_fr * (10 / 100), 'currently': 0
    },
    '2_18_24': {
        'percentage': 7, 'expected': total_fr * (7 / 100), 'currently': 0
    },
    '2_25_34': {
        'percentage': 10, 'expected': total_fr * (10 / 100), 'currently': 0
    },
    '2_35_44': {
        'percentage': 11, 'expected': total_fr * (11 / 100), 'currently': 0
    },
    '2_45_54': {
        'percentage': 11, 'expected': total_fr * (11 / 100), 'currently': 0
    },
    '2_55_64': {
        'percentage': 11, 'expected': total_fr * (11 / 100), 'currently': 0
    },
}

quota_gender_age_groups_ko = {
    '1_18_24': {
        'percentage': 7, 'expected': total_ko * (7 / 100), 'currently': 0
    },
    '1_25_34': {
        'percentage': 11, 'expected': total_ko * (11 / 100), 'currently': 0
    },
    '1_35_44': {
        'percentage': 11, 'expected': total_ko * (11 / 100), 'currently': 0
    },
    '1_45_54': {
        'percentage': 12, 'expected': total_ko * (12 / 100), 'currently': 0
    },
    '1_55_64': {
        'percentage': 8, 'expected': total_ko * (8 / 100), 'currently': 0
    },
    '2_18_24': {
        'percentage': 6, 'expected': total_ko * (6 / 100), 'currently': 0
    },
    '2_25_34': {
        'percentage': 10, 'expected': total_ko * (10 / 100), 'currently': 0
    },
    '2_35_44': {
        'percentage': 12, 'expected': total_ko * (12 / 100), 'currently': 0
    },
    '2_45_54': {
        'percentage': 12, 'expected': total_ko * (12 / 100), 'currently': 0
    },
    '2_55_64': {
        'percentage': 9, 'expected': total_ko * (9 / 100), 'currently': 0
    },
}

quota_gender_age_groups_gmi = {
    '1_18_24': {
        'percentage': 7, 'expected': total_gmi * (7 / 100), 'currently': 0
    },
    '1_25_34': {
        'percentage': 10, 'expected': total_gmi * (10 / 100), 'currently': 0
    },
    '1_35_44': {
        'percentage': 11, 'expected': total_gmi * (11 / 100), 'currently': 0
    },
    '1_45_54': {
        'percentage': 11, 'expected': total_gmi * (11 / 100), 'currently': 0
    },
    '1_55_64': {
        'percentage': 10, 'expected': total_gmi * (10 / 100), 'currently': 0
    },
    '2_18_24': {
        'percentage': 7, 'expected': total_gmi * (7 / 100), 'currently': 0
    },
    '2_25_34': {
        'percentage': 10, 'expected': total_gmi * (10 / 100), 'currently': 0
    },
    '2_35_44': {
        'percentage': 11, 'expected': total_gmi * (11 / 100), 'currently': 0
    },
    '2_45_54': {
        'percentage': 11, 'expected': total_gmi * (11 / 100), 'currently': 0
    },
    '2_55_64': {
        'percentage': 11, 'expected': total_gmi * (11 / 100), 'currently': 0
    },
}

SESSION_CONFIGS = [
    {
        'name': 'test',
        'display_name': 'TEST',
        'num_demo_participants': 126,
        'app_sequence': [
            'timer_start', 'trust', 'timer_stop', 'redirect_speedsters'
        ],
        'treatment': 'A1a',
        'language_code': 'fr-fr',
        'payoff_group': 0,
        'speedsters_threshold': 10 * 60,
        'quota_redirects': quota_redirects,
        'quota_total_population': total_fr,
        'quota_gender_age_groups': quota_gender_age_groups_fr,
    },


    {
        'name': 'trustlab_2016_run01_A1a_fr_2',
        'display_name': 'TRUSTLAB | Sept 2016 | FR | path A1a or A1b | Payoff Group 2',
        'num_demo_participants': 126,
        'app_sequence': [
            'quota', 'trust', 'public_goods',
            'dictator', 'iat', 'survey_i18n', 'earnings'
        ],
        'treatment': 'A1a',
        'language_code': 'fr-fr',
        'payoff_group': 2,
        'quota_redirects': quota_redirects,
        'quota_total_population': total_fr,
        'quota_gender_age_groups': quota_gender_age_groups_fr,
    },
    {
        'name': 'trustlab_2016_run01_A2a_fr_2',
        'display_name': 'TRUSTLAB | Sept 2016 | FR | path A2a or A2b | Payoff Group 2',
        'num_demo_participants': 126,
        'app_sequence': [
            'quota', 'trust', 'public_goods',
            'dictator', 'iat', 'survey_i18n', 'earnings'
        ],
        'treatment': 'A2a',
        'language_code': 'fr-fr',
        'payoff_group': 2,
        'quota_redirects': quota_redirects,
        'quota_total_population': total_fr,
        'quota_gender_age_groups': quota_gender_age_groups_fr,
    },
    {
        'name': 'trustlab_2016_run01_B1a_fr_2',
        'display_name': 'TRUSTLAB | Sept 2016 | FR | path B1a or B1b | Payoff Group 2',
        'num_demo_participants': 126,
        'app_sequence': [
            'quota', 'trust', 'public_goods',
            'dictator', 'iat', 'survey_i18n', 'earnings'
        ],
        'treatment': 'B1a',
        'language_code': 'fr-fr',
        'payoff_group': 2,
        'quota_redirects': quota_redirects,
        'quota_total_population': total_fr,
        'quota_gender_age_groups': quota_gender_age_groups_fr,
    },
    {
        'name': 'trustlab_2016_run01_B2a_fr_2',
        'display_name': 'TRUSTLAB | Sept 2016 | FR | path B2a or B2b | Payoff Group 2',
        'num_demo_participants': 126,
        'app_sequence': [
            'quota', 'trust', 'public_goods',
            'dictator', 'iat', 'survey_i18n', 'earnings'
        ],
        'treatment': 'B2a',
        'language_code': 'fr-fr',
        'payoff_group': 2,
        'quota_redirects': quota_redirects,
        'quota_total_population': total_fr,
        'quota_gender_age_groups': quota_gender_age_groups_fr,
    },



    {
        'name': 'trustlab_2016_run01_A1a_fr',
        'display_name': 'TRUSTLAB | Sept 2016 | FR | path A1a or A1b',
        'num_demo_participants': 126,
        'app_sequence': [
            'quota', 'trust', 'public_goods',
            'dictator', 'iat', 'survey_i18n', 'earnings'
        ],
        'treatment': 'A1a',
        'language_code': 'fr-fr',
        'payoff_group': 1,
        'quota_redirects': quota_redirects,
        'quota_total_population': total_fr,
        'quota_gender_age_groups': quota_gender_age_groups_fr,
    },
    {
        'name': 'trustlab_2016_run01_A2a_fr',
        'display_name': 'TRUSTLAB | Sept 2016 | FR | path A2a or A2b',
        'num_demo_participants': 126,
        'app_sequence': [
            'quota', 'trust', 'public_goods',
            'dictator', 'iat', 'survey_i18n', 'earnings'
        ],
        'treatment': 'A2a',
        'language_code': 'fr-fr',
        'payoff_group': 1,
        'quota_redirects': quota_redirects,
        'quota_total_population': total_fr,
        'quota_gender_age_groups': quota_gender_age_groups_fr,
    },
    {
        'name': 'trustlab_2016_run01_B1a_fr',
        'display_name': 'TRUSTLAB | Sept 2016 | FR | path B1a or B1b',
        'num_demo_participants': 126,
        'app_sequence': [
            'quota', 'trust', 'public_goods',
            'dictator', 'iat', 'survey_i18n', 'earnings'
        ],
        'treatment': 'B1a',
        'language_code': 'fr-fr',
        'payoff_group': 1,
        'quota_redirects': quota_redirects,
        'quota_total_population': total_fr,
        'quota_gender_age_groups': quota_gender_age_groups_fr,
    },
    {
        'name': 'trustlab_2016_run01_B2a_fr',
        'display_name': 'TRUSTLAB | Sept 2016 | FR | path B2a or B2b',
        'num_demo_participants': 126,
        'app_sequence': [
            'quota', 'trust', 'public_goods',
            'dictator', 'iat', 'survey_i18n', 'earnings'
        ],
        'treatment': 'B2a',
        'language_code': 'fr-fr',
        'payoff_group': 1,
        'quota_redirects': quota_redirects,
        'quota_total_population': total_fr,
        'quota_gender_age_groups': quota_gender_age_groups_fr,
    },

    {
        'name': 'trustlab_2016_run01_A1a_ko',
        'display_name': 'TRUSTLAB | Sept 2016 | KO | path A1a or A1b',
        'num_demo_participants': 126,
        'app_sequence': [
            'quota', 'trust', 'public_goods',
            'dictator', 'iat', 'survey_i18n', 'earnings'
        ],
        'treatment': 'A1a',
        'language_code': 'ko-kr',
        'payoff_group': 1,
        'quota_redirects': quota_redirects,
        'quota_total_population': total_ko,
        'quota_gender_age_groups': quota_gender_age_groups_ko,
    },
    {
        'name': 'trustlab_2016_run01_A2a_ko',
        'display_name': 'TRUSTLAB | Sept 2016 | KO | path A2a or A2b',
        'num_demo_participants': 126,
        'app_sequence': [
            'quota', 'trust', 'public_goods',
            'dictator', 'iat', 'survey_i18n', 'earnings'
        ],
        'treatment': 'A2a',
        'language_code': 'ko-kr',
        'payoff_group': 1,
        'quota_redirects': quota_redirects,
        'quota_total_population': total_ko,
        'quota_gender_age_groups': quota_gender_age_groups_ko,
    },
    {
        'name': 'trustlab_2016_run01_B1a_ko',
        'display_name': 'TRUSTLAB | Sept 2016 | KO | path B1a or B1b',
        'num_demo_participants': 126,
        'app_sequence': [
            'quota', 'trust', 'public_goods',
            'dictator', 'iat', 'survey_i18n', 'earnings'
        ],
        'treatment': 'B1a',
        'language_code': 'ko-kr',
        'payoff_group': 1,
        'quota_redirects': quota_redirects,
        'quota_total_population': total_ko,
        'quota_gender_age_groups': quota_gender_age_groups_ko,
    },
    {
        'name': 'trustlab_2016_run01_B2a_ko',
        'display_name': 'TRUSTLAB | Sept 2016 | KO | path B2a or B2b',
        'num_demo_participants': 126,
        'app_sequence': [
            'quota', 'trust', 'public_goods',
            'dictator', 'iat', 'survey_i18n', 'earnings'
        ],
        'treatment': 'B2a',
        'language_code': 'ko-kr',
        'payoff_group': 1,
        'quota_redirects': quota_redirects,
        'quota_total_population': total_ko,
        'quota_gender_age_groups': quota_gender_age_groups_ko,
    },

    {
        'name': 'iat',
        'display_name': (
            'IAT'
        ),
        'num_demo_participants': total_gmi,
        'app_sequence': [
            'iat'
        ],
        'treatment': 'A1a',
        'language_code': 'fr-fr',
        'payoff_group': 1,
        'quota_redirects': quota_redirects,
        'quota_total_population': total_gmi,
        'quota_gender_age_groups': quota_gender_age_groups_gmi,
    },
    # {
    #     'name': 'survey_i18n',
    #     'display_name': (
    #         'Survey'
    #     ),
    #     'num_demo_participants': total_gmi,
    #     'app_sequence': [
    #         'survey_i18n'
    #     ],
    #     'treatment': 'A1a',
    #     'language_code': 'fr-fr',
    #     'payoff_group': 1,
    #     'quota_redirects': quota_redirects,
    #     'quota_total_population': total_gmi,
    #     'quota_gender_age_groups': quota_gender_age_groups_gmi,
    # },
    # {
    #     'name': 'trustlab_2016_gmi',
    #     'display_name': (
    #         'TRUSTLAB | Sept 2016 | EN | GMI Quota Test Run ' +
    #         '(20 participants max)'
    #     ),
    #     'num_demo_participants': total_gmi,
    #     'app_sequence': [
    #         'quota', 'trust', 'public_goods',
    #         'dictator', 'iat', 'survey_i18n', 'earnings'
    #     ],
    #     'treatment': 'A1a',
    #     'language_code': 'en-us',
    #     'payoff_group': 1,
    #     'quota_redirects': quota_redirects,
    #     'quota_total_population': total_gmi,
    #     'quota_gender_age_groups': quota_gender_age_groups_gmi,
    # },



    # {
    #     'name': 'trustlab_2016_run01_A1b_fr',
    #     'display_name': 'TRUSTLAB | Sept 2016 | FR | path A1b',
    #     'num_demo_participants': 126,
    #     'app_sequence': [
    #         'quota', 'trust', 'public_goods',
    #         'dictator', 'iat', 'survey_i18n', 'earnings'
    #     ],
    #     'treatment': 'A1b',
    #     'language_code': 'fr-fr',
    #     'payoff_group': 1,
    #     'quota_redirects': quota_redirects,
    #     'quota_total_population': total_fr,
    #     'quota_gender_age_groups': quota_gender_age_groups_fr,
    # },



    # {
    #     'name': 'trustlab_2016_run01_A2b_fr',
    #     'display_name': 'TRUSTLAB | Sept 2016 | FR | path A2b',
    #     'num_demo_participants': 126,
    #     'app_sequence': [
    #         'quota', 'trust', 'public_goods',
    #         'dictator', 'iat', 'survey_i18n', 'earnings'
    #     ],
    #     'treatment': 'A2b',
    #     'language_code': 'fr-fr',
    #     'payoff_group': 1,
    #     'quota_redirects': quota_redirects,
    #     'quota_total_population': total_fr,
    #     'quota_gender_age_groups': quota_gender_age_groups_fr,
    # },



    # {
    #     'name': 'trustlab_2016_run01_B1b_fr',
    #     'display_name': 'TRUSTLAB | Sept 2016 | FR | path B1b',
    #     'num_demo_participants': 126,
    #     'app_sequence': [
    #         'quota', 'trust', 'public_goods',
    #         'dictator', 'iat', 'survey_i18n', 'earnings'
    #     ],
    #     'treatment': 'B1b',
    #     'language_code': 'fr-fr',
    #     'payoff_group': 1,
    #     'quota_redirects': quota_redirects,
    #     'quota_total_population': total_fr,
    #     'quota_gender_age_groups': quota_gender_age_groups_fr,
    # },



    # {
    #     'name': 'trustlab_2016_run01_B2b_fr',
    #     'display_name': 'TRUSTLAB | Sept 2016 | FR | path B2b',
    #     'num_demo_participants': 126,
    #     'app_sequence': [
    #         'quota', 'trust', 'public_goods',
    #         'dictator', 'iat', 'survey_i18n', 'earnings'
    #     ],
    #     'treatment': 'B2b',
    #     'language_code': 'fr-fr',
    #     'payoff_group': 1,
    #     'quota_redirects': quota_redirects,
    #     'quota_total_population': total_fr,
    #     'quota_gender_age_groups': quota_gender_age_groups_fr,
    # },

    # {
    #     'name': 'trustlab_2016_run01_A2b_ko',
    #     'display_name': 'TRUSTLAB | Sept 2016 | KO | path A2b',
    #     'num_demo_participants': 126,
    #     'app_sequence': [
    #         'quota', 'trust', 'public_goods',
    #         'dictator', 'iat', 'survey_i18n', 'earnings'
    #     ],
    #     'treatment': 'A2b',
    #     'language_code': 'ko-kr',
    #     'payoff_group': 2,
    #     'quota_redirects': quota_redirects,
    #     'quota_total_population': total_ko,
    #     'quota_gender_age_groups': quota_gender_age_groups_ko,
    # },

    # {
    #     'name': 'trustlab_2016_run01_B1a_ko',
    #     'display_name': 'TRUSTLAB | Sept 2016 | KO | path B1a',
    #     'num_demo_participants': 126,
    #     'app_sequence': [
    #         'quota', 'trust', 'public_goods',
    #         'dictator', 'iat', 'survey_i18n', 'earnings'
    #     ],
    #     'treatment': 'B1a',
    #     'language_code': 'ko-kr',
    #     'payoff_group': 2,
    #     'quota_redirects': quota_redirects,
    #     'quota_total_population': total_ko,
    #     'quota_gender_age_groups': quota_gender_age_groups_ko,
    # },

    # {
    #     'name': 'trustlab_2016_run01_B1b_ko',
    #     'display_name': 'TRUSTLAB | Sept 2016 | KO | path B1b',
    #     'num_demo_participants': 126,
    #     'app_sequence': [
    #         'quota', 'trust', 'public_goods',
    #         'dictator', 'iat', 'survey_i18n', 'earnings'
    #     ],
    #     'treatment': 'B1b',
    #     'language_code': 'ko-kr',
    #     'payoff_group': 2,
    #     'quota_redirects': quota_redirects,
    #     'quota_total_population': total_ko,
    #     'quota_gender_age_groups': quota_gender_age_groups_ko,
    # },

    # {
    #     'name': 'trustlab_2016_run01_B2a_ko',
    #     'display_name': 'TRUSTLAB | Sept 2016 | KO | path B2a',
    #     'num_demo_participants': 126,
    #     'app_sequence': [
    #         'quota', 'trust', 'public_goods',
    #         'dictator', 'iat', 'survey_i18n', 'earnings'
    #     ],
    #     'treatment': 'B2a',
    #     'language_code': 'ko-kr',
    #     'payoff_group': 2,
    #     'quota_redirects': quota_redirects,
    #     'quota_total_population': total_ko,
    #     'quota_gender_age_groups': quota_gender_age_groups_ko,
    # },

    # {
    #     'name': 'trustlab_2016_run01_B2b_ko',
    #     'display_name': 'TRUSTLAB | Sept 2016 | KO | path B2b',
    #     'num_demo_participants': 126,
    #     'app_sequence': [
    #         'quota', 'trust', 'public_goods',
    #         'dictator', 'iat', 'survey_i18n', 'earnings'
    #     ],
    #     'treatment': 'B2b',
    #     'language_code': 'ko-kr',
    #     'payoff_group': 2,
    #     'quota_redirects': quota_redirects,
    #     'quota_total_population': total_ko,
    #     'quota_gender_age_groups': quota_gender_age_groups_ko,
    # },

    # {
    #     'name': 'trustlab_2016_run01_A1a_en',
    #     'display_name': 'TRUSTLAB | Sept 2016 | EN | path A1a',
    #     'num_demo_participants': 126,
    #     'app_sequence': [
    #         'quota', 'trust', 'public_goods',
    #         'dictator', 'iat', 'survey_i18n', 'earnings'
    #     ],
    #     'treatment': 'A1a',
    #     'language_code': 'en-us',
    #     'payoff_group': 1,
    #     'quota_redirects': quota_redirects,
    #     'quota_total_population': total_fr,
    #     'quota_gender_age_groups': quota_gender_age_groups_fr,
    # },

    # {
    #     'name': 'trustlab_2016_run01_A1b_en',
    #     'display_name': 'TRUSTLAB | Sept 2016 | EN | path A1b',
    #     'num_demo_participants': 126,
    #     'app_sequence': [
    #         'quota', 'trust', 'public_goods',
    #         'dictator', 'iat', 'survey_i18n', 'earnings'
    #     ],
    #     'treatment': 'A1b',
    #     'language_code': 'en-us',
    #     'payoff_group': 1,
    #     'quota_redirects': quota_redirects,
    #     'quota_total_population': total_fr,
    #     'quota_gender_age_groups': quota_gender_age_groups_fr,
    # },

    # {
    #     'name': 'trustlab_2016_run01_A2a_en',
    #     'display_name': 'TRUSTLAB | Sept 2016 | EN | path A2a',
    #     'num_demo_participants': 126,
    #     'app_sequence': [
    #         'quota', 'trust', 'public_goods',
    #         'dictator', 'iat', 'survey_i18n', 'earnings'
    #     ],
    #     'treatment': 'A2a',
    #     'language_code': 'en-us',
    #     'payoff_group': 1,
    #     'quota_redirects': quota_redirects,
    #     'quota_total_population': total_fr,
    #     'quota_gender_age_groups': quota_gender_age_groups_fr,
    # },

    # {
    #     'name': 'trustlab_2016_run01_A2b_en',
    #     'display_name': 'TRUSTLAB | Sept 2016 | EN | path A2b',
    #     'num_demo_participants': 126,
    #     'app_sequence': [
    #         'quota', 'trust', 'public_goods',
    #         'dictator', 'iat', 'survey_i18n', 'earnings'
    #     ],
    #     'treatment': 'A2b',
    #     'language_code': 'en-us',
    #     'payoff_group': 1,
    #     'quota_redirects': quota_redirects,
    #     'quota_total_population': total_fr,
    #     'quota_gender_age_groups': quota_gender_age_groups_fr,
    # },

    # {
    #     'name': 'trustlab_2016_run01_B1a_en',
    #     'display_name': 'TRUSTLAB | Sept 2016 | EN | path B1a',
    #     'num_demo_participants': 126,
    #     'app_sequence': [
    #         'quota', 'trust', 'public_goods',
    #         'dictator', 'iat', 'survey_i18n', 'earnings'
    #     ],
    #     'treatment': 'B1a',
    #     'language_code': 'en-us',
    #     'payoff_group': 1,
    #     'quota_redirects': quota_redirects,
    #     'quota_total_population': total_fr,
    #     'quota_gender_age_groups': quota_gender_age_groups_fr,
    # },

    # {
    #     'name': 'trustlab_2016_run01_B1b_en',
    #     'display_name': 'TRUSTLAB | Sept 2016 | EN | path B1b',
    #     'num_demo_participants': 126,
    #     'app_sequence': [
    #         'quota', 'trust', 'public_goods',
    #         'dictator', 'iat', 'survey_i18n', 'earnings'
    #     ],
    #     'treatment': 'B1b',
    #     'language_code': 'en-us',
    #     'payoff_group': 1,
    #     'quota_redirects': quota_redirects,
    #     'quota_total_population': total_fr,
    #     'quota_gender_age_groups': quota_gender_age_groups_fr,
    # },

    # {
    #     'name': 'trustlab_2016_run01_B2a_en',
    #     'display_name': 'TRUSTLAB | Sept 2016 | EN | path B2a',
    #     'num_demo_participants': 126,
    #     'app_sequence': [
    #         'quota', 'trust', 'public_goods',
    #         'dictator', 'iat', 'survey_i18n', 'earnings'
    #     ],
    #     'treatment': 'B2a',
    #     'language_code': 'en-us',
    #     'payoff_group': 1,
    #     'quota_redirects': quota_redirects,
    #     'quota_total_population': total_fr,
    #     'quota_gender_age_groups': quota_gender_age_groups_fr,
    # },

    # {
    #     'name': 'trustlab_2016_run01_B2b_en',
    #     'display_name': 'TRUSTLAB | Sept 2016 | EN | path B2b',
    #     'num_demo_participants': 126,
    #     'app_sequence': [
    #         'quota', 'trust', 'public_goods',
    #         'dictator', 'iat', 'survey_i18n', 'earnings'
    #     ],
    #     'treatment': 'B2b',
    #     'language_code': 'en-us',
    #     'payoff_group': 1,
    #     'quota_redirects': quota_redirects,
    #     'quota_total_population': total_fr,
    #     'quota_gender_age_groups': quota_gender_age_groups_fr,
    # },
]
