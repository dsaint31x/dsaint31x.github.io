# Module, Package and Library

아주 엄밀한 정의는 아니더라도, 해당 용어들의 개념은 알고 있어야 프로그래밍이 가능하다. Python에만 국한된 용어는 아니며 대략적인 의미들은 공유하지만, 실제 구현물로 가면 조금씩 차이가 존재하는 용어들이다.  

> 이 문서에서는 Python 기준으로 설명한다.

일단 이들 용어들은 포함관계를 가지는 계층구조로 애기할 수 있다.

* Library는 여러 package와 module들로 구성된다.
* Package는 여러 Moudle들로 구성된다.
* Module은 여러 function과 variable, class들로 구성된다.

## Library

SW의 구성요소 중 하나로 SW에 특정 기능을 추가하기 위해 요구되는 실행가능한 기계어(or 바이트코드) 형태로 제공되는 ***모듈화된 프로그램들의 묶음*** 으로, 이를 사용하는 개발자들은 해당 Library의 API를 통해 SW에서 사용함.

앞서 애기한 대로 여러 package와 moduel들로 구성되며, SW에서 사용될 때 동적 또는 정적으로 link된다.

많은 프로그래밍 언어에서 SW를 개발할 때 요구되는 기능들을 Library로 제공하며 이를 ***표준 라이브러리*** 라고 부른다. 특정 프로그래밍 언어를 배우는 과정에서 많은 부분이 해당 언어의 표준 라이브러리의 사용법을 익히는 (바꿔말하면 API를 익히는) 데 할애된다.

`openCV`, `numPy`, `PyTorch`, `Pandas` 등이 Python의 대표적인 라이브러리들이다.

> Framework와 Library는 약간 다른 의미를 가지지만, SW를 개발하기 위해 필요한 큰 부품들을 묶음이라는 의미에선 유사하다. 사실 엄밀한 구분 기준은 없으나 대부분이 인정하는 차이점은 있다. 보통 제공하는 기능들을 사용할 때, SW의 **제어흐름** 을 자유롭게 개발자가 정할 수 있는 경우 library라고 부르며, 이미 상당부분이 고정되어 있고 개발자는 해당 순서에 동작하는 함수 등에 기능을 추가하는 수정을 가하는 형태로 작업이 이루어지면 Framework라고 부른다. 좀더 자세한 부분 설명은 다음 URL을 참고하라.   
> [Library vs. Framework](https://dsaint31.tistory.com/entry/Programming-Library-vs-Framework)

## Package

비슷한 기능이나 목적을 가지는 여러 module들을 묶어놓은 것이 바로 Package임. Python에서는 module 하나를 `.py` 파일로 볼 수 있고, 이들이 속해있는 directory를 패키지로 볼 수 있다. 이는 Pakcage 내에 sub-package를 가질 수 있으며, package들이 모여서 library (or framework)를 구성한다.

sub-directory를 가지듯이 sub-package를 가질 수 있기 때문에, library를 package라고도 부를 수도 있다. 때문에 `NumPy`나 `Pandas` 등의 library를 package라고도 종종 부른다.

## Module

Python에서 module은 여러 function과 variable, class들의 묶음으로 실제로는 이들을 정의 및 구현하고 있는 python code file을 가르킨다. Python에서 `.py` 확장자로 끝나는 모든 파일이 module이며 `import` 및 `from`을 통해 다른 module의 function과 varialbe등을 사용할 수 있다.  

function이 code들을 하나의 기능으로 묶은 단위로 modular programming의 최소 단위라면, module은 Python의 프로그램 아키텍처 에서의 ***최상위 구성단위*** 라고 생각할 수 있다. 즉, 하나의 Python으로 만든 SW는 여러 `.py` 파일들, 즉 module들로 구성된다 (이 경우, library나 package도 module로 애기하는 게 아주 틀린 애기가 아니라는 것을 의미함).

* 주의할 건, Python의 경우, C나 C++등의 다른 언어로 제공되는 확장 기능들도 Module 형태로 사용한다 (공식용어로는 `external modules`라고 지칭된다). 


file은 module로 directory는 package로 나누는게 가장 많이 받아들여지는 구분법이지만, 엄격하게 지켜지는 법률같은 건 아니므로 context에 맞춰 이해해야 한다.

> `os`, `sys` 등의 Python이 기본으로 제공하는 표준라이브러리 를 package 개념 없이 module들로 표현하는 경우가 많다. Package의 경우, java등에서 많이 사용되는 용어이며 Python의 경우 package까지 그냥 module이라고 지칭하는 경우도 꽤 된다. 때문에 **표준 라이브러리 모듈** 이라는 용어가 **표준 라이브러리 패키지** 라는 용어보다 python에서는 더 많이 사용되는 편이다. `from` 이나 `import` 에서도 package보다는 module로 지칭하는 경우가 대다수 이다.  
> 
> * 헷갈리는 부분으로 이 때문에 package도 module이라고 지칭하는 경우가 꽤 있다. 
  
---
  

### 참고자료 (Learning Python 5th Edition, ch03 Module Import and Reload)
> Python에서 module은 일종의 namespace 라고 언급하는 경우도 많다. 이 namespace(=module)은 일종의 "varaible, function, class등에 대한 name로 구성된 package(묶음)"을 가르키며, "attribute는 해당 묶음 내의 name (=variable, function, class들의 이름)들"을 가르키는 용어로 사용된다.  
> 예를 들면, 특정 `.py`파일 내의 function과 variable, class에 접근하려면, 해당 `.py`파일의 이름을 통해 접근하게 된다. 즉, 파일의 이름이 일종의 namespace라고 생각할 수 있고, 이 밑으로 다양한 function과 variable, class에 접근은 해당 namepace의 attribute 형태로 가능하다.

* `from`의 경우, module내의 attribute를 현재의 module로 복사하기 때문에 namespace로 구분된 경계를 일부 무너뜨린다고 볼 수 있다. 때문에 엄격한 일부 프로그래머들은 `import`를 사용하는 것을 권장한다. 하지만... 적절히 `from`을 구사할 경우, 이름이 겹치는 문제는 일어나지 않고, 무엇보다도 개발자가 매번 namespace에 해당하는 module명을 입력하지 않게 해주는 편리성을 버리긴 어렵기 때문에 굳이 `import`만을 사용할 필요는 없을 거 같다.
* `from`은 namespace가 붙은 attribute를 값으로 하여, namespace가 빠진 name에 할당하는 동작 (이를 줄여서 "복사"했다고 언급한다)이 이루어진다고 생각하면 된다. 
