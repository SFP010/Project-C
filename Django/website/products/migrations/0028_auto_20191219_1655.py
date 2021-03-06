# Generated by Django 3.0 on 2019-12-19 15:55

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('products', '0027_auto_20191211_2028'),
    ]

    operations = [
        migrations.CreateModel(
            name='DesignArtCoordinate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coordinate_left', models.DecimalField(decimal_places=3, default=10, max_digits=10)),
                ('coordinate_top', models.DecimalField(decimal_places=3, default=10, max_digits=10)),
                ('height', models.DecimalField(decimal_places=3, default=300, max_digits=10)),
                ('width', models.DecimalField(decimal_places=3, default=300, max_digits=10)),
            ],
        ),
        migrations.CreateModel(
            name='DesignArtFrameCoordinate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('frame_height', models.DecimalField(decimal_places=3, default=300, max_digits=10)),
                ('frame_width', models.DecimalField(decimal_places=3, default=300, max_digits=10)),
                ('frame_coordinate_left', models.DecimalField(decimal_places=3, default=10, max_digits=10)),
                ('frame_coordinate_top', models.DecimalField(decimal_places=3, default=10, max_digits=10)),
                ('frame_border_radius', models.IntegerField(default=0)),
                ('rotation', models.CharField(default='matrix(1, 0, 0, 1, 0, 0)', max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name='DesignTextCoordinate',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('coordinate_left', models.DecimalField(decimal_places=3, default=300, max_digits=10)),
                ('coordinate_top', models.DecimalField(decimal_places=3, default=300, max_digits=10)),
                ('font', models.CharField(max_length=60)),
                ('font_weight', models.CharField(max_length=60)),
                ('font_style', models.CharField(max_length=60)),
                ('font_color', models.CharField(max_length=60)),
            ],
        ),
        migrations.RemoveField(
            model_name='design',
            name='coordinate_left',
        ),
        migrations.RemoveField(
            model_name='design',
            name='coordinate_top',
        ),
        migrations.RemoveField(
            model_name='design',
            name='frame_border_radius',
        ),
        migrations.RemoveField(
            model_name='design',
            name='frame_coordinate_left',
        ),
        migrations.RemoveField(
            model_name='design',
            name='frame_coordinate_top',
        ),
        migrations.RemoveField(
            model_name='design',
            name='frame_height',
        ),
        migrations.RemoveField(
            model_name='design',
            name='frame_width',
        ),
        migrations.RemoveField(
            model_name='design',
            name='height',
        ),
        migrations.RemoveField(
            model_name='design',
            name='rotation',
        ),
        migrations.RemoveField(
            model_name='design',
            name='width',
        ),
        migrations.AddField(
            model_name='design',
            name='DesignArtCoordinate',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.DesignArtCoordinate'),
        ),
        migrations.AddField(
            model_name='design',
            name='DesignArtFrameCoordinate',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.DesignArtFrameCoordinate'),
        ),
        migrations.AddField(
            model_name='design',
            name='DesignTextCoordinate',
            field=models.ForeignKey(blank=True, default=None, null=True, on_delete=django.db.models.deletion.CASCADE, to='products.DesignTextCoordinate'),
        ),
    ]
