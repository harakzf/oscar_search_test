from django.test import TestCase
from django.utils import timezone

from srhapp.models import Good

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

class GoodTest(TestCase):
    """Goodクラスのテスト"""

    """何も登録しなければレコードの数は0個"""
    def test_is_empty(self):
        saved_goods = Good.objects.all()
        self.assertEqual(saved_goods.count(), 0)

    """1つデータを登録すればレコードの数は1個"""
    def test_is_not_empty(self):
        goods = Good()
        goods.save()
        saved_goods = Good.objects.all()
        self.assertEqual(saved_goods.count(), 1)

    """商品名(title), カテゴリ(category), 価格(price)を属性として持つ"""
    def test_saving_and_retrieving_good(self):
        first_goods = Good()
        title, category, price = 'ワンピース', 'スカート', '100'

        check_title = 'ワンピース'
        check_category = 'スカート'
        check_price = 100

        first_goods.title = title
        first_goods.category = category
        first_goods.price = price
        first_goods.save()

        saved_goods = Good.objects.all()
        actual_goods = saved_goods[0]

        self.assertEqual(actual_goods.title, check_title, 'TBL属性が想定（文字列）と異なっています')
        self.assertEqual(actual_goods.category, check_category, 'TBL属性が想定(文字列）と異なっています')
        self.assertEqual(actual_goods.price, check_price, 'TBL属性が想定（数値）と異なっています')