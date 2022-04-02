#!/bin/bash
sudo systemctl daemon-reload
sudo systemctl start castle
sudo systemctl enable castle
sudo systemctl status castle -l
