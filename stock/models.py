# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models



class stock_list(models.Model):
    name = models.CharField(max_length=20)
    fullname = models.CharField(max_length=15)




class StockTable1108(models.Model):
    stock_id = models.AutoField(primary_key=True)
    date = models.IntegerField(blank=True, null=True)
    low_price = models.IntegerField(blank=True, null=True)
    high_price = models.IntegerField(blank=True, null=True)
    close_price = models.IntegerField(blank=True, null=True)
    open_price = models.IntegerField(blank=True, null=True)
    capacity = models.IntegerField(blank=True, null=True)
    turnover = models.IntegerField(blank=True, null=True)
    transaction_list = models.IntegerField(blank=True, null=True)
    change = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_table_1108'


class StockTable1201(models.Model):
    stock_id = models.AutoField(primary_key=True)
    date = models.IntegerField(blank=True, null=True)
    low_price = models.IntegerField(blank=True, null=True)
    high_price = models.IntegerField(blank=True, null=True)
    close_price = models.IntegerField(blank=True, null=True)
    open_price = models.IntegerField(blank=True, null=True)
    capacity = models.IntegerField(blank=True, null=True)
    turnover = models.IntegerField(blank=True, null=True)
    transaction_list = models.IntegerField(blank=True, null=True)
    change = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_table_1201'


class StockTable1234(models.Model):
    stock_id = models.AutoField(primary_key=True)
    date = models.IntegerField(blank=True, null=True)
    low_price = models.IntegerField(blank=True, null=True)
    high_price = models.IntegerField(blank=True, null=True)
    close_price = models.IntegerField(blank=True, null=True)
    open_price = models.IntegerField(blank=True, null=True)
    capacity = models.IntegerField(blank=True, null=True)
    turnover = models.IntegerField(blank=True, null=True)
    transaction_list = models.IntegerField(blank=True, null=True)
    change = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_table_1234'


class StockTable1604(models.Model):
    stock_id = models.AutoField(primary_key=True)
    date = models.IntegerField(blank=True, null=True)
    low_price = models.IntegerField(blank=True, null=True)
    high_price = models.IntegerField(blank=True, null=True)
    close_price = models.IntegerField(blank=True, null=True)
    open_price = models.IntegerField(blank=True, null=True)
    capacity = models.IntegerField(blank=True, null=True)
    turnover = models.IntegerField(blank=True, null=True)
    transaction_list = models.IntegerField(blank=True, null=True)
    change = models.IntegerField(blank=True, null=True)



    class Meta:
        managed = False
        db_table = 'stock_table_1604'


class StockTable2886(models.Model):
    stock_id = models.AutoField(primary_key=True)
    date = models.IntegerField(blank=True, null=True)
    low_price = models.IntegerField(blank=True, null=True)
    high_price = models.IntegerField(blank=True, null=True)
    close_price = models.IntegerField(blank=True, null=True)
    open_price = models.IntegerField(blank=True, null=True)
    capacity = models.IntegerField(blank=True, null=True)
    turnover = models.IntegerField(blank=True, null=True)
    transaction_list = models.IntegerField(blank=True, null=True)
    change = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_table_2886'


class StockTable2887(models.Model):
    stock_id = models.AutoField(primary_key=True)
    date = models.IntegerField(blank=True, null=True)
    low_price = models.IntegerField(blank=True, null=True)
    high_price = models.IntegerField(blank=True, null=True)
    close_price = models.IntegerField(blank=True, null=True)
    open_price = models.IntegerField(blank=True, null=True)
    capacity = models.IntegerField(blank=True, null=True)
    turnover = models.IntegerField(blank=True, null=True)
    transaction_list = models.IntegerField(blank=True, null=True)
    change = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_table_2887'


class StockTable2890(models.Model):
    stock_id = models.AutoField(primary_key=True)
    date = models.IntegerField(blank=True, null=True)
    low_price = models.IntegerField(blank=True, null=True)
    high_price = models.IntegerField(blank=True, null=True)
    close_price = models.IntegerField(blank=True, null=True)
    open_price = models.IntegerField(blank=True, null=True)
    capacity = models.IntegerField(blank=True, null=True)
    turnover = models.IntegerField(blank=True, null=True)
    transaction_list = models.IntegerField(blank=True, null=True)
    change = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_table_2890'


class StockTable2892(models.Model):
    stock_id = models.AutoField(primary_key=True)
    date = models.IntegerField(blank=True, null=True)
    low_price = models.IntegerField(blank=True, null=True)
    high_price = models.IntegerField(blank=True, null=True)
    close_price = models.IntegerField(blank=True, null=True)
    open_price = models.IntegerField(blank=True, null=True)
    capacity = models.IntegerField(blank=True, null=True)
    turnover = models.IntegerField(blank=True, null=True)
    transaction_list = models.IntegerField(blank=True, null=True)
    change = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_table_2892'


class StockTable3045(models.Model):
    stock_id = models.AutoField(primary_key=True)
    date = models.IntegerField(blank=True, null=True)
    low_price = models.IntegerField(blank=True, null=True)
    high_price = models.IntegerField(blank=True, null=True)
    close_price = models.IntegerField(blank=True, null=True)
    open_price = models.IntegerField(blank=True, null=True)
    capacity = models.IntegerField(blank=True, null=True)
    turnover = models.IntegerField(blank=True, null=True)
    transaction_list = models.IntegerField(blank=True, null=True)
    change = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_table_3045'


class StockTable5876(models.Model):
    stock_id = models.AutoField(primary_key=True)
    date = models.IntegerField(blank=True, null=True)
    low_price = models.IntegerField(blank=True, null=True)
    high_price = models.IntegerField(blank=True, null=True)
    close_price = models.IntegerField(blank=True, null=True)
    open_price = models.IntegerField(blank=True, null=True)
    capacity = models.IntegerField(blank=True, null=True)
    turnover = models.IntegerField(blank=True, null=True)
    transaction_list = models.IntegerField(blank=True, null=True)
    change = models.IntegerField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'stock_table_5876'


