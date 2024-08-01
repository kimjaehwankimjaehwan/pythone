한글깨짐방지

# 한글설정
!apt-get install -y fonts-nanum*

!rm -rf /root/.cache/matplotlib/* # 폰트 캐시 재설정


# 런타임 다시 시작 후 실행
%matplotlib inline
import matplotlib.pyplot as plt
import matplotlib as mpl 
#
path = '/usr/share/fonts/truetype/nanum/NanumGothic.ttf'
font_name = mpl.font_manager.FontProperties(fname=path).get_name()
plt.rcParams['font.family'] = font_name


![image](https://github.com/user-attachments/assets/21e8d05a-c7c3-4f7d-b5d2-296823465280)
