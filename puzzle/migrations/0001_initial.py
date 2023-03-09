# Generated by Django 3.0.3 on 2021-01-29 15:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='ibpsclerk',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('puzzle_hindi', models.TextField()),
                ('puzzle_eng', models.TextField()),
                ('solution_img', models.ImageField(null=True, upload_to='gallery/')),
                ('question_1', models.CharField(max_length=500)),
                ('question1_answer', models.CharField(max_length=200)),
                ('question1_option_1', models.CharField(max_length=200)),
                ('question1_option_2', models.CharField(max_length=200)),
                ('question1_option_3', models.CharField(max_length=200)),
                ('question1_option_4', models.CharField(max_length=200)),
                ('question_2', models.CharField(max_length=500)),
                ('question2_answer', models.CharField(max_length=200)),
                ('question2_option_1', models.CharField(max_length=200)),
                ('question2_option_2', models.CharField(max_length=200)),
                ('question2_option_3', models.CharField(max_length=200)),
                ('question2_option_4', models.CharField(max_length=200)),
                ('question_3', models.CharField(max_length=500)),
                ('question3_answer', models.CharField(max_length=200)),
                ('question3_option_1', models.CharField(max_length=200)),
                ('question3_option_2', models.CharField(max_length=200)),
                ('question3_option_3', models.CharField(max_length=200)),
                ('question3_option_4', models.CharField(max_length=200)),
                ('question_4', models.CharField(max_length=500)),
                ('question4_answer', models.CharField(max_length=200)),
                ('question4_option_1', models.CharField(max_length=200)),
                ('question4_option_2', models.CharField(max_length=200)),
                ('question4_option_3', models.CharField(max_length=200)),
                ('question4_option_4', models.CharField(max_length=200)),
                ('question_5', models.CharField(max_length=500)),
                ('question5_answer', models.CharField(max_length=200)),
                ('question5_option_1', models.CharField(max_length=200)),
                ('question5_option_2', models.CharField(max_length=200)),
                ('question5_option_3', models.CharField(max_length=200)),
                ('question5_option_4', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'ibpsclerk',
            },
        ),
        migrations.CreateModel(
            name='ibpsclerkmain',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('puzzle_hindi', models.TextField()),
                ('puzzle_eng', models.TextField()),
                ('solution_img', models.ImageField(null=True, upload_to='gallery/')),
                ('question_1', models.CharField(max_length=500)),
                ('question1_answer', models.CharField(max_length=200)),
                ('question1_option_1', models.CharField(max_length=200)),
                ('question1_option_2', models.CharField(max_length=200)),
                ('question1_option_3', models.CharField(max_length=200)),
                ('question1_option_4', models.CharField(max_length=200)),
                ('question_2', models.CharField(max_length=500)),
                ('question2_answer', models.CharField(max_length=200)),
                ('question2_option_1', models.CharField(max_length=200)),
                ('question2_option_2', models.CharField(max_length=200)),
                ('question2_option_3', models.CharField(max_length=200)),
                ('question2_option_4', models.CharField(max_length=200)),
                ('question_3', models.CharField(max_length=500)),
                ('question3_answer', models.CharField(max_length=200)),
                ('question3_option_1', models.CharField(max_length=200)),
                ('question3_option_2', models.CharField(max_length=200)),
                ('question3_option_3', models.CharField(max_length=200)),
                ('question3_option_4', models.CharField(max_length=200)),
                ('question_4', models.CharField(max_length=500)),
                ('question4_answer', models.CharField(max_length=200)),
                ('question4_option_1', models.CharField(max_length=200)),
                ('question4_option_2', models.CharField(max_length=200)),
                ('question4_option_3', models.CharField(max_length=200)),
                ('question4_option_4', models.CharField(max_length=200)),
                ('question_5', models.CharField(max_length=500)),
                ('question5_answer', models.CharField(max_length=200)),
                ('question5_option_1', models.CharField(max_length=200)),
                ('question5_option_2', models.CharField(max_length=200)),
                ('question5_option_3', models.CharField(max_length=200)),
                ('question5_option_4', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'ibpsclerkmain',
            },
        ),
        migrations.CreateModel(
            name='ibpspo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('puzzle_hindi', models.TextField()),
                ('puzzle_eng', models.TextField()),
                ('solution_img', models.ImageField(null=True, upload_to='gallery/')),
                ('question_1', models.CharField(max_length=500)),
                ('question1_answer', models.CharField(max_length=200)),
                ('question1_option_1', models.CharField(max_length=200)),
                ('question1_option_2', models.CharField(max_length=200)),
                ('question1_option_3', models.CharField(max_length=200)),
                ('question1_option_4', models.CharField(max_length=200)),
                ('question_2', models.CharField(max_length=500)),
                ('question2_answer', models.CharField(max_length=200)),
                ('question2_option_1', models.CharField(max_length=200)),
                ('question2_option_2', models.CharField(max_length=200)),
                ('question2_option_3', models.CharField(max_length=200)),
                ('question2_option_4', models.CharField(max_length=200)),
                ('question_3', models.CharField(max_length=500)),
                ('question3_answer', models.CharField(max_length=200)),
                ('question3_option_1', models.CharField(max_length=200)),
                ('question3_option_2', models.CharField(max_length=200)),
                ('question3_option_3', models.CharField(max_length=200)),
                ('question3_option_4', models.CharField(max_length=200)),
                ('question_4', models.CharField(max_length=500)),
                ('question4_answer', models.CharField(max_length=200)),
                ('question4_option_1', models.CharField(max_length=200)),
                ('question4_option_2', models.CharField(max_length=200)),
                ('question4_option_3', models.CharField(max_length=200)),
                ('question4_option_4', models.CharField(max_length=200)),
                ('question_5', models.CharField(max_length=500)),
                ('question5_answer', models.CharField(max_length=200)),
                ('question5_option_1', models.CharField(max_length=200)),
                ('question5_option_2', models.CharField(max_length=200)),
                ('question5_option_3', models.CharField(max_length=200)),
                ('question5_option_4', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'ibpspo',
            },
        ),
        migrations.CreateModel(
            name='ibpspomain',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('puzzle_hindi', models.TextField()),
                ('puzzle_eng', models.TextField()),
                ('solution_img', models.ImageField(null=True, upload_to='gallery/')),
                ('question_1', models.CharField(max_length=500)),
                ('question1_answer', models.CharField(max_length=200)),
                ('question1_option_1', models.CharField(max_length=200)),
                ('question1_option_2', models.CharField(max_length=200)),
                ('question1_option_3', models.CharField(max_length=200)),
                ('question1_option_4', models.CharField(max_length=200)),
                ('question_2', models.CharField(max_length=500)),
                ('question2_answer', models.CharField(max_length=200)),
                ('question2_option_1', models.CharField(max_length=200)),
                ('question2_option_2', models.CharField(max_length=200)),
                ('question2_option_3', models.CharField(max_length=200)),
                ('question2_option_4', models.CharField(max_length=200)),
                ('question_3', models.CharField(max_length=500)),
                ('question3_answer', models.CharField(max_length=200)),
                ('question3_option_1', models.CharField(max_length=200)),
                ('question3_option_2', models.CharField(max_length=200)),
                ('question3_option_3', models.CharField(max_length=200)),
                ('question3_option_4', models.CharField(max_length=200)),
                ('question_4', models.CharField(max_length=500)),
                ('question4_answer', models.CharField(max_length=200)),
                ('question4_option_1', models.CharField(max_length=200)),
                ('question4_option_2', models.CharField(max_length=200)),
                ('question4_option_3', models.CharField(max_length=200)),
                ('question4_option_4', models.CharField(max_length=200)),
                ('question_5', models.CharField(max_length=500)),
                ('question5_answer', models.CharField(max_length=200)),
                ('question5_option_1', models.CharField(max_length=200)),
                ('question5_option_2', models.CharField(max_length=200)),
                ('question5_option_3', models.CharField(max_length=200)),
                ('question5_option_4', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'ibpspomain',
            },
        ),
        migrations.CreateModel(
            name='product',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('puzzle_hindi', models.TextField()),
                ('puzzle_eng', models.TextField()),
                ('solution_img', models.ImageField(null=True, upload_to='gallery/')),
                ('question_1', models.CharField(max_length=500)),
                ('question1_answer', models.CharField(max_length=200)),
                ('question1_option_1', models.CharField(max_length=200)),
                ('question1_option_2', models.CharField(max_length=200)),
                ('question1_option_3', models.CharField(max_length=200)),
                ('question1_option_4', models.CharField(max_length=200)),
                ('question_2', models.CharField(max_length=500)),
                ('question2_answer', models.CharField(max_length=200)),
                ('question2_option_1', models.CharField(max_length=200)),
                ('question2_option_2', models.CharField(max_length=200)),
                ('question2_option_3', models.CharField(max_length=200)),
                ('question2_option_4', models.CharField(max_length=200)),
                ('question_3', models.CharField(max_length=500)),
                ('question3_answer', models.CharField(max_length=200)),
                ('question3_option_1', models.CharField(max_length=200)),
                ('question3_option_2', models.CharField(max_length=200)),
                ('question3_option_3', models.CharField(max_length=200)),
                ('question3_option_4', models.CharField(max_length=200)),
                ('question_4', models.CharField(max_length=500)),
                ('question4_answer', models.CharField(max_length=200)),
                ('question4_option_1', models.CharField(max_length=200)),
                ('question4_option_2', models.CharField(max_length=200)),
                ('question4_option_3', models.CharField(max_length=200)),
                ('question4_option_4', models.CharField(max_length=200)),
                ('question_5', models.CharField(max_length=500)),
                ('question5_answer', models.CharField(max_length=200)),
                ('question5_option_1', models.CharField(max_length=200)),
                ('question5_option_2', models.CharField(max_length=200)),
                ('question5_option_3', models.CharField(max_length=200)),
                ('question5_option_4', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'product',
            },
        ),
        migrations.CreateModel(
            name='rrbclerkmain',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('puzzle_hindi', models.TextField()),
                ('puzzle_eng', models.TextField()),
                ('solution_img', models.ImageField(null=True, upload_to='gallery/')),
                ('question_1', models.CharField(max_length=500)),
                ('question1_answer', models.CharField(max_length=200)),
                ('question1_option_1', models.CharField(max_length=200)),
                ('question1_option_2', models.CharField(max_length=200)),
                ('question1_option_3', models.CharField(max_length=200)),
                ('question1_option_4', models.CharField(max_length=200)),
                ('question_2', models.CharField(max_length=500)),
                ('question2_answer', models.CharField(max_length=200)),
                ('question2_option_1', models.CharField(max_length=200)),
                ('question2_option_2', models.CharField(max_length=200)),
                ('question2_option_3', models.CharField(max_length=200)),
                ('question2_option_4', models.CharField(max_length=200)),
                ('question_3', models.CharField(max_length=500)),
                ('question3_answer', models.CharField(max_length=200)),
                ('question3_option_1', models.CharField(max_length=200)),
                ('question3_option_2', models.CharField(max_length=200)),
                ('question3_option_3', models.CharField(max_length=200)),
                ('question3_option_4', models.CharField(max_length=200)),
                ('question_4', models.CharField(max_length=500)),
                ('question4_answer', models.CharField(max_length=200)),
                ('question4_option_1', models.CharField(max_length=200)),
                ('question4_option_2', models.CharField(max_length=200)),
                ('question4_option_3', models.CharField(max_length=200)),
                ('question4_option_4', models.CharField(max_length=200)),
                ('question_5', models.CharField(max_length=500)),
                ('question5_answer', models.CharField(max_length=200)),
                ('question5_option_1', models.CharField(max_length=200)),
                ('question5_option_2', models.CharField(max_length=200)),
                ('question5_option_3', models.CharField(max_length=200)),
                ('question5_option_4', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'rrbclerkmain',
            },
        ),
        migrations.CreateModel(
            name='rrbpo',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('puzzle_hindi', models.TextField()),
                ('puzzle_eng', models.TextField()),
                ('solution_img', models.ImageField(null=True, upload_to='gallery/')),
                ('question_1', models.CharField(max_length=500)),
                ('question1_answer', models.CharField(max_length=200)),
                ('question1_option_1', models.CharField(max_length=200)),
                ('question1_option_2', models.CharField(max_length=200)),
                ('question1_option_3', models.CharField(max_length=200)),
                ('question1_option_4', models.CharField(max_length=200)),
                ('question_2', models.CharField(max_length=500)),
                ('question2_answer', models.CharField(max_length=200)),
                ('question2_option_1', models.CharField(max_length=200)),
                ('question2_option_2', models.CharField(max_length=200)),
                ('question2_option_3', models.CharField(max_length=200)),
                ('question2_option_4', models.CharField(max_length=200)),
                ('question_3', models.CharField(max_length=500)),
                ('question3_answer', models.CharField(max_length=200)),
                ('question3_option_1', models.CharField(max_length=200)),
                ('question3_option_2', models.CharField(max_length=200)),
                ('question3_option_3', models.CharField(max_length=200)),
                ('question3_option_4', models.CharField(max_length=200)),
                ('question_4', models.CharField(max_length=500)),
                ('question4_answer', models.CharField(max_length=200)),
                ('question4_option_1', models.CharField(max_length=200)),
                ('question4_option_2', models.CharField(max_length=200)),
                ('question4_option_3', models.CharField(max_length=200)),
                ('question4_option_4', models.CharField(max_length=200)),
                ('question_5', models.CharField(max_length=500)),
                ('question5_answer', models.CharField(max_length=200)),
                ('question5_option_1', models.CharField(max_length=200)),
                ('question5_option_2', models.CharField(max_length=200)),
                ('question5_option_3', models.CharField(max_length=200)),
                ('question5_option_4', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'rrbpo',
            },
        ),
        migrations.CreateModel(
            name='rrbpomain',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('puzzle_hindi', models.TextField()),
                ('puzzle_eng', models.TextField()),
                ('solution_img', models.ImageField(null=True, upload_to='gallery/')),
                ('question_1', models.CharField(max_length=500)),
                ('question1_answer', models.CharField(max_length=200)),
                ('question1_option_1', models.CharField(max_length=200)),
                ('question1_option_2', models.CharField(max_length=200)),
                ('question1_option_3', models.CharField(max_length=200)),
                ('question1_option_4', models.CharField(max_length=200)),
                ('question_2', models.CharField(max_length=500)),
                ('question2_answer', models.CharField(max_length=200)),
                ('question2_option_1', models.CharField(max_length=200)),
                ('question2_option_2', models.CharField(max_length=200)),
                ('question2_option_3', models.CharField(max_length=200)),
                ('question2_option_4', models.CharField(max_length=200)),
                ('question_3', models.CharField(max_length=500)),
                ('question3_answer', models.CharField(max_length=200)),
                ('question3_option_1', models.CharField(max_length=200)),
                ('question3_option_2', models.CharField(max_length=200)),
                ('question3_option_3', models.CharField(max_length=200)),
                ('question3_option_4', models.CharField(max_length=200)),
                ('question_4', models.CharField(max_length=500)),
                ('question4_answer', models.CharField(max_length=200)),
                ('question4_option_1', models.CharField(max_length=200)),
                ('question4_option_2', models.CharField(max_length=200)),
                ('question4_option_3', models.CharField(max_length=200)),
                ('question4_option_4', models.CharField(max_length=200)),
                ('question_5', models.CharField(max_length=500)),
                ('question5_answer', models.CharField(max_length=200)),
                ('question5_option_1', models.CharField(max_length=200)),
                ('question5_option_2', models.CharField(max_length=200)),
                ('question5_option_3', models.CharField(max_length=200)),
                ('question5_option_4', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'rrbpomain',
            },
        ),
        migrations.CreateModel(
            name='sbiclerk',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('puzzle_hindi', models.TextField()),
                ('puzzle_eng', models.TextField()),
                ('solution_img', models.ImageField(null=True, upload_to='gallery/')),
                ('question_1', models.CharField(max_length=500)),
                ('question1_answer', models.CharField(max_length=200)),
                ('question1_option_1', models.CharField(max_length=200)),
                ('question1_option_2', models.CharField(max_length=200)),
                ('question1_option_3', models.CharField(max_length=200)),
                ('question1_option_4', models.CharField(max_length=200)),
                ('question_2', models.CharField(max_length=500)),
                ('question2_answer', models.CharField(max_length=200)),
                ('question2_option_1', models.CharField(max_length=200)),
                ('question2_option_2', models.CharField(max_length=200)),
                ('question2_option_3', models.CharField(max_length=200)),
                ('question2_option_4', models.CharField(max_length=200)),
                ('question_3', models.CharField(max_length=500)),
                ('question3_answer', models.CharField(max_length=200)),
                ('question3_option_1', models.CharField(max_length=200)),
                ('question3_option_2', models.CharField(max_length=200)),
                ('question3_option_3', models.CharField(max_length=200)),
                ('question3_option_4', models.CharField(max_length=200)),
                ('question_4', models.CharField(max_length=500)),
                ('question4_answer', models.CharField(max_length=200)),
                ('question4_option_1', models.CharField(max_length=200)),
                ('question4_option_2', models.CharField(max_length=200)),
                ('question4_option_3', models.CharField(max_length=200)),
                ('question4_option_4', models.CharField(max_length=200)),
                ('question_5', models.CharField(max_length=500)),
                ('question5_answer', models.CharField(max_length=200)),
                ('question5_option_1', models.CharField(max_length=200)),
                ('question5_option_2', models.CharField(max_length=200)),
                ('question5_option_3', models.CharField(max_length=200)),
                ('question5_option_4', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'sbiclerk',
            },
        ),
        migrations.CreateModel(
            name='sbiclerkmain',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('puzzle_hindi', models.TextField()),
                ('puzzle_eng', models.TextField()),
                ('solution_img', models.ImageField(null=True, upload_to='gallery/')),
                ('question_1', models.CharField(max_length=500)),
                ('question1_answer', models.CharField(max_length=200)),
                ('question1_option_1', models.CharField(max_length=200)),
                ('question1_option_2', models.CharField(max_length=200)),
                ('question1_option_3', models.CharField(max_length=200)),
                ('question1_option_4', models.CharField(max_length=200)),
                ('question_2', models.CharField(max_length=500)),
                ('question2_answer', models.CharField(max_length=200)),
                ('question2_option_1', models.CharField(max_length=200)),
                ('question2_option_2', models.CharField(max_length=200)),
                ('question2_option_3', models.CharField(max_length=200)),
                ('question2_option_4', models.CharField(max_length=200)),
                ('question_3', models.CharField(max_length=500)),
                ('question3_answer', models.CharField(max_length=200)),
                ('question3_option_1', models.CharField(max_length=200)),
                ('question3_option_2', models.CharField(max_length=200)),
                ('question3_option_3', models.CharField(max_length=200)),
                ('question3_option_4', models.CharField(max_length=200)),
                ('question_4', models.CharField(max_length=500)),
                ('question4_answer', models.CharField(max_length=200)),
                ('question4_option_1', models.CharField(max_length=200)),
                ('question4_option_2', models.CharField(max_length=200)),
                ('question4_option_3', models.CharField(max_length=200)),
                ('question4_option_4', models.CharField(max_length=200)),
                ('question_5', models.CharField(max_length=500)),
                ('question5_answer', models.CharField(max_length=200)),
                ('question5_option_1', models.CharField(max_length=200)),
                ('question5_option_2', models.CharField(max_length=200)),
                ('question5_option_3', models.CharField(max_length=200)),
                ('question5_option_4', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'sbiclerkmain',
            },
        ),
        migrations.CreateModel(
            name='sbipo',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('puzzle_hindi', models.TextField()),
                ('puzzle_eng', models.TextField()),
                ('solution_img', models.ImageField(null=True, upload_to='gallery/')),
                ('question_1', models.CharField(max_length=500)),
                ('question1_answer', models.CharField(max_length=200)),
                ('question1_option_1', models.CharField(max_length=200)),
                ('question1_option_2', models.CharField(max_length=200)),
                ('question1_option_3', models.CharField(max_length=200)),
                ('question1_option_4', models.CharField(max_length=200)),
                ('question_2', models.CharField(max_length=500)),
                ('question2_answer', models.CharField(max_length=200)),
                ('question2_option_1', models.CharField(max_length=200)),
                ('question2_option_2', models.CharField(max_length=200)),
                ('question2_option_3', models.CharField(max_length=200)),
                ('question2_option_4', models.CharField(max_length=200)),
                ('question_3', models.CharField(max_length=500)),
                ('question3_answer', models.CharField(max_length=200)),
                ('question3_option_1', models.CharField(max_length=200)),
                ('question3_option_2', models.CharField(max_length=200)),
                ('question3_option_3', models.CharField(max_length=200)),
                ('question3_option_4', models.CharField(max_length=200)),
                ('question_4', models.CharField(max_length=500)),
                ('question4_answer', models.CharField(max_length=200)),
                ('question4_option_1', models.CharField(max_length=200)),
                ('question4_option_2', models.CharField(max_length=200)),
                ('question4_option_3', models.CharField(max_length=200)),
                ('question4_option_4', models.CharField(max_length=200)),
                ('question_5', models.CharField(max_length=500)),
                ('question5_answer', models.CharField(max_length=200)),
                ('question5_option_1', models.CharField(max_length=200)),
                ('question5_option_2', models.CharField(max_length=200)),
                ('question5_option_3', models.CharField(max_length=200)),
                ('question5_option_4', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'sbipo',
            },
        ),
        migrations.CreateModel(
            name='sbipomain',
            fields=[
                ('id', models.AutoField(primary_key=True, serialize=False)),
                ('puzzle_hindi', models.TextField()),
                ('puzzle_eng', models.TextField()),
                ('solution_img', models.ImageField(null=True, upload_to='gallery/')),
                ('question_1', models.CharField(max_length=500)),
                ('question1_answer', models.CharField(max_length=200)),
                ('question1_option_1', models.CharField(max_length=200)),
                ('question1_option_2', models.CharField(max_length=200)),
                ('question1_option_3', models.CharField(max_length=200)),
                ('question1_option_4', models.CharField(max_length=200)),
                ('question_2', models.CharField(max_length=500)),
                ('question2_answer', models.CharField(max_length=200)),
                ('question2_option_1', models.CharField(max_length=200)),
                ('question2_option_2', models.CharField(max_length=200)),
                ('question2_option_3', models.CharField(max_length=200)),
                ('question2_option_4', models.CharField(max_length=200)),
                ('question_3', models.CharField(max_length=500)),
                ('question3_answer', models.CharField(max_length=200)),
                ('question3_option_1', models.CharField(max_length=200)),
                ('question3_option_2', models.CharField(max_length=200)),
                ('question3_option_3', models.CharField(max_length=200)),
                ('question3_option_4', models.CharField(max_length=200)),
                ('question_4', models.CharField(max_length=500)),
                ('question4_answer', models.CharField(max_length=200)),
                ('question4_option_1', models.CharField(max_length=200)),
                ('question4_option_2', models.CharField(max_length=200)),
                ('question4_option_3', models.CharField(max_length=200)),
                ('question4_option_4', models.CharField(max_length=200)),
                ('question_5', models.CharField(max_length=500)),
                ('question5_answer', models.CharField(max_length=200)),
                ('question5_option_1', models.CharField(max_length=200)),
                ('question5_option_2', models.CharField(max_length=200)),
                ('question5_option_3', models.CharField(max_length=200)),
                ('question5_option_4', models.CharField(max_length=200)),
            ],
            options={
                'db_table': 'sbipomain',
            },
        ),
    ]