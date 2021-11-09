# This is an auto-generated Django model module.
# You'll have to do the following manually to clean this up:
#   * Rearrange models' order
#   * Make sure each model has one field with primary_key=True
#   * Make sure each ForeignKey and OneToOneField has `on_delete` set to the desired behavior
#   * Remove `managed = False` lines if you wish to allow Django to create, modify, and delete the table
# Feel free to rename the models, but don't rename db_table values or field names.
from django.db import models


class Efmigrationshistory(models.Model):
    migrationid = models.CharField(db_column='MigrationId', primary_key=True, max_length=150)  # Field name made lowercase.
    productversion = models.CharField(db_column='ProductVersion', max_length=32)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = '__efmigrationshistory'


class PgAddress(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    zipcode = models.TextField(db_column='ZipCode', blank=True, null=True)  # Field name made lowercase.
    city = models.TextField(db_column='City', blank=True, null=True)  # Field name made lowercase.
    country = models.TextField(db_column='Country', blank=True, null=True)  # Field name made lowercase.
    state = models.TextField(db_column='State', blank=True, null=True)  # Field name made lowercase.
    street = models.TextField(db_column='Street', blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    createdby = models.TextField(db_column='CreatedBy', blank=True, null=True)  # Field name made lowercase.
    lastupdateddate = models.DateTimeField(db_column='LastUpdatedDate', blank=True, null=True)  # Field name made lowercase.
    lastupdatedby = models.TextField(db_column='LastUpdatedBy', blank=True, null=True)  # Field name made lowercase.
    deleteddate = models.DateTimeField(db_column='DeletedDate', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.TextField(db_column='DeletedBy', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pg_address'


class PgAdmin(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    nom = models.TextField(db_column='Nom')  # Field name made lowercase.
    email = models.TextField(db_column='Email')  # Field name made lowercase.
    password = models.TextField(db_column='Password')  # Field name made lowercase.
    activationcode = models.CharField(db_column='ActivationCode', max_length=36, db_collation='ascii_general_ci')  # Field name made lowercase.
    role = models.TextField(db_column='Role', blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    createdby = models.TextField(db_column='CreatedBy', blank=True, null=True)  # Field name made lowercase.
    lastupdateddate = models.DateTimeField(db_column='LastUpdatedDate', blank=True, null=True)  # Field name made lowercase.
    lastupdatedby = models.TextField(db_column='LastUpdatedBy', blank=True, null=True)  # Field name made lowercase.
    deleteddate = models.DateTimeField(db_column='DeletedDate', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.TextField(db_column='DeletedBy', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pg_admin'


class PgBrand(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name')  # Field name made lowercase.
    description = models.TextField(db_column='Description')  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    createdby = models.TextField(db_column='CreatedBy', blank=True, null=True)  # Field name made lowercase.
    lastupdateddate = models.DateTimeField(db_column='LastUpdatedDate', blank=True, null=True)  # Field name made lowercase.
    lastupdatedby = models.TextField(db_column='LastUpdatedBy', blank=True, null=True)  # Field name made lowercase.
    deleteddate = models.DateTimeField(db_column='DeletedDate', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.TextField(db_column='DeletedBy', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pg_brand'


class PgCarrier(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name')  # Field name made lowercase.
    description = models.TextField(db_column='Description')  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    createdby = models.TextField(db_column='CreatedBy', blank=True, null=True)  # Field name made lowercase.
    lastupdateddate = models.DateTimeField(db_column='LastUpdatedDate', blank=True, null=True)  # Field name made lowercase.
    lastupdatedby = models.TextField(db_column='LastUpdatedBy', blank=True, null=True)  # Field name made lowercase.
    deleteddate = models.DateTimeField(db_column='DeletedDate', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.TextField(db_column='DeletedBy', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pg_carrier'


class PgCart(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    clientid = models.ForeignKey('PgClient', models.DO_NOTHING, db_column='ClientId', blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    createdby = models.TextField(db_column='CreatedBy', blank=True, null=True)  # Field name made lowercase.
    lastupdateddate = models.DateTimeField(db_column='LastUpdatedDate', blank=True, null=True)  # Field name made lowercase.
    lastupdatedby = models.TextField(db_column='LastUpdatedBy', blank=True, null=True)  # Field name made lowercase.
    deleteddate = models.DateTimeField(db_column='DeletedDate', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.TextField(db_column='DeletedBy', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pg_cart'


class PgCategory(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name')  # Field name made lowercase.
    description = models.TextField(db_column='Description')  # Field name made lowercase.
    imagepath = models.TextField(db_column='ImagePath', blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    createdby = models.TextField(db_column='CreatedBy', blank=True, null=True)  # Field name made lowercase.
    lastupdateddate = models.DateTimeField(db_column='LastUpdatedDate', blank=True, null=True)  # Field name made lowercase.
    lastupdatedby = models.TextField(db_column='LastUpdatedBy', blank=True, null=True)  # Field name made lowercase.
    deleteddate = models.DateTimeField(db_column='DeletedDate', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.TextField(db_column='DeletedBy', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pg_category'


class PgCharacteristic(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name')  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    createdby = models.TextField(db_column='CreatedBy', blank=True, null=True)  # Field name made lowercase.
    lastupdateddate = models.DateTimeField(db_column='LastUpdatedDate', blank=True, null=True)  # Field name made lowercase.
    lastupdatedby = models.TextField(db_column='LastUpdatedBy', blank=True, null=True)  # Field name made lowercase.
    deleteddate = models.DateTimeField(db_column='DeletedDate', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.TextField(db_column='DeletedBy', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pg_characteristic'


class PgClient(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    lastname = models.TextField(db_column='LastName', blank=True, null=True)  # Field name made lowercase.
    firstname = models.TextField(db_column='FirstName', blank=True, null=True)  # Field name made lowercase.
    email = models.TextField(db_column='Email', blank=True, null=True)  # Field name made lowercase.
    password = models.TextField(db_column='Password', blank=True, null=True)  # Field name made lowercase.
    addressid = models.IntegerField(db_column='AddressId')  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    createdby = models.TextField(db_column='CreatedBy', blank=True, null=True)  # Field name made lowercase.
    lastupdateddate = models.DateTimeField(db_column='LastUpdatedDate', blank=True, null=True)  # Field name made lowercase.
    lastupdatedby = models.TextField(db_column='LastUpdatedBy', blank=True, null=True)  # Field name made lowercase.
    deleteddate = models.DateTimeField(db_column='DeletedDate', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.TextField(db_column='DeletedBy', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pg_client'


class PgImage(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    path = models.TextField(db_column='Path', blank=True, null=True)  # Field name made lowercase.
    productid = models.ForeignKey('PgProduct', models.DO_NOTHING, db_column='ProductId', blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    createdby = models.TextField(db_column='CreatedBy', blank=True, null=True)  # Field name made lowercase.
    lastupdateddate = models.DateTimeField(db_column='LastUpdatedDate', blank=True, null=True)  # Field name made lowercase.
    lastupdatedby = models.TextField(db_column='LastUpdatedBy', blank=True, null=True)  # Field name made lowercase.
    deleteddate = models.DateTimeField(db_column='DeletedDate', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.TextField(db_column='DeletedBy', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pg_image'


class PgProduct(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name')  # Field name made lowercase.
    description = models.TextField(db_column='Description')  # Field name made lowercase.
    price = models.IntegerField(db_column='Price')  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity')  # Field name made lowercase.
    categoryid = models.IntegerField(db_column='CategoryId')  # Field name made lowercase.
    brandid = models.IntegerField(db_column='BrandId')  # Field name made lowercase.
    attributid = models.IntegerField(db_column='AttributId')  # Field name made lowercase.
    caracteristicid = models.IntegerField(db_column='CaracteristicId')  # Field name made lowercase.
    retailerid = models.IntegerField(db_column='RetailerId')  # Field name made lowercase.
    promotionid = models.IntegerField(db_column='PromotionId', blank=True, null=True)  # Field name made lowercase.
    cartid = models.ForeignKey(PgCart, models.DO_NOTHING, db_column='CartId', blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    createdby = models.TextField(db_column='CreatedBy', blank=True, null=True)  # Field name made lowercase.
    lastupdateddate = models.DateTimeField(db_column='LastUpdatedDate', blank=True, null=True)  # Field name made lowercase.
    lastupdatedby = models.TextField(db_column='LastUpdatedBy', blank=True, null=True)  # Field name made lowercase.
    deleteddate = models.DateTimeField(db_column='DeletedDate', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.TextField(db_column='DeletedBy', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pg_product'


class PgPromotion(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name')  # Field name made lowercase.
    discount = models.FloatField(db_column='Discount')  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    createdby = models.TextField(db_column='CreatedBy', blank=True, null=True)  # Field name made lowercase.
    lastupdateddate = models.DateTimeField(db_column='LastUpdatedDate', blank=True, null=True)  # Field name made lowercase.
    lastupdatedby = models.TextField(db_column='LastUpdatedBy', blank=True, null=True)  # Field name made lowercase.
    deleteddate = models.DateTimeField(db_column='DeletedDate', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.TextField(db_column='DeletedBy', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pg_promotion'


class PgRetailer(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name')  # Field name made lowercase.
    description = models.TextField(db_column='Description')  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    createdby = models.TextField(db_column='CreatedBy', blank=True, null=True)  # Field name made lowercase.
    lastupdateddate = models.DateTimeField(db_column='LastUpdatedDate', blank=True, null=True)  # Field name made lowercase.
    lastupdatedby = models.TextField(db_column='LastUpdatedBy', blank=True, null=True)  # Field name made lowercase.
    deleteddate = models.DateTimeField(db_column='DeletedDate', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.TextField(db_column='DeletedBy', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pg_retailer'


class PgTransaction(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    paypalid = models.TextField(db_column='PaypalId', blank=True, null=True)  # Field name made lowercase.
    currentstate = models.TextField(db_column='CurrentState', blank=True, null=True)  # Field name made lowercase.
    paymentmethod = models.TextField(db_column='PaymentMethod', blank=True, null=True)  # Field name made lowercase.
    clientid = models.IntegerField(db_column='ClientId')  # Field name made lowercase.
    carrierid = models.IntegerField(db_column='CarrierId')  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    createdby = models.TextField(db_column='CreatedBy', blank=True, null=True)  # Field name made lowercase.
    lastupdateddate = models.DateTimeField(db_column='LastUpdatedDate', blank=True, null=True)  # Field name made lowercase.
    lastupdatedby = models.TextField(db_column='LastUpdatedBy', blank=True, null=True)  # Field name made lowercase.
    deleteddate = models.DateTimeField(db_column='DeletedDate', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.TextField(db_column='DeletedBy', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pg_transaction'


class PgTransactionproduct(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    productid = models.ForeignKey(PgProduct, models.DO_NOTHING, db_column='ProductId', blank=True, null=True)  # Field name made lowercase.
    transactionid = models.IntegerField(db_column='TransactionId')  # Field name made lowercase.
    price = models.FloatField(db_column='Price')  # Field name made lowercase.
    reduction = models.FloatField(db_column='Reduction')  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    createdby = models.TextField(db_column='CreatedBy', blank=True, null=True)  # Field name made lowercase.
    lastupdateddate = models.DateTimeField(db_column='LastUpdatedDate', blank=True, null=True)  # Field name made lowercase.
    lastupdatedby = models.TextField(db_column='LastUpdatedBy', blank=True, null=True)  # Field name made lowercase.
    deleteddate = models.DateTimeField(db_column='DeletedDate', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.TextField(db_column='DeletedBy', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pg_transactionproduct'


class PgTypeattribut(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    attribut = models.TextField(db_column='Attribut', blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    createdby = models.TextField(db_column='CreatedBy', blank=True, null=True)  # Field name made lowercase.
    lastupdateddate = models.DateTimeField(db_column='LastUpdatedDate', blank=True, null=True)  # Field name made lowercase.
    lastupdatedby = models.TextField(db_column='LastUpdatedBy', blank=True, null=True)  # Field name made lowercase.
    deleteddate = models.DateTimeField(db_column='DeletedDate', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.TextField(db_column='DeletedBy', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pg_typeattribut'


class PgValeurattribut(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    typeid = models.ForeignKey(PgTypeattribut, models.DO_NOTHING, db_column='TypeId', blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    createdby = models.TextField(db_column='CreatedBy', blank=True, null=True)  # Field name made lowercase.
    lastupdateddate = models.DateTimeField(db_column='LastUpdatedDate', blank=True, null=True)  # Field name made lowercase.
    lastupdatedby = models.TextField(db_column='LastUpdatedBy', blank=True, null=True)  # Field name made lowercase.
    deleteddate = models.DateTimeField(db_column='DeletedDate', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.TextField(db_column='DeletedBy', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pg_valeurattribut'


class PgValeurcharacteristic(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    name = models.TextField(db_column='Name', blank=True, null=True)  # Field name made lowercase.
    typecharacteristicid = models.ForeignKey(PgCharacteristic, models.DO_NOTHING, db_column='TypeCharacteristicId', blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate')  # Field name made lowercase.
    createdby = models.TextField(db_column='CreatedBy', blank=True, null=True)  # Field name made lowercase.
    lastupdateddate = models.DateTimeField(db_column='LastUpdatedDate', blank=True, null=True)  # Field name made lowercase.
    lastupdatedby = models.TextField(db_column='LastUpdatedBy', blank=True, null=True)  # Field name made lowercase.
    deleteddate = models.DateTimeField(db_column='DeletedDate', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.TextField(db_column='DeletedBy', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pg_valeurcharacteristic'
