# 챗GPT를 이용한 상품 비교 및 추천 서비스 API 개발 '상추'

## 1. 소개

## 2. 기술 스택

## 3. 코드 샘플
<aspectapp>
Get 방식으로 Django 서버에 있는 JSON 데이터(text list)에서 상품 정보(상품명, 상품평, 상품 상세 정보)를 추출해 저장

GPT 모델에 상품 정보를 전달하고, GPT 모델에 질문(product1, product2 중 6가지 측면에서 비교해줘!) 후 답변(1번, 2번, 3번, 4번, 5번, 6번) 받기

클라이언트가 요청을 하면 aspect_list = [1번, 2번, 3번, 4번, 5번, 6번], aspect api 새로 생성 후 Get 방식으로 넘겨줌


<comparisonapp>
클라이언트로부터 Post 방식으로 번호를 보내면 받음

GPT 모델에 측면 번호{n}번 전달

GPT 모델에 질문({aspect}번 측면에서 product1, product2 중 더 좋은 제품을 골라줘) 후 답변(gpt 추천) 받기

get 방식을 이용해 클라이언트에게 보냄

## 4. 기여도


## 5. 마무리
<배운 점>

get과 post에 대한 이해도 향상

Chat gpt Open Ai를 활용한 Api 제작

