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
   * @brief 初始化该模块。
   */
  uint8_t begin(void);

	/**
   * @fn setDACOutRange
   * @brief 设置DAC输出范围
   * @param range DAC输出范围
   * @return NONE
   */
  void setDACOutRange(eOutPutRange range);
    
  /**
   * @fn setDACOutVoltage
   * @brief 设置不同通道输出DAC值
   * @param data 需要输出的电压值
   * @param channel 输出通道 0:通道0;1:通道1;2:全部通道
   * @return NONE
   */
  void setDACOutVoltage(uint16_t data,uint8_t channel);
  /**
   * @brief 将设置的电压保存在芯片内部
   */
	void store(void);
  /**
   * @brief 调用函数输出正弦波
   * @param amp 设点正弦波幅度Vp
   * @param freq 设置正弦波频率f
   * @param offset 设置正弦波直流偏置Voffset
   * @param channel 输出通道 0:通道0;1:通道1;2:全部通道
   */
	void outputSin(uint16_t amp, uint16_t freq, uint16_t offset,uint8_t channel);
  /**
   * @brief 调用函数输出三角波
   * @param amp 设点正弦波幅度Vp
   * @param freq 设置正弦波频率f
   * @param offset 设置正弦波直流偏置Voffset
   * @param dutyCycle 设定三角（锯齿）波占空比
   * @param channel 输出通道 0:通道0;1:通道1;2:全部通道
   */
	void outputTriangle(uint16_t amp, uint16_t freq, uint16_t offset, int8_t dutyCycle, uint8_t channel);
  /**
   * @brief 调用函数输出方波
   * @param amp 设点正弦波幅度Vp
   * @param freq 设置正弦波频率f
   * @param offset 设置正弦波直流偏置Voffset
   * @param dutyCycle 设定方波波占空比
   * @param channel 输出通道 0:通道0;1:通道1;2:全部通道
   */
	void outputSquare(uint16_t amp, uint16_t freq, uint16_t offset, int8_t dutyCycle, uint8_t channel);
```
## 兼容性

MCU                |  Work Well    | Work Wrong   | Untested    | Remarks
------------------ | :----------: | :----------: | :---------: | -----
ESP32-S3            |      √       |              |             | 

## 历史

- 2022/05/17 - 1.0.0 版本

## 创作者

Written by tangjie(jie.tang@dfrobot.com), 2022. (Welcome to our [website](https://www.dfrobot.com/))

