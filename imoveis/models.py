
import os

from django.conf import settings
from django.db import models
from PIL import Image

User = settings.AUTH_USER_MODEL


def content_file_name(instance, filename):
    ext = filename.split('.')[-1]
    filename = "%s_%s.%s" % (
        instance.imovel.propietario_id, instance.imovel.id, ext)
    return os.path.join(
        f'imoveis/fotos/{instance.imovel.propietario_id}/{instance.imovel.id}',
        filename
    )


class Imovel(models.Model):
    class Meta:
        verbose_name_plural = 'Imoveis'

    choices_sim_nao = (
        ("sim", "Sim"),
        ("nao", "Não")
    )
    choices_teto = (
        ("laje", "Laje"),
        ("telhado", "Telhado"),
        ("ambos", "Ambos")
    )

    choices_qtd_quartos_banheiro = (
        (1, "1"),
        (2, "2"),
        (3, "3"),
        (4, "4"),
    )

    choices_qtd_vagas = (
        (0, "0"),
        (1, "1"),
        (2, "2"),
        (3, "3"),
    )

    titulo = models.CharField(max_length=65, verbose_name='Título')
    cep = models.CharField(
        max_length=9, verbose_name='CEP')

    rua = models.CharField(
        max_length=65, verbose_name='Rua')

    bairro = models.CharField(max_length=65, verbose_name='Bairro')

    cidade = models.CharField(
        max_length=65, verbose_name='Cidade')

    estado = models.CharField(
        max_length=65, verbose_name='Estado')

    valor_aluguel = models.DecimalField(
        max_digits=8, decimal_places=2, verbose_name='Valor do aluguel')
    paga_deposito = models.CharField(
        max_length=3, default="nao", choices=choices_sim_nao,
        verbose_name='Paga depósito?')

    valor_deposito = models.DecimalField(
        max_digits=8, decimal_places=2, blank=True, default=0.00,
        verbose_name='Valor do depósito')

    paga_iptu = models.CharField(
        max_length=3, default="nao", choices=choices_sim_nao,
        verbose_name='Paga IPTU?')

    valor_iptu = models.DecimalField(
        max_digits=8, decimal_places=2, blank=True, default=0.00,
        verbose_name='Valor do IPTU')

    paga_incendio = models.CharField(
        max_length=3, default="nao", choices=choices_sim_nao,
        verbose_name='Paga taxa de icêndio?')

    valor_incendio = models.DecimalField(
        max_digits=8, decimal_places=2, blank=True, default=0.00,
        verbose_name='Valor da taxa de incêndio')

    paga_luz = models.CharField(
        max_length=3, default="sim", choices=choices_sim_nao,
        verbose_name='Paga luz?')

    paga_agua = models.CharField(
        max_length=3, default="sim", choices=choices_sim_nao,
        verbose_name='Paga água?')

    qtd_quarto = models.IntegerField(
        default=1, choices=choices_qtd_quartos_banheiro,
        verbose_name='Qtd. Quartos')

    qtd_banheiro = models.IntegerField(
        default=1, choices=choices_qtd_quartos_banheiro,
        verbose_name='Qtd. Banheiros')

    qtd_vaga = models.IntegerField(default=0, choices=choices_qtd_vagas,
                                   verbose_name='Qtd. Vagas')

    idependente = models.CharField(
        max_length=3, default="sim", choices=choices_sim_nao,
        verbose_name='Casa idependente?')

    aceita_pet = models.CharField(
        max_length=3, default="sim", choices=choices_sim_nao,
        verbose_name='Aceita Pet?')

    aceita_crianca = models.CharField(
        max_length=3, default="sim", choices=choices_sim_nao,
        verbose_name='Aceita criança?')

    comunidade = models.CharField(
        max_length=3, default="nao", choices=choices_sim_nao,
        verbose_name='É comunidade?')

    comunidade_nome = models.CharField(max_length=65, blank=True, default="",
                                       verbose_name='Nome da comunidade')

    tipo_teto = models.CharField(
        max_length=8, default="laje", choices=choices_teto,
        verbose_name='Tipo do teto')

    descricao = models.TextField(blank=True, default='',
                                 verbose_name='Descrição do imóvel')

    disponivel = models.CharField(
        max_length=3, default="sim", choices=choices_sim_nao,
        verbose_name='Disponível para locação?')

    data_anuncio = models.DateTimeField(auto_now_add=True, blank=True)
    data_update = models.DateTimeField(auto_now=True)
    propietario = models.ForeignKey(User, on_delete=models.CASCADE)

    def __str__(self):
        return self.titulo


class ImovelFoto(models.Model):
    imovel = models.ForeignKey(Imovel, default=None, on_delete=models.CASCADE)
    foto = models.ImageField(upload_to=content_file_name)

    class Meta:
        default_related_name = 'imoveisfotos'

    @staticmethod
    def resize_image(image, new_width=800):

        image_full_path = os.path.join(settings.MEDIA_ROOT, image.name)
        image_pillow = Image.open(image_full_path)
        original_width, original_height = image_pillow.size

        watermark_path = os.path.join(
            'base_static/global/images/logo/mainlogo.png')
        watermark = Image.open(watermark_path)

        if original_width <= new_width:
            width, height = image_pillow.size
            base_image = image_pillow
            transparent = Image.new('RGBA', (width, height), (0, 0, 0, 0))
            transparent.paste(base_image, (0, 0))
            transparent.paste(watermark, (0, 0), mask=watermark)
            if transparent.mode in ("RGBA", "P"):
                transparent = transparent.convert("RGB")
            image_pillow = transparent
            image_pillow.save(image_full_path)
            # image_pillow.close()
            return

        new_height = round((new_width * original_height) / original_width)

        new_image = image_pillow.resize(
            (new_width, new_height), Image.LANCZOS)
        new_image.save(
            image_full_path,
            optimize=True,
            quality=50,
        )

        width, height = new_image.size
        base_image = new_image
        transparent = Image.new('RGBA', (width, height), (0, 0, 0, 0))
        transparent.paste(base_image, (0, 0))
        transparent.paste(watermark, (0, 0), mask=watermark)
        if transparent.mode in ("RGBA", "P"):
            transparent = transparent.convert("RGB")
        transparent.save(image_full_path)

    def save(self, *args, **kwargs):

        saved = super().save(*args, **kwargs)

        if self.foto:
            try:
                self.resize_image(self.foto, 800)
            except FileNotFoundError:
                ...

        return saved

    # Essa função delta os arquivos quando o registro for deletado
    def delete(self, *args, **kwargs):
        self.foto.delete()
        super().delete(*args, **kwargs)

    def __str__(self):
        return self.foto.url
