f_name = ['post_comments_info1.csv','post_comments_info2.csv','post_comments_info3.csv','post_comments_info4.csv','post_comments_info5.csv','post_comments_info6.csv','post_comments_info7.csv','post_comments_info8.csv','post_comments_info9.csv','post_comments_info10.csv','post_comments_info11.csv','post_comments_info12.csv']
new_file = open('post_comments_info_total.csv','a')
for name in f_name:
    f = open('data/'+name, 'r').readlines()
    new_file.writelines(f)
