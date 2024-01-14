from collections import Counter
from matplotlib import pyplot as plt
import pandas as pd

color = 'yellowgreen'

class otd:
    @staticmethod
    def rm_duplicate(lt: list) -> list:
        return list(set(lt))

    @staticmethod
    def sort_dict(dict: dict, reversed: bool=False) -> dict:
        if reversed:
            return {k: v for k, v in sorted(dict.items(), key=lambda x: x[1])}
        else:
            return {k: v for k, v in sorted(dict.items(), key=lambda x: -x[1])}

class analyzer:
    def __init__(self, filename: str='data/data.csv'):
        self.df = pd.read_csv(filename)

    def show_region(self) -> None:
        regions_data: list = self.df.iloc[:, 0].tolist() # 중복 포함 지역 전체
        regions = otd.rm_duplicate(regions_data)
        
        print(regions)
        
    def scatter(self):
        # 위도: latitude, 경도: longitude
        latitude = [round(float(x), 5) for x in self.df.iloc[:, 10] if x != '']
        longitude = [round(float(x), 5) for x in self.df.iloc[:, 11] if x != '']

        pos = [(round(x, 2), round(y, 2)) for (x, y) in zip(latitude, longitude)]
        cnt = dict(Counter(pos)) # {(x, y): z,}
        
        sub_lat, sub_lon = zip(*list(cnt.keys()))
        sub_cnt = [round(x/1.5)+10 for x in list(cnt.values())]

        plt.rc('font', family='Malgun Gothic')
        plt.figure(figsize=(7,7)).add_subplot(111).set_aspect('equal')

        plt.scatter(sub_lon, sub_lat, s=sub_cnt, c=range(len(sub_cnt)), cmap='Greens')
        plt.xlabel('경도(˚E)')
        plt.ylabel('위도(˚N)')
        plt.title('지역별 학원 분포')

        plt.show()