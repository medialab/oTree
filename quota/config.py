# This is an exemple config for SESSION_CONFIGS when you
# want to create an experiment using quota from GMI.
total = 10

config = {
    'name': 'quota',
    'display_name': 'Quota',
    'num_demo_participants': 100,
    'app_sequence': ['quota'],

    # URL stems for redirections
    'quota_redirects': {
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
    },

    # Must match number of participants for this link.
    'quota_total_population': total,

    # Initialize as well vars used for monitoring:
    # `expected` -> % of `quota_total_population` passing in the given quota
    # `currently` -> incrementable counter for current % of used slot
    # Increment `currently` at each passage of a user on the Quota app.
    # When `currently` >= `expected`, quota is full.

    # Catching (TBA) GET variable from GMI
    # TODO: Recompose name using variable names when known.
    'quota_income_groups': {
        'i_1': {
            'percentage': 33.33,
            'expected': total * (33.33 / 100),
            'currently': 0
        },
        'i_2': {
            'percentage': 33.33,
            'expected': total * (33.33 / 100),
            'currently': 0
        },
        'i_3': {
            'percentage': 33.33,
            'expected': total * (33.33 / 100),
            'currently': 0
        }
    },

    # Catching 'gender' and 'age' GET variables from GMI.
    # TODO: Recompose name using variable names when known.
    'quota_gender_age_groups': {
        '1_18_24': {
            'percentage': 7, 'expected': total * (7 / 100), 'currently': 0
        },
        '1_25_34': {
            'percentage': 10, 'expected': total * (10 / 100), 'currently': 0
        },
        '1_35_44': {
            'percentage': 11, 'expected': total * (11 / 100), 'currently': 0
        },
        '1_45_54': {
            'percentage': 11, 'expected': total * (11 / 100), 'currently': 0
        },
        '1_55_64': {
            'percentage': 11, 'expected': total * (11 / 100), 'currently': 0
        },
        '2_18_24': {
            'percentage': 12, 'expected': total * (12 / 100), 'currently': 0
        },
        '2_25_34': {
            'percentage': 7, 'expected': total * (7 / 100), 'currently': 0
        },
        '2_35_44': {
            'percentage': 10, 'expected': total * (10 / 100), 'currently': 0
        },
        '2_45_54': {
            'percentage': 11, 'expected': total * (11 / 100), 'currently': 0
        },
        '2_55_64': {
            'percentage': 11, 'expected': total * (11 / 100), 'currently': 0
        },
    }
}
