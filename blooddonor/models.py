from email.policy import default
from django.db import models


class BloodDonorProfile(models.Model):
    # Personal info
    firstName = models.CharField(max_length=25, blank=False)
    lastName = models.CharField(max_length=25, blank=False)
    age = models.IntegerField(blank=False)
    email = models.EmailField(max_length=50, blank=False)
    password = models.CharField(max_length=250, blank=False)

    # Additional
    image = models.ImageField(upload_to='profile_pics',
                              default='default.jpg', blank=True, null=True)
    bg = [
        ('A+', 'A+'), ('A-',  'A-'), ('B+',  'B+'), ('B-',  'B-'), ('AB+', 'AB+'),
        ('AB-',  'AB-'), ('O+',  'O+'), ('O-',  'O-')
    ]
    bloodGroup = models.CharField(max_length=5, choices=bg, blank=False)
    bd_district = [
        ('Dhaka', 'Dhaka'), ('Faridpur', 'Faridpur'), ('Gazipur', 'Gazipur'),
        ('Gopalganj', 'Gopalganj'), ('Jamalpur', 'Jamalpur'),
        ('Kishoreganj', 'Kishoreganj'), ('Madaripur', 'Madaripur'),
        ('Manikganj', 'Manikganj'), ('Munshiganj', 'Munshiganj'),
        ('Mymensingh', 'Mymensingh'), ('Narayanganj', 'Narayanganj'),
        ('Narsingdi', 'Narsingdi'), ('Netrokona', 'Netrokona'),
        ('Rajbari', 'Rajbari'), ('Shariatpur', 'Shariatpur'),
        ('Sherpur', 'Sherpur'), ('Tangail', 'Tangail'), ('Bogra', 'Bogra'),
        ('Joypurhat', 'Joypurhat'), ('Naogaon', 'Naogaon'), ('Natore', 'Natore'),
        ('Nawabganj', 'Nawabganj'), ('Pabna', 'Pabna'), ('Rajshahi', 'Rajshahi'),
        ('Sirajgonj', 'Sirajgonj'), ('Dinajpur',
                                     'Dinajpur'), ('Gaibandha', 'Gaibandha'),
        ('Kurigram', 'Kurigram'), ('Lalmonirhat', 'Lalmonirhat'),
        ('Nilphamari', 'Lalmonirhat'), ('Panchagarh',
                                        'Panchagarh'), ('Rangpur', 'Rangpur'),
        ('Thakurgaon', 'Thakurgaon'), ('Barguna',
                                       'Barguna'), ('Barisal', 'Barisal'),
        ('Bhola', 'Bhola'), ('Jhalokati', 'Jhalokati'), ('Patuakhali', 'Patuakhali'),
        ('Pirojpur', 'Pirojpur'), ('Bandarban',
                                   'Bandarban'), ('Brahmanbaria', 'Brahmanbaria'),
        ('Chandpur', 'Chandpur'), ('Chittagong',
                                   'Chittagong'), ('Comilla', 'Comilla'),
        ('Cox''s Bazar', 'Cox''s Bazar'), ('Feni',
                                           'Feni'), ('Khagrachari', 'Khagrachari'),
        ('Lakshmipur', 'Lakshmipur'), ('Noakhali',
                                       'Noakhali'), ('Rangamati', 'Rangamati'),
        ('Habiganj', 'Habiganj'), ('Maulvibazar',
                                   'Maulvibazar'), ('Sunamganj', 'Sunamganj'),
        ('Sylhet', 'Sylhet'), ('Bagerhat', 'Bagerhat'), ('Chuadanga', 'Bagerhat'),
        ('Jessore', 'Jessore'), ('Jhenaidah',
                                 'Jhenaidah'), ('Khulna', 'Khulna'), ('Kushtia', 'Kushtia'),
        ('Magura', 'Magura'), ('Meherpur', 'Meherpur'), ('Narail',
                                                         'Narail'), ('Satkhira', 'Satkhira')
    ]
    BDDistrict = models.CharField(
        max_length=15, choices=bd_district, blank=False)
    mobileNumber = models.IntegerField(blank=False)
    donor_status = [
        ('Available', 'Available'), ('Unavailable', 'Unavailable')
    ]
    donorStatus = models.CharField(
        max_length=15, choices=donor_status, blank=False)

    def __str__(self):
        return self.firstName
