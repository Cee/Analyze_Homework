__author__ = 'Xc'

from matplotlib import pyplot as plt


def draw_comments_num_graph(source_data, asia_data):
    product_name_list = []
    product_comment_num_list = []
    comment_num_list = []
    i = 1

    for asia in asia_data:
        # print source_data[asia['ASIN']]['name']
        product_name_list += [source_data[asia['ASIN']]['name']]
        product_comment_num_list += [float(source_data[asia['ASIN']]['review_count'])]
        comment_num_list += [[source_data[asia['ASIN']]['review_count']]]

    print product_name_list
    print product_comment_num_list
    plt.plot(product_name_list, product_comment_num_list, 'o-')
    plt.xlabel('Product')
    plt.ylabel('Number of comments')

    plt.xticks((1, 20), product_name_list)

    comment_num_list = [product_comment_num_list, product_name_list]
    plt.bar(left=(0, 1), height=(100, 0.5), width=1, align="center")

    plt.hist(comment_num_list, color='grey', align='mid', bins=5, rwidth=0.5)

    plt.show()
