from django.db import models
import datetime

#CLASS ADDRESS
class Address(models.Model):
    ZipCode = models.CharField(max_length = 6)
    City = models.CharField(max_length = 50)
    Country = models.CharField(max_length = 50)
    State = models.CharField(max_length = 50)
    Street = models.CharField(max_length = 50)

    def GetZipCode(self):
        return "%s" % (self.ZipCode)

    def GetCity(self):
        return "%s" % (self.City)

    def GetCoutry(self):
        return "%s" % (self.Country)

    def GetState(self):
        return "%s" % (self.State)

    def GetStreet(self):
        return "%s" % (self.Street)

#CLASS BASE OBJECT
class BaseObject(models.Model):
    Id = models.IntegerField()
    def GetId(self):
        return "%s" % (self.Id)

    CreatedDate = models.DateTimeField()
    def GetCreatedDate(self):
        return "%s" % (self.CreatedDate)

    CreatedBy = models.CharField(max_length = 50)
    def GetCreatedBy(self):
        return "%s" % (self.CreatedBy)

    LastUpdatedDate = models.DateTimeField()
    def GetLastUpdatedDate(self):
        return "%s" % (self.LastUpdatedDate)

    LastupdateBy = models.CharField(max_length = 50)
    def GetLastUpdatedBy(self):
        return "%s" % (self.LastupdateBy)

    DeletedDate = models.DateTimeField()
    def GetDeletedDate(self):
        return "%s" % (self.DeletedDate)

    DeletedBy = models.CharField(max_length = 50)
    def GetDeletedBy(self):
        return "%s" % (self.DeletedBy)


    class Meta:
        abstract = True

#CLASS ADMINUSER
class AdminUser(BaseObject):
    ROLE_ADMIN = "Admin"
    ROLE_CLIENT = "Client"

    Name = models.CharField(max_length = 50)
    def GetName(self):
        return "%s" % (self.Name)

    Email = models.CharField(max_length = 50)
    def GetEmail(self):
        return "%s" % (self.Email)

    Password = models.CharField(max_length = 50)
    def GetPassword(self):
        return "%s" % (self.Password)

    ActivationCode = models.CharField(max_length = 50)
    def GetActivationCode(self):
        return "%s" % (self.ActivationCode)

    Role = models.CharField(max_length = 50)
    def GetRole(self):
        return "%s" % (self.Role)


#CLASS BRAND
class Brand(BaseObject):
    Name = models.CharField(max_length = 50)
    def GetName(self):
        return "%s" % (self.Name)

    Description = models.CharField(max_length = 50)
    def GetDescription(self):
        return "%s" % (self.Description)

#CLASS CARRIER
class Carrier(BaseObject):
    Name = models.CharField(max_length = 50)
    def GetName(self):
        return "%s" % (self.Name)

    Description = models.CharField(max_length = 50)
    def GetDescription(self):
        return "%s" % (self.Description)

#CLASS CLIENT
class Client(BaseObject):
    LastName = models.CharField(max_length = 50)
    def GetLastName(self):
        return "%s" % (self.LastName)

    FirstName = models.CharField(max_length = 50)
    def GetFirstName(self):
        return "%s" % (self.FirstName)

    Email = models.CharField(max_length = 50)
    def GetEmail(self):
        return "%s" % (self.Email)
        
    Password = models.CharField(max_length = 50)
    def GetPassword(self):
        return "%s" % (self.Password)

    AddressId = models.IntegerField()
    def GetAddressId(self):
        return "%s" % (self.AddressId)

#CLASS IMAGE
class Image(BaseObject):
    Path = models.CharField(max_length = 50)
    def GetPath(self):
        return "%s" % (self.Path)

#CLASS PRODUCT
class Product(BaseObject):
    Name = models.CharField(max_length = 50)
    def GetName(self):
        return "%s" % (self.Name)

    Description = models.CharField(max_length = 50)
    def GetDescription(self):
        return "%s" % (self.Description)
        
    Price = models.IntegerField()
    def GetPrice(self):
        return "%s" % (self.Price)

    Quantity = models.IntegerField()
    def GetQuantity(self):
        return "%s" % (self.Quantity)

    CategoryId = models.IntegerField()
    BrandId = models.IntegerField()
    AttributId = models.IntegerField()
    CharacteristicId = models.IntegerField()
    RetailerId = models.IntegerField()
    PromotionId = models.IntegerField()
    
    
    Images = models.ForeignKey(Image,on_delete=models.CASCADE)

#CLASS CART
class Cart(BaseObject):
    Client = models.ForeignKey(Client,on_delete=models.CASCADE)
    def GetClient(self):
        return "%s" % (self.Client)

    
    #À été vérifier avec Steve suposer marcher
    ProductId = models.ForeignKey(Product,on_delete=models.CASCADE)
    

#CLASS CATEGORY
class Category(BaseObject):
    Name = models.CharField(max_length = 50)
    def GetName(self):
        return "%s" % (self.Name)

    Description = models.CharField(max_length = 50)
    def GetDescription(self):
        return "%s" % (self.Description)

    ImagePath = models.CharField(max_length = 50)
    def GetImagePath(self):
        return "%s" % (self.ImagePath)

#CLASS CHARACTERISTIC
class Characteristic(BaseObject):
    Name = models.CharField(max_length = 50)
    def GetName(self):
        return "%s" % (self.Name)




#CLASS PROMOTION
class Promotion(BaseObject):
    Name = models.CharField(max_length = 50)
    def GetName(self):
        return "%s" % (self.Name)

    Discount = models.FloatField()
    def GetDiscount(self):
        return "%s" % (self.Discount)

#CLASS RETAILER
class Retailer(BaseObject):
    Name = models.CharField(max_length = 50)
    def GetName(self):
        return "%s" % (self.Name)

    Description = models.CharField(max_length = 50)
    def GetDescription(self):
        return "%s" % (self.Description)

#CLASS TRANSACTION
class Transaction(BaseObject):
    PaypalId = models.CharField(max_length = 50)
    def GetPaypalId(self):
        return "%s" % (self.PaypalId)

    CurrentState = models.CharField(max_length = 50)
    def GetCurrentState(self):
        return "%s" % (self.CurrentState)

    PaymentMethod = models.CharField(max_length = 50)
    def GetPaymentMethod(self):
        return "%s" % (self.PaymentMethod)

    ClientId = models.IntegerField()
    CarrierId = models.IntegerField()

#CLASS TRANSACTION PRODUCT
class TransactionProduct(BaseObject):
    Product = models.ForeignKey(Product,on_delete=models.CASCADE)
    def GetProduct(self):
        return "%s" % (self.Product)

    TransactionId = models.IntegerField()
    Price = models.FloatField()
    def GetPrice(self):
        return "%s" % (self.Price)

    Reduction = models.FloatField()
    def GetReduction(self):
        return "%s" % (self.Reduction)

#CLASS TYPEATTRIBUT
class TypeAttribut(BaseObject):
    Attribut = models.CharField(max_length = 50)
    def GetAttribut(self):
        return "%s" % (self.Attribut)

#CLASS VALEURATTRIBUT
class ValeurAttribut(BaseObject):
    Name = models.CharField(max_length = 50)
    def GetName(self):
        return "%s" % (self.Name)

    Type = models.ForeignKey(TypeAttribut,on_delete=models.CASCADE)
    def GetType(self):
        return "%s" % (self.Type)
    
