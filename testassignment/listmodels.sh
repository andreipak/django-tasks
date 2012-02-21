#!/bin/bash

python manage.py listmodels --tee-stderr 2> $(date '+%Y-%m-%d').dat