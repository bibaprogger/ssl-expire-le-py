python script that check domains in letsencrypt dir, and send notification into telegram chat when expiration date reaches threshold.

require your config.py file with unique TOKEN, CHAT_ID and THREAD_ID variables.

run this script with crontab: @daily python3 /var/lib/ssl-expire-le-py/main.py 

TODO: auto renewal
