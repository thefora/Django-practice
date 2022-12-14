# django-practice

<br><br>

### 미션 : 커뮤니티 서비스 만들기
```
프론트엔드 개발자와 협업하여 유저들이 자유롭게 소통할 수 있는 커뮤니티를 만들어야 합니다. 
커뮤니티를 위한 API를 만들어봅시다! :)

(어떤 어떤 API가 필요하다고 구체적으로 작성하진 않겠습니다. 
본인이 해당 서비스를 만들기 위해 전체적인 설계를 진행하면서 필요하다고 생각되는 API를 만들어보세요!) 
```
<br><br>

#### 요구사항 및 필요정보
<hr>

1. 유저는 여러명 존재할 수 있고, 유저 정보는 로그인 ID, PW, e-mail, 이름, 전화번호, 성별, 닉네임이 필요합니다.<br>
    - 로그인 API는 만들지 않아도 됩니다. 유저의 ID, PW로 요청을 보내면 데이터베이스의 정보와 일치하는지만 확인하세요

<br>

2. 커뮤니티는 유저가 자유롭게 생성할 수 있으며, 최초 커뮤니티 생성자는 해당 커뮤니티의 관리자 권한을 갖습니다. 
	  - 관리자는 커뮤니티를 삭제할 수 있습니다.

<br>

3. 커뮤니티는 모든 유저가 자유롭게 드나들 수 있습니다.

<br>

4. 커뮤니티 안에서는 누구든 게시글을 작성할 수 있습니다. 게시글은 제목, 내용, 조회수, 작성날짜, 작성자, 댓글을 포함해야합니다.   
    - 작성자 형태 : 닉네임(ID) ex) Ash(ashash123123)
    - 게시글을 작성할 때, 말머리를 선택할 수 있습니다. (선택 안할 수도 있음)
	 - 말머리는 커뮤니티 관리자가 등록, 삭제, 수정할 수 있으며, 여러개가 존재할 수 있습니다. 
	 - 기존 말머리가 수정되면 해당 말머리로 작성된 게시글의 말머리도 수정 돼야합니다. 

	 - 댓글은 해당 게시글에만 종속되며, 누구나 게시글에 댓글을 작성할 수 있습니다. 댓글은 내용, 작성날짜, 작성자를 포함해야합니다.   
	   - 작성자 형태 : 닉네임(ID) ex) Ash(ashash123123)
	 - 댓글 삭제는 작성자만 가능합니다.

	 - 게시글 삭제는 해당 게시글을 작성한 사람 또는 관리자만 가능합니다.

<br>

5. 관리자는 게시글/댓글을 작성한 특정 유저를 해당 커뮤니티에서 블락시킬 수 있습니다. 
    - 블락된 유저는 해당 커뮤니티 접근이 불가능하며( 3번에만 제약사항을 걸면 됩니다. ), 작성한 게시글/댓글은 모두 삭제됩니다. 
	  - 한 커뮤니티에서 여러명의 유저를 블락할 수 있고, 관리자는 특정 유저의 블락을 해제할 수 있습니다.

<br>

6. 커뮤니티의 게시글/댓글/말머리/블락유저 등 커뮤니티마다 종속되는 데이터를 모두 종합하여 <br>
nested형태로 응답 데이터를 보내도록 합니다. (GET method만)

<br>

7. 유저는 자신의 정보를 수정할 수 있습니다. 수정 가능한 요소 : PW, e-mail, 전화번호, 닉네임 -- 마지막에 시간 남으면 하세요. 

<br>
