# Generated by Django 3.2.8 on 2022-01-19 11:38

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='BloodDonorProfile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('firstName', models.CharField(max_length=25)),
                ('lastName', models.CharField(max_length=25)),
                ('age', models.IntegerField()),
                ('email', models.EmailField(max_length=50)),
                ('pasword', models.CharField(max_length=250)),
                ('image', models.ImageField(blank=True, default='default.jpg', null=True, upload_to='profile_pics')),
                ('bloodGroup', models.CharField(choices=[('A+', 'A+'), ('A-', 'A-'), ('B+', 'B+'), ('B-', 'B-'), ('AB+', 'AB+'), ('AB-', 'AB-'), ('O+', 'O+'), ('O-', 'O-')], max_length=5)),
                ('BDDistrict', models.CharField(choices=[('Dhaka', 'Dhaka'), ('Faridpur', 'Faridpur'), ('Gazipur', 'Gazipur'), ('Gopalganj', 'Gopalganj'), ('Jamalpur', 'Jamalpur'), ('Kishoreganj', 'Kishoreganj'), ('Madaripur', 'Madaripur'), ('Manikganj', 'Manikganj'), ('Munshiganj', 'Munshiganj'), ('Mymensingh', 'Mymensingh'), ('Narayanganj', 'Narayanganj'), ('Narsingdi', 'Narsingdi'), ('Netrokona', 'Netrokona'), ('Rajbari', 'Rajbari'), ('Shariatpur', 'Shariatpur'), ('Sherpur', 'Sherpur'), ('Tangail', 'Tangail'), ('Bogra', 'Bogra'), ('Joypurhat', 'Joypurhat'), ('Naogaon', 'Naogaon'), ('Natore', 'Natore'), ('Nawabganj', 'Nawabganj'), ('Pabna', 'Pabna'), ('Rajshahi', 'Rajshahi'), ('Sirajgonj', 'Sirajgonj'), ('Dinajpur', 'Dinajpur'), ('Gaibandha', 'Gaibandha'), ('Kurigram', 'Kurigram'), ('Lalmonirhat', 'Lalmonirhat'), ('Nilphamari', 'Lalmonirhat'), ('Panchagarh', 'Panchagarh'), ('Rangpur', 'Rangpur'), ('Thakurgaon', 'Thakurgaon'), ('Barguna', 'Barguna'), ('Barisal', 'Barisal'), ('Bhola', 'Bhola'), ('Jhalokati', 'Jhalokati'), ('Patuakhali', 'Patuakhali'), ('Pirojpur', 'Pirojpur'), ('Bandarban', 'Bandarban'), ('Brahmanbaria', 'Brahmanbaria'), ('Chandpur', 'Chandpur'), ('Chittagong', 'Chittagong'), ('Comilla', 'Comilla'), ('Coxs Bazar', 'Coxs Bazar'), ('Feni', 'Feni'), ('Khagrachari', 'Khagrachari'), ('Lakshmipur', 'Lakshmipur'), ('Noakhali', 'Noakhali'), ('Rangamati', 'Rangamati'), ('Habiganj', 'Habiganj'), ('Maulvibazar', 'Maulvibazar'), ('Sunamganj', 'Sunamganj'), ('Sylhet', 'Sylhet'), ('Bagerhat', 'Bagerhat'), ('Chuadanga', 'Bagerhat'), ('Jessore', 'Jessore'), ('Jhenaidah', 'Jhenaidah'), ('Khulna', 'Khulna'), ('Kushtia', 'Kushtia'), ('Magura', 'Magura'), ('Meherpur', 'Meherpur'), ('Narail', 'Narail'), ('Satkhira', 'Satkhira')], max_length=15)),
                ('mobileNumber', models.IntegerField()),
                ('donorStatus', models.CharField(choices=[('Available', 'Available'), ('Unavailable', 'Unavailable')], max_length=15)),
            ],
        ),
    ]
