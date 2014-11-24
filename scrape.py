from newspaper import Article

def extract(article_url):

	article = Article(url=article_url)

	article.download()

	article.parse()

	return article.title,article.text

if __name__=='__main__':
	#just testing
	artcl = extract('http://www.cnn.com/2014/11/22/us/university-of-virginia-sexual-assault-allegations/')
	print artcl[0]
	print artcl[1]