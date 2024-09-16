#카메라 좌표계를 로봇 암 좌표계로 변환하고, 
# 6축 좌표계로 변환하는 기본적인 Python 코드임!

import numpy as np
import math
import json
import os

# 링크 길이 (L1~L5) - 각 링크 사이의 거리를 측정해서 여기에 넣으세요
L1 = 10  # 베이스(1축)에서 어깨(2축)까지의 거리 (단위: cm)
L2 = 15  # 어깨(2축)에서 팔꿈치(3축)까지의 거리 (단위: cm)
L3 = 15  # 팔꿈치(3축)에서 손목(4축)까지의 거리 (단위: cm)
L4 = 10  # 손목(4축)에서 손목 회전부(5축)까지의 거리 (단위: cm)
L5 = 5   # 손목 회전부(5축)에서 엔드 이펙터(6축)까지의 거리 (단위: cm)

# 역기구학 함수: XYZ 좌표와 각도(Roll, Pitch, Yaw)를 입력으로 받아 6축 로봇 암의 각도를 계산
def inverse_kinematics(x, y, z, roll, pitch, yaw):
    """
    6축 로봇 암의 역기구학을 계산하는 함수
    :param x: 목표 위치의 x 좌표 (cm)
    :param y: 목표 위치의 y 좌표 (cm)
    :param z: 목표 위치의 z 좌표 (cm)
    :param roll: 엔드 이펙터의 roll (x축 회전 각도, 단위: radian)
    :param pitch: 엔드 이펙터의 pitch (y축 회전 각도, 단위: radian)
    :param yaw: 엔드 이펙터의 yaw (z축 회전 각도, 단위: radian)
    :return: 6개의 서보모터 각도 (theta1 ~ theta6)
    """
    # Step 1: 베이스 회전 각도 (theta1) 계산
    theta1 = math.atan2(y, x)  # 베이스의 회전 각도 (1축)

    # Step 2: 팔의 평면 거리 (r)와 수직 거리 (z') 계산
    r = math.sqrt(x**2 + y**2)  # 수평 거리
    z_prime = z - L1  # z 좌표에서 L1(베이스 높이) 빼기

    # Step 3: 어깨와 팔꿈치 각도 (theta2, theta3) 계산
    D = (r**2 + z_prime**2 - L2**2 - L3**2) / (2 * L2 * L3)
    theta3 = math.atan2(math.sqrt(1 - D**2), D)  # 팔꿈치 각도 (3축)
    theta2 = math.atan2(z_prime, r) - math.atan2(L3 * math.sin(theta3), L2 + L3 * math.cos(theta3))  # 어깨 각도 (2축)

    # Step 4: 손목 부분 회전 각도 (theta4) 계산
    # roll, pitch, yaw는 엔드 이펙터의 방향을 나타냄
    theta4 = pitch  # 손목 회전 각도 (4축)

    # Step 5: 손목 회전부의 좌우 회전 각도 (theta5) 계산
    theta5 = roll  # 손목 회전 각도 (5축)

    # Step 6: 엔드 이펙터의 회전 각도 (theta6) 계산
    theta6 = yaw  # 엔드 이펙터 회전 각도 (6축)

    # 각도를 도 단위로 변환
    theta1_deg = math.degrees(theta1)
    theta2_deg = math.degrees(theta2)
    theta3_deg = math.degrees(theta3)
    theta4_deg = math.degrees(theta4)
    theta5_deg = math.degrees(theta5)
    theta6_deg = math.degrees(theta6)

    return theta1_deg, theta2_deg, theta3_deg, theta4_deg, theta5_deg, theta6_deg

# json 파일에서 좌표 읽기
def read_coordinates_from_json():
    """
    coordinates.json 파일에서 XYZ 좌표를 읽어오는 함수
    """
    base_dir = os.path.dirname(__file__)
    json_path = os.path.join(base_dir, 'coordinates.json')

    with open(json_path, 'r') as file:
        data = json.load(file)
    
    x = data['x']
    y = data['y']
    z = data['z']

    return x, y, z

# coordinates.json에서 목표 좌표 읽기
x, y, z = read_coordinates_from_json()

# 엔드 이펙터 각도 (roll, pitch, yaw)
roll = math.radians(0)  # 엔드 이펙터의 x축 회전 (roll)
pitch = math.radians(0)  # 엔드 이펙터의 y축 회전 (pitch)
yaw = math.radians(0)  # 엔드 이펙터의 z축 회전 (yaw)

# 역기구학을 이용하여 서보모터 각도 계산
theta1, theta2, theta3, theta4, theta5, theta6 = inverse_kinematics(x, y, z, roll, pitch, yaw)

# 각 서보모터의 각도 출력
print(f"서보모터 각도:")
print(f"1축 (베이스): {theta1:.2f}°")
print(f"2축 (어깨): {theta2:.2f}°")
print(f"3축 (팔꿈치): {theta3:.2f}°")
print(f"4축 (손목): {theta4:.2f}°")
print(f"5축 (손목 회전): {theta5:.2f}°")
print(f"6축 (엔드 이펙터): {theta6:.2f}°")
