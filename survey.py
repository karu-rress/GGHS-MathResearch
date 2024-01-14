import csv
import pandas as pd
from collections import Counter
from matplotlib import pyplot as plt
from analyze import color

class surveyer:
    def __init__(self, filename: str='data/survey.csv'):
        self.df = pd.read_csv(filename)

    def show_needed(self) -> None:
        subject_data = self.df.iloc[:, 2]
        subjects = ['국어', '영어', '수학', '과학', '예체능']
        subjects_value = [0, 0, 0, 0, 0]
        
        for i in subject_data:
            texts = i.split(';')
            for j in texts:
                print(j)
                for k in range(5):
                    if j == subjects[k]:
                        subjects_value[k] += 1
        
        print(subjects_value)
        dictionary = dict(zip(subjects, subjects_value))
                
        plt.rc('font', family='Malgun Gothic')
        plt.figure(figsize=(10, 8))
        plt.bar(*zip(*dictionary.items()), color=color)
        plt.title('사교육이 가장 필요한 과목은?')
        plt.xlabel('과목')
        plt.ylabel('응답 수')
        plt.show()
        
    def show_is_needed(self) -> None:
        needed = self.df.iloc[:, 1]
        yes = (needed == '받고 있다').sum()
        no = len(needed) - yes
        
        labels = ['받고 있다', '받고 있지 않다']
        yesp = yes / (yes + no) * 100
        nop = no / (yes + no) * 100
        sizes = [yesp, nop]
        colors = ['mediumaquamarine','forestgreen']
        explode = (0.1, 0)
        plt.title('현재 사교육을 받고 있나요?')
        plt.pie(sizes, explode=explode, labels=labels, colors=colors,
                autopct='%1.1f%%', shadow=True, startangle=90)
        plt.axis('equal')
        plt.show()