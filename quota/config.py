# This is an exemple config for SESSION_CONFIGS when you
# want to create an experiment using quota from GMI.
config = {
    'name': 'quota',
    'display_name': 'Quota',
    'num_demo_participants': 100,
    'app_sequence': ['quota'],

    # Must match number of participants for this link.
    'quota_total_population': 100,

    # Catching (TBA) GET variable from GMI
    # TODO: Recompose name using variable names when known.
    'quota_income_groups': {
        'i_1': {'percentage': 33.33},
        'i_2': {'percentage': 33.33},
        'i_3': {'percentage': 33.33}
    },

    # Catching 'gender' and 'age' GET variables from GMI.
    # TODO: Recompose name using variable names when known.
    'quota_gender_age_groups': {
        'm_18_24': {'percentage': 7},
        'm_18_24': {'percentage': 10},
        'm_18_24': {'percentage': 11},
        'm_18_24': {'percentage': 11},
        'f_18_24': {'percentage': 12},
        'f_18_24': {'percentage': 7},
        'f_18_24': {'percentage': 10},
        'f_18_24': {'percentage': 11},
        'f_18_24': {'percentage': 11},
        'f_18_24': {'percentage': 12}
    }
}
