f = open('post_comments_info_total.csv','r')
f = f.readlines()
print("total comments are {}".format(len(f)))
users = set()
for line in f:
    line = line.split('\n')[0].split(',')
    users.add(line[2])
    users.add(line[3])
print("total users are {}".format(len(users)))