import os

myPath = 'C:/Users/88697/Desktop/nhenail/Books'
allFileList = os.listdir(myPath)
n = 0
for file in allFileList:
    if n < 2:               # 第一本跟第二本不用翻譯
        pass
    else:
        json_path = myPath + "/" + allFileList[n]  # 抓子資料夾內路徑
        json_allFileList = os.listdir(json_path)
        json_index = json_allFileList.index("book.json")  #獲得txt標籤
        f = open(json_path + "/book.json", 'r', encoding="utf-8" )
        line = f.read()
        line_split_title = line.split('titleJP":"')
        line_split_end = line_split_title[1].split(',"titlePretty')
        line_split_symbol = line_split_end[0].replace('\\', '').replace('/', '').replace('*', '').replace('?', '').replace('"', '') \
        .replace('<', '').replace('>', '').replace('|', '').replace(':', '').replace('"', '').replace('null', '')

        if line_split_symbol == "":
            line_split_title = line.split(',"titlePretty":"')
            line_split_end = line_split_title[1].split('","uploadTime')
            line_split_symbol = line_split_end[0].replace('\\', '').replace('/', '').replace('*', '').replace('?', '').replace('"', '') \
                .replace('<', '').replace('>', '').replace('|', '').replace(':', '').replace('"', '').replace('null', '')

        f.close()
        file_oldname = os.path.join(myPath, file)
        file_newname_newfile = os.path.join(myPath, file + line_split_symbol)  # code:202 修改檔名
        os.rename(file_oldname, file_newname_newfile)  # 實際修改檔名

    n = n + 1

    # for json in
    # file_oldname = os.path.join(myPath, file)
    # file_newname_newfile = os.path.join(myPath, file)  # code:202 修改檔名
    # os.rename(file_oldname, file_newname_newfile)  # 實際修改檔名