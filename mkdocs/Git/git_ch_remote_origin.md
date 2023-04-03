# How to change remote origin 

https 프로토콜 등으로 github의 repository를 clone한 경우, 이후 소스 수정을 반영시키려면 제대로 동작을 하지 않는다.

* 2021년 이후로 github에서 ssh등을 이용한 push 등이 가능하지, id/passwd 로 수행할 수 있는 기능이 아예 막혔기 때문임.

때문에, https 프로토콜로 clone한 경우, 다음을 통해 origin의 프로토콜을 ssh가 가능하도록 remote origin의 URL을 수정해야 함.

* ssh를 통해 접근하려면 URL이 `git@`으로 시작한다.

```Bash
git remote remove origin
git remote add origin git@~github_remote_repository_url.
```

## remote repository 추가하기

앞서 살펴본 명령어는 기존의 remote repository 인 origin(이를 단축이름이라고 부름)을 삭제하고, 새로운 origin을 추가하는 명령어였다.

즉, `git remote add <단축이름> <URL>` 명령어가 입력된 단축이름으로 URL에 해당하는 remote repository를 추가하는 것이다.

이렇게 추가된 경우, remote repository의 URL 대신 단축이름을 통해 git의 명령어에서 remote repository를 지칭할 수 있게 된다.

## Remote Repository

remote repository는 인터넷이나 네트워크 어딘가에 있는 저장소(repository)를 뜻하지만, 엄격하게 애기한다면, push, pull등을 통해 데이터를 올리고 받는 repository를 말한다.

> 이는, local machine에 remote repository가 같이 있을 수도 있다는 뜻이다.

`git remote` 명령어를 수행하면, 현재 프로젝트에 등록된 remote repository의 단축이름을 확인할 수 있다. 

* github에서 clone한 repository의 경우, 일반적으로 origin 이라는 이름의 remote repository를 확인할 수 있다.

`git remote -v` 명령어를 사용하면 단축이름과 함께 URL까지 확인 가능하다.

