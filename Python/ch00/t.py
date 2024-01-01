# coding: utf-8
import argparse 

def set_config():
    parser = argparse.ArgumentParser(
        description = 'This program is an example to show how to use argparse!'
    )
    
    # 반드시 프로그램 수행시 요구되는 optioin 설정은 positional argument로 
    # 처리하면 가장 쉽다.
    # - 아래의 arg0의 경우 positional argument이며 반드시 넘겨져야 함.
    # - 수행시 넘겨지지 않으면 error발생.
    parser.add_argument('arg0', help='required argment!')
    
    # 선택적으로 입력할 option (or argument)은 다음과 같이 설정가능함.
    # - `--arg1 input_arg` 와 같이 필수 option 이후에서 추가적으로 기재.
    # - 입력을 안해도 에러나지 않음. 입력 안하면 None이 할당됨.
    # - 하이픈이 2개 연속으로 주어진 경우, 풀네임으로 option 이름을 기재하고,
    #   하이픈이 1개인 경우로 시작하는 경우는 약어로 한 문자로 option를 나타냄. 
    parser.add_argument('--arg1', '-a', help='optionial argment!')
    
    # option인 argumnet도 다음과 같이 필수로 바꿀 수 있음.
    parser.add_argument('--req_arg', required=True)
    
    # optional argument의 경우 default 값을 할당할 수도 있음.
    parser.add_argument('--arg2', default='def_arg2',
                        help='required argment! default="def_arg2"')
    
    # option에 해당하는 attribute 명은 기본적으로 argument name (or option name)으로
    # 하이픈을 뺀 문자열이 되지만, `dest` parameter를 사용하여 지정가능함.
    # parser.add_argument('--dst_arg', action='store', dest='data')
    parser.add_argument('--dst_arg', dest='data')
    
    
    # 기본적으로 argument는 string이나, type을 지정할 수도 있음.
    parser.add_argument('--arg3', '-i', type=int,
                        default=0, 
                        help='optional int type arg!')
    
    # type을 함수로 지정하여, 여러 값들을 구분자로 구분하여 입력하고 
    # list로 받을 수도 있음.
    comma_parse = lambda arg: list(map(float, arg.split(',')))
    parser.add_argument('--flist', type=comma_parse,
                        help='3,2,3 -> [3.,2.,3.]')
    
    # space를 구분자로 여러개를 입력하려면, nargs를 통해 입력받을 갯수를 
    # 지정하면 된다. 만약 nargs가 *이며 가변형이 됨.
    parser.add_argument('--multiargs', nargs=2)
    
    # option의 값을 제한하려면 다음을 이용.
    # `--help` 로 선택가능한 값을 확인할 수 있음.
    # "--limited_arg {0,1}" 형태로 출력됨.
    parser.add_argument('--limited_arg', choices=['0','1'])
    
    # 사실 command line에서 option들의 상당수는 flag모드로 동작한다.
    # 값을 입력받는 게 아닌 해당 option 명만 지정하면, True로, 아니면 False로 
    # 동작하는 방법임.
    # - 아래와 같이 action='store_true`로 지정시 해당 option이 입력되면 True값을 가짐.
    parser.add_argument("--flag", "-f", action='store_true', 
                        help="enable verbosity" )
    
    return parser

if __name__ == '__main__':
    
    parser = set_config()
    args = parser.parse_args()
    
    # argparse의 args 객체에서 입력된 argument들에 접근은 argument의 풀네임으로 접근.
    print(args.arg0, args.arg1)
    
    # 모든 구성 varaible을 보여주는 vars와
    # 특정 객체에서 attribute를 두번째 argment에 해당 attribute의 이름의 문자열로
    # 얻어오는 getattr 와 같은
    # 내장함수로 argument들을 출력하는 부분.
    for idx, a in enumerate(sorted(vars(args))):
        attr = getattr(args, a)
        print(f'[{idx:02d}] {a} : {attr}')
    
    
    
    
    
