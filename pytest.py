import main as run
import queue
from math import isclose


if __name__ == '__main__':

    Q = queue.Queue()
    fin = './in/in1.mp4'
    fout = './out/in1.mp4_480p.mp4'
    Q.put(fin)
    run.convert_video(Q)
    orig_meta = run.ffprobe(fin)
    orig_duration = float(orig_meta['streams'][0]['duration'])

    meta_480 = run.ffprobe(fout)
    duration_480 = float(meta_480['streams'][0]['duration'])
    assert orig_duration == isclose(duration_480)
