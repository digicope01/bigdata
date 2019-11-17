pip install numpy pandas

=============================================
#### - pandas DataFrame 행 출력 최대값 설정방법

pd.set_option('display.max_rows', 1000)

=============================================
#### - pandas apply()와 람다식을 사용한 범위 분류


##### # 나이에 따라 세분화된 분류를 수행하는 함수 생성. 
def get_category(age):

    cat = ''
    
    if age <= 5: cat = 'Baby'
    
    elif age <= 12: cat = 'Child'
    
    elif age <= 18: cat = 'Teenager'
    
    elif age <= 25: cat = 'Student'
    
    elif age <= 35: cat = 'Young Adult'
    
    elif age <= 60: cat = 'Adult'
    
    else : cat = 'Elderly'
    
    
    return cat

##### # lambda 식에 위에서 생성한 get_category( ) 함수를 반환값으로 지정. 
##### # get_category(X)는 입력값으로 ‘age’ 컬럼 값을 받아서 해당하는 cat 반환
titanic['age_cat'] = titanic['age'].apply(lambda x : get_category(x))

titanic[['age','age_cat']].head(100)

titanic


=============================================

#### Pandas로 컬럼의 유일한 값(unique value)을 찾고 개수 세어보기

 

 - pd.Series.unique() 를 이용한 유일한 값 찾기

   (Return np.ndarray of unique values in the object)

 

 - pd.Series.value_counts() 를 이용한 유일한 값별 개수 세기

   (Returns object containing counts of unique values)



출처: https://rfriend.tistory.com/267 [R, Python 분석과 프로그래밍의 친구 (by R Friend)]


=============================================


- merge() 예제 리스트 데이터셋

employee = [{'empno':1, 'ename':'kim', 'dept':1}, 

            {'empno':2, 'ename':'lee', 'dept':2}, 
            {'empno':3, 'ename':'park', 'dept':1}, 
            {'empno':4, 'ename':'song', 'dept':3},
            {'empno':5, 'ename':'min', 'dept':2} ]
            

dept=[{'dept':1, 'deptname':'관리직'}, 

      {'dept':2, 'deptname':'영업직'},
      {'dept':3, 'deptname':'개발직'} ]

info =[{'empno':1, 'addr':'서울시','phone':'010-1111-1111'},

       {'empno':3, 'addr':'부산시','phone':'010-2222-2222'}, 
       {'empno':2, 'addr':'광주시','phone':'010-3333-3333'}, 
       {'empno':5, 'addr':'광주시','phone':'010-4444-4444'},
       {'empno':4, 'addr':'광주시','phone':'010-5555-5555'} ]
=================================     

- grouby() 와 pivot_table() 예제 데이터셋

from numpy.random import seed

from numpy.random import rand

from numpy.random import randint

seed(42)

df = pd.DataFrame({
   'Weather' : ['cold', 'hot', 'cold', 'hot',
   'cold', 'hot', 'cold'],
   
   'Food' : ['soup', 'soup', 'icecream', 'chocolate',
   'icecream', 'icecream', 'soup'],
   
   'Price' : 10 * rand(7), 'Number' : randint(1, 9, 7)})


============================================================

### 구글 colaboratory 사용법 : 무료 GPU 사용 (1회 12시간 이내)

https://hiseon.me/data-analytics/google-colaboratory/


============================================================
