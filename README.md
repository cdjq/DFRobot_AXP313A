# DFRobot_AXP313A

* [中文版](./README_CN.md)

这是ESP32-S3主板上摄像头电源管理的库。


## Product Link（[www.dfrobot.com](www.dfrobot.com)）
    SKU: 无

## Table of Contents
  - [Summary](#summary)
  - [Installation](#installation)
  - [Methods](#methods)
  - [Compatibility](#compatibility)
  - [History](#history)
  - [Credits](#credits)

## Summary
这是ESP32-S3主板上摄像头电源管理的库。

## Installation

There two methods: 
1. To use this library, first download the library file, paste it into the \Arduino\libraries directory, then open the examples folder and run the demo in the folder.
2. Search the DFRobot_AXP313A library from the Arduino Software Library Manager and download it.

## Methods

```C++
  /**
   * @fn begin
   * @brief 初始化传感器
   * @return 返回初始化状态
   * @retval 0 初始化成功
   * @retval 1 初始化失败
   */
  uint8_t begin(void);

  /**
   * @fn enablePower
   * @brief 使能电源输出
   * @param DVDD DVDD电压设置,默认电压为1.5V
   * @param AVDDandDOVDD AVDD和DOVDD电压设置，默认电压为2.8V
   * @return NONE
   */
  void enablePower(float DVDD = 1.5,float AVDDorDOVDD = 2.8);

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
  void setShutdownKeyLevelTime(eShutdownKeyLevelTime_t offLevelTime);
```
## Compatibility

MCU                |  Work Well    | Work Wrong   | Untested    | Remarks
------------------ | :----------: | :----------: | :---------: | -----
ESP32-s3           |      √       |              |             | 


## History

- 2022/05/17 - Version 1.0.0 released.

## Credits

Written by tangjie(jie.tang@dfrobot.com), 2022. (Welcome to our [website](https://www.dfrobot.com/))

