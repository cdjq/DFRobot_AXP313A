from machine import Pin, I2C
import time

eOV2640 = 0
e0V7725 = 1
eTime6s = 0
eTime10s = 1

class AXP313A:
    def __init__(self):
        self.i2c = I2C(1, scl=Pin(2), sda=Pin(1))
        
    def begin(self):
        '''
            @fn begin
            @brief 初始化传感器
            @return 返回初始化状态
        '''
        scan = self.i2c.scan()
        for i in scan:
            print(i)
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
		self.i2c.writeto_mem(0x36, reg, bytearray([data]))
     
