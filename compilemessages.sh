#!/bin/bash
cd trust && django-admin compilemessages && cd ../public_goods && django-admin compilemessages && cd ../dictator && django-admin compilemessages && cd ../iat && django-admin compilemessages && cd ../survey_i18n && django-admin compilemessages && cd ../earnings && django-admin makemessages && cd ../
