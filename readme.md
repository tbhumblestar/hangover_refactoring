# Project : Hangover

### 개요
- 'VIVINO'사이트를 모티브로, 원하는 주류를 선택하고 구매한 술에 대해 리뷰를 작성할 수 있는 웹 어플리케이션
- Hangover라는 단어에 맞추어, 도수와 숙취도를 기반으로 하는 주류 추천 및 소개 페이지
- 기존에 만들었던 Hanover사이트의 아이디어를 가져와서 리팩토링을 진행

<br/>

### 시연영상
https://www.youtube.com/watch?v=salXD8PgdBI

<br/>

[![Video Label](http://img.youtube.com/vi/salXD8PgdBI/0.jpg)](https://youtu.be/salXD8PgdBI?t=0s)

<br/>

### 프로젝트 멤버 및 역할
- 멤버 : 김영빈(Back) & 이지수(Front)
- 맡은 역할 : Backend 전담

<br/>

### 사용한 기술스택(Backend)
- Python
- Django / Django Rest Framework
- MYSQL
- Github
- AWS(EC2, RDS)


<br/>

### API
- Product, Image, User,  관련 API 구현

<br/>

### 구현기능
- genericview를 활용한 전반적인 API 구현
- drf_ysrg를 활용한 문서화
- selenium을 활용한 데이터 크롤링 및 적재
- custom user model, 자체로그인 & 소셜로그인 및 DRF의 Permission을 활용한 인증, 인가

<br/>

### 배포
- AWS EC2,RDS를 활용해 backend api 서버 배포