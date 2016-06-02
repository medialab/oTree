# -*- coding: utf-8 -*-
"""Exporter for IAT results."""

import sys
import ast
import csv


# Each user ends up being 3 CSVs: <id>_meta, <id>_results, <id>_errors.
meta = []
results = []
errors = []


def write_meta_file(meta):
    """Write down meta CSV file."""
    for m in meta:
        filename = (
            'exports_iat/META__' + m[1][3] + '__' +
            m[1][1] + '__' + m[1][2]
        )
        with open(filename + '.csv', 'w') as csvfile:
            writer = csv.writer(csvfile, delimiter=',', quotechar='|')
            writer.writerows(m)


def write_file(res, stem):
    """Write down results CSV file."""
    filename = (
        'exports_iat/' + stem + '__' + res[0][1][4] + '__' +
        res[0][1][2] + '__' + res[0][1][3] + '__'
    )
    with open(filename + '.csv', 'wb') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='|')
        writer.writerow(res[0][0])
        for r in res:
            writer.writerow(r[1])


def remove_html(value):
    """Clean up HTML from entered values."""
    return str(value).replace(
        '<br /><span style=""color:white"">', ' '
    ).replace('</span><br />', ' ')


with open(sys.argv[1], 'r') as f:
    # Index of current user.
    count = 0

    for line in f.readlines():
        # Skip header line.
        if 'Participant._id_in_session' not in line:
            # First batch of data (meta - before actual IAT test).
            m = line[:line.find('"')]

            # Get ID in session, code, label, time started.
            m = m.split(',')
            # Process only finished sessions.
            if 'Not visited yet' not in m[7]:
                id_in_session = m[0].replace('\n', '')
                code = m[1].replace('\n', '')
                label = m[2].replace('\n', '')
                time_started = m[10].replace('\n', '')

                meta.append([
                    [
                        'ID in session', 'Code', 'Label', 'Time started',
                        'Trials order', 'Error percentage'
                    ],
                    [
                        id_in_session, code, label, time_started
                    ]

                ])

                # Second batch of data (actual IAT results): isolate it.
                data = line[line.find('"') + 1:line.rfind('"')]
                data = data.replace('u\'', '\'')

                try:
                    # Deserialize data as dict.
                    data = ast.literal_eval(data)

                    # Get more metadata: trials order, % of errors.
                    meta[count][1].append(data['order'])
                    meta[count][1].append(data['error_percentage'])

                    # Process regular trials' results:
                    trials_results = data['results']
                    for r in trials_results:
                        results.append([
                            [
                                'Trial ID', 'Player ID in session', 'Code',
                                'Label', 'Time started', 'Left category',
                                'Right category', 'Stimuli word',
                                'Correct position', 'Correct category',
                                'Time taken'
                            ],
                            [
                                remove_html(r['id']),
                                id_in_session, code, label, time_started,
                                remove_html(r['left']),
                                remove_html(r['right']),
                                remove_html(r['stimuli']),
                                remove_html(r['correctPosition']),
                                remove_html(r['correctCategory']),
                                r['timing']
                            ]
                        ])

                    # Process regular trials' errors:
                    trials_results = data['errors']
                    for r in trials_results:
                        errors.append([
                            [
                                'Trial ID', 'ID in session', 'Code', 'Label',
                                'Time started', 'Left category',
                                'Right category', 'Stimuli word',
                                'Correct position', 'Correct category',
                                'Failed by time out', 'Time taken'
                            ],
                            [
                                remove_html(r['id']),
                                id_in_session, code, label, time_started,
                                remove_html(r['left']),
                                remove_html(r['right']),
                                remove_html(r['stimuli']),
                                remove_html(r['correctPosition']),
                                remove_html(r['correctCategory']),
                                r['timedOut'],
                                r['timing']
                            ]
                        ])
                except Exception as e:
                    print(e)

                count += 1
    f.close()

write_meta_file(meta)
write_file(results, 'RESULTS')
write_file(errors, 'ERRORS')
