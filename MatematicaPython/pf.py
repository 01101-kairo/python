import requests as r
import datetime as td
import csv
from PIL import Image
from IPython.display import display

def get_datasets(y, labels):
    if type(y[0])==list:
        ddatasets = []
        for i in range(len(y)):
            ddatasets.append({
                'labels': labels[i],
                'data':y[i]
            })
            return ddatasets
        else:
            return[
                {
                    'labels':labels[0],
                    'data':y
                }
            ]


def set_title(title=''):
    if title != '':
        display ='true'
    else:display='false'
    return{
        'title':title,
        'display':display
    }


def create_chart(x,y,labels,kind='bar',title=''):
    datasets=get_datasets(y,labels)
    options=set_title(title)

    chart = {
        'type':kind,
        'data':{
            'labels':x,
            'datasets':datasets
        },
        'options':options
    }
    return chart


def get_api_chart(chart):
    url_base = 'https://quickchart.io/chart'
    resp = r.get(f'{url_base}?c={str(chart)}')
    return resp.content


def save_image(path, content):
    with open(path,'wb') as image:
        image.write(content)


def display_image(path):
    img_pil = Image.open(path)
    display(img_pil)


url= 'https://api.covid19api.com./dayone/country/brazil'
resp = r.get(url)
# print(resp.status_code)

raw_data = resp.json()
# print(raw_data[0])
final_date = []
for obs in raw_data:
    final_date.append([obs['Confirmed'],obs['Deaths'],obs['Recovered'],obs['Active'],obs['Date'],])

final_date.insert(0,['Confirmed','Deaths','Recovered','Active','Date'])
final_date
CONFIRMADOS=0
OBITOS=1
RECUPERADOS=2
ATIVOS=3
DATE=4

for i in range(1,len(final_date)):
    final_date[i][DATE]=final_date[i][DATE][:10]

final_date


with open('brasil-covid.csv','w') as file:
    writer = csv.writer(file)
    writer.writerow(final_date)

for i in range(1, len(final_date)):
    final_date[i][DATE]=td.datetime.strptime(final_date[i][DATE],'%Y-%m-%d')


y_data_1 = []
for obs in final_date[1::10]:
    y_data_1.append(obs[CONFIRMADOS])

y_data_2 = []
for obs in final_date[1::10]:
    y_data_2.append(obs[RECUPERADOS])

labels=['Confirmados','Recuperados']

x=[]
for obs in final_date[1::10]:
    x.append(obs[DATE].strftime('%d/%m/%Y'))

chart = create_chart(x,[y_data_1,y_data_2],labels,title='grafico recuperado vs recuperados')
chart_content = get_api_chart(chart)
save_image('grafo.png', chart_content)
display_image('grafo.png')
