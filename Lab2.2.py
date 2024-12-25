import numpy as np
import csv
data=[]
with open('diem_hoc_phan.csv', 'r', encoding='utf-8') as file:
    reader=csv.reader(file)
    next(reader)
    for row in reader:
        data.append(row)
np_data=np.array(data)
scores=np_data[:, 2:].astype(float)
def quy_doi_diem(score):
    if 8.5 <= score <=10:
        return 'A'
    elif 8.0<= score <8.5:
        return 'B+'
    elif 7.0<= score<8.0:
        return 'B'
    elif 6.5 <= score <7.0:
        return 'C+'
    elif 5.5 <= score <6.5:
        return 'C'
    elif 5.0 <=score <5.5: 
        return 'D+'
    elif 4.0 <= score < 5.0:
        return 'D'
    else:
        return 'F'
    grades = np.vectorize(grade_conversion)(scores)
hp1_scores = scores[:, 0]
hp2_scores = scores[:, 1]
hp3_scores = scores[:, 2]
def analyze_subject(scores):
    total = np.sum(scores)
    mean = np.mean(scores)
    std_dev = np.std(scores)
    return total, mean, std_dev
hp1_analysis = analyze_subject(hp1_scores)
hp2_analysis = analyze_subject(hp2_scores)
hp3_analysis = analyze_subject(hp3_scores)
def count_grades(grades):
    unique, counts = np.unique(grades, return_counts=True)
    return dict(zip(unique, counts))
all_grades = grades.flatten()
grade_distribution = count_grades(all_grades)
print("Phân tích học phần HP1:", hp1_analysis)
print("Phân tích học phần HP2:", hp2_analysis)
print("Phân tích học phần HP3:", hp3_analysis)
print("Phân phối điểm tổng hợp:", grade_distribution)

    
