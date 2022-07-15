1. Working Directory
   * 내가 작업하고 있는 실제 디렉토리
2. Staging Area
   * 커밋으로 남기고 싶은, 특정 버전으로 관리하고 싶은 파일이 있는 곳
3. Repository
   * 커밋들이 저장되는 곳



# Git

---



**git init** -> 파일 작성 -> **git add**(tracked) -> **git commit**(tracked)



**git init** : 초기화 (.git 파일 생성)

**git status** : 파일의 관리 상태 (untracked / tracked)

**git add** (파일명.확장자): 해당 파일을 Stage Area에 올림

**git add .** : 디렉토리 안에 있는 모든 파일을 Stage Area에 올림

**git commit -m"메시지"** : (변경된 내용, 시간, 사용자) Stage Area에 있는 파일을 repository에 올림

**git log** : 



# git local

```bash
git init
touch a.txt
git add .
git commit -m 'add a.txt'
git log #레퍼지토리에서 확인함 (git log --online : 한 줄 씩)

touch b.txt
git add .
git status #워킹 디렉토리에서 확인함
git commit -m 'add b.txt'

a 수정
git status (빨간 modified)
git add .
git status (녹색 modified)
git commit -m "modify a.txt"

```



# git remote

```bash
git remote add origin {http://...~}
git push -u origin master # 처음만 이렇게 작성
git push # 나중에는 이렇게 작성

```



# get clone (url)

```bash
git clone https://github.com/Hurlang/ssafy8.git

```





# 자격 증명 관리

![image-20220715162110919](./README.assets/image-20220715162110919.png)