# База данных обхода квартир

В базе данных реализованы модели: инспектора (Inspector), обхода (Bypass), квартиры (Flat), плательщик (Renter), здания (House) и адресса (Address)

## Модель Renter

    class Renter(models.Model):
    idRenter = models.IntegerField(primary_key=True)
    passport = models.CharField("Person's passport", max_length=12)
    privilege = models.FloatField("Person's privilege")
    firstName = models.CharField("First name", max_length=20)
    surname = models.CharField("Surname", max_length=20)
    patronymic = models.CharField("Patronymic", max_length=20)

    class Meta:
        ordering = ['idRenter']


* `idRenter` - Идентификатор плательщика
* `passport` - Серия и номер паспорта
* `firstName` - Имя плательщика
* `surname` - Фамилия плательщика
* `patronymic` - Отчество плательщика


        class Meta:
            ordering = ['idRenter']

В данном фрагменте кода происходит сортировка по полю `idRenter`


## Модель Adress

    class Adress(models.Model):
    idAdress = models.IntegerField(primary_key=True)
    district = models.CharField("District", max_length=20)
    street = models.CharField("Street", max_length=20)

    class Meta:
        ordering = ['idAdress']


* `idAdress` - Идентификатор адреса
* `district` - Район
* `street` - Улица


## Модель House

    class House(models.Model):
    idAdress = models.ForeignKey(Adress, on_delete=models.CASCADE)
    idBuilding = models.IntegerField(primary_key=True)
    buildingNumb = models.IntegerField("Number of building")
    building = models.IntegerField("Corps")

    class Meta:
        ordering = ['idBuilding']


* `idAdress` - Идентификатор адреса
* `idBuilding` - Идентификатор здания
* `buildingNumb` - Номер дома
* `building` - Корпус дома


## Модель Inspector

Данная модель используется для создания пользователей, наследуясь от класса `AbstractUser`

    class Inspector(AbstractUser):
    servNumb = models.IntegerField("Service number", primary_key=True)
    phone = models.CharField("Phone number", max_length=12)
    first_name = models.CharField("First name", max_length=20)
    last_name = models.CharField("Surname", max_length=20)
    patronymic = models.CharField("Patronymic", max_length=20)
    is_staff = models.BooleanField(default=True)

    class Meta:
        ordering = ['servNumb']


* `servNumb` - Табельный номер инспектора
* `phone` - Номер телефон инспектора
* `first_name` - Имя инспектора
* `last_name` - Фамилия инспектора
* `patronymic` - Отчество инспектора
* `is_staff` - Поле, наследуемое из класса `AbstractUser` и обозначающее то, является ли пользователь сотрудником. 

    Данное поле не учавствует на этапе регистрации, вместо этого на этапе регистрации, данное поле принимает значение `True` - `Является работником`. В дальнейшем поле может изминять пользователь с правами`superuser`


## Модель Flat

    class Flat(models.Model):
    idFlat = models.IntegerField(primary_key=True)
    flat = models.IntegerField("Flat")
    flatType = models.CharField("Flat type", max_length=30)
    eStove1 = 'Is present'
    eStove2 = 'Isn\'t present'
    eStoveChoices = (
        (eStove1, "Is present"),
        (eStove2, "Isn't present")
    )
    eStove = models.CharField("Availability of electric stove", max_length=13, choices=eStoveChoices, default=eStove2)
    peopleCount = models.IntegerField("People count")
    house = models.ForeignKey(House, on_delete=models.CASCADE)
    renter = models.ForeignKey(Renter, on_delete=models.CASCADE)

    class Meta:
        ordering = ['idFlat']

* `idFlat` - Идентификатор квартиры
* `flat` - Номер квартиры
* `eStove` - Наличие электрической плиты в квартире
* `peopleCount` - Количество жильцов
* `house` - Дом, в котором расположена квартира
* `renter` - Плательщик

    В данной модели используется выбор из списка значений

        eStove1 = 'Is present'
        eStove2 = 'Isn\'t present'
        eStoveChoices = (
            (eStove1, "Is present"),
            (eStove2, "Isn't present")
        )
        eStove = models.CharField("Availability of electric stove", max_length=13, choices=eStoveChoices, default=eStove2)


## Модель Bypass

    class Bypass(models.Model):
    bypassNumb = models.IntegerField("Bypass number", primary_key=True)
    dateOfBypass = models.DateField("Bypass date")
    status1 = 'completed'
    status2 = 'uncompleted'
    statusChoices = (
        (status1, 'completed'),
        (status2, 'uncompleted')
    )
    status = models.CharField("Bypass status", max_length=11, choices=statusChoices, default=status2)
    comment = models.CharField("Comment", max_length=100, blank=True)
    inspectorServNumb = models.ForeignKey(Inspector, on_delete=models.CASCADE)
    flat = models.ForeignKey(Flat, on_delete=models.CASCADE)

    class Meta:
        ordering = ['bypassNumb']

* `bypassNumb` - Табельный номер обхода
* `dateOfBypass` - Дата обхода
* `status` - Статус обхода
* `comment` - Комментарий
* `inspectorServNumb` - Табельный номер инспектора
* `flat` - Квартира