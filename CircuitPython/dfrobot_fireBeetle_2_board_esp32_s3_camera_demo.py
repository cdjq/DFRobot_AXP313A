'''
DFRobot FireBeetle_2_Board_ESP32_S3 摄像头演示程序

使用指导：请务必参考以下网址的使用指导，否则可能会出现各种问题
    https://mc.dfrobot.com.cn/thread-316903-1-1.html

参考资料:
    https://learn.adafruit.com/adafruit-ov5640-camera-breakout/jpeg-capture-demo
    https://wiki.dfrobot.com.cn/_SKU_DFR0975_FireBeetle_2_Board_ESP32_S3_Advanced_Tutorial#target_12
    https://learn.adafruit.com/circuitpython-essentials/circuitpython-storage
'''

import board
import busio
import time
import espidf
import espcamera
import AXP313A

'''
PWDN_GPIO_NUM      = -1
RESET_GPIO_NUM     = -1
XCLK_GPIO_NUM      = 45
SIOD_GPIO_NUM      = 1
SIOC_GPIO_NUM      = 2

Y9_GPIO_NUM        = 48
Y8_GPIO_NUM        = 46
Y7_GPIO_NUM        = 8
Y6_GPIO_NUM        = 7
Y5_GPIO_NUM        = 4
Y4_GPIO_NUM        = 41
Y3_GPIO_NUM        = 40
Y2_GPIO_NUM        = 39
VSYNC_GPIO_NUM     = 6
HREF_GPIO_NUM      = 42
PCLK_GPIO_NUM      = 5
'''

# 数据引脚定义 data pins
CAMERA_DATA = (
    board.GPIO39,
    board.GPIO40,
    board.GPIO41,
    board.GPIO4,
    board.GPIO7,
    board.GPIO8,
    board.GPIO46,
    board.GPIO48
)

# 控制引脚定义 controll pins
CAMERA_PCLK=board.GPIO5
CAMERA_VSYNC=board.GPIO6
CAMERA_HREF=board.GPIO42
CAMERA_XCLK=board.GPIO45

# 延时函数定义 delay function
delay = lambda n: time.sleep(n/1000)

print("check reserved psram")
reserved_psram = espidf.get_reserved_psram()
if reserved_psram<1048576:
    print("Please config settings.toml: CIRCUITPY_RESERVED_PSRAM=1048576")
    print("  and then reset the board")
    raise Exception("MemoryError:")

print("i2c init")
i2c = busio.I2C(scl=board.GPIO2, sda=board.GPIO1)
while not i2c.try_lock():
    print("try lock");
    delay(1000)
i2c.unlock()

delay(1000)
print("AXP313A init")
axp = AXP313A.AXP313A(i2c)

delay(1000)
print("AXP313A begin")
while not axp.begin():
    print("init error");
    delay(1000)

delay(1000)
print("AXP313A enable_camera_power")
axp.enable_camera_power(AXP313A.eOV2640) # 设置摄像头供电 power on

delay(1000)

print("Initializing camera")
cam = espcamera.Camera(
    data_pins=CAMERA_DATA,
    external_clock_pin=CAMERA_XCLK,
    pixel_clock_pin=CAMERA_PCLK,
    vsync_pin=CAMERA_VSYNC,
    href_pin=CAMERA_HREF,
    pixel_format=espcamera.PixelFormat.RGB565,
    frame_size=espcamera.FrameSize.QVGA,
    i2c=i2c,
    external_clock_frequency=20_000_000,
    framebuffer_count=1)
print("initialized")

print("reconfigure")
# for display
#cam.reconfigure(
#    pixel_format=espcamera.PixelFormat.RGB565,
#    frame_size=espcamera.FrameSize.QVGA,
#)
#frame = cam.take(1)

# for jpeg
cam.reconfigure(
    pixel_format=espcamera.PixelFormat.JPEG,
    frame_size=espcamera.FrameSize.SVGA,
)

print("capture")
jpeg = cam.take(1)

print("write")
filename = f"/test_001.jpg"
with open(filename, "wb") as f:
    f.write(jpeg)

print("AXP313A disable_power")
axp.disable_power() # 设置摄像头断电 power off

print("i2c deinit")
i2c.deinit()