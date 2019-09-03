#encoding=utf-8
import re
import urllib.request
import time

def hupuNBAMainPage(url):
    try:
        req = urllib.request.Request(url)
        # req.add_header()
        data = urllib.request.urlopen(req).read().decode('utf-8')  # 爬取网页的内容
        # print(data)
        pat_all = '''<span class="textSpan">\n<a href="/.+.html" target="_blank" title=".+">\n<span class=".+">.+</span>\n</a>\n<em>\n\d+亮\d+回复</em>'''
        pat_all = re.compile(pat_all)
        results = pat_all.findall(data)
        return results

    except Exception as e:
        print('连接异常-->' + str(e))
        return -1

def titleHref(results):
    '''
    :param results:   抓取的结果
    :return:   贴名与链接
    '''
    pat_answer_num = '''\d+亮\d+回复'''
    pat_answer_num = re.compile(pat_answer_num)
    pat_title = '''title=".+">\n<span'''
    pat_title = re.compile(pat_title)
    pat_url = '''href="/[0-9]+.html"'''
    pat_url = re.compile(pat_url)

    titles = [pat_title.findall(item)[0][7:-8] for item in results if not None]
    hrefs = [url[:-8] + pat_url.findall(item)[0][6:-1] for item in results if not None]
    answer_num = [pat_answer_num.findall(item)[0] for item in results]


    # print(answer_num)
    # print(answer_num[0])
    # for item in titles:
    #     print(item)
    # for item in hrefs:
    #     print(item)
    # hrefs.pop()
    # dic = {}

    if len(titles) == len(hrefs):
    #     for i in range(len(titles)):
    #         dic[titles[i]] = hrefs[i]
        return titles, hrefs
    else:
        print('标题与链接数量不一致')
        return -1, -1

def reviewsPage(url):
    '''
    :param url: 每一个帖子的url，形如 https://bbs.hupu.com/27406916.html
    :return: -->list 返回正则匹配的本页的评论内容列表
    '''
    try:
        req = urllib.request.Request(url)
        # req.add_header()
        data = urllib.request.urlopen(req).read().decode('utf-8')  # 爬取网页的内容
        # print(data)
        pat_reviews = '''</blockquote>.+\n'''
        pat_all = re.compile(pat_reviews)
        results = pat_all.findall(data)
        for item in results:
            print(item.strip('\n').strip('</p>').strip('</blockquote><br>').strip('<p>'))
            # print()
        return results

    except Exception as e:
        print('连接异常-->' + str(e))
        return -1


if __name__=='__main__':
    t = time.time()
    url = 'https://bbs.hupu.com/all-nba'
    results = hupuNBAMainPage(url)
    titles, hrefs = titleHref(results)
    if titles!=1 and hrefs!=-1:
        for ii in range(len(titles)):
            print(titles[ii] + ': ' + hrefs[ii])
            # print()
    print(hrefs[0])
    reviewsPage(hrefs[0])
    print('\n总共花费了%f秒'%(time.time() - t))
    time.sleep(10)
