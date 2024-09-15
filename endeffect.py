#!/usr/bin/env python3
#coding=utf-8

import time
from Arm_Lib import Arm_Device

# 로봇 팔 객체 생성
Arm = Arm_Device()

time.sleep(0.1)

# 6번 서보 모터를 제어하여 물건을 잡고 놓는 함수
def control_gripper():
    # 물건 잡기: 6번 서보를 각도 30도로 이동 (잡기)
    print("Grabbing the object...")
    Arm.Arm_serial_servo_write(6, 180, 500)  # 6번 서보를 30도로 설정하여 물건을 잡음
    time.sleep(1)  # 1초 대기하여 동작 완료

    # 동작 후 서보의 현재 각도 읽기
    current_angle = Arm.Arm_serial_servo_read(6)
    print(f"Gripper current angle after grabbing: {current_angle} degrees")

    # 잠시 대기
    time.sleep(2)

    # 물건 놓기: 6번 서보를 100도로 이동 (놓기)
    print("Releasing the object...")
    #Arm.Arm_serial_servo_write(6, 10, 500)  # 6번 서보를 100도로 설정하여 물건을 놓음
    #time.sleep(1)  # 1초 대기하여 동작 완료

    # 동작 후 서보의 현재 각도 읽기
    current_angle = Arm.Arm_serial_servo_read(6)
    print(f"Gripper current angle after releasing: {current_angle} degrees")

try:
    control_gripper()
except KeyboardInterrupt:
    print(" 프로그램이 종료되었습니다!")
finally:
    # 로봇 팔 객체 해제
    del Arm
    print("로봇 팔이 초기화되었습니다.")

