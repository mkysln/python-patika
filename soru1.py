def flatten_list(_2d_list):
    duz_list = []

    for element in _2d_list:
        if type(element) is list:

            for item in element:
                duz_list.append(item)
        else:
            duz_list.append(element)

    return duz_list


orj_liste = [1,"a",[3,5],"s",True,"x",False]
print("Orijinal Liste:",orj_liste)
print("Düzleştirilmiş Liste:",flatten_list(orj_liste))