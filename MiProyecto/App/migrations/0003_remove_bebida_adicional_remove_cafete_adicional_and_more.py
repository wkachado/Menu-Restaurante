# Generated by Django 5.1.1 on 2024-10-17 23:32

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('App', '0002_adicional_bebida_adicional_cafete_adicional_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='bebida',
            name='adicional',
        ),
        migrations.RemoveField(
            model_name='cafete',
            name='adicional',
        ),
        migrations.RemoveField(
            model_name='comida',
            name='adicional',
        ),
        migrations.RemoveField(
            model_name='guarnicion',
            name='adicional',
        ),
        migrations.RemoveField(
            model_name='postre',
            name='adicional',
        ),
        migrations.AddField(
            model_name='pedido',
            name='adicional_bebida',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='adicionales_bebida', to='App.adicional'),
        ),
        migrations.AddField(
            model_name='pedido',
            name='adicional_cafe_te',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='adicionales_cafe_te', to='App.adicional'),
        ),
        migrations.AddField(
            model_name='pedido',
            name='adicional_guarnicion',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='adicionales_guarnicion', to='App.adicional'),
        ),
        migrations.AddField(
            model_name='pedido',
            name='adicional_plato_principal',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='adicionales_plato', to='App.adicional'),
        ),
        migrations.AddField(
            model_name='pedido',
            name='adicional_postre',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='adicionales_postre', to='App.adicional'),
        ),
    ]