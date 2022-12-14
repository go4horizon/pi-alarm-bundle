import os
from dotenv import load_dotenv

load_dotenv()

B_PIN = int(os.getenv('B_PIN', 13))
DEFAULT_SOUND_PATH = os.getenv('DEFAULT_SOUND_PATH', './resources/')
VOLUME_SOUND_PATH = os.getenv('VOLUME_SOUND_PATH', '/mnt/volume/')
ALARM_F_NAME = os.getenv('ALARM_F_NAME', '1.mp3')
NO_F_NAME = os.getenv('NO_F_NAME', '2.mp3')
API_PATH = os.getenv('API_PATH', 'https://ociokexap5.execute-api.eu-central-1.amazonaws.com/v1/status/device')


def serial() -> str:
    cpuserial = "0000000000000000"
    try:
        f = open('/proc/cpuinfo', 'r')
        for line in f:
            if line[0:6] == 'Serial':
                cpuserial = line[10:26]
        f.close()
    except:
        cpuserial = "ERROR000000000"

    return cpuserial


if __name__ == '__main__':
    print('Serial: ' + serial())
