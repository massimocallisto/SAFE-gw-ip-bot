# Get IP interfaces with Telegram
Use a Telegram bot to send on request the local IP addresses

## Install the service

Edit `telegram-bot.service` according to your deploy path.

Copy `telegram-bot.service` to the /etc/systemd/system/ directory

Reload the systemd manager configuration, reload it and run:

    sudo systemctl daemon-reload
    sudo systemctl enable telegram-bot.service
    sudo systemctl start telegram-bot.service

Check the system with:

    journalctl -f -u telegram-both
