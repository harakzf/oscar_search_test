from django.test.utils import override_settings

# テストクラスに継承させるTestCaseをインポート
from django.test import TestCase

# reverse関数のインポート（URLの逆引きに必要）
from django.urls import reverse

# srhapp直下のmodelsをインポート
from srhapp import models
from srhapp.models import Good

# ViewのIndexViewをインポート（factory_categoryとfactory_ticket関数が定義されている）
from srhapp.views import IndexView
from unicodedata import category

"""
UnitTestの書き方
・アプリケーションの下に test から始まるファイルを作る
・django.test.TestCaseを継承したクラスを作る
・メソッド名をtestから始める


メソッド                 確認事項
assertEqual(a, b)        a == b
assertNotEqual(a, b)     a != b
assertTrue(x)            bool(x) is True
assertFalse(x)           bool(x) is False

例外が発生したらOK
def test_exception2(self):
self.assertRaises(Exception, func)

"""

# Ticketというモデルのリスト作成に関するテストコードを定義するクラスを作成
class IndexViewTest(TestCase):

    @override_settings(DEBUG=True) #テスト実行時にデバッグ=Trueで実行

    def test_post(self):
        # DBデータを事前に登録しておく
        Good(title='ワンピース', category='スカート', price=100).save()

        #チェック用
        check_title, check_category, check_price = 'ワンピース', 'スカート', 100

        # リクエストを擬似的に送ってくれるHTTPクライアント（self.cliant）でレスポンスオブジェクトを生成
        response = self.client.post(reverse('srhapp:index'), {'title':'ワンピース', 'category':'スカート', 'price':100})

        # 結果が正常に返ってきていることを確認
        assert response.status_code == 200

        #検索結果が1件であることを確認
        self.assertEqual(response.context['object_list'].count(),1)

        #検索結果の値突合
        self.assertEqual(response.context['object_list'].first().title, check_title)
        self.assertEqual(response.context['object_list'].first().category, check_category)
        self.assertEqual(response.context['object_list'].first().price, check_price)

