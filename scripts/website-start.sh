#!/bin/bash
source ~/my-website-venv/bin/activate
cd ~/my-website/my-website
gunicorn -w 1 --forwarded-allow-ips="*" website:app
