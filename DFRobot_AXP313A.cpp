/*!
 * @file DFRobot_AXP313A.cpp
 * @brief 这是AXP313A的方法实现文件
 * @copyright   Copyright (c) 2010 DFRobot Co.Ltd (http://www.dfrobot.com)
 * @license     The MIT License (MIT)
 * @author [TangJie](jie.tang@dfrobot.com)
 * @version  V1.0
 * @date  2022-05-17
 * @url https://github.com/DFRobor/DFRobot_AXP313A
 */
#include "DFRobot_AXP313A.h"


DFRobot_AXP313A::DFRobot_AXP313A(uint8_t addr, TwoWire *pWire)
{
  _pWire = pWire;
	_addr  = addr;
}

uint8_t DFRobot_AXP313A::begin(void)
{
  uint8_t state = 0x04;
  _pWire->begin();
  _pWire->beginTransmission(_addr);
  _pWire->write(0x00);
  if(_pWire->endTransmission() != 0)
    return 1;
  writeReg(0x00,&state,1);
  return 0;

}

void DFRobot_AXP313A::enableCameraPower(eCamera_t camera)
{
  if(camera == eCamera_t::eOV2640){
    setCameraPower(1.2,2.8);
  }else{
    setCameraPower(1.8,3.3);
  }
}

void DFRobot_AXP313A::setCameraPower(float DVDD, float AVDDorDOVDD)
{

  uint8_t ALDOData = 0;
  uint8_t DLDOData = 0;
  uint8_t state = 0x19;
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
  writeReg(0x10,&state,1);
  delay(10);
  writeReg(0x16,&ALDOData,1);//ALDO
  delay(10);
  writeReg(0x17,&DLDOData,1);//DLDO
  delay(10);
}

void DFRobot_AXP313A::disablePower(void)
{
  uint8_t data = 0x01;
  writeReg(0x10,&data,1);
  delay(10);
}

void DFRobot_AXP313A::setShutdownKeyLevelTime(eShutdownKeyLevelTime_t offLevelTime)
{
  uint8_t data = offLevelTime << 1;
  writeReg(0x1E,&data,1);
}

void DFRobot_AXP313A::writeReg(uint8_t reg, void *pBuf, size_t size)
{
  uint8_t *_pBuf = (uint8_t*)pBuf;
  _pWire->beginTransmission(_addr);
  _pWire->write(reg);

  for(size_t i = 0; i < size; i++){
    _pWire->write(_pBuf[i]);
  }
  _pWire->endTransmission();
}
