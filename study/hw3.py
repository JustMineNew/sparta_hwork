# **과제 내용:**
#
# 1. **`Member`** 클래스와 **`Post`** 클래스를 정의하세요.                                      
#
# 4. **`Post`** 클래스에는 다음과 같은 속성을 가지고 있어야 합니다.
#     - 게시물 제목 (**`title`**)
#     - 게시물 내용 (**`content`**)
#     - 작성자 (**`author`**) : 회원의 `username` 이 저장되어야 함!
# 6. 각각의 회원이 게시글을 세개 이상 작성하는 코드를 만들어주세요.(회원이 세명이명 총 9개 이상의 post 인스턴스가 만들어져야 합니다). 만들어진 게시글 인스턴스들은 posts 빈리스트에 append를 써서 저장해주세요
#     1. for 문을 돌면서 특정유저가 작성한 게시글의 제목을 모두 프린트 해주세요
#     2. for문을 돌면서 ‘특정 단어’가 content에 포함된 게시글의 제목을 모ß두 프린트 해주세

# ----- 코드 정의 ------
# 1. 내가 만드려는 객체는

class Member:
    def __init__(self, name, username, password):
        self.name = name
        self.username = username
        self.password = password


    def display(self):
        print(f'{self.name}님은 {self.username}을 사용하고 있습니다.')

member1 = Member('손흥민','토트넘','korea7')
member2 = Member('김민재','뮌헨','korea4')
member3 = Member('황희찬','울브스', 'korea11')



class Post:
   def __init__(self, title, content, author):
       self.title = title
       self.content = content
       self.author = author
       author = Member.name
       

    # pass
# ----- 코드 실행 ------
members = []
# 회원 인스턴스
members.append (member1)
members.append (member2)
members.append (member3)
# 회원 이름만 출력
for member in members:
    print(member.name)
       


posts = []
# posts 인스턴스
posts.append (Post('친구케인','합작골 47골','손흥민'))
posts.append (Post('epl득점왕','2021/22','손흥민'))
posts.append (Post('이강인','화해','손흥민'))
posts.append (Post('중국행','민짜이시러해','김민재'))
posts.append (Post('전북','친정팀','김민재'))
posts.append (Post('나폴리우승','2022/23','김민재'))
posts.append (Post('친구미나미노','잘츠부르크','황희찬'))
posts.append (Post('친구홀란','괴물...','황희찬'))
posts.append (Post('접기','반다이크꺽기','황희찬'))

for post in posts:
    print(post.title,post.author)