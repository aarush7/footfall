# Generated by Django 2.2.5 on 2019-11-07 16:19

from django.db import migrations, models
import django.db.models.deletion
import phone_field.models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='bb',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('framecount', models.CharField(max_length=40)),
                ('startx', models.CharField(max_length=40)),
                ('starty', models.CharField(max_length=40)),
                ('endx', models.CharField(max_length=40)),
                ('endy', models.CharField(max_length=40)),
                ('in_time', models.DateTimeField(verbose_name='in timing')),
            ],
        ),
        migrations.CreateModel(
            name='camera',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('last_modification_time', models.DateTimeField(auto_now=True)),
                ('cuuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('model', models.CharField(blank=True, max_length=100)),
                ('location', models.CharField(blank=True, max_length=100)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='candidate',
            fields=[
                ('cauuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=100)),
                ('sex', models.CharField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE'), ('OTHERS', 'OTHERS')], max_length=10)),
                ('age', models.IntegerField()),
                ('height', models.IntegerField()),
                ('skintone', models.CharField(choices=[('UNDERTONE', 'UNDERTONE'), ('COOLTONE', 'COOLTONE'), ('WARMTONE', 'WARMTONE'), ('OTHERS', 'OTHERS')], max_length=40)),
                ('clothing', models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='summary',
            fields=[
                ('smuuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('total_in', models.IntegerField()),
                ('total_out', models.IntegerField()),
                ('peak', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='tenant',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('last_modification_time', models.DateTimeField(auto_now=True)),
                ('tuuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='store',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('last_modification_time', models.DateTimeField(auto_now=True)),
                ('suuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('map_id', models.CharField(max_length=100)),
                ('address', models.CharField(max_length=200)),
                ('start_time', models.DateTimeField(max_length=50)),
                ('end_time', models.DateTimeField(max_length=50)),
                ('category', models.CharField(choices=[('GROCERY', 'GROCERIES'), ('MEDICAL', 'MEDICINE'), ('APPARELS', 'APPARELS'), ('ELECTRONICS', 'ELECTRONICS'), ('WHOLESALE', 'WHOLESALE'), ('SUPERMARKET', 'SUPERMARKET'), ('AUTOMOBILE', 'AUTOMOBILE'), ('ENTERTAINMENT AND ARTS', 'ENTERTAINMENT AND ARTS'), ('HEALTH AND BEAUTY', 'HEALTH AND BEAUTY'), ('FOOD', 'FOOD'), ('TRAVEL', 'TRAVEL'), ('SPORTS', 'SPORTS')], max_length=50)),
                ('contact_id', phone_field.models.PhoneField(help_text='Contact phone number', max_length=50)),
                ('tuuid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foot.tenant')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='staff',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('last_modification_time', models.DateTimeField(auto_now=True)),
                ('stuuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('contact_number', phone_field.models.PhoneField(help_text='Contact phone number', max_length=50)),
                ('sex', models.CharField(choices=[('MALE', 'MALE'), ('FEMALE', 'FEMALE'), ('OTHERS', 'OTHERS')], max_length=10)),
                ('age', models.IntegerField()),
                ('designation', models.CharField(choices=[('MANAGER', 'MANAGER'), ('ASSISTANT MANAGER', 'ASSISTANT MANAGER'), ('CASHIER', 'CASHIER'), ('CUSTOMER SERVICE REPRESENTATIVE', 'CUSTOMER SERVICE REPRESENTATIVE'), ('TRAINEE', 'TRAINEE'), ('SECURITY', 'SECURITY'), ('CLEANING', 'CLEANING')], max_length=50)),
                ('suuid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='staff_suuid', to='foot.store')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='eventpool',
            fields=[
                ('name', models.CharField(max_length=100)),
                ('creation_time', models.DateTimeField(auto_now_add=True)),
                ('last_modification_time', models.DateTimeField(auto_now=True)),
                ('euuid', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('start_time', models.DateTimeField(max_length=50)),
                ('end_time', models.DateTimeField(max_length=50)),
                ('type', models.CharField(choices=[('IN', 'IN'), ('OUT', 'OUT'), ('STANDING', 'STANDING'), ('OTHERS', 'OTHERS')], max_length=40)),
                ('event_time', models.DateTimeField(max_length=50)),
                ('kind', models.CharField(default='eventpool', max_length=30)),
                ('cauuid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='eventpool_cauuid', to='foot.candidate')),
                ('cuuid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='eventpool_cuuid', to='foot.camera')),
                ('tuuid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='foot.tenant')),
            ],
            options={
                'abstract': False,
            },
        ),
        migrations.AddField(
            model_name='candidate',
            name='suuid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='candidate_suuid', to='foot.store'),
        ),
        migrations.AddField(
            model_name='camera',
            name='suuid',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='camera_suuid', to='foot.store'),
        ),
    ]