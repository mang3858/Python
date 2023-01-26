#설치된 폰트 확인
import matplotlib.font_manager as fm

font_list = [font.name for font in fm.fontManager.ttflist]
print(font_list)
