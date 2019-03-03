import main as sun
import queue
from math import isclose
import subprocess
import json
from pathlib import Path

def ffprobe(filename:Path) -> dict:
    meta = subprocess.check_output(['ffprobe', '-v', 'warning',
                                        '-print_format', 'json',
                                        '-show_streams',
                                        '-show_format',
                                        filename], universal_newlines=True)
    return json.loads(meta)


def test_time():
    Q = queue.Queue()
    fin = './in/in1.mp4'
    fout = './out/in1.mp4_480p.mp4'
    Q.put(fin)
    sun.convert_video(Q)
    orig_meta = ffprobe(fin)
    orig_duration = float(orig_meta['streams'][0]['duration'])

    meta_480 = ffprobe(fout)
    duration_480 = float(meta_480['streams'][0]['duration'])
    assert orig_duration == isclose(duration_480)



if __name__ == '__main__':

    test_time()



