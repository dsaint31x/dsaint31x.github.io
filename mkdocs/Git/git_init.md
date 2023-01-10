# Git 설치 후 해줄 작업 정리.

## 개행문자 설정.

`core.autocrlf`  : git에서 파일을 git repository 에 업로드할 때 개행문자(new line)를 처리하는 option.

`core.autocrlf` 는 다음과 같은 세가지 mode를 지원.

* `core.autocrlf = false` (default)
    - 파일 내용을 그대로 반영.
* `core.autocrlf = true`
    - git repository에 업로드 할 때, 모든 개행문자를 LF로 변경.
    - 단, local로 체크아웃할 때는 LF를 CRLF로 변경.
* `core.autocrlf = input`
    - git repository에 업로드시 CRLF가 있으면 LF로 변경.
    - local로 체크아웃할 때는 git repository의 내용 그대로 반영.

### 권장 설정.

다음과 같이 Windows의 git에서는 `true`로, Linux or MacOS 에서는 `input`으로 설정하면 큰 문제가 없을 것으로 생각된다.

```
# Windows
$ git config --global core.autocrlf true

# Linux, MacOS
$ git config --global core.autocrlf input
```

## Git에서 editor설정

다양한 editor 중에서도 linux를 위해서 vim은 다룰 줄 아는게 중요함.

git config --global core.editor 명령으로 어떤 editor를 사용할지 선택 가능함.

```
git config --global core.editor "vim"
```

또는 `.gitconifg` 파일에 다음 내용을 추가.

```
editor = vim
```