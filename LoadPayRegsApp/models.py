from django.db import models

# Create your models here:
class DocFile(models.Model):
    docfile = models.FileField(verbose_name="Загрузка файла", null=True, blank=True)
    
    class Meta:
        verbose_name = "Загрузка файла"
        verbose_name_plural = "Загрузка файлов"
        #ordering = ['organization']
        
    def __str__(self):
        return str(self.docfile)
    
    
    
class TableAndUrlColumns(models.Model):
    #url = models.URLField(null=True, blank=True)
    docfile = models.ForeignKey('DocFile', on_delete=models.CASCADE, verbose_name="Ссылка", null=True, blank=True)
    organization = models.CharField(max_length=255, verbose_name="Организация", default="", blank=True)
    material_assigning = models.CharField(max_length=255, verbose_name="Назначение материала", default="", blank=True)
    account_purpose = models.CharField(max_length=255, verbose_name="Назначение счёта", default="", blank=True)
    contract_number = models.CharField(max_length=255, verbose_name="№ договора", default="", blank=True)
    contract_amount = models.DecimalField(max_digits=14, decimal_places=2, verbose_name="Сумма по договору", null=True, blank=True)
    paid1 = models.DecimalField(max_digits=14, decimal_places=2, verbose_name="Оплачено", null=True, blank=True)
    account_number = models.CharField(max_length=255, verbose_name="№ счёта", default="", blank=True)
    account_date = models.DateField(verbose_name="Дата счёта", null=True, blank=True)
    accounts_amount = models.DecimalField(max_digits=14, decimal_places=2, verbose_name="Сумма по счётам", null=True, blank=True)
    for_payment = models.DecimalField(max_digits=14, decimal_places=2, verbose_name="В оплату", null=True, blank=True)
    payment_balance = models.DecimalField(max_digits=14, decimal_places=2, verbose_name="Остаток по оплате", null=True, blank=True)
    paid2 = models.DecimalField(max_digits=14, decimal_places=2, verbose_name="Оплачено", null=True, blank=True)
    remainder = models.DecimalField(max_digits=14, decimal_places=2, verbose_name="Остаток", null=True, blank=True)
    note = models.CharField(max_length=255, verbose_name="Примечание", default="", blank=True)
    total = models.DecimalField(max_digits=14, decimal_places=2, verbose_name="Сумма-1", null=True, blank=True)
    #result_sum1 = TableColumns.objects.aggregate(Sum('accounts_amount'))
    #result_sum2 = TableColumns.objects.aggregate(Sum('payment_balance'))
    
    class Meta:
        verbose_name = "Запись с реестра"
        verbose_name_plural = "Записи с реестра"
        ordering = ['organization']
        
    def __str__(self):
        return self.organization
        
    # ====== Пример для корректировки: ======
    #def save(self, *args, **kwargs):
        #if not self.slug:
            #self.slug = from_cyrillic_to_eng(str(self.name))
        #super().save(*args, **kwargs)