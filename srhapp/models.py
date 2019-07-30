from django.db import models


# 新規テーブル作成　※１クラス＝１テーブルに該当
class Good(models.Model):
    """商品モデル"""

    class Meta:  # テーブル名を定義
        db_table = 'goods'

    # テーブルのカラムに対応するフィールドを定義
    title = models.CharField(verbose_name = '商品名', max_length = 255) # verbose_name：フィールド名
    category = models.CharField(verbose_name = 'カテゴリ', max_length = 255)
    price = models.IntegerField(verbose_name = '価格', null = True, blank = True) # null：DBでのnull制約（True=許可）、blank：フォームで入力必須にするかの判定

    # 管理サイトに表示させる文字列を定義
    def __str__(self):
        return self.title

