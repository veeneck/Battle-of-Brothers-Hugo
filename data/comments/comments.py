import xmltodict
import time
import hashlib
import os
import cgi

total_count = 0
m = hashlib.md5()

#_id: bc1e49d0-58fa-11e8-bebb-13146c4ef23d
#_parent: 2016-07-12-isometric-projectile-trajectory-in-swift-and-spritekit
#reply_to: ''
#name: r
#email: 604a2592fdc946151a05706ed0d9978f
#body: r
#date: '2018-05-16T11:17:35.978Z'

with open('big_data.xml') as fd:
    cfg = xmltodict.parse(fd.read())

for item in cfg['rss']['channel']['item']:
    print ""
    print "Title: " + item['title']
    print ""
    try:
        for comment in item['wp:comment']:
            total_count += 1
            try:
                comment_time = comment['wp:comment_date_gmt']
                post_time = item['wp:post_date']
                post_time = post_time.split(" ")[0]
                pattern = '%Y-%m-%d %H:%M:%S'
                epoch = int(time.mktime(time.strptime(comment_time, pattern)))
                dirname = post_time + "-" + item["wp:post_name"].rstrip("-2")
                filename = dirname + "/"  + "comment-" + str(epoch) + ".yml"
                print "opening " + filename
                if not os.path.isdir(dirname):
                    os.mkdir(dirname)
                    print("creating " + dirname)
                if os.path.exists(filename):
                    fh = open(filename, "r")
                else:
                    fh = open(filename, "w")
                fh.write("_parent: " + dirname + "\n")
            except Exception as e:
                print(e)
                pass
            try:
                print "_id: " + comment['wp:comment_id']
                fh.write("_id: " + comment['wp:comment_id'] + "\n")
            except:
                pass
            try:
                print "name: " + comment['wp:comment_author']
                fh.write("name: " + comment['wp:comment_author'] + "\n")
            except:
                pass
            try:
                if comment['wp:comment_parent'] != '0':
                    print "reply_to: " + comment['wp:comment_parent']
                    fh.write("reply_to: " + comment['wp:comment_parent'] + "\n")
            except:
                pass
            try:
                temp_email = comment['wp:comment_author_email']
                temp_email = temp_email.strip()
                temp_email = temp_email.lower()
                m.update(temp_email)

                print "email: " + m.hexdigest()
                fh.write("email: " + m.hexdigest() + "\n")
            except:
                pass
            try:
                comment_body = cgi.escape(comment['wp:comment_content'], True)
                print "body: " + comment['wp:comment_content']
                fh.write("body: '" + comment_body.replace("'","&#39;") + "'\n")
            except Exception as e:
                print(e)
                pass
            try:
                print "date: " + comment['wp:comment_date_gmt']
                fh.write("date: '" + str(comment['wp:comment_date_gmt']) + "'")
            except:
                pass
            print ""
            fh.close
    except:
        pass

print "Total Count: " + str(total_count)