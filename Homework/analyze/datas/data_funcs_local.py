__author__ = 'Xc'
_DIR_ = r'D:\xampp\htdocs\pythondata'
_ASIN_ = "B0099HX6HY"
import os


def get_all_category():
    return os.listdir(_DIR_)


def get_product_data_bycate(product_asin, cate, field=None):
    tmpdir = _DIR_ + '\\' + cate + '\\' + product_asin + '.txt'
    datafile = open(tmpdir, 'r')
    data = ''
    while True:
        line = datafile.readline()
        if line:
            data += line
        else:
            break
    return eval(data)


def get_product_data(product_asin, field=None):
    for cate in get_all_category():
        if get_asin_in_category(cate).__contains__(product_asin):
            return get_product_data_bycate(product_asin, cate)


def get_asin_in_category(category_name):
    tmp_dir = _DIR_ + '\\' + category_name
    # print tmp_dir
    tmp_dir = tmp_dir.replace('>','')
    tmp_dir = tmp_dir.replace('$','&')

    file_list = os.listdir(tmp_dir)
    # print file_list
    return [filename[0:-4] for filename in file_list]


if __name__ == '__main__':
    print get_asin_in_category(r'Electronics>Video Game Consoles & Accessories>Xbox 360')