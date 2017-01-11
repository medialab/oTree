#!/bin/bash
cd ./introduction && $(which django-admin) makemessages --settings=otree.settings &&\
cd ../trust && $(which django-admin) makemessages --settings=otree.settings &&\
cd ../public_goods && $(which django-admin) makemessages --settings=otree.settings &&\
cd ../dictator && $(which django-admin) makemessages --settings=otree.settings &&\
cd ../iat && $(which django-admin) makemessages --settings=otree.settings &&\
cd ../survey_i18n && $(which django-admin) makemessages --settings=otree.settings &&\
cd ../earnings && $(which django-admin) makemessages --settings=otree.settings &&
cd ../
