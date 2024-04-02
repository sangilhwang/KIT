from django.shortcuts import render
from analysis_data.models import DistrictData, EmployeeData, FloatPopData, SeoulPopData


# Create your views here.
def analysisplot(request):
    keyword = request.GET.get("keyword", None)
    print(type(keyword))

    if keyword: #keyword값이 주어진 경우
    # 이름에 전달받은 키워드 값이 포함된 버거를 검색
        district = DistrictData.objects.all().order_by(keyword).values()
        
        # labels = [item["district_name"] for item in district]
        # values1 = [item[keyword] for item in district]
        # values10 = [item["small_2_rent"] for item in district]

    else:  # keyword가 주어지지 않아, None이 할당된 경우
        district = DistrictData.objects.all().order_by("district_name").values()

        # labels = [item["district_name"] for item in district]
        # values1 = [item[keyword] for item in district]
        # values10 = [item["small_2_rent"] for item in district]

    labels = [item["district_name"] for item in district]
    values1 = [item["large_b1_rent"] for item in district]
    values2 = [item["large_1_rent"] for item in district]
    values3 = [item["large_2_rent"] for item in district]
    values4 = [item["large_3_rent"] for item in district]
    values5 = [item["large_4_rent"] for item in district]
    values6 = [item["large_5_rent"] for item in district]
    values7 = [item["large_6to10_rent"] for item in district]
    values8 = [item["small_b1_rent"] for item in district]
    values9 = [item["small_1_rent"] for item in district]
    values10 = [item["small_2_rent"] for item in district]

    context = {
        "keyword" : keyword,
        "labels" : labels,
        "values1" : values1,
        "values2" : values2,
        "values3" : values3,
        "values4" : values4,
        "values5" : values5,
        "values6" : values6,
        "values7" : values7,
        "values8" : values8,
        "values9" : values9,
        "values10" : values10,
        }
    return render(request, "analysis_page.html", context)
