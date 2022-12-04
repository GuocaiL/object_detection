from pdf2image import convert_from_path
import os
import pandas as pd

def transpdf2img(filePath = './title_recognition/source_data', filaName = '贝格达伺服产品选型手册.pdf'):
    pages = convert_from_path(os.path.join(filePath, filaName) ,dpi=500, size=(1462, 1970))

    # 保存
    for i, page in enumerate(pages):
        # print(page.filename)
        page.save('./title_recognition/images/{}.png'.format(filaName[:filaName.rfind(".")] + "-" + str(i) ), 'png')
        
ts = set()
for p in os.listdir('./title_recognition/source_data'):
    if p.endswith(".pdf"):
        print(p)
        if not os.path.exists('./title_recognition/images/{}.png'.format(p[:p.rfind(".")] + "-" + '0')):
            transpdf2img(filaName = p)
    # if p.endswith(".xlsx"):
    #     # print(p)
    #     ts |= set( pd.read_excel(os.path.join('./title_recognition/source_data', p))['类型'].values.tolist())
# set(pd.read_excel(os.path.join('./title_recognition/source_data', "消防用破拆工具.xlsx"))['类型'].values.tolist()  )  