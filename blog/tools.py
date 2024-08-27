import os
from django.utils.text import slugify
from django.utils.timezone import now

def post_banner_directory_path(instance, filename):
    # Extrai a extensão do arquivo
    ext = filename.split('.')[-1]

    # Gera um slug a partir do título do post
    slugified_title = slugify(instance.title)

    # Define o nome do arquivo como "<slugified_title>_<timestamp>.<ext>"
    filename = f'{slugified_title}_{now().strftime("%Y%m%d%H%M%S")}.{ext}'

    # Define o caminho onde o arquivo será salvo: "banners/<slugified_title>/<filename>"
    return os.path.join(f'banners/{slugified_title}', filename)