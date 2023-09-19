import board
import time

eOV2640 = 0
e0V7725 = 1
eTime6s = 0
eTime10s = 1

class AXP313A:
    '''
        @fn __init__
        @brief 初始化AXP313A
        @param i2c i2c设备
    '''
    def __init__(self, i2c):
        self.i2c = i2c

    def begin(self):
        '''
            @fn begin
            @brief 初始化传感器
            @return 返回初始化状态
        '''
        while not self.i2c.try_lock():
            pass
        try:
            scan = self.i2c.scan()
            print("scan: ", scan)
        finally:
            self.i2c.unlock()

        for i in scan:
            if(i == 0x36):
                return True
        return False

    def enable_camera_power(self,camera):
        '''
            @fn enableCameraPower
            @brief 使能摄像头电源
            @param camera 摄像头选择
        '''
        if camera == 0:
            self.set_camera_power(1.2,2.8)
        else:
            self.set_camera_power(1.8,3.3)


    def set_camera_power(self,DVDD,AVDDorDOVDD):
        '''
            @fn enablePower
            @brief 设置电压输出
            @param DVDD DVDD电压设置,默认电压为1.5V
            @param AVDDandDOVDD AVDD和DOVDD电压设置，默认电压为2.8V
        '''
        state = 0x19
        ALDOData = 0
        DLDOData = 0
        if(DVDD < 0.5) or (AVDDorDOVDD < 0.5):
            ALDOData = 0
            DLDOData = 0
        elif(DVDD > 3.5) or (AVDDorDOVDD > 3.5):
            ALDOData = 31
            DLDOData = 31
        else:
            ALDOData = (DVDD-0.5) * 10
            DLDOData = (AVDDorDOVDD-0.5) *10
        self.WriteByte(0x10, state)
        time.sleep(0.01)
        self.WriteByte(0x16, int(ALDOData))
        time.sleep(0.01)
        self.WriteByte(0x17, int(DLDOData))
        time.sleep(0.01)

    def set_shutdown_key_level_time(self,offLevelTime):
        '''
            @fn setShutdownKeyLevelTime
            @brief 设置关机按键电平时间
            @param offLevelTime 关机按键电平时间
        '''
        data = offLevelTime << 1
        self.WriteByte(0x1E, data)
        time.sleep(0.01)

    def disable_power(self):
        '''
            @fn disablePower
            @brief 关闭摄像头电源
        '''
        data = 0x01;
        self.WriteByte(0x10, data)
        time.sleep(0.01)

    def WriteByte(self, reg, data):
        buf = bytearray(1)
        buf[0] = reg
        buf.extend(bytearray([data]))
        while not self.i2c.try_lock():
            pass
        try:
            self.i2c.writeto(0x36, buf)
        finally:
            self.i2c.unlock()

if __name__ == "__main__":
    import busio
    
    delay = lambda n: time.sleep(n/1000)

    print("i2c init")
    i2c = busio.I2C(scl=board.GPIO2, sda=board.GPIO1)
    while not i2c.try_lock():
        print("try lock");
        delay(1000)
    i2c.unlock()

    delay(1000)
    print("AXP313A init")
    axp = AXP313A(i2c)

    delay(1000)
    print("AXP313A begin")
    while not axp.begin():
        print("init error");
        delay(1000)

    delay(1000)
    print("AXP313A enable_camera_power")
    axp.enable_camera_power(eOV2640) # 设置摄像头供电 power on

    delay(3000)

    print("AXP313A disable_power")
    axp.disable_power() # 设置摄像头断电 power off

    print("i2c deinit")
    i2c.deinit()

