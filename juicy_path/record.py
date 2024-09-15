#!/usr/bin/env python3
#coding=utf-8
import time
from Arm_Lib import Arm_Device

# 로봇 팔 객체 생성
Arm = Arm_Device()
#Arm.Arm_Button_Mode(1)

#Arm.Arm_Action_Study()

#Arm.Arm_Button_Mode(0)

#num = Arm.Arm_Read_Action_Num()
#print(num)

Arm.Arm_Action_Mode(1)

#Arm.Arm_Action_Mode(2)

#Arm.Arm_Action_Mode(0)

#Arm.Arm_Clear_Action()

#del Arm