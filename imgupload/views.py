from django.http import HttpResponse
from django.shortcuts import render, redirect
from .forms import *


# Create your views here.
def dog_image_view(request):
    if request.method == 'POST':
        form = ImgForm(request.POST, request.FILES)

        if form.is_valid():
            form.save() # 저장
            return redirect('dog_image/') #/image_upload/dog_image/ 경로로 이동
    else:
        form = ImgForm()
    return render(request, 'dog_image_form.html', {'form': form}) #초기 등록화면. 사진 업로드 버튼

def display_dog_images(request):
    if request.method == 'GET':
        Dog = Photo.objects.all().order_by('-id')[:1] #가장 최근에 저장된 사진

        return render(request, 'display_dog_images.html', {'dog_images': Dog}) #현재 표정 등록된 화면. 분석하기 버튼

def success(request):
    return HttpResponse('successfully uploaded')

def process(request):
    #이미지 불러와서 감정 분석 처리하기
    #https://heannim-world.tistory.com/39 참고해서 진행

    #return render(request, 'dog_image_form.html', {'form': form})
    return render(request, "process_result.html") #처리 후 결과 화면 파일
          #        {'file_name': file_name, 'y_predict': y_predict, 'category': category})
                    # process_result.html에 활용할 변수 저장.