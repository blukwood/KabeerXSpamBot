from kabeer import kabeercmd, vcraidcmd
from kabeer import Config

LOGGER = Config.LOG_CHANNEL
if __name__ == '__main__':
    print("KABEER : STARTING BOT")
    kabeercmd.start()
    print("KABEER : STARTING VC RAIDER")
    vcraidcmd.start()
    print("STARTED PLEASE SEE LOG CHANNEL FOR MORE INFO.")
    kabeercmd.send_message(LOGGER, "BOT STARTED")
    vcraidcmd.send_message(LOGGER, "VC RAIDER STARTED")
