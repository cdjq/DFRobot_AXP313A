# DFRobot_AXP313A

* [English Version](./README.md)

这是ESP32-S3主板上摄像头电源管理的库。

## 产品链接（（[www.dfrobot.com](www.dfrobot.com)）
    SKU: 无

## 目录
  - [概述](#概述)
  - [库安装](#库安装)
  - [方法](#方法)
  - [兼容性](#兼容性)
  - [历史](#历史)
  - [创作者](#创作者)

## 概述
这是ESP32-S3主板上摄像头电源管理的库。

## 库安装

这里有2种安装方法：
1. 使用此库前，请首先下载库文件，将其粘贴到\Arduino\libraries目录中，然后打开examples文件夹并在该文件夹中运行演示。
2. 直接在Arduino软件库管理中搜索下载 DFRobot_AXP313A 库

## 方法

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
## 兼容性

MCU                |  Work Well    | Work Wrong   | Untested    | Remarks
------------------ | :----------: | :----------: | :---------: | -----
ESP32-S3            |      √       |              |             | 

## 历史

- 2022/05/17 - 1.0.0 版本

## 创作者

Written by tangjie(jie.tang@dfrobot.com), 2022. (Welcome to our [website](https://www.dfrobot.com/))

