from kabeer import exploiter
from kabeer import Config

LOGGER = Config.LOG_CHANNEL
if __name__ == '__main__':
    print("KABEER : STARTING BOT")
    exploiter.run()
    print("STARTED PLEASE SEE LOG CHANNEL FOR MORE INFO.")
    kabeercmd.send_message(LOGGER, "BOT STARTED")
