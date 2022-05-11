from django.core.management.base import BaseCommand
from ... import baker_recipes as recipes


class Command(BaseCommand):
    help = """
    Seed the database with some data.
    Optional arguments:
        --scale: scale of created objects eg 10 = tens, 1000 = thousands etc. Default is 10.
    """

    def add_arguments(self, parser):
        parser.add_argument(
            "--scale",
            default=10,
            action="store_true",
            help="scale of created objects eg 10 = tens, 1000 = thousands etc. Default is 10.",
        )

    def handle(self, *args, **options):
        scale = options["scale"]
        recipes.seed(scale=scale)
