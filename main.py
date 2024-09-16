from data import create_yaml_from_json
from train import train_model
from inference import run_inference

def main():
    print("YAML 파일 생성 중...")
    create_yaml_from_json()  # JSON을 YAML로 변환

    print("모델 학습 시작...")
    train_model()  # 모델 학습 시작

    # Inference 실행
    print("Inference 시작...")
    run_inference()  # 추론 수행

if __name__ == "__main__":
    main()
