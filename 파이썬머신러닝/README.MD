


교재: 파이썬 머신러닝 완벽가이드 - 권철민 지음, 위키북스


예제코드 : https://github.com/wikibook/ml-definitive-guide/


데이터 파일  : https://www.kaggle.com/c/titanic/data



타이타닉 생존자 예측 머신러닝 

Titanic: Machine Learning from Disaster
Start here! Predict survival on the Titanic and get familiar with ML basics

https://www.kaggle.com/c/titanic/overview/tutorials



=======================================================================

 Tensorflow 머신러닝 동영상 강의
 
 홍콩과기대 김성훈 교수 우리말 강의
 https://hunkim.github.io/ml/
 
 
 스탠포드대 앤드류 응(Andrew Ng) 교수의 영어 강의
https://class.coursera.org/ml-003/lecture


=====================================================================

# fit() 과 transform() 결합사용
from sklearn.base import TransformerMixin
class A(TransformerMixin):
    def fit(self,X):
        print('fit:',X)
        return self
    def transform(self,X):
        print('trans:',X)
        return X
        
inst = A()
inst.fit('x_data')
inst.transform('y_data')
inst.fit_transform('my_data')   


=====================================================================
