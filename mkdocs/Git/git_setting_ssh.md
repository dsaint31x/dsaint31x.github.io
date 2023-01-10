# SSH Key and Github Repository


## SSH Private Key와 Public Key 확인 또는 생성.
ssH 키가 있는지 확인.

```
ls -al ~/.ssh
```

* `~/.ssh`는 기본적으로 SSH키들이 놓이는 디렉토리임. 
* 키를 생성할 때 변경한 경우엔 다른 곳에 놓이게 할 수 있음.

만약 이미 SSH키를 가지고 있는 경우 해당 경로에 다음의 파일들이 존재함.

```
id_rsa.pub
id_ecdsa.pub
id_ed25519.pub
```

* 암호알고리즘에 따라 이름이 조금 다를 수 있음.

없다면 다음을 통해 SSH키를 새로 만든다.

```
ssh-keygen -t rsa -C "dsaint31@gachon.ac.kr"
```

* 경로 설정 등을 물어보는데, 이때 그냥 엔터를 입력시 `~/.ssh`가 저장 경로가 됨.
* 키의 암호를 입력(한번 더 확인 물어봄)하면 저장 경로에 키가 생성됨.

## Github Repository등록

Github에는 public key를 등록한다. 이 후에는 대응되는 private key를 가진 사람만이 Github의 repository에 접근하게 됨.

`Settings` 에서 `SSH and GPG Keys`로 이동.

* most top right의 계정 아이콘을 클릭하면 나오는 메뉴에서 `Sign out` 위에 `Settings`가 있음.

이후, `New SSH Key`를 클릭하고 `Title`에 해당 키를 Github 설정창에서 구분하기 위한 제목을 입력해준 다음, `Key` 부분에 `id_rsa.pub` (public key)의 내용을 복사해준다.

public key의 내용은 다음의 명령어로 확인 가능함.

```
cat ~/.ssh/id_rsa.pub
```

* 출력되는 내용을 copy and past해주면 됨.
* `ssh-rsa`로 시작해서 키를 만들 때 입력한 `e-mail`주소로 끝나는 문자열임.

## Etc.

* 이후 사용할 Github repository의 `Clone or download` 을 클릭하여 나오는 URL중, `SSH`를 선택.
* 해당 URL을 복사하고, SSH공개키로 Github에 붙을 장비의 터미널에서 다음을 수행.

```
git config remote.origin.url 복사한_repostory_url
```

* 이는 기존의 다른 프로토콜이었던 경우에 대한 해법임.

