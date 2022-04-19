from numpy import transpose
def split_urls_for_api(url_data):
    i = 0
    j = 100
    new1 = []
    new2 = []
    while i < 100:
        new1.append(url_data[i])
        i += 1
    while j < 200:
        new2.append(url_data[j])
        j += 1
    new1 = transpose(new1)
    new2 = transpose(new2)
    return  new1, new2