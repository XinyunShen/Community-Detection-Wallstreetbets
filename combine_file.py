def get_whole_file():
    f_name = ['post_comments_info1.csv','post_comments_info2.csv','post_comments_info3.csv','post_comments_info4.csv','post_comments_info5.csv','post_comments_info6.csv','post_comments_info7.csv','post_comments_info8.csv','post_comments_info9.csv','post_comments_info10.csv','post_comments_info11.csv','post_comments_info12.csv']
    new_file = open('post_comments_info_total.csv','a')
    for name in f_name:
        f = open('data/'+name, 'r').readlines()
        new_file.writelines(f)

def get_test_file():
    file = open('post_comments_info_total.csv','r').readlines()
    new_file = open('post_comments_info_test.csv','a')
    i = 0
    for name in file:
        if i == 100:
            new_file.write(name)
            i = 0
        else:
            i += 1

def main():
    get_test_file()


if __name__ == "__main__":
    main()