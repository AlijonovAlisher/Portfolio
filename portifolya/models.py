from django.db import models
from django.core.exceptions import ValidationError
from django.core.validators import RegexValidator
import re
from django.core.validators import MaxValueValidator, MinValueValidator

class SendMessage(models.Model):
    name = models.CharField(max_length=120)
    email = models.EmailField()
    subject = models.CharField(max_length=255)
    message = models.TextField()

    def __str__(self):
        return f'{self.name}, {self.subject}'




def validate_url(value):

    regex = re.compile(
        r'^(http|https)://' 
        r'(?:(?:[A-Z0-9](?:[A-Z0-9-]{0,61}[A-Z0-9])?\.)+(?:[A-Z]{2,6}\.?|[A-Z0-9-]{2,}\.?)|'  # Domain nomi
        r'localhost|'  # localhost
        r'\d{1,3}\.\d{1,3}\.\d{1,3}\.\d{1,3}|'  # IPv4
        r'\[?[A-F0-9]*:[A-F0-9:]+\]?)'  # IPv6
        r'(?::\d+)?'  # Port
        r'(?:/?|[/?]\S+)$', re.IGNORECASE)  # Yo'l

    if not regex.match(value):
        raise ValidationError('Noto‘g‘ri URL formati')  # Ushbu koddagi URL formati noto'g'ri

class About(models.Model):

        facebook = models.CharField(
            max_length=200,  # Talablariga mos keladigan maksimal uzunlikni belgilang
            validators=[validate_url],  # Bo'sh qoldirish uchun blank=True sozini qo'shing
            blank=True,  # Ilovalama field bo'sh qoldirilishi mumkin
            null=True,  # Ma'lumotlar bazasida bo'sh qiymat qo'yilishi mumkin
            verbose_name='Facebook manzilingizni keriting',
            # Adm   in panelda mallumotlarni kergizayotgan vaqtingizda verbose_name ga quyilgan str malumotni quyadi yani colomnni nomi emas balki verbose_name ga quyilgan malumoy chiqadi
        )
        telegram = models.CharField(
            max_length=200,  # Talablariga mos keladigan maksimal uzunlikni belgilang
            validators=[validate_url],  # Bo'sh qoldirish uchun blank=True sozini qo'shing
            blank=True,  # Ilovalama field bo'sh qoldirilishi mumkin
            null=True,  # Ma'lumotlar bazasida bo'sh qiymat qo'yilishi mumkin
            verbose_name='Telegram manzilingizni keriting',
            # Admin panelda mallumotlarni kergizayotgan vaqtingizda verbose_name ga quyilgan str malumotni quyadi yani colomnni nomi emas balki verbose_name ga quyilgan malumoy chiqadi
        )
        instagram = models.CharField(
            max_length=200,  # Talablariga mos keladigan maksimal uzunlikni belgilang
            validators=[validate_url],  # Bo'sh qoldirish uchun blank=True sozini qo'shing
            blank=True,  # Ilovalama field bo'sh qoldirilishi mumkin
            null=True,  # Ma'lumotlar bazasida bo'sh qiymat qo'yilishi mumkin
            verbose_name='Instagram manzilingizni keriting',
            # Admin panelda mallumotlarni kergizayotgan vaqtingizda verbose_name ga quyilgan str malumotni quyadi yani colomnni nomi emas balki verbose_name ga quyilgan malumoy chiqadi
        )


        class Meta:
            verbose_name = 'About'
            verbose_name_plural = 'Abouts'



class contact(models.Model):
    location = models.CharField(
        max_length=100,
        null=True,
        blank=True,
        verbose_name='Manzilingizni kiriting: ',
        unique=True,
    )

    phone_number = models.CharField(
        unique=True,
        max_length=20,
        validators=[
            RegexValidator(
                regex=r'^\+?998\d{9}$',
                # Telefon raqami formatini moslashtiring: +998 yoki 998 bilan boshlanishi va keyin 9 ta raqam kelsin
                message='To\'g\'ri telefon raqamini kiriting.'  # Xabarni o'zgartiring
            ),
        ],
        blank=True,  # Maydonni bo'sh qoldirish uchun blank=True sozini qo'shing
        null=True,  # Ma'lumotlar bazasida bo'sh qiymat qo'yilishi mumkin
        verbose_name='Telefon raqamingizni keriting',
        # Admin panelda mallumotlarni kergizayotgan vaqtingizda verbose_name ga quyilgan str malumotni quyadi yani colomnni nomi emas balki verbose_name ga quyilgan malumoy chiqadi
    )

    email = models.EmailField(
        unique=True,
        verbose_name='Email manzilingizni kiriting',
        null=True,
        blank=True,
        max_length=70,
    )

    website = models.URLField(
        verbose_name='Website manzilingizni kiriting',
        null=True,
        blank=True,
    )

    def __str__(self):
        return f'Location: {self.location}\nEmail: {self.email}\nWebsite: {self.website}'
    class Meta:
        verbose_name = 'Contact'
        verbose_name_plural = 'Contacts'
        ordering = ('location', 'email', 'website')


class service(models.Model):
    location = models.CharField(max_length=120)
    phone_number = models.CharField(max_length=120)
    email = models.CharField(max_length=120)



    class Meta:
        verbose_name_plural = 'Services'
        ordering = ('location', 'email', 'phone_number')

class follower(models.Model):
    awards = models.BigIntegerField(
        null=True,
        blank=True,
    )
    projects = models.BigIntegerField(
        null=True,
        blank=True,
    )
    customers = models.BigIntegerField(
        null=True,
        blank=True,
    )
    coffee = models.BigIntegerField(
        null=True,
        blank=True,
    )




class skill(models.Model):
    skill_name = models.CharField(max_length=120, unique=True, verbose_name='Skill')
    skill_foiz = models.PositiveSmallIntegerField(
        default=0,
        validators=[MinValueValidator(1, message="1 dan katta kiriting"), MaxValueValidator(100, message="100 dan kichik kiriting")]
    )

    def str(self):
        return self.skill_name

    class Meta:
        verbose_name = 'Skill'
        verbose_name_plural = 'Skills'
        ordering = ['skill_name']



class About_Me(models.Model):
    full_name = models.CharField(max_length=50, verbose_name="To'liq ismingizni kiriting : ")
    date_of_birth = models.DateField()
    address = models.CharField(
        max_length=100, verbose_name="Manzilni kiriting : ",
        null=True,
        blank=True,
    )
    email = models.EmailField(
        unique=True,
        verbose_name='Email manzilingizni kiriting',
        null=True,
        blank=True,
        max_length=70,
    )
    phone_number = models.CharField(
        unique=True,
        max_length=20,
        validators=[
            RegexValidator(
                regex=r'^\+?998\d{9}$',
                # Telefon raqami formatini moslashtiring: +998 yoki 998 bilan boshlanishi va keyin 9 ta raqam kelsin
                message='To\'g\'ri telefon raqamini kiriting.'  # Xabarni o'zgartiring
            ),
        ],
        blank=True,  # Maydonni bo'sh qoldirish uchun blank=True sozini qo'shing
        null=True,  # Ma'lumotlar bazasida bo'sh qiymat qo'yilishi mumkin
        verbose_name='Telefon raqamingizni keriting',
        # Admin panelda mallumotlarni kergizayotgan vaqtingizda verbose_name ga quyilgan str malumotni quyadi yani colomnni nomi emas balki verbose_name ga quyilgan malumoy chiqadi
    )




    def __str__(self):
        return self.full_name





class Resume(models.Model):
    since = models.CharField(max_length=10, unique=True, verbose_name='yilni kiriting masalan(2014-2015)')
    title = models.CharField(
        max_length=50,
        unique=True,
        verbose_name='sarlavhani kiriting'
    )
    where = models.CharField(
        max_length=30,
        unique=True,
        verbose_name='Qayerdaligini kiriting'

    )
    description = models.TextField(
        max_length=300,
        verbose_name='Izoh yozing'

    )


    def __str__(self):
        return self.title
























