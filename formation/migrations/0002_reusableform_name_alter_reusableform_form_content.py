# Generated by Django 4.1.6 on 2023-02-20 15:30

from django.db import migrations, models
import wagtail.blocks
import wagtail.fields


class Migration(migrations.Migration):

    dependencies = [
        ('formation', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='reusableform',
            name='name',
            field=models.CharField(default='', max_length=200),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='reusableform',
            name='form_content',
            field=wagtail.fields.StreamField([('elaborate', wagtail.blocks.StructBlock([('form_name', wagtail.blocks.CharBlock()), ('fields', wagtail.blocks.StreamBlock([('text', wagtail.blocks.StructBlock([('name', wagtail.blocks.CharBlock()), ('label', wagtail.blocks.CharBlock())])), ('integer', wagtail.blocks.StructBlock([('name', wagtail.blocks.CharBlock()), ('label', wagtail.blocks.CharBlock())])), ('field_list', wagtail.blocks.ListBlock(wagtail.blocks.StructBlock([('name', wagtail.blocks.CharBlock()), ('label', wagtail.blocks.CharBlock())]))), ('field_container', wagtail.blocks.StreamBlock([('text', wagtail.blocks.StructBlock([('name', wagtail.blocks.CharBlock()), ('label', wagtail.blocks.CharBlock())])), ('integer', wagtail.blocks.StructBlock([('name', wagtail.blocks.CharBlock()), ('label', wagtail.blocks.CharBlock())]))])), ('disclaimer', wagtail.blocks.CharBlock()), ('container', wagtail.blocks.StructBlock([('title', wagtail.blocks.CharBlock()), ('border_color', wagtail.blocks.CharBlock()), ('fields', wagtail.blocks.StreamBlock([('text', wagtail.blocks.StructBlock([('name', wagtail.blocks.CharBlock()), ('label', wagtail.blocks.CharBlock())])), ('integer', wagtail.blocks.StructBlock([('name', wagtail.blocks.CharBlock()), ('label', wagtail.blocks.CharBlock())]))]))]))])), ('email_to_address', wagtail.blocks.CharBlock())])), ('newsletter', wagtail.blocks.StructBlock([('form_name', wagtail.blocks.CharBlock()), ('fields', wagtail.blocks.StreamBlock([('text', wagtail.blocks.StructBlock([('name', wagtail.blocks.CharBlock()), ('label', wagtail.blocks.CharBlock())])), ('boolean', wagtail.blocks.StructBlock([('name', wagtail.blocks.CharBlock()), ('label', wagtail.blocks.CharBlock())])), ('rich_text', wagtail.blocks.RichTextBlock(features=['bold', 'italic', 'link']))])), ('thank_you_msg', wagtail.blocks.CharBlock())]))], use_json_field=False),
        ),
    ]
