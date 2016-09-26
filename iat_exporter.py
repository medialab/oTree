# -*- coding: utf-8 -*-
#!/usr/bin/env python
"""Exporter for IAT results."""

import sys
import ast
import csv
import json


# Each user ends up being 3 CSVs: <id>_meta, <id>_results, <id>_errors.
meta = []
results = []
errors = []


# Arguments for CLI are:
# - file to parse
# - label to add to filename (optional)
# - path to directory to save to (optional, default to "./exports_iat")
file_to_parse = sys.argv[1]
file_label = ''
export_dir = 'exports_iat'

try:
    file_label = sys.argv[2]
except:
    pass

try:
    export_dir = sys.argv[3]
except:
    pass


def write_meta_file(meta):
    """Write down meta CSV file."""
    filename = (
        export_dir + '/IAT_metadata_' + file_label
    )
    with open(filename + '.csv', 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='|')
        writer.writerow(meta[0][0])
        for m in meta:
            writer.writerow(m[1])


def write_file(res, stem):
    """Write down results CSV file."""
    filename = (
        export_dir + '/IAT_' + stem + '_' + file_label
    )
    with open(filename + '.csv', 'w') as csvfile:
        writer = csv.writer(csvfile, delimiter=',', quotechar='|')
        writer.writerow(res[0][0])
        for r in res:
            writer.writerow(r[1])


def remove_html(value):
    """Clean up HTML from entered values."""
    return str(value).replace(
        '<br /><span style=""color:white"">', ' '
    ).replace('</span><br />', ' ')


with open(file_to_parse, 'r') as f:
    # Index of current user.
    count = 0

    for line in f.readlines():
        line = line.replace('""""""', '').replace('""', '"')
        # print(line)

        # Skip header line.
        if 'Participant._id_in_session' not in line:
            # First batch of data (meta - before actual IAT test).
            m = line[:line.find('"')]

            # Get MTurk ID, code, label, time started.
            m = m.split(',')
            # Process only finished sessions.
            if 'Not visited yet' not in m[7]:
                mturk_id = m[15]
                code = m[1].replace('\n', '')
                label = m[2].replace('\n', '')
                time_started = m[10].replace('\n', '')

                if mturk_id is not None and mturk_id != '':
                    meta.append([
                        [
                            'MTurk ID', 'Code', 'Label', 'Time started',
                            'Trials order', 'Error percentage'
                        ],
                        [
                            mturk_id, code, label, time_started
                        ]

                    ])

                    # Second batch of data (actual IAT results): isolate it.
                    data = line[line.find('"') + 1:line.rfind('"')]
                    print(data[0:20])
                    # data = data.replace('u\'', '\'')

                    try:
                        # Deserialize data as dict.
                        # data = ast.literal_eval(data)
                        data = json.loads(data)

                        # Get more metadata: trials order, % of errors.
                        meta[count][1].append(data['order'])
                        meta[count][1].append(data['error_percentage'])

                        # Process regular trials' results:
                        trials_results = data['results']
                        for r in trials_results:
                            results.append([
                                [
                                    'Trial ID', 'Player MTurk ID', 'Code',
                                    'Label', 'Time started', 'Left category',
                                    'Right category', 'Stimuli word',
                                    'Correct position', 'Correct category',
                                    'Time taken'
                                ],
                                [
                                    remove_html(r['id']),
                                    mturk_id, code, label, time_started,
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
                                    'Trial ID', 'MTurk ID', 'Code', 'Label',
                                    'Time started', 'Left category',
                                    'Right category', 'Stimuli word',
                                    'Correct position', 'Correct category',
                                    'Failed by time out', 'Time taken'
                                ],
                                [
                                    remove_html(r['id']),
                                    mturk_id, code, label, time_started,
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
write_file(results, 'results')
write_file(errors, 'errors')
