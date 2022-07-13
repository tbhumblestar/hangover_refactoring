## Hanover Project refactoring
    - 'VIVINO'사이트를 모티브로 진행했던 프로젝트를 리팩토링
    - 기존 프로젝트 github : https://github.com/tbhumblestar/32-1st-Hangover-backend

## 리팩토링 변경점
    - DRF적용
    - Selenium, Scrappy를 활용한 데이터 크롤링 및 적재
    - Custom User Model
    - 소셜로그인 기반의 인증인가
    - 마이페이지 추가
    - 필터페이지 : 주류 타입, 가격, 도수, 원산지 작성
    - Pagination, Throttle
    - 디테일페이지 : 리뷰 좋아요 및 주류 정보
    - TestCode

## 적용해보고 싶은 부분
    - Redis
    - Nginx, Gunicorn
    - Docker
    - (가능한)객체지향적인 코드..

## 일정
#### 7/4~7/11
    - selenium, scrapy를 사용한 데이터 적재
    - Product 데이터 속성 결정
    - 카카오 기반 소셜로그인 구현
#### 7/12~7/19
    - Product List View : GenericView적용 / filter / pagination
    - TestCode : ProductListView / KaoKaoLogin,Logout