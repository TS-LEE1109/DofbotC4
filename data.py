import json
import os
from params import train_params

def create_yaml_from_json():
    json_dir = train_params.json_dir
    yaml_path = train_params.yaml_path

    # 첫 번째 JSON 파일을 열어서 클래스 이름을 추출
    json_files = [f for f in os.listdir(json_dir) if f.endswith('.json')]
    if json_files:
        with open(os.path.join(json_dir, json_files[0]), 'r') as f:
            data = json.load(f)

        # 클래스 이름 추출
        categories = data['categories']
        class_names = [category['name'] for category in categories]

        # YAML 파일 내용 작성
        yaml_content = f"""
        train: ./train/images  # 훈련 이미지 경로 (수정 필요)
        val: ./val/images      # 검증 이미지 경로 (수정 필요)

        nc: {len(class_names)}
        names: {class_names}
        """

        # YAML 파일 저장
        with open(yaml_path, 'w') as f:
            f.write(yaml_content)

        print(f"YAML 파일이 생성되었습니다: {yaml_path}")
    else:
        print("JSON 파일을 찾을 수 없습니다.")
