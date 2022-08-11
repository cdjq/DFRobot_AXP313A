/*!
 * @file power.ino
 * @brief AXP313A摄像头电源管理例程，运行例程设置关机按键电平时间，设置摄像头供电延时1秒关闭摄像头供电
 * @copyright  Copyright (c) 2021 DFRobot Co.Ltd (http://www.dfrobot.com)
 * @license The MIT License (MIT)
 * @author [TangJie](jie.tang@dfrobot.com)
 * @version V1.0
 * @date 2022-05-17
 * @url https://github.com/DFRobot/DFRobot_AXP313A
 */

#include "DFRobot_AXP313A.h"

DFRobot_AXP313A axp;
void setup(){
  Serial.begin(115200);
  while(axp.begin() != 0){
    Serial.println("init error");
    delay(1000);
  }
  Serial.println("init succeed");
  axp.setShutdownKeyLevelTime(axp.eTime10s);//设置关机按键电平时间
  axp.enableCameraPower(axp.eOV2640);//设置摄像头供电
  delay(1000);
  axp.disablePower();//关闭摄像头供电
}

void loop(){
  delay(100);
}