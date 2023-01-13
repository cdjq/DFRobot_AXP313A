#include "DFRobot_AXP313A.h"

static esp_err_t __attribute__((unused)) i2cWriteData(i2c_port_t i2c_num, uint8_t *data_wr, size_t size)
{
    i2c_cmd_handle_t cmd = i2c_cmd_link_create();
    i2c_master_start(cmd);
    i2c_master_write_byte(cmd, (_addr << 1) | I2C_MASTER_WRITE, 0x1);
    i2c_master_write(cmd, data_wr, size, 0x1);
    i2c_master_stop(cmd);
    esp_err_t ret = i2c_master_cmd_begin(i2c_num, cmd, 1000 / portTICK_RATE_MS);
    i2c_cmd_link_delete(cmd);
    return ret;
}

void begin(i2c_port_t i2c_num,uint8_t addr)
{
    _i2c_num = i2c_num;
    _addr = addr;
    uint8_t data[2];
    data[0] = 0x00;
    data[1] = 0x04;
   int ret =i2cWriteData(_i2c_num,data,2);  
    vTaskDelay(100);
}

void setCameraPower(float DVDD ,float AVDDorDOVDD)
{
    uint8_t ALDOData = 0;
    uint8_t DLDOData = 0;
    uint8_t state = 0x19;
    uint8_t data[2];
    if(DVDD < 0.5 || AVDDorDOVDD < 0.5){
        ALDOData = 0;
        DLDOData = 0;
    }else if(DVDD > 3.5 || AVDDorDOVDD > 3.5){
        ALDOData = 31;
        DLDOData = 31;
    }else{
        ALDOData = (DVDD-0.5) * 10;
        DLDOData = (AVDDorDOVDD-0.5) *10;
    }
    data[0] = 0x10;
    data[1] = state;
    i2cWriteData(_i2c_num,data,2);  
    vTaskDelay(100);
    data[0] = 0x16;
    data[1] = ALDOData;
    i2cWriteData(_i2c_num,data,2);  
    vTaskDelay(100);
    data[0] = 0x17;
    data[1] = DLDOData;
    i2cWriteData(_i2c_num,data,2);  
    vTaskDelay(100);

}
void disablePower(void)
{
    uint8_t data[2];
    data[0] = 0x10;
    data[1] = 0x01;
    i2cWriteData(_i2c_num,data,2);
    vTaskDelay(100);
}
 void enableCameraPower(uint8_t camera)
 {
    if(camera == 0){
        setCameraPower(1.2,2.8);
    }else{
        setCameraPower(1.8,3.3);
    }
 }
void setShutdownKeyLevelTime(uint8_t offLevelTime)
{
    uint8_t data[2];
    data[0] = 0x1E;
    data[1] = offLevelTime<<1;
    i2cWriteData(_i2c_num,data,2);
    vTaskDelay(100);
}

