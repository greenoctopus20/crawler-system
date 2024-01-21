from django.db import models

class User(models.Model):
    id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=250, default="unknown")
    site_count = models.IntegerField(default=0)



class Site(models.Model):
    id = models.AutoField(primary_key=True)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    domain_url = models.CharField(max_length=255)
    article_xpath = models.CharField(max_length=255)
    title_xpath = models.CharField(max_length=255)
    body_xpath = models.CharField(max_length=255)
    author_xpath = models.CharField(max_length=255)
    date_xpath = models.CharField(max_length=255)



    @classmethod
    def create(cls, user_id, domain_url, article_xpath, title_xpath, body_xpath, author_xpath, date_xpath):
        site = cls(
            user_id=user_id,
            domain_url=domain_url,
            article_xpath=article_xpath,
            title_xpath=title_xpath,
            body_xpath=body_xpath,
            author_xpath=author_xpath,
            date_xpath=date_xpath
        )
        return site

    def get_config(self):
        return {
            'id': self.id,
            'domain_url': self.domain_url,
            'article_xpath': self.article_xpath,
            'title_xpath': self.title_xpath,
            'body_xpath': self.body_xpath,
            'author_xpath': self.author_xpath,
            'date_xpath': self.date_xpath,
        }
