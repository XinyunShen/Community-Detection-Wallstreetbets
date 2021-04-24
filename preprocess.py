def add_to_dict(author_dict, author):
    if author in author_dict:
        author_dict[author] += 1
    else :
        author_dict[author] = 1

def find_eliminated_author(author_dict, threshold):
    elminated_author = set()
    for author in author_dict.keys():
        if author_dict[author] <= threshold:
            elminated_author.add(author)
    return elminated_author

def main():
    f = open('post_comments_info_total.csv','r').readlines()
    author_dict = {}
    for line in f:
        line = line.split('\n')[0].split(',')
        author1 = line[2]
        author2 = line[3]
        add_to_dict(author_dict, author1)
        add_to_dict(author_dict, author2)
    elminated_author = find_eliminated_author(author_dict, 20)
    print(len(author_dict.keys())- len(elminated_author))

    new_f = open('post_comments_info_after_preprocss.csv','a')
    for line in f:
        out = line
        line = line.split('\n')[0].split(',')
        author1 = line[2]
        author2 = line[3]
        if author1 not in elminated_author and author2 not in elminated_author:
            new_f.write(out)



if __name__ == "__main__":
    main()