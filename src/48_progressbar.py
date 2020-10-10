from progressbar import ProgressBar
import time

if __name__ == '__main__':
    # progressbar module test
    pbar = ProgressBar(maxval=10).start()
    for i in range(10):
        pbar.update(i)
        time.sleep(1)
    pbar.finish()
