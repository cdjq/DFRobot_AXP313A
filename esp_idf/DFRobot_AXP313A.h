#ifndef _DFROBOT_AXP313A_H_
#define _DFROBOT_AXP313A_H_
#include "stdio.h"
#include "driver/i2c.h"
#define OV2640 0
#define OV7725 1
#define TIME6S 0
#define TIME10S 0

i2c_port_t _i2c_num; 
uint8_t _addr;

/**
 * @brief 配置I2C通信
 * @param i2c_num i2c端口
 * @param addr 设置地址
 */
  void begin(i2c_port_t i2c_num,uint8_t addr);
  /**
   * @fn enableCameraPower
   * @brief 使能摄像头电源
   * @param camera 摄像头选择
   * @return NONE
   */
  void enableCameraPower(uint8_t camera);

  /**
   * @fn disablePower
   * @brief 关闭摄像头电源
   * @return NONE
   */
  void disablePower(void);

  /**
   * @fn setShutdownKeyLevelTime
   * @brief 设置关机按键电平时间
   * @param offLevelTime 关机按键电平时间
   * @return NONE
   */
  void setShutdownKeyLevelTime(uint8_t offLevelTime);

  /**
   * @fn enablePower
   * @brief 使能电源输出
   * @param DVDD DVDD电压设置,默认电压为1.5V
   * @param AVDDandDOVDD AVDD和DOVDD电压设置，默认电压为2.8V
   * @return NONE
   */
  void setCameraPower(float DVDD ,float AVDDorDOVDD);
   

#endif
