# pip install yaspin

import time
from yaspin import yaspin

# 命令行动画等待
with yaspin(text="loading...", color="yellow") as sp:
    time.sleep(2)

