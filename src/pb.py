# progressbar module test
from progressbar import ProgressBar
import time

pbar = ProgressBar(maxval=10).start()
for i in range(10):
    pbar.update(i)
    time.sleep(1)
pbar.finish()
