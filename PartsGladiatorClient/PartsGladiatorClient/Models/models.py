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


class AuthGroup(models.Model):
    name = models.CharField(unique=True, max_length=150)

    class Meta:
        managed = False
        db_table = 'auth_group'


class AuthGroupPermissions(models.Model):
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)
    permission = models.ForeignKey('AuthPermission', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'auth_group_permissions'
        unique_together = (('group', 'permission'),)


class AuthPermission(models.Model):
    name = models.CharField(max_length=255)
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING)
    codename = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'auth_permission'
        unique_together = (('content_type', 'codename'),)


class AuthenCustomuser(models.Model):
    last_login = models.DateTimeField(blank=True, null=True)
    is_superuser = models.IntegerField()
    username = models.CharField(unique=True, max_length=150)
    first_name = models.CharField(max_length=150)
    last_name = models.CharField(max_length=150)
    is_staff = models.IntegerField()
    is_active = models.IntegerField()
    date_joined = models.DateTimeField()
    lastname = models.TextField(db_column='LastName', blank=True, null=True)  # Field name made lowercase.
    firstname = models.TextField(db_column='FirstName', blank=True, null=True)  # Field name made lowercase.
    email = models.TextField(db_column='Email', blank=True, null=True)  # Field name made lowercase.
    password = models.TextField(db_column='Password', blank=True, null=True)  # Field name made lowercase.
    addressid = models.IntegerField(db_column='AddressId', blank=True, null=True)  # Field name made lowercase.
    createddate = models.DateTimeField(db_column='CreatedDate', blank=True, null=True)  # Field name made lowercase.
    createdby = models.TextField(db_column='CreatedBy', blank=True, null=True)  # Field name made lowercase.
    lastupdateddate = models.DateTimeField(db_column='LastUpdatedDate', blank=True, null=True)  # Field name made lowercase.
    lastupdatedby = models.TextField(db_column='LastUpdatedBy', blank=True, null=True)  # Field name made lowercase.
    deleteddate = models.DateTimeField(db_column='DeletedDate', blank=True, null=True)  # Field name made lowercase.
    deletedby = models.TextField(db_column='DeletedBy', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'authen_customuser'


class AuthenCustomuserGroups(models.Model):
    customuser = models.ForeignKey(AuthenCustomuser, models.DO_NOTHING)
    group = models.ForeignKey(AuthGroup, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'authen_customuser_groups'
        unique_together = (('customuser', 'group'),)


class AuthenCustomuserUserPermissions(models.Model):
    customuser = models.ForeignKey(AuthenCustomuser, models.DO_NOTHING)
    permission = models.ForeignKey(AuthPermission, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'authen_customuser_user_permissions'
        unique_together = (('customuser', 'permission'),)


class DjangoAdminLog(models.Model):
    action_time = models.DateTimeField()
    object_id = models.TextField(blank=True, null=True)
    object_repr = models.CharField(max_length=200)
    action_flag = models.PositiveSmallIntegerField()
    change_message = models.TextField()
    content_type = models.ForeignKey('DjangoContentType', models.DO_NOTHING, blank=True, null=True)
    user = models.ForeignKey(AuthenCustomuser, models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'django_admin_log'


class DjangoContentType(models.Model):
    app_label = models.CharField(max_length=100)
    model = models.CharField(max_length=100)

    class Meta:
        managed = False
        db_table = 'django_content_type'
        unique_together = (('app_label', 'model'),)


class DjangoMigrations(models.Model):
    app = models.CharField(max_length=255)
    name = models.CharField(max_length=255)
    applied = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_migrations'


class DjangoSession(models.Model):
    session_key = models.CharField(primary_key=True, max_length=40)
    session_data = models.TextField()
    expire_date = models.DateTimeField()

    class Meta:
        managed = False
        db_table = 'django_session'


class PaypalIpn(models.Model):
    business = models.CharField(max_length=127)
    charset = models.CharField(max_length=255)
    custom = models.CharField(max_length=256)
    notify_version = models.DecimalField(max_digits=64, decimal_places=2, blank=True, null=True)
    parent_txn_id = models.CharField(max_length=19)
    receiver_email = models.CharField(max_length=254)
    receiver_id = models.CharField(max_length=255)
    residence_country = models.CharField(max_length=2)
    test_ipn = models.IntegerField()
    txn_id = models.CharField(max_length=255)
    txn_type = models.CharField(max_length=255)
    verify_sign = models.CharField(max_length=255)
    address_country = models.CharField(max_length=64)
    address_city = models.CharField(max_length=40)
    address_country_code = models.CharField(max_length=64)
    address_name = models.CharField(max_length=128)
    address_state = models.CharField(max_length=40)
    address_status = models.CharField(max_length=255)
    address_street = models.CharField(max_length=200)
    address_zip = models.CharField(max_length=20)
    contact_phone = models.CharField(max_length=20)
    first_name = models.CharField(max_length=64)
    last_name = models.CharField(max_length=64)
    payer_business_name = models.CharField(max_length=127)
    payer_email = models.CharField(max_length=127)
    payer_id = models.CharField(max_length=13)
    auth_amount = models.DecimalField(max_digits=64, decimal_places=2, blank=True, null=True)
    auth_exp = models.CharField(max_length=28)
    auth_id = models.CharField(max_length=19)
    auth_status = models.CharField(max_length=255)
    exchange_rate = models.DecimalField(max_digits=64, decimal_places=16, blank=True, null=True)
    invoice = models.CharField(max_length=127)
    item_name = models.CharField(max_length=127)
    item_number = models.CharField(max_length=127)
    mc_currency = models.CharField(max_length=32)
    mc_fee = models.DecimalField(max_digits=64, decimal_places=2, blank=True, null=True)
    mc_gross = models.DecimalField(max_digits=64, decimal_places=2, blank=True, null=True)
    mc_handling = models.DecimalField(max_digits=64, decimal_places=2, blank=True, null=True)
    mc_shipping = models.DecimalField(max_digits=64, decimal_places=2, blank=True, null=True)
    memo = models.CharField(max_length=255)
    num_cart_items = models.IntegerField(blank=True, null=True)
    option_name1 = models.CharField(max_length=64)
    option_name2 = models.CharField(max_length=64)
    payer_status = models.CharField(max_length=255)
    payment_date = models.DateTimeField(blank=True, null=True)
    payment_gross = models.DecimalField(max_digits=64, decimal_places=2, blank=True, null=True)
    payment_status = models.CharField(max_length=255)
    payment_type = models.CharField(max_length=255)
    pending_reason = models.CharField(max_length=255)
    protection_eligibility = models.CharField(max_length=255)
    quantity = models.IntegerField(blank=True, null=True)
    reason_code = models.CharField(max_length=255)
    remaining_settle = models.DecimalField(max_digits=64, decimal_places=2, blank=True, null=True)
    settle_amount = models.DecimalField(max_digits=64, decimal_places=2, blank=True, null=True)
    settle_currency = models.CharField(max_length=32)
    shipping = models.DecimalField(max_digits=64, decimal_places=2, blank=True, null=True)
    shipping_method = models.CharField(max_length=255)
    tax = models.DecimalField(max_digits=64, decimal_places=2, blank=True, null=True)
    transaction_entity = models.CharField(max_length=255)
    auction_buyer_id = models.CharField(max_length=64)
    auction_closing_date = models.DateTimeField(blank=True, null=True)
    auction_multi_item = models.IntegerField(blank=True, null=True)
    for_auction = models.DecimalField(max_digits=64, decimal_places=2, blank=True, null=True)
    amount = models.DecimalField(max_digits=64, decimal_places=2, blank=True, null=True)
    amount_per_cycle = models.DecimalField(max_digits=64, decimal_places=2, blank=True, null=True)
    initial_payment_amount = models.DecimalField(max_digits=64, decimal_places=2, blank=True, null=True)
    next_payment_date = models.DateTimeField(blank=True, null=True)
    outstanding_balance = models.DecimalField(max_digits=64, decimal_places=2, blank=True, null=True)
    payment_cycle = models.CharField(max_length=255)
    period_type = models.CharField(max_length=255)
    product_name = models.CharField(max_length=255)
    product_type = models.CharField(max_length=255)
    profile_status = models.CharField(max_length=255)
    recurring_payment_id = models.CharField(max_length=255)
    rp_invoice_id = models.CharField(max_length=127)
    time_created = models.DateTimeField(blank=True, null=True)
    amount1 = models.DecimalField(max_digits=64, decimal_places=2, blank=True, null=True)
    amount2 = models.DecimalField(max_digits=64, decimal_places=2, blank=True, null=True)
    amount3 = models.DecimalField(max_digits=64, decimal_places=2, blank=True, null=True)
    mc_amount1 = models.DecimalField(max_digits=64, decimal_places=2, blank=True, null=True)
    mc_amount2 = models.DecimalField(max_digits=64, decimal_places=2, blank=True, null=True)
    mc_amount3 = models.DecimalField(max_digits=64, decimal_places=2, blank=True, null=True)
    password = models.CharField(max_length=24)
    period1 = models.CharField(max_length=255)
    period2 = models.CharField(max_length=255)
    period3 = models.CharField(max_length=255)
    reattempt = models.CharField(max_length=1)
    recur_times = models.IntegerField(blank=True, null=True)
    recurring = models.CharField(max_length=1)
    retry_at = models.DateTimeField(blank=True, null=True)
    subscr_date = models.DateTimeField(blank=True, null=True)
    subscr_effective = models.DateTimeField(blank=True, null=True)
    subscr_id = models.CharField(max_length=19)
    username = models.CharField(max_length=64)
    case_creation_date = models.DateTimeField(blank=True, null=True)
    case_id = models.CharField(max_length=255)
    case_type = models.CharField(max_length=255)
    receipt_id = models.CharField(max_length=255)
    currency_code = models.CharField(max_length=32)
    handling_amount = models.DecimalField(max_digits=64, decimal_places=2, blank=True, null=True)
    transaction_subject = models.CharField(max_length=256)
    ipaddress = models.CharField(max_length=39, blank=True, null=True)
    flag = models.IntegerField()
    flag_code = models.CharField(max_length=16)
    flag_info = models.TextField()
    query = models.TextField()
    response = models.TextField()
    created_at = models.DateTimeField()
    updated_at = models.DateTimeField()
    from_view = models.CharField(max_length=6, blank=True, null=True)
    mp_id = models.CharField(max_length=128, blank=True, null=True)
    option_selection1 = models.CharField(max_length=200)
    option_selection2 = models.CharField(max_length=200)

    class Meta:
        managed = False
        db_table = 'paypal_ipn'


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


class PgCartproduct(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity')  # Field name made lowercase.
    cartid = models.ForeignKey(PgCart, models.DO_NOTHING, db_column='CartId', blank=True, null=True)  # Field name made lowercase.
    productid = models.ForeignKey('PgProduct', models.DO_NOTHING, db_column='ProductId', blank=True, null=True)  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'pg_cartproduct'


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
    productid = models.ForeignKey('PgProduct', models.DO_NOTHING, db_column='ProductId')  # Field name made lowercase.
    order = models.IntegerField(db_column='Order')  # Field name made lowercase.
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
    price = models.FloatField(db_column='Price')  # Field name made lowercase.
    quantity = models.IntegerField(db_column='Quantity')  # Field name made lowercase.
    categoryid = models.IntegerField(db_column='CategoryId')  # Field name made lowercase.
    brandid = models.IntegerField(db_column='BrandId')  # Field name made lowercase.
    attributid = models.IntegerField(db_column='AttributId')  # Field name made lowercase.
    caracteristicid = models.IntegerField(db_column='CaracteristicId')  # Field name made lowercase.
    retailerid = models.IntegerField(db_column='RetailerId')  # Field name made lowercase.
    promotionid = models.IntegerField(db_column='PromotionId', blank=True, null=True)  # Field name made lowercase.
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
    active = models.IntegerField(db_column='Active')  # Field name made lowercase.
    path = models.TextField(db_column='Path')  # Field name made lowercase.
    startdate = models.DateTimeField(db_column='StartDate')  # Field name made lowercase.
    enddate = models.DateTimeField(db_column='EndDate')  # Field name made lowercase.
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

    

    
class prodpromoviews(models.Model):
    productid = models.AutoField(db_column='productid', primary_key=True)
    productname = models.TextField(
        db_column='productname', blank=True, null=True)
    productname = models.TextField(db_column='productname', blank=True, null=True)
        
    price = models.FloatField(db_column='price')
    promoname = models.TextField(db_column='promoname')
    prixrabais = models.FloatField(db_column='prixrabais')
    path = models.TextField(db_column='Path', blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'prodpromoviews'


class OneImageProductViews(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    name = models.TextField(db_column='Name', blank=True, null=True)
    description = models.TextField(db_column='Description', blank=True, null=True)
    path = models.TextField(db_column='Path', blank=True, null=True)
    class Meta:
        managed = False
        db_table = 'OneImageProductViews'