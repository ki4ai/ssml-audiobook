# ssml-audiobook

버전: 0.95
작성자: 박세직
히스토리:
2020/11/23, 초안작성

***

#### Note

* (2020/11/23) 11월 마스터 버전이 업데이트 되었습니다.

***

#### System/SW Overview

* 개발목표: 텍스트를 음성합성모델에서 활용할 수 있도록 전처리
* 최종 결과물: 음성합성 모델에 대한 Dataset

***

#### Quick start

* Step1. GPU Version - 호스트 머신에서 아래 명령을 실행한다. 
```
export CUDA_VISIBLE_DEVICES=<GPUID>
python flask_server.py : 통합 버전용
또는 python flask_server_test.py : 개별 테스트용
```

* Step2. (POST 방법 참조) GPU Version - 클라이언트 머신(예제는 호스트와 동일)에서 아래 명령을 실행한다. 
```
python client.py: 통합 버전용
또는 python client_test.py: 개별 테스트용
개별 테스트 용은 argument를 sentence를 주는 것을 통해 문장을 넣을 수 있습니다.
또는 argument를 from_txt로 사용할 시에 examples.txt의 내용을 가져와서 활용하게 됩니다.
결과는 M1.4 폴더 아래에 생성이 됩니다. (통합 버전: TTS_INPUT (데이터셋), 개별 테스트용: SSML_result.txt)
```
```
주요 라인
r = s.post(ip_address, data={'sentence': ss, 'ssml': ssml, 'korean_normalization': korean_normalization})
설명
sentence: 문장 정보, ssml: ssml 처리 여부, korean_normalization: normalization 한글 또는 영어 선택
```
