import glob

판매보고들 = glob.glob(r'여러개의 엑셀 판매보고서 합치기\판매보고_*.xlsx')

for 판매보고 in 판매보고들:
    print(판매보고)