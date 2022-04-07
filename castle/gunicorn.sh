#!/bin/bash
sudo gunicorn -w 4 --reload --bind 0.0.0.0:80 "castle.__init__:create_app()"
