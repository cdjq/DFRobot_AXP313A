'''
说明：
1. 修改后，使得CircuitPython可以写入到内置存储，但将不能在电脑上直接进入U盘修改文件。
2. 在编辑器中，修改Flase为True，或者直接注释掉上面的行，就恢复原样。
3. 修改后，需要断电重启一次生效
'''

import storage
storage.remount("/", False)
