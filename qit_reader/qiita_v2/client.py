# -*- coding: utf-8 -*-
''' qiita.QiitaClient
Python wrapper for Qiita API v2
Details: http://qiita.com/api/v2/docs

created by @petitviolet
'''
from .client_base import QiitaClientBase

class QiitaClient(QiitaClientBase):
    def create_access_token(self, params=None, headers=None):
        ''' 与えられた認証情報をもとに新しいアクセストークンを発行します。
        '''
        return self.post("/access_tokens", params, headers)

    def delete_access_token(self, token, params=None, headers=None):
        ''' 与えられたアクセストークンを失効させ、それ以降利用されないようにします。
        '''
        return self.delete("/access_tokens/{}".format(token), params, headers)

    def get_comment(self, id, params=None, headers=None):
        ''' 特定のコメントを返します。
        '''
        return self.get("/comments/{}".format(id), params, headers)

    def delete_comment(self, id, params=None, headers=None):
        ''' 特定のコメントを削除します。
        '''
        return self.delete("/comments/{}".format(id), params, headers)

    def update_comment(self, id, params=None, headers=None):
        ''' 特定のコメントを更新します。
        '''
        return self.patch("/comments/{}".format(id), params, headers)

    def list_item_comments(self, item_id, params=None, headers=None):
        ''' 特定の投稿に寄せられたコメント一覧を返します。
        '''
        return self.get("/items/{}/comments".format(item_id), params, headers)

    def create_item_comment(self, item_id, params=None, headers=None):
        ''' 特定の投稿にコメントを付けます。
        '''
        return self.post("/items/{}/comments".format(item_id), params, headers)

    def thank_comment(self, comment_id, params=None, headers=None):
        ''' 特定のコメントにThankを付けます。
        '''
        return self.put("/comments/{}/thank".format(comment_id), params, headers)

    def unthank_comment(self, comment_id, params=None, headers=None):
        ''' 特定のコメントからThankを外します。
        '''
        return self.delete("/comments/{}/thank".format(comment_id), params, headers)

    def list_items(self, params=None, headers=None):
        ''' 新着順に全ての投稿一覧を返します。
        '''
        return self.get("/items", params, headers)

    def create_item(self, params=None, headers=None):
        ''' 新たに投稿を作成します。
        '''
        return self.post("/items", params, headers)

    def get_item(self, id, params=None, headers=None):
        ''' 特定の投稿を返します。
        '''
        return self.get("/items/{}".format(id), params, headers)

    def update_item(self, id, params=None, headers=None):
        ''' 特定の投稿を編集します。
        '''
        return self.patch("/items/{}".format(id), params, headers)

    def delete_item(self, id, params=None, headers=None):
        ''' 特定の投稿を削除します。
        '''
        return self.delete("/items/{}".format(id), params, headers)

    def list_tag_items(self, id, params=None, headers=None):
        ''' 特定のタグが付けられた投稿一覧を返します。
        '''
        return self.get("/tags/{}/items".format(id), params, headers)

    def list_user_items(self, user_id, params=None, headers=None):
        ''' 特定のユーザの投稿一覧を返します。
        '''
        return self.get("/users/{}/items".format(user_id), params, headers)

    def list_user_stocks(self, user_id, params=None, headers=None):
        ''' 特定のユーザがストックした投稿一覧を返します。
        '''
        return self.get("/users/{}/stocks".format(user_id), params, headers)

    def get_item_stock(self, item_id, params=None, headers=None):
        ''' 特定の投稿をストックしている場合に204を返します。
        '''
        return self.get("/items/{}/stock".format(item_id), params, headers)

    def stock_item(self, item_id, params=None, headers=None):
        ''' 特定の投稿をストックします。
        '''
        return self.put("/items/{}/stock".format(item_id), params, headers)

    def unstock_item(self, item_id, params=None, headers=None):
        ''' 特定の投稿をストックから取り除きます。
        '''
        return self.delete("/items/{}/stock".format(item_id), params, headers)

    def lgtm_item(self, item_id, params=None, headers=None):
        ''' 特定の投稿に「いいね！」を付けます。
        '''
        return self.put("/items/{}/lgtm".format(item_id), params, headers)

    def unlgtm_item(self, item_id, params=None, headers=None):
        ''' 特定の投稿への「いいね！」を取り消します。
        '''
        return self.delete("/items/{}/lgtm".format(item_id), params, headers)

    def list_projects(self, params=None, headers=None):
        ''' チーム内に存在するプロジェクト一覧を返します。
        '''
        return self.get("/projects", params, headers)

    def get_project(self, id, params=None, headers=None):
        ''' 特定のプロジェクトを返します。
        '''
        return self.get("/projects/{}".format(id), params, headers)

    def create_project(self, params=None, headers=None):
        ''' プロジェクトを新たに作成します。
        '''
        return self.post("/projects", params, headers)

    def delete_project(self, id, params=None, headers=None):
        ''' 特定のプロジェクトを削除します。
        '''
        return self.delete("/projects/{}".format(id), params, headers)

    def update_project(self, id, params=None, headers=None):
        ''' 特定のプロジェクトを編集します。
        '''
        return self.patch("/projects/{}".format(id), params, headers)

    def create_expanded_template(self, params=None, headers=None):
        ''' 受け取ったテンプレート用文字列の変数を展開して返します。
        '''
        return self.post("/expanded_templates", params, headers)

    def list_tags(self, params=None, headers=None):
        ''' 全てのタグ一覧を返します。
        '''
        return self.get("/tags", params, headers)

    def get_tag(self, id, params=None, headers=None):
        ''' 特定のタグを返します。
        '''
        return self.get("/tags/{}".format(id), params, headers)

    def list_user_following_tags(self, user_id, params=None, headers=None):
        ''' 特定のユーザがフォローしているタグ一覧を返します。
        '''
        return self.get("/users/{}/following_tags".format(user_id), params, headers)

    def get_tag_following(self, id, params=None, headers=None):
        ''' 特定のタグをフォローしている場合に204を返します。
        '''
        return self.get("/tags/{}/following".format(id), params, headers)

    def follow_tag(self, id, params=None, headers=None):
        ''' 特定のタグをフォローします。
        '''
        return self.put("/tags/{}/following".format(id), params, headers)

    def unfollow_tag(self, id, params=None, headers=None):
        ''' 特定のタグへのフォローを解除します。
        '''
        return self.delete("/tags/{}/following".format(id), params, headers)

    def list_teams(self, params=None, headers=None):
        ''' 現在のリクエストで認証されているユーザが所属している全てのチームを返します。
        '''
        return self.get("/teams", params, headers)

    def list_templates(self, params=None, headers=None):
        ''' 全てのテンプレート一覧を返します。
        '''
        return self.get("/templates", params, headers)

    def get_template(self, id, params=None, headers=None):
        ''' 特定のテンプレートを返します。
        '''
        return self.get("/templates/{}".format(id), params, headers)

    def delete_template(self, id, params=None, headers=None):
        ''' 特定のテンプレートを削除します。
        '''
        return self.delete("/templates/{}".format(id), params, headers)

    def create_template(self, params=None, headers=None):
        ''' 新しくテンプレートを作成します。
        '''
        return self.post("/templates", params, headers)

    def update_template(self, id, params=None, headers=None):
        ''' 特定のテンプレートを編集します。
        '''
        return self.patch("/templates/{}".format(id), params, headers)

    def list_users(self, params=None, headers=None):
        ''' 全てのユーザの一覧を返します。
        '''
        return self.get("/users", params, headers)

    def get_user(self, id, params=None, headers=None):
        ''' 特定のユーザを返します。
        '''
        return self.get("/users/{}".format(id), params, headers)

    def get_authenticated_user(self, params=None, headers=None):
        ''' アクセストークンに紐付いたユーザを返します。
        '''
        return self.get("/authenticated_user", params, headers)

    def list_user_followees(self, user_id, params=None, headers=None):
        ''' 特定のユーザがフォローしているユーザ一覧を返します。
        '''
        return self.get("/users/{}/followees".format(user_id), params, headers)

    def list_user_followers(self, user_id, params=None, headers=None):
        ''' 特定のユーザをフォローしているユーザ一覧を返します。
        '''
        return self.get("/users/{}/followers".format(user_id), params, headers)

    def list_item_stockers(self, item_id, params=None, headers=None):
        ''' 特定の投稿をストックしているユーザ一覧を返します。
        '''
        return self.get("/items/{}/stockers".format(item_id), params, headers)

    def get_user_following(self, user_id, params=None, headers=None):
        ''' 特定のユーザをフォローしている場合に204を返します。
        '''
        return self.get("/users/{}/following".format(user_id), params, headers)

    def follow_user(self, user_id, params=None, headers=None):
        ''' 特定のユーザをフォローします。
        '''
        return self.put("/users/{}/following".format(user_id), params, headers)

    def unfollow_user(self, user_id, params=None, headers=None):
        ''' 特定のユーザへのフォローを外します。
        '''
        return self.delete("/users/{}/following".format(user_id), params, headers)
