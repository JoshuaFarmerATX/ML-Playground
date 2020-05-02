import urllib.request, json
from pprint import pprint 

with urllib.request.urlopen("https://covid-mgzrmsj5kq-uc.a.run.app/API/USA/timeseries/") as url:
    data = json.loads(url.read().decode())
    USPop = 331002651

    # pprint(data[-1]['Cases'])
    recentinfectedratio = (data[-1]['Cases']) / USPop
    # print(recentinfectedratio)

    # initialinfectedratio = (data[0]['Cases']) / USPop
    # print(initialinfectedratio)

    for i in range(len(data)):
        cases = (data[i]['Cases'])
        deaths = (data[i]['Deaths'])
        recovered = (data[i]['Recovered'])

        # pprint(f"Cases: {cases}, Deaths: {deaths}, Recoveries: {recovered}")
        try:
            percrecovered = recovered / cases * 100
            percdead = deaths / cases * 100
            drratio = percdead / percrecovered * 100
            print(f"""Date: {data[i]['Total Results as of Date']}
            Recovered: {percrecovered}
            Dead: {percdead}
            Death/Recovered Ratio: {drratio}
            """)
        except:
            continue