import main as sun
import queue
import subprocess
import json
from pytest import approx
from pathlib import Path


def ffprobe_b(filename:Path) -> dict:
    meta = subprocess.check_output(['ffprobe', '-v', 'warning',
                                        '-print_format', 'json',
                                        '-show_streams',
                                        '-show_format',
                                        str(filename)], universal_newlines=True)
    return json.loads(meta)

def test_time():
    Q = queue.Queue()
    fin = './in/in1.mp4'
    fout = './out/in1.mp4_480p.mp4'
    fout_720 = './out/in1.mp4_720p.mp4'
    name = 'in1.mp4'
    Q.put(name)
    sun.convert_video(Q)
    orig_meta = ffprobe_b(fin)
    orig_duration = float(orig_meta['streams'][0]['duration'])

    meta_480 = ffprobe_b(fout)
    duration_480 = float(meta_480['streams'][0]['duration'])
    meta_720 = ffprobe_b(fout_720)
    duration_720 = float(meta_720['streams'][0]['duration'])
    
    assert orig_duration== approx(duration_480, rel=0.01)
    assert orig_duration== approx(duration_720, rel=0.01)


if __name__ == '__main__':

    test_time()




