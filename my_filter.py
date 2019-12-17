def ReadData():
    file = open("filtering/filter.txt","a")
    text = file.read()
    file.close()
    return text

def FormatData():
    text = ReadData()
    text_list = text.split(',')
    #removes empty list items
    return list(filter(None, text_list))
    
def my_filter():
    return FormatData()