# 교과 영역
dic_1 = {'A': '기초',
         'B': '탐구',
         'C': '체육과 예술',
         'D': '생활과 교양', }
# 교과군
dic_2 = {'A': '국어',
         'B': '영어',
         'C': '수학',
         'D': '사회',
         'E': '과학',
         'F': '예술',
         'G': '체육',
         'H': '기술과 가정',
         'I': '제2외국어',
         'J': '한문',
         'K': '교양'}
# 구분
dic_3 = {'A': '일반',
         'B': '진로',
         'C': '공통'}
# 단위수
dic_4 = {'A': 2,
         'B': 3,
         'C': 4,
         'D': 5,
         'E': 6, }
# 과목구분코드
dic = {'연극': 'CFAC',
       '음악연주+미술창작': 'CFBA',

       '언어와 매체': 'AAAB-1',
       '확률과 통계': 'ACAB-1',
       '영어회화': 'ABAB-1',
       '영미 문학 읽기': 'ABBB-1',

       '한국지리': 'BDAE-1',
       '사회문화': 'BDAE-2',
       '세계사': 'BDAE-3',
       '생활과 윤리': 'BDAE-4',
       '경제': 'BDAE-5',

       '물리학1': 'BEAE-1',
       '화학1': 'BEAE-2',
       '생명과학1': 'BEAE-3',
       '지구과학1': 'BEAE-4',

       '프로그래밍': 'DHBE-6',

       '화법과 작문': 'AAAE-2',
       '심화 국어': 'AABB-1',
       '고전 읽기': 'AABB-2',
       '실용 국어': 'AABB-3',

       '미적분': 'ACAE-2',
       '기하': 'ACBE-1',
       '수학과제 탐구': 'ACBB-2',
       '경제수학': 'ACBB-3',
       '실용 수학': 'ACBB-4',

       '영어 독해와 작문': 'ABAE-2',
       '영어권문학': 'ABBB-2',
       '실용영어': 'ABBB-3',

       '미술 감상과 비평': 'CFBB-1',
       '드로잉': 'CFBB-2',
       '시창청음': 'CFBB-3',
       '음악 감상과 비평': 'CFBB-4',

       '세계지리': 'BDAE-6',
       '윤리와 사상': 'BDAE-7',
       '동아시아사': 'BDAE-8',
       '정치와 법': 'BDAE-9',
       '여행지리': 'BDBB-1',
       '사회문제 탐구': 'BDBB-2',
       '고전과 윤리': 'BDAB-3',

       '물리학2': 'BEBE-1',
       '화학2': 'BEBE-2',
       '생명과학2': 'BEBE-3',
       '지구과학2': 'BEBE-4',
       '물리학실험': 'BEBB-5',
       '화학실험': 'BEBB-6',
       '생명과학실험': 'BEBB-7',
       '지구과학실험': 'BEBB-8',
       '과학사': 'BEBB-9',
       '생활과 과학': 'BEBB-10',

       '진로와 직업': 'DKAB-10',
       '가정 과학': 'DHBB-5',
       '공학 일반': 'DHBB-6',
       '사물 인터넷 서비스': 'DHBB-7',
       '빅데이터 분석': 'DHBB-8',

       '체육전공실기기초': 'DCBA-1',
       '스포츠 경기 체력': 'DCBA-2',

       '중국어 회화1': 'DIBA-1',
       '일본어 회화1': 'DIBA-2',
       '중국문화': 'DIBA-3',
       '일본문화': 'DIBA-4',

       '철학': 'DKAA-1',
       '논리학': 'DKAA-2',
       '심리학': 'DKAA-3',
       '교육학': 'DKAA-4',
       '논술': 'DKAA-5',
       '환경': 'DKAA-6',
       '강원도의 역사와 문화': 'DKAA-7',
       '실용 경제': 'DKAA-8',
       '공중 보건': 'DKAA-9',
       '바리스타': 'DKAA-10',

       '창의 경영': 'DHBA-1',
       '인간발달': 'DHBA-2',
       '건축 일반': 'DHBA-3',
       '기초 제도': 'DHBA-4',

       '응용 프로그래밍 개발': 'DHBA-5', }


def SrcVl(nmbr, Vl):
    if nmbr == 0:
        return dic[Vl]
    if nmbr == 1:
        return dic_1[Vl]
    elif nmbr == 2:
        return dic_2[Vl]
    elif nmbr == 3:
        return dic_3[Vl]
    elif nmbr == 4:
        return dic_4[Vl]
    else:
        return -1