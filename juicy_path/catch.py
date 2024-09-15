#!/usr/bin/env python3
#coding=utf-8

import time
from Arm_Lib import Arm_Device

# 로봇 팔 객체 생성
Arm = Arm_Device()

# 잠시 대기
time.sleep(0.1)

def main():
    # 서보를 중앙 위치로 초기화
    Arm.Arm_serial_servo_write6(180, 30, 0, 165, 180, 180, 2000)
    time.sleep(2)
    Arm.Arm_serial_servo_write(6, 140, 1500)
    time.sleep(1)
    Arm.Arm_serial_servo_write6(180, 23, 20, 150, 180, 120, 1500)
    time.sleep(1)
    Arm.Arm_serial_servo_write(6, 180, 1000)
    time.sleep(1)
    #Arm.Arm_serial_servo_write(1, 180, 500) #1
    #time.sleep(1)
    #Arm.Arm_serial_servo_write(2, 65, 1500)
    #time.sleep(1)
    #Arm.Arm_serial_servo_write(3, 55, 1500)
    #time.sleep(1)
    #Arm.Arm_serial_servo_write(4, 25, 1500)
    #time.sleep(1)
    #Arm.Arm_serial_servo_write(5, 180, 1000)
    #time.sleep(1)  #end
    #Arm.Arm_serial_servo_write(2, 30, 1500) #1
    #time.sleep(1)
    #Arm.Arm_serial_servo_write(4, 165, 1500) #1
    #time.sleep(1)
    #Arm.Arm_serial_servo_write(3, 0, 1500) #1
    #time.sleep(1)
    #Arm.Arm_serial_servo_write(5, 180, 1500) #1
    #time.sleep(1)
    #Arm.Arm_serial_servo_write(6, 150, 1500)
    #time.sleep(1)
    #Arm.Arm_serial_servo_write(2, 24, 500) #1
    #time.sleep(1)
    #Arm.Arm_serial_servo_write(4, 160, 1000) #1
    #time.sleep(1)
    #Arm.Arm_serial_servo_write(3, 20, 1000) #1
    #time.sleep(1)
    #Arm.Arm_serial_servo_write(6, 180, 1500)
    #time.sleep(1)


try:
    main()
except KeyboardInterrupt:
    print("프로그램이 종료되었습니다!")
    pass

# 로봇 팔 객체 해제
del Arm