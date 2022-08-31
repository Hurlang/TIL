from django.db import models # 기본적으로 import 되어있습니다.

# Create your models here.
class Article(models.Model): # models 모듈안에 Model 클래스를 상속받습니다.
    #id 컬럼은 테이블 생성 시 django 자동으로 만들어 줍니다.
    title = models.CharField(max_length=10) # title은 필드의 이름, models.CharField()는 타입이 됩니다.
    content = models.TextField() # CharField vs TextField 길이 제한 (TextField가 더 길다)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title