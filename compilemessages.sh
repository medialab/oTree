#!/bin/bash
cd trust && django-admin compilemessages && cd ../public_goods && django-admin compilemessages && cd ../dictator && django-admin compilemessages && cd ../
